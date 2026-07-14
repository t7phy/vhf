use neopdf::pdf::PDF;

fn main() {
    // Name of the PDF set: can be a standard LHAPDF name
    // or a NeoPDF grid such as "NNPDF40_nnlo_as_01180.neopdf.lz4".
    let pdf_name = "NNPDF40_nnlo_as_01180";
    let member = 0usize; // central replica

    // Load the PDF member.
    let pdf = PDF::load(pdf_name, member);

    // Parton ID (PDG): 21 = gluon.
    let pid = 21;

    // Example kinematics.
    let x_values = vec![5e-2, 1.5e-1, 2.5e-1, 3.5e-1, 4.5e-1];
    let q2 = 100.0;

    for x in x_values {
        let xf = pdf.xfxq2(pid, &[x, q2]);
        println!("{:10.3e} {:20.8e}", x, xf);
    }
}