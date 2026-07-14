from LeProHQ import cg1, cgBar1
import numpy as np
from scipy.integrate import quad

import lhapdf
lhapdf.setVerbosity(0)

pdf = lhapdf.mkPDF("ToyPDF", 0)

def fxq(x, q):
    return pdf.xfxQ2(21, x, q**2)/x

mc = 1.3
# xvec = [0.00001, 0.0001, 0.001, 0.01, 0.1, 0.2, 0.3, 0.4, 0.5] #[1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 0.3]
# qvec = [1.3, 1.5, 1.75, 1.8, 2.0, 2.5, 3.5, 4.0, 4.75, 5.0, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 75.0, 80.0, 90.0, 100.0, 110.0, 200.0, 300.0, 400.0, 500.0, 600.0]

# qvec_v2 = [
#    1.30000,
#    1.36665,
#    1.43672,
#    1.51038,
#    1.58782,
#    1.66923,
#    1.75482,
#    1.84479,
#    1.93937,
#    2.03881,
#    2.14334,
#    2.25323,
#    2.36875,
#    2.49020,
#    2.61788,
#    2.75210,
#    2.89320,
#    3.04154,
#    3.19748,
#    3.36142,
#    3.53377,
#    3.71495,
#    3.90542,
#    4.10565,
#    4.31615,
#    4.53745,
#    4.77009,
#    5.01465,
#    5.27176,
#    5.54205,
#    5.82620,
#    6.12491,
#    6.43894,
#    6.76907,
#    7.11613,
#    7.48098,
#    7.86454,
#    8.26777,
#    8.69166,
#    9.13729,
#    9.60577,
#   10.09827,
#   10.61602,
#   11.16032,
#   11.73252,
#   12.33406,
#   12.96644,
#   13.63124,
#   14.33013,
#   15.06485,
#   15.83724,
#   16.64923,
#   17.50286,
#   18.40025,
#   19.34365,
#   20.33542,
#   21.37804,
#   22.47412,
#   23.62639,
#   24.83774,
#   26.11120,
#   27.44995,
#   28.85734,
#   30.33688,
#   31.89229,
#   33.52744,
#   35.24643,
#   37.05355,
#   38.95333,
#   40.95051,
#   43.05009,
#   45.25731,
#   47.57770,
#   50.01707,
#   52.58150,
#   55.27741,
#   58.11154,
#   61.09098,
#   64.22318,
#   67.51598,
#   70.97760,
#   74.61669,
#   78.44237,
#   82.46420,
#   86.69223,
#   91.13704,
#   95.80973,
#  100.72200,
#  105.88613,
#  111.31503,
#  117.02227,
#  123.02213,
#  129.32961,
#  135.96048,
#  142.93132,
#  150.25957,
#  157.96354,
#  166.06251,
#  174.57671,
#  183.52745,
#  192.93711,
#  202.82920,
#  213.22848,
#  224.16094,
#  235.65391,
#  247.73615,
#  260.43785,
#  273.79079,
#  287.82834,
#  302.58562,
#  318.09951,
#  334.40882,
#  351.55433,
#  369.57891,
#  388.52762,
#  408.44786,
# ]

def evaluator(x, q2):
    if q2 * (1 - x) / x <= 4 * mc**2:
        return 0.0
    xi = q2 / mc**2
    eta = xi / 4.0 * (1.0 / x - 1.0) - 1.0

    return q2/(np.pi*mc**2) / x * (4*np.pi)**2 * ( cg1("F2","VV",xi,eta) + cgBar1("F2","VV",xi,eta)*np.log(xi) )

def evaluator_log(x, q2):
    if q2 * (1 - x) / x <= 4 * mc**2:
        return 0.0
    xi = q2 / mc**2
    eta = xi / 4.0 * (1.0 / x - 1.0) - 1.0

    return cgBar1("F2","VV",xi,eta)*np.log(xi)

def evaluator_log_indep(x, q2):
    if q2 * (1 - x) / x <= 4 * mc**2:
        return 0.0
    xi = q2 / mc**2
    eta = xi / 4.0 * (1.0 / x - 1.0) - 1.0

    return cg1("F2","VV",xi,eta)

