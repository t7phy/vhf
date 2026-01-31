import os
import sys
import re
from pathlib import Path
import argparse

def translate_head(content):
    target = '#include "../sidis.h"\n\n\n\n/* Helpers */'
    replacement = 'use crate::sidis::internal::*;'
    return content.replace(target, replacement)

def translate_non_rg_func(content):
    # 1. Signature replacement: double <name>(double x, double z, double NF) {
    # Becomes: pub fn <name>(x: f64, z: f64, NF: f64) -> f64 {
    # Specifically excludes names starting with RG_RG_
    sig_pattern = r"double\s+((?!RG_RG_)\w+_\w+_\d{3})\s*\(double\s+x,\s+double\s+z,\s+double\s+NF\)\s*\{"
    content = re.sub(sig_pattern, r"fn \1(x: f64, z: f64, NF: f64) -> f64 {", content)

    # 2. Discard the specific initialization line
    content = content.replace("    double res = 0.0;\n", "")

    # 3. Handle the assignment and number logic
    def process_expression_line(match):
        indent = match.group(1)
        expr = match.group(2)

        # 1. First, handle the trailing plus signs before the semicolon
        # We look for ' + +' at the very end of the expression
        if expr.strip().endswith("+  +"):
            expr = expr.rstrip().removesuffix("+  +")
        elif expr.strip().endswith("+ +"):
            expr = expr.rstrip().removesuffix("+ +")
        elif expr.strip().endswith(" +"):
            expr = expr.rstrip().removesuffix(" +")

            
        # 2. Then handle double pluses inside the expression
        expr = expr.replace(" +  +  +  +  + ", " + ")
        expr = expr.replace(" +  +  + ", " + ")
        expr = expr.replace(" +  +", " + ")
        expr = expr.replace(" + +", " + ")
        # expr = expr.replace("+ ;", ";")
        # Catch any remaining weird spacing patterns
        expr = expr.replace(" +   + ", " + ")
        

        # Number conversion: 5 -> 5.0 (skip second arg of pow)
        def float_replacer(num_match):
            full_expr = num_match.string
            pos = num_match.start()
            # Check for a minus sign immediately before the number
            is_negative = full_expr[pos-1] == '-' if pos > 0 else False
            
            before = full_expr[:pos]
            # Check if we are inside the second argument of pow
            if re.search(r"pow\([^,]+,\s*-?$", before):
                return num_match.group(0)
            return num_match.group(0) + ".0"
        
        processed_expr = re.sub(r"\b\d+\b(?!\.)", float_replacer, expr)
        return f"{indent}let res: f64 = {processed_expr};"

    # Match the line starting with res = ...;
    content = re.sub(r"^(\s*)res = (.*?);", process_expression_line, content, flags=re.MULTILINE)
    
    return content

