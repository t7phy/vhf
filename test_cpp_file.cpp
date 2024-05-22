double C1Pq2gEq(double inx, double inz, std::string cx, std::string cz,
                double Q, double muR, double muF, double muA)
{
    double res = 0.0;

    double rln2 = ln(2.0);

    double LMUR = 2 * log(muR / Q);
    double LMUF = 2 * log(muF / Q);
    double LMUA = 2 * log(muA / Q);

    double NC = 3.0;
    double CF = 4.0 / 3.0;
    double TR = 0.5;

    if (cx == "D" && cz == "D")
    {
        res = 0;

        return res;
    }
    if (cx == "D" && cz == "0")
    {
        res = 0;

        return res;
    }
}