def convolver(x, q):
    def integrand(z):
        return (pdf.alphasQ2(q**2)/(4*np.pi))**2 * fxq(x/z, q) * evaluator(z, q**2) / z

    return quad(integrand, x, 1.0)[0] * x * (4/9)

q = np.array([
    1.30, 1.50, 1.75, 1.80, 2.00, 2.50, 3.50,
    4.00, 4.75, 5.00, 6.00, 8.00, 10.00, 15.00,
    20.00, 30.00, 40.00, 50.00, 60.00, 70.00,
    75.00, 80.00, 90.00, 100.00, 110.00, 200.00,
    300.00, 400.00
])

for q in q:
    print(f"{q:.2f} {convolver(0.01, q):.5e}")
    # print(f"{q:.2f} {evaluator(0.01, q**2):.9e}")

# for x in xvec:
#     for q in qvec:
#         print(f"{x:.1e} {q:.2f} {convolver(x, q):.5e}")

# print("x q c2g")
# for x in xvec:
#     for q in qvec_v2:
#         try:
#             # Try to calculate the value
#             val = evaluator(x, q**2)
#         except ZeroDivisionError:
#             # If a division by zero occurs anywhere in the call stack, return NaN
#             val = np.nan
            
#         print(f"{x:.1e} {q:.5f} {val:.5e}")

# def compare_c2g_all_points(file1_path, file2_path):
#     data1 = {}
#     data2 = {}

#     # 1. Parse the first file (c2g.txt: x, q, c2g)
#     with open(file1_path, 'r') as f1:
#         next(f1)  # Skip the header line
#         for line in f1:
#             parts = line.split()
#             if len(parts) >= 3:
#                 x_val = float(parts[0])
#                 q_val = float(parts[1])
#                 c2g_val = float(parts[2])
                
#                 key = f"{x_val:.6e}_{q_val:.5f}"
#                 data1[key] = {'x': x_val, 'q': q_val, 'c2g': c2g_val}

#     # 2. Parse the second file (forTanishq_c2g.txt: x, Q, log, c2g)
#     with open(file2_path, 'r') as f2:
#         next(f2)  # Skip the header line
#         for line in f2:
#             parts = line.split()
#             if len(parts) >= 4:
#                 x_val = float(parts[0])
#                 q_val = float(parts[1])
#                 c2g_val = float(parts[3]) 
                
#                 key = f"{x_val:.6e}_{q_val:.5f}"
#                 data2[key] = c2g_val

#     # 3. Compare the matching keys
#     comparisons = []
    
#     for key, d1 in data1.items():
#         if key in data2:
#             val1 = d1['c2g']
#             val2 = data2[key]
            
#             abs_diff = abs(val1 - val2)
#             rel_diff_percent = (abs_diff / abs(val2) * 100) if val2 != 0 else 0.0
            
#             comparisons.append({
#                 'x': d1['x'],
#                 'q': d1['q'],
#                 'c2g_1': val1,
#                 'c2g_2': val2,
#                 'abs_diff': abs_diff,
#                 'rel_diff_percent': rel_diff_percent
#             })

#     if not comparisons:
#         print("No matching x and q data points found between the two files.")
#         return

#     # 4. Sort the comparisons by 'x' then 'q' for a logical reading order
#     comparisons.sort(key=lambda item: (item['x'], item['q']))

#     # 5. Print ALL points in a formatted table
#     print(f"{'x':<11} | {'q':<10} | {'c2g (File 1)':<15} | {'c2g (File 2)':<15} | {'Abs Diff':<13} | {'Rel Diff %'}")
#     print("-" * 88)
    
#     for c in comparisons:
#         print(f"{c['x']:<11.1e} | {c['q']:<10.5f} | {c['c2g_1']:<15.5e} | {c['c2g_2']:<15.5e} | {c['abs_diff']:<13.5e} | {c['rel_diff_percent']:.5f}%")

#     # 6. Calculate Summary Statistics
#     max_abs_diff = max(c['abs_diff'] for c in comparisons)
#     max_rel_diff = max(c['rel_diff_percent'] for c in comparisons)
#     avg_rel_diff = sum(c['rel_diff_percent'] for c in comparisons) / len(comparisons)