def translate_rg_func(content):
    # Regex to capture the function name and the body for RG_RG_XXX functions
    rg_pattern = r"double\s+(RG_RG_\d{3})\s*\(double\s+x,\s+double\s+z,\s+double\s+NF\)\s*\{(.*?)\n\}"
    
    def process_rg(match):
        func_name = match.group(1)
        body = match.group(2)
        discarded_conditions = []

        # 1. The hardcoded Rust preamble
        rust_preamble = f"""
    let mut res: f64 = 0.0;
    let tiny: f64 = 1e-4;
    let tinyinv: f64 = 1.0 / tiny;

    let u: f64 = x + z;
    let v: f64 = x - z;

    // x=z
    if (v.abs() <= tiny && u >= 2.0 - tiny) || (v.abs() <= tiny && u <= tiny) {{
        return 0.0;
    }}

    // intersection region of x=z and x=1-z:
    if v.abs() < 0.99 * tiny && (u - 1.0).abs() < 0.99 * tiny {{
        let u0: f64 = 1.0 - tiny;
        let v0: f64 = -tiny;
        let u1: f64 = 1.0 - tiny;
        let v1: f64 = tiny;
        let u2: f64 = 1.0 + tiny;
        let v2: f64 = -tiny;

        let x0: f64 = 0.5 * (u0 + v0);
        let z0: f64 = 0.5 * (u0 - v0);
        let x1: f64 = 0.5 * (u1 + v1);
        let z1: f64 = 0.5 * (u1 - v1);
        let x2: f64 = 0.5 * (u2 + v2);
        let z2: f64 = 0.5 * (u2 - v2);

        let pt0: f64 = {func_name}(x0, z0, NF);
        let pt1: f64 = {func_name}(x1, z1, NF);
        let pt2: f64 = {func_name}(x2, z2, NF);

        res = pt0 + 0.5 * (pt1 - pt0) * tinyinv * (v - v0) + 0.5 * (pt2 - pt0) * tinyinv * (u - u0);
        return res;
    }}
    if v.abs() < 0.99 * tiny {{
        let v0: f64 = -tiny;
        let v1: f64 = tiny;

        let x0: f64 = 0.5 * (u + v0);
        let z0: f64 = 0.5 * (u - v0);
        let x1: f64 = 0.5 * (u + v1);
        let z1: f64 = 0.5 * (u - v1);

        let pt0: f64 = {func_name}(x0, z0, NF);
        let pt1: f64 = {func_name}(x1, z1, NF);
        res = pt0 + 0.5 * (pt1 - pt0) * tinyinv * (v - v0);
        return res;
    }}

    // x=1-z
    if (u - 1.0).abs() <= tiny && v <= tiny - 1.0 {{
        res = 0.0;
        return res;
    }}
    if (u - 1.0).abs() <= tiny && v >= 1.0 - tiny {{
        res = 0.0;
        return res;
    }}
    if (u - 1.0).abs() < 0.99 * tiny {{
        let u0: f64 = 1.0 - tiny;
        let u1: f64 = 1.0 + tiny;

        let x0: f64 = 0.5 * (u0 + v);
        let z0: f64 = 0.5 * (u0 - v);
        let x1: f64 = 0.5 * (u1 + v);
        let z1: f64 = 0.5 * (u1 - v);

        let pt0: f64 = {func_name}(x0, z0, NF);
        let pt1: f64 = {func_name}(x1, z1, NF);
        res = pt0 + 0.5 * (pt1 - pt0) * tinyinv * (u - u0);
        return res;
    }}"""

        # 2. Extract logic AFTER the preamble
        parts = body.split('if (z')
        if len(parts) < 2:
            return f"fn {func_name}(x: f64, z: f64, NF: f64) -> f64 {{{rust_preamble}\n    res\n}}"
        
        raw_logic = 'if (z' + 'if (z'.join(parts[1:])
        raw_logic = raw_logic.replace("return res;", "").strip()
        
        pattern = r"if\s*\((.*?)\)\s*\{\s*double\s+tmp\s*=\s*0\.0\s*;\s*tmp\s*=\s*(.*?);\s*res\s*\+=\s*tmp\s*;\s*\}"
        
        def convert_block(m):
            cond = m.group(1)
            expr = m.group(2).strip()
            
            if expr == "0":
                discarded_conditions.append(cond)
                return ""
            
            expr = expr.replace(" +  +  +  +  + ", " + ").replace(" +  +  + ", " + ").replace(" + +", " + ").replace(" +  + ", " + ").replace(" +   +", " + ")
            
            def float_replacer(num_match):
                full_expr = num_match.string
                pos = num_match.start()
                before = full_expr[:pos]
                if re.search(r"pow\([^,]+,\s*-?$", before):
                    return num_match.group(0)
                return num_match.group(0) + ".0"
            
            expr = re.sub(r"\b\d+\b(?!\.)", float_replacer, expr)
            
            # Use 8 spaces for the internal lines, no leading space for the 'if' here
            # because we add the 4-space indent in the final join.
            return f"if {cond} {{\n        let tmp: f64 = {expr};\n        res += tmp;\n    }}"

        final_logic_raw = re.sub(pattern, convert_block, raw_logic, flags=re.DOTALL)
        
        # Split into blocks, filter empty, and then prefix every single block with 4 spaces.
        logic_blocks = [block.strip() for block in final_logic_raw.split('if ') if block.strip()]
        final_logic = "\n\n".join([f"    if {block}" for block in logic_blocks])

        discard_comment = ""
        # if discarded_conditions:
        #     discard_comment = f"\n\n    // Discarded conditions where tmp = 0: {', '.join(discarded_conditions)}"

        return f"fn {func_name}(x: f64, z: f64, NF: f64) -> f64 {{{rust_preamble}\n\n{final_logic}{discard_comment}\n\n    return res;\n}}"

    return re.sub(rg_pattern, process_rg, content, flags=re.DOTALL)