#     # 7. Print the Summary at the end
#     print("\n" + "=" * 88)
#     print(" " * 35 + "SUMMARY STATISTICS")
#     print("=" * 88)
#     print(f"Total matching points compared: {len(comparisons)}")
#     print(f"Maximum absolute difference:    {max_abs_diff:.5e}")
#     print(f"Maximum relative difference:    {max_rel_diff:.5f}%")
#     print(f"Average relative difference:    {avg_rel_diff:.5f}%")
#     print("=" * 88)

# # Run the function
# if __name__ == "__main__":
#     compare_c2g_all_points("c2g.txt", "forTanishq_c2g.txt")

# import matplotlib.pyplot as plt

# def plot_c2g_differences(file1_path, file2_path):
#     data1 = {}
#     data2 = {}

#     # 1. Parse the first file (c2g.txt: x, q, c2g)
#     with open(file1_path, 'r') as f1:
#         next(f1)  # Skip the header line
#         for line in f1:
#             parts = line.split()
#             if len(parts) >= 3:
#                 x_val = float(parts[0])
#                 q_val = float(parts[1])
#                 c2g_val = float(parts[2])
                
#                 key = f"{x_val:.6e}_{q_val:.5f}"
#                 data1[key] = {'x': x_val, 'q': q_val, 'c2g': c2g_val}

#     # 2. Parse the second file (forTanishq_c2g.txt: x, Q, log, c2g)
#     with open(file2_path, 'r') as f2:
#         next(f2)  # Skip the header line
#         for line in f2:
#             parts = line.split()
#             if len(parts) >= 4:
#                 x_val = float(parts[0])
#                 q_val = float(parts[1])
#                 c2g_val = float(parts[3]) 
                
#                 key = f"{x_val:.6e}_{q_val:.5f}"
#                 data2[key] = c2g_val

#     # 3. Match keys and group by 'x'
#     # Dictionary structure: { x_val : [(q_val, rel_diff_percent), ...] }
#     grouped_data = {}
    
#     for key, d1 in data1.items():
#         if key in data2:
#             val1 = d1['c2g']
#             val2 = data2[key]
            
#             abs_diff = abs(val1 - val2)
#             rel_diff_percent = (abs_diff / abs(val2) * 100) if val2 != 0 else 0.0
            
#             x = d1['x']
#             q = d1['q']
            
#             if x not in grouped_data:
#                 grouped_data[x] = []
                
#             grouped_data[x].append((q, rel_diff_percent))

#     if not grouped_data:
#         print("No matching points found. Cannot generate plots.")
#         return

#     # 4. Generate a plot for each unique 'x' value
#     print(f"Found {len(grouped_data)} unique 'x' values. Generating plots...")
    
#     for x_val in sorted(grouped_data.keys()):
#         # Retrieve the points for this x value and sort them sequentially by 'q'
#         points = sorted(grouped_data[x_val], key=lambda item: item[0])
        
#         # Split into x and y lists for matplotlib
#         q_vals = [p[0] for p in points]
#         rel_diffs = [p[1] for p in points]
        
#         # Create the plot
#         plt.figure(figsize=(8, 5))
#         plt.plot(q_vals, rel_diffs, marker='o', linestyle='-', color='b', markersize=4)
        
#         plt.yscale('log')
#         # Formatting
#         plt.title(f"Relative Difference vs q (for x = {x_val:.1e})")
#         plt.xlabel("q")
#         plt.ylabel("Relative Difference (%)")
#         plt.grid(True, linestyle='--', alpha=0.7)
        
#         # Adjust layout and save the figure
#         plt.tight_layout()
        
#         # Format the filename to be safe (removes any + signs from scientific notation)
#         filename = f"reldiff_x_{x_val:.1e}.pdf".replace('+', '')
#         plt.savefig(filename)
        
#         # Close the plot to free up memory before the next loop
#         plt.close()
        
#         print(f"Saved: {filename}")

#     print("All plots generated successfully!")

# # Run the script
# if __name__ == "__main__":
#     plot_c2g_differences("c2g.txt", "forTanishq_c2g.txt")

# import matplotlib.pyplot as plt

# def plot_c2g_overlay(file1_path, file2_path):
#     data1 = {}
#     data2 = {}