# def translate_sv_map(content):
#     # 1. Locate the Inverted Branch Report block
#     report_pattern = r"/\*\s+Inverted Branch Report \(By Number\):(.*?)\*/"
#     match = re.search(report_pattern, content, re.DOTALL)
    
#     if not match:
#         return content

#     report_body = match.group(1).strip()
    
#     # 2. Parse the lines
#     map_entries = []
#     lines = report_body.splitlines()
#     for line in lines:
#         line = line.strip()
#         if not line.startswith("- "): continue
#         try:
#             key_part, values_part = line.replace("- ", "").split(":")
#             key = key_part.strip() 
#             values = [v.strip() for v in values_part.split(",")]
#             rust_vec = 'vec![' + ', '.join([f'"{v}"' for v in values]) + ']'
#             map_entries.append(f'    m.insert("{key}", {rust_vec});')
#         except ValueError: continue

#     # 3. Generate the Rust code block
#     rust_map_code = [

#         "",
#         "pub fn get_sv_map() -> HashMap<&'static str, Vec<&'static str>> {",
#         "    let mut m = HashMap::new();"
#     ]
#     rust_map_code.extend(map_entries)
#     rust_map_code.append("    m")
#     rust_map_code.append("}")
    
#     map_final_string = "\n".join(rust_map_code)

#     # 4. Remove both C++ report comment blocks from the original content
#     # This prevents the raw reports from staying in your Rust file
#     content = re.sub(r"/\*\s+Branch extraction report:.*?\*/", "", content, flags=re.DOTALL)
#     content = re.sub(r"/\*\s+Inverted Branch Report.*?\*/", "", content, flags=re.DOTALL)

#     # 5. Return the existing content (translated functions) PLUS the new Rust map
#     return content.strip() + map_final_string
# def translate_sv_map(content):
#     # 1. Locate the Inverted Branch Report block
#     report_pattern = r"/\*\s+Inverted Branch Report \(By Number\):(.*?)\*/"
#     match = re.search(report_pattern, content, re.DOTALL)
    
#     if not match:
#         return content

#     report_body = match.group(1).strip()
    
#     # 2. Parse the lines
#     map_entries = []
#     lines = report_body.splitlines()
#     for line in lines:
#         line = line.strip()
#         if not line.startswith("- "): continue
#         try:
#             key_part, values_part = line.replace("- ", "").split(":")
#             key = key_part.strip() 
#             values = [v.strip() for v in values_part.split(",")]
#             # Construct the (string, identifier) pairs for the macro
#             pairs = ", ".join([f'("{v}", {v}_{key})' for v in values])
#             map_entries.append(f'        "{key}" => [{pairs}],')
#         except ValueError: continue

#     # 3. Generate the Rust code block
#     rust_map_code = [
#         "",
#         "pub fn get_sv_map() -> sv_map {",
#         "    generate_sv_map! {"
#     ]
#     rust_map_code.extend(map_entries)
#     rust_map_code.append("    }")
#     rust_map_code.append("}")
    
#     map_final_string = "\n".join(rust_map_code)

#     # 4. Remove both C++ report comment blocks from the original content
#     content = re.sub(r"/\*\s+Branch extraction report:.*?\*/", "", content, flags=re.DOTALL)
#     content = re.sub(r"/\*\s+Inverted Branch Report.*?\*/", "", content, flags=re.DOTALL)

#     # 5. Return the existing content (translated functions) PLUS the new Rust map
#     return content.strip() + map_final_string