#     # 1. Parse the first file (c2g.txt -> Felix)
#     with open(file1_path, 'r') as f1:
#         next(f1)  # Skip the header line
#         for line in f1:
#             parts = line.split()
#             if len(parts) >= 3:
#                 x_val = float(parts[0])
#                 q_val = float(parts[1])
#                 c2g_val = float(parts[2])
                
#                 key = f"{x_val:.6e}_{q_val:.5f}"
#                 data1[key] = {'x': x_val, 'q': q_val, 'c2g': c2g_val}

#     # 2. Parse the second file (forTanishq_c2g.txt -> Yao)
#     with open(file2_path, 'r') as f2:
#         next(f2)  # Skip the header line
#         for line in f2:
#             parts = line.split()
#             if len(parts) >= 4:
#                 x_val = float(parts[0])
#                 q_val = float(parts[1])
#                 c2g_val = float(parts[3]) 
                
#                 key = f"{x_val:.6e}_{q_val:.5f}"
#                 data2[key] = c2g_val

#     # 3. Match keys and group the c2g values by 'x'
#     # Dictionary structure: { x_val : [(q_val, felix_c2g, yao_c2g), ...] }
#     grouped_data = {}
    
#     for key, d1 in data1.items():
#         if key in data2:
#             x = d1['x']
#             q = d1['q']
#             felix_c2g = d1['c2g']
#             yao_c2g = data2[key]
            
#             if x not in grouped_data:
#                 grouped_data[x] = []
                
#             grouped_data[x].append((q, felix_c2g, yao_c2g))

#     if not grouped_data:
#         print("No matching points found. Cannot generate plots.")
#         return

#     # 4. Generate an overlay plot for each unique 'x' value
#     print(f"Found {len(grouped_data)} unique 'x' values. Generating comparison plots...")
    
#     for x_val in sorted(grouped_data.keys()):
#         # Retrieve the points for this x value and sort them sequentially by 'q'
#         points = sorted(grouped_data[x_val], key=lambda item: item[0])
        
#         # Split into individual lists for matplotlib
#         q_vals = [p[0] for p in points]
#         felix_vals = [p[1] for p in points]
#         yao_vals = [p[2] for p in points]
        
#         # Create the plot
#         plt.figure(figsize=(8, 5))
        
#         # Plot Felix and Yao with contrasting styles so both are visible
#         plt.plot(q_vals, felix_vals, marker='o', linestyle='-', color='blue', label='Felix')
#         plt.plot(q_vals, yao_vals, marker='x', linestyle='--', color='red', label='Yao')
        
#         # Keep the logarithmic y-axis (change 'symlog' to 'linear' if you don't want log scaling)
#         plt.yscale('linear')
        
#         # Formatting
#         plt.title(f"c2g values vs q (for x = {x_val:.1e})")
#         plt.xlabel("q")
#         plt.ylabel("c2g Value")
#         plt.legend(loc="best") # Automatically puts the legend in the corner with the least data
#         plt.grid(True, linestyle='--', alpha=0.7)
        
#         # Adjust layout and save the figure
#         plt.tight_layout()
        
#         # Format the filename
#         filename = f"c2g_overlay_x_{x_val:.1e}.pdf".replace('+', '')
#         plt.savefig(filename)
        
#         # Close the plot to free up memory
#         plt.close()
        
#         print(f"Saved: {filename}")

#     print("All comparison plots generated successfully!")

# # Run the script
# if __name__ == "__main__":
#     plot_c2g_overlay("c2g.txt", "forTanishq_c2g.txt")

# import numpy as np
# import matplotlib.pyplot as plt

# # Q values in GeV
# q = np.array([
#     1.30, 1.50, 1.75, 1.80, 2.00, 2.50, 3.50,
#     4.00, 4.75, 5.00, 6.00, 8.00, 10.00, 15.00,
#     20.00, 30.00, 40.00, 50.00, 60.00, 70.00,
#     75.00, 80.00, 90.00, 100.00, 110.00, 200.00,
#     300.00, 400.00
# ])

# # Third column of the first block
# leprohq = np.array([
#     3.84988e-03, 5.71955e-03, 8.30263e-03, 8.84552e-03,
#     1.10680e-02, 1.66856e-02, 2.66368e-02, 3.07009e-02,
#     3.57632e-02, 3.72163e-02, 4.21344e-02, 4.90414e-02,
#     5.37601e-02, 6.12669e-02, 6.59846e-02, 7.19741e-02,
#     7.61027e-02, 7.82004e-02, 8.06130e-02, 8.24679e-02,
#     8.33301e-02, 8.41137e-02, 8.54959e-02, 8.66928e-02,
#     8.77443e-02, 9.37569e-02, 9.73406e-02, 9.96799e-02
# ])

# # Second set of results
# svn1995 = np.array([
#     0.00394468, 0.00580404, 0.00838577, 0.0089372,
#     0.0110915, 0.0167991, 0.0267235, 0.030864,
#     0.0358244, 0.0372743, 0.0421489, 0.0490505,
#     0.0537455, 0.0612308, 0.0660136, 0.0720204,
#     0.0759413, 0.0788553, 0.0811586, 0.0829395,
#     0.0837528, 0.0844107, 0.0857281, 0.0868256,
#     0.0879806, 0.0938564, 0.0973086, 0.0995279
# ])

# svn1995_nf1 = np.array([
#     0.00394468, 0.00575333, 0.00824558, 0.00877547,
#     0.010835, 0.0162499, 0.0254722, 0.0292537,
#     0.033702, 0.0349902, 0.0392715, 0.0452139,
#     0.0491799, 0.0554267, 0.0594113, 0.0644043,
#     0.0676774, 0.0701255, 0.0720701, 0.0735619,
#     0.0742499, 0.0747928, 0.0759055, 0.0768256,
#     0.0778245, 0.0828099, 0.0857359, 0.0876153
# ])

# assert len(q) == len(leprohq) == len(svn1995) == len(svn1995_nf1)

# arxiv_2509_16124 = np.array([
#     -0.0261269, -0.0235232, -0.0209831, -0.0204932,
#     -0.018466, -0.0126041, 0.00260834, 0.0103698,
#     0.0198092, 0.0227468, 0.0315495, 0.0424997,
#     0.0484321, 0.0558454, 0.0598604, 0.0647722,
#     0.0679591, 0.0703145, 0.0721594, 0.0736689,
#     0.0743276, 0.0749466, 0.0760377, 0.0769952,
#     0.0778441, 0.0827955, 0.0858092, 0.0877898
# ])

# assert len(q) == len(arxiv_2509_16124)

# fig, ax = plt.subplots(figsize=(7.5, 5.5))

# ax.plot(
#     q, arxiv_2509_16124,
#     color="tab:purple",
#     marker="D",
#     markersize=4.5,
#     linewidth=1.8,
#     linestyle=":",
#     label="2509.16124"
# )
# ax.axhline(0.0, color="black", linewidth=0.8, alpha=0.6)

# ax.plot(
#     q, svn1995_nf1,
#     color="tab:green",
#     marker="^",
#     markersize=5,
#     linewidth=1.8,
#     linestyle="-.",
#     label=r"SvN1995 $H^{(2)}_{2,g}(N_f+1)$"
# )




# ax.plot(
#     q, svn1995,
#     color="tab:red", marker="s", markersize=4.5,
#     linewidth=1.8, linestyle="--",
#     label=r"SvN1995 $H^{(2)}_{2,g}(N_f)$"
# )
# ax.plot(
#     q, leprohq,
#     color="tab:blue", marker="o", markersize=5,
#     linewidth=1.8, label="LeProHQ"
# )

# ax.set_xscale("log")
# ax.set_xlabel(r"$Q\ \mathrm{[GeV]}$", fontsize=14)
# ax.set_ylabel(r"$F_{2c}$", fontsize=14)

# ax.grid(True, which="both", linestyle=":", alpha=0.5)
# ax.legend(frameon=False, fontsize=12)
# ax.tick_params(axis="both", which="both", direction="in", labelsize=11)

# fig.tight_layout()
# fig.savefig("F2c_comparison.pdf", bbox_inches="tight")
# # fig.savefig("F2c_comparison.png", dpi=300, bbox_inches="tight")