def translate_sv_map(content):
    # 1. Strict 36-slot order (Indices 0-35)
    # This MUST match the order of your Rust macro's @gen_wrappers block
    ORDERED_KEYS = [
        "RG_RG", "RG_D0", "RG_D1", "RG_D2", "RG_D3", "RG_DL", # 0-5
        "D0_RG", "D0_D0", "D0_D1", "D0_D2", "D0_D3", "D0_DL", # 6-11
        "D1_RG", "D1_D0", "D1_D1", "D1_D2", "D1_D3", "D1_DL", # 12-17
        "D2_RG", "D2_D0", "D2_D1", "D2_D2", "D2_D3", "D2_DL", # 18-23
        "D3_RG", "D3_D0", "D3_D1", "D3_D2", "D3_D3", "D3_DL", # 24-29
        "DL_RG", "DL_D0", "DL_D1", "DL_D2", "DL_D3", "DL_DL"  # 30-35
    ]

    # 2. Extract the report block
    report_pattern = r"/\*\s+Inverted Branch Report \(By Number\):(.*?)\*/"
    match = re.search(report_pattern, content, re.DOTALL)
    if not match:
        return content

    report_body = match.group(1).strip()
    
    # 3. Build the SV Mapping Comment Block (Formatted for Rust)
    sv_comment = ["/*", "  SV mapping:"]
    sv_comment.extend([f"  {line}" for line in report_body.splitlines()])
    sv_comment.append("*/")

    # 4. Generate the mkcoeff! macro entries
    macro_entries = []
    lines = report_body.splitlines()
    
    for line in lines:
        line = line.strip()
        if not line or not line.startswith("- "): continue
        
        try:
            # Parse line format: "- 000: D0_D0, RG_RG, ..."
            scale_part, funcs_part = line.replace("- ", "").split(":")
            scale = scale_part.strip()
            
            # Clean up function names (remove whitespace)
            available_funcs = [f.strip() for f in funcs_part.split(",") if f.strip()]
            
            # Initialize 36 slots with underscores
            slots = ["_"] * 36
            
            for func in available_funcs:
                if func in ORDERED_KEYS:
                    idx = ORDERED_KEYS.index(func)
                    # Resulting identifier: D0_D0_000
                    slots[idx] = f"{func}_{scale}"
            
            # Construct the entry tuple
            terms_str = ", ".join(slots)
            macro_entries.append(f'    ("{scale}", [{terms_str}])')
            
        except ValueError:
            continue

    # 5. Join entries with commas and wrap in mkcoeff!
    # Using a trailing comma in the list to avoid the "unexpected end" error
    macro_final_call = "mkcoeff!(\n" + ",\n".join(macro_entries) + "\n);"

    # 6. Cleanup original C++ content and assemble Rust content
    content = re.sub(r"/\*\s+Branch extraction report:.*?\*/", "", content, flags=re.DOTALL)
    content = re.sub(report_pattern, "", content, flags=re.DOTALL)

    # return content.strip() + "\n\n" + "\n".join(sv_comment) + "\n" + macro_final_call
    final_output = (
        content.strip() + 
        "\n\n" + 
        macro_final_call + 
        "\n\n" + 
        "\n".join(sv_comment) + 
        "\n"
    )
    
    return final_output

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir")
    parser.add_argument("output_dir")
    args = parser.parse_args()

    input_path = Path(args.input_dir)
    output_path = Path(args.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # List to track processed module names
    processed_modules = []

    for cpp_file in input_path.glob("*.cpp"):
        with open(cpp_file, 'r', encoding='utf-8') as f:
            data = f.read()

        data = translate_head(data)
        data = translate_non_rg_func(data)
        data = translate_rg_func(data)
        data = translate_sv_map(data)

        module_name = cpp_file.stem
        processed_modules.append(module_name)

        with open(output_path / (module_name + ".rs"), 'w', encoding='utf-8') as f:
            f.write(data)
        
        print(f"Processed: {cpp_file.name}")

    # Create the mod.rs file
    if processed_modules:
        # Sort modules alphabetically for a clean mod file
        processed_modules.sort()
        mod_content = "\n".join([f"pub mod {m};" for m in processed_modules])
        
        with open(output_path / "mod.rs", "w", encoding="utf-8") as f:
            f.write(mod_content)
        
        print(f"Created: mod.rs with {len(processed_modules)} modules.")