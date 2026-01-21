#include "../sidis.h"



/* Helpers */

double DL_DL_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-511. / 32. * CF * pow(NQCD, -1)) + (- 1537. / 96. * CF * NQCD) + 127. / 24. * CF * NF + 15. / 2. * zeta3 * CF * pow(NQCD, -1) + 41. / 6. * zeta3 * CF * NQCD + 2. / 3. * zeta3 * CF * NF + (- 29. / 24. * pow(pi, 2) * CF * pow(NQCD, -1)) + (- 277. / 216. * pow(pi, 2) * CF * NQCD) + 19. / 54. * pow(pi, 2) * CF * NF + 7. / 180. * pow(pi, 4) * CF * pow(NQCD, -1) + 1. / 18. * pow(pi, 4) * CF * NQCD + ;
    return res;
}

double DL_DL_001(double x, double z, double NF) {
    double res = 0.0;
    res = (- 93. / 8. * lmua * CF * pow(NQCD, -1)) + 245. / 24. * lmua * CF * NQCD + 1. / 6. * lmua * CF * NF + 10 * lmua * zeta3 * CF * pow(NQCD, -1) + (- 4 * lmua * zeta3 * CF * NQCD) + (- 1. / 2. * lmua * pow(pi, 2) * CF * pow(NQCD, -1)) + (- 13. / 18. * lmua * pow(pi, 2) * CF * NQCD) + 2. / 9. * lmua * pow(pi, 2) * CF * NF;
    return res;
}

double DL_DL_002(double x, double z, double NF) {
    double res = 0.0;
    res = (- 9. / 4. * pow(lmua, 2) * CF * pow(NQCD, -1)) + 31. / 4. * pow(lmua, 2) * CF * NQCD + (- pow(lmua, 2) * CF * NF) + 2. / 3. * pow(lmua, 2) * pow(pi, 2) * CF * pow(NQCD, -1) + (- 2. / 3. * pow(lmua, 2) * pow(pi, 2) * CF * NQCD);
    return res;
}

double DL_DL_010(double x, double z, double NF) {
    double res = 0.0;
    res = (- 93. / 8. * lmuf * CF * pow(NQCD, -1)) + 245. / 24. * lmuf * CF * NQCD + 1. / 6. * lmuf * CF * NF + 10 * lmuf * zeta3 * CF * pow(NQCD, -1) + (- 4 * lmuf * zeta3 * CF * NQCD) + (- 1. / 2. * lmuf * pow(pi, 2) * CF * pow(NQCD, -1)) + (- 13. / 18. * lmuf * pow(pi, 2) * CF * NQCD) + 2. / 9. * lmuf * pow(pi, 2) * CF * NF;
    return res;
}

double DL_DL_011(double x, double z, double NF) {
    double res = 0.0;
    res = (- 9. / 2. * lmuf * lmua * CF * pow(NQCD, -1)) + 9. / 2. * lmuf * lmua * CF * NQCD;
    return res;
}

double DL_DL_020(double x, double z, double NF) {
    double res = 0.0;
    res = (- 9. / 4. * pow(lmuf, 2) * CF * pow(NQCD, -1)) + 31. / 4. * pow(lmuf, 2) * CF * NQCD + (-pow(lmuf, 2) * CF * NF) + 2. / 3. * pow(lmuf, 2) * pow(pi, 2) * CF * pow(NQCD, -1) + (- 2. / 3. * pow(lmuf, 2) * pow(pi, 2) * CF * NQCD);
    return res;
}

double DL_DL_100(double x, double z, double NF) {
    double res = 0.0;
    res = (- 88. / 3. * lmur * CF * NQCD) + 16. / 3. * lmur * CF * NF;
    return res;
}

double DL_DL_101(double x, double z, double NF) {
    double res = 0.0;
    res = (- 11 * lmur * lmua * CF * NQCD) + 2 * lmur * lmua * CF * NF;
    return res;
}

double DL_DL_110(double x, double z, double NF) {
    double res = 0.0;
    res = (- 11 * lmur * lmuf * CF * NQCD) + 2 * lmur * lmuf * CF * NF;
    return res;
}

double DL_D0_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-202. / 27. * CF * NQCD) + 28. / 27. * CF * NF + (- 4 * zeta3 * CF * pow(NQCD, -1)) + 11 * zeta3 * CF * NQCD + 11. / 18. * pow(pi, 2) * CF * NQCD + (- 1. / 9. * pow(pi, 2) * CF * NF);
    return res;
}

double DL_D0_001(double x, double z, double NF) {
    double res = 0.0;
    res = (- 16 * lmua * CF * pow(NQCD, -1)) + 10. / 9. * lmua * CF * NQCD + 20. / 9. * lmua * CF * NF + (- 2. / 3. * lmua * pow(pi, 2) * CF * pow(NQCD, -1)) + 4. / 3. * lmua * pow(pi, 2) * CF * NQCD;
    return res;
}

double DL_D0_002(double x, double z, double NF) {
    double res = 0.0;
    res = (- 6 * pow(lmua, 2) * CF * pow(NQCD, -1)) + 40. / 3. * pow(lmua, 2) * CF * NQCD + (- 4. / 3. * pow(lmua, 2) * CF * NF);
    return res;
}

double DL_D0_010(double x, double z, double NF) {
    double res = 0.0;
    res = (- 2. / 3. * lmuf * pow(pi, 2) * CF * pow(NQCD, -1)) + 2. / 3. * lmuf * pow(pi, 2) * CF * NQCD;
    return res;
}

double DL_D0_011(double x, double z, double NF) {
    double res = 0.0;
    res = (- 6 * lmuf * lmua * CF * pow(NQCD, -1)) + 6 * lmuf * lmua * CF * NQCD;
    return res;
}

double DL_D0_101(double x, double z, double NF) {
    double res = 0.0;
    res = (- 44. / 3. * lmur * lmua * CF * NQCD) + 8. / 3. * lmur * lmua * CF * NF;
    return res;
}

double DL_D1_000(double x, double z, double NF) {
    double res = 0.0;
    res = 8 * CF * pow(NQCD, -1) + (- 5. / 9. * CF * NQCD) + (- 10. / 9. * CF * NF) + 2. / 3. * pow(pi, 2) * CF * pow(NQCD, -1) + (- pow(pi, 2) * CF * NQCD);
    return res;
}

double DL_D1_001(double x, double z, double NF) {
    double res = 0.0;
    res = 3 * lmua * CF * pow(NQCD, -1) + (- 3 * lmua * CF * NQCD);
    return res;
}

double DL_D1_002(double x, double z, double NF) {
    double res = 0.0;
    res = (- 8 * pow(lmua, 2) * CF * pow(NQCD, -1)) + 8 * pow(lmua, 2) * CF * NQCD;
    return res;
}

double DL_D1_010(double x, double z, double NF) {
    double res = 0.0;
    res = 3 * lmuf * CF * pow(NQCD, -1) + (- 3 * lmuf * CF * NQCD);
    return res;
}

double DL_D1_100(double x, double z, double NF) {
    double res = 0.0;
    res = 22. / 3. * lmur * CF * NQCD + (- 4. / 3. * lmur * CF * NF);
    return res;
}

double DL_D2_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-11. / 6. * CF * NQCD) + 1. / 3. * CF * NF;
    return res;
}

double DL_D2_001(double x, double z, double NF) {
    double res = 0.0;
    res = 6 * lmua * CF * pow(NQCD, -1) + (- 6 * lmua * CF * NQCD);
    return res;
}

double DL_D3_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-CF * pow(NQCD, -1)) + CF * NQCD;
    return res;
}

double D0_DL_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-202. / 27. * CF * NQCD) + 28. / 27. * CF * NF + (- 4 * zeta3 * CF * pow(NQCD, -1)) + 11 * zeta3 * CF * NQCD + 11. / 18. * pow(pi, 2) * CF * NQCD + (- 1. / 9. * pow(pi, 2) * CF * NF);
    return res;
}

double D0_DL_001(double x, double z, double NF) {
    double res = 0.0;
    res = (- 2. / 3. * lmua * pow(pi, 2) * CF * pow(NQCD, -1)) + 2. / 3. * lmua * pow(pi, 2) * CF * NQCD;
    return res;
}

double D0_DL_010(double x, double z, double NF) {
    double res = 0.0;
    res = (- 16 * lmuf * CF * pow(NQCD, -1)) + 10. / 9. * lmuf * CF * NQCD + 20. / 9. * lmuf * CF * NF + (- 2. / 3. * lmuf * pow(pi, 2) * CF * pow(NQCD, -1)) + 4. / 3. * lmuf * pow(pi, 2) * CF * NQCD;
    return res;
}

double D0_DL_011(double x, double z, double NF) {
    double res = 0.0;
    res = (- 6 * lmuf * lmua * CF * pow(NQCD, -1)) + 6 * lmuf * lmua * CF * NQCD;
    return res;
}

double D0_DL_020(double x, double z, double NF) {
    double res = 0.0;
    res = (- 6 * pow(lmuf, 2) * CF * pow(NQCD, -1)) + 40. / 3. * pow(lmuf, 2) * CF * NQCD + (- 4. / 3. * pow(lmuf, 2) * CF * NF);
    return res;
}

double D0_DL_110(double x, double z, double NF) {
    double res = 0.0;
    res = (- 44. / 3. * lmur * lmuf * CF * NQCD) + 8. / 3. * lmur * lmuf * CF * NF;
    return res;
}

double D0_D0_000(double x, double z, double NF) {
    double res = 0.0;
    res = 8 * CF * pow(NQCD, -1) + (- 5. / 9. * CF * NQCD) + (- 10. / 9. * CF * NF) + 2. / 3. * pow(pi, 2) * CF * pow(NQCD, -1) + (- pow(pi, 2) * CF * NQCD);
    return res;
}

double D0_D0_001(double x, double z, double NF) {
    double res = 0.0;
    res = 3 * lmua * CF * pow(NQCD, -1) + (- 3 * lmua * CF * NQCD);
    return res;
}

double D0_D0_010(double x, double z, double NF) {
    double res = 0.0;
    res = 3 * lmuf * CF * pow(NQCD, -1) + (- 3 * lmuf * CF * NQCD);
    return res;
}

double D0_D0_011(double x, double z, double NF) {
    double res = 0.0;
    res = (- 8 * lmuf * lmua * CF * pow(NQCD, -1)) + 8 * lmuf * lmua * CF * NQCD;
    return res;
}

double D0_D0_100(double x, double z, double NF) {
    double res = 0.0;
    res = 22. / 3. * lmur * CF * NQCD + (- 4. / 3. * lmur * CF * NF);
    return res;
}

double D0_D1_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-11. / 3. * CF * NQCD) + 2. / 3. * CF * NF;
    return res;
}

double D0_D1_001(double x, double z, double NF) {
    double res = 0.0;
    res = 8 * lmua * CF * pow(NQCD, -1) + (- 8 * lmua * CF * NQCD);
    return res;
}

double D0_D1_010(double x, double z, double NF) {
    double res = 0.0;
    res = 4 * lmuf * CF * pow(NQCD, -1) + (- 4 * lmuf * CF * NQCD);
    return res;
}

double D0_D2_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-3 * CF * pow(NQCD, -1)) + 3 * CF * NQCD;
    return res;
}

double D1_DL_000(double x, double z, double NF) {
    double res = 0.0;
    res = 8 * CF * pow(NQCD, -1) + (- 5. / 9. * CF * NQCD) + (- 10. / 9. * CF * NF) + 2. / 3. * pow(pi, 2) * CF * pow(NQCD, -1) + (- pow(pi, 2) * CF * NQCD);
    return res;
}

double D1_DL_001(double x, double z, double NF) {
    double res = 0.0;
    res = 3 * lmua * CF * pow(NQCD, -1) + (- 3 * lmua * CF * NQCD);
    return res;
}

double D1_DL_010(double x, double z, double NF) {
    double res = 0.0;
    res = 3 * lmuf * CF * pow(NQCD, -1) + (- 3 * lmuf * CF * NQCD);
    return res;
}

double D1_DL_020(double x, double z, double NF) {
    double res = 0.0;
    res = (- 8 * pow(lmuf, 2) * CF * pow(NQCD, -1)) + 8 * pow(lmuf, 2) * CF * NQCD;
    return res;
}

double D1_DL_100(double x, double z, double NF) {
    double res = 0.0;
    res = 22. / 3. * lmur * CF * NQCD + (- 4. / 3. * lmur * CF * NF);
    return res;
}

double D1_D0_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-11. / 3. * CF * NQCD) + 2. / 3. * CF * NF;
    return res;
}

double D1_D0_001(double x, double z, double NF) {
    double res = 0.0;
    res = 4 * lmua * CF * pow(NQCD, -1) + (- 4 * lmua * CF * NQCD);
    return res;
}

double D1_D0_010(double x, double z, double NF) {
    double res = 0.0;
    res = 8 * lmuf * CF * pow(NQCD, -1) + (- 8 * lmuf * CF * NQCD);
    return res;
}

double D1_D1_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-6 * CF * pow(NQCD, -1)) + 6 * CF * NQCD;
    return res;
}

double D2_DL_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-11. / 6. * CF * NQCD) + 1. / 3. * CF * NF;
    return res;
}

double D2_DL_010(double x, double z, double NF) {
    double res = 0.0;
    res = 6 * lmuf * CF * pow(NQCD, -1) + (- 6 * lmuf * CF * NQCD);
    return res;
}

double D2_D0_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-3 * CF * pow(NQCD, -1)) + 3 * CF * NQCD;
    return res;
}

double D3_DL_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-CF * pow(NQCD, -1)) + CF * NQCD;
    return res;
}

double DL_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-1. / 4. * CF * pow(NQCD, -1)) + 197. / 108. * CF * NQCD + (- 19. / 54. * CF * NF) + 1. / 4. * z * CF * pow(NQCD, -1) + 611. / 108. * z * CF * NQCD + (- 37. / 54. * z * CF * NF) + (- 4 * zeta3 * CF * pow(NQCD, -1)) + 5. / 2. * zeta3 * CF * NQCD + (- 4 * zeta3 * z * CF * pow(NQCD, -1)) + 5. / 2. * zeta3 * z * CF * NQCD + 7. / 12. * pow(pi, 2) * CF * pow(NQCD, -1) + (- 29. / 36. * pow(pi, 2) * CF * NQCD) + 1. / 18. * pow(pi, 2) * CF * NF + 1. / 6. * pow(pi, 2) * z * CF * pow(NQCD, -1) + (- 2. / 9. * pow(pi, 2) * z * CF * NQCD) + 1. / 18. * pow(pi, 2) * z * CF * NF + (- 5. / 4. * ln(1 - z) * CF * pow(NQCD, -1)) + 67. / 36. * ln(1 - z) * CF * NQCD + 2. / 9. * ln(1 - z) * CF * NF + (- 7 * ln(1 - z) * z * CF * pow(NQCD, -1)) + (- 14. / 9. * ln(1 - z) * z * CF * NQCD) + 8. / 9. * ln(1 - z) * z * CF * NF + (- 5. / 12. * ln(1 - z) * pow(pi, 2) * CF * pow(NQCD, -1)) + 3. / 4. * ln(1 - z) * pow(pi, 2) * CF * NQCD + (- 5. / 12. * ln(1 - z) * pow(pi, 2) * z * CF * pow(NQCD, -1)) + 3. / 4. * ln(1 - z) * pow(pi, 2) * z * CF * NQCD + 11. / 12. * pow(ln(1 - z), 2) * CF * NQCD + (- 1. / 6. * pow(ln(1 - z), 2) * CF * NF) + 11. / 12. * pow(ln(1 - z), 2) * z * CF * NQCD + (- 1. / 6. * pow(ln(1 - z), 2) * z * CF * NF) + 1. / 2. * pow(ln(1 - z), 3) * CF * pow(NQCD, -1) + (- 1. / 2. * pow(ln(1 - z), 3) * CF * NQCD) + 1. / 2. * pow(ln(1 - z), 3) * z * CF * pow(NQCD, -1) + (- 1. / 2. * pow(ln(1 - z), 3) * z * CF * NQCD) + 1. / 2. * ln(1 - z) * Li2(1 - z) * CF * pow(NQCD, -1) + (- 1. / 2. * ln(1 - z) * Li2(1 - z) * CF * NQCD) + 1. / 2. * ln(1 - z) * Li2(1 - z) * z * CF * pow(NQCD, -1) + (- 1. / 2. * ln(1 - z) * Li2(1 - z) * z * CF * NQCD) + 1. / 2. * ln(1 - z) * Li2(z) * CF * pow(NQCD, -1) + (- 3. / 2. * ln(1 - z) * Li2(z) * CF * NQCD) + 1. / 2. * ln(1 - z) * Li2(z) * z * CF * pow(NQCD, -1) + (- 3. / 2. * ln(1 - z) * Li2(z) * z * CF * NQCD) +  +  + (- 15. / 4. * ln(z) * CF * pow(NQCD, -1)) + 233. / 36. * ln(z) * CF * NQCD + (- 1. / 18. * ln(z) * CF * NF) + (- 29. / 4. * ln(z) * z * CF * pow(NQCD, -1)) +  + 101. / 36. * ln(z) * z * CF * NQCD + 11. / 18. * ln(z) * z * CF * NF + (- 1. / 3. * ln(z) * pow(pi, 2) * CF * pow(NQCD, -1)) + 1. / 2. * ln(z) * pow(pi, 2) * CF * NQCD + (- 1. / 3. * ln(z) * pow(pi, 2) * z * CF * pow(NQCD, -1)) + 1. / 2. * ln(z) * pow(pi, 2) * z * CF * NQCD + (- 3. / 2. * ln(z) * ln(1 - z) * CF * pow(NQCD, -1)) + 3. / 2. * ln(z) * ln(1 - z) * CF * NQCD + 3. / 2. * ln(z) * ln(1 - z) * z * CF * pow(NQCD, -1) + (- 3. / 2. * ln(z) * ln(1 - z) * z * CF * NQCD) + ln(z) * pow(ln(1 - z), 2) * CF * pow(NQCD, -1) + (- 2 * ln(z) * pow(ln(1 - z), 2) * CF * NQCD) + ln(z) * pow(ln(1 - z), 2) * z * CF * pow(NQCD, -1) + (- 2 * ln(z) * pow(ln(1 - z), 2) * z * CF * NQCD) +  + 21. / 8. * pow(ln(z), 2) * CF * pow(NQCD, -1) + (- 25. / 12. * pow(ln(z), 2) * CF * NQCD) + 1. / 12. * pow(ln(z), 2) * CF * NF + 7. / 8. * pow(ln(z), 2) * z * CF * pow(NQCD, -1) + (- 5. / 6. * pow(ln(z), 2) * z * CF * NQCD) + 1. / 12. * pow(ln(z), 2) * z * CF * NF + (- 1. / 4. * pow(ln(z), 2) * ln(1 - z) * CF * pow(NQCD, -1)) + 1. / 4. * pow(ln(z), 2) * ln(1 - z) * CF * NQCD + (- 1. / 4. * pow(ln(z), 2) * ln(1 - z) * z * CF * pow(NQCD, -1)) + 1. / 4. * pow(ln(z), 2) * ln(1 - z) * z * CF * NQCD + (- 25. / 24. * pow(ln(z), 3) * CF * pow(NQCD, -1)) + 5. / 8. * pow(ln(z), 3) * CF * NQCD + (- 25. / 24. * pow(ln(z), 3) * z * CF * pow(NQCD, -1)) + 5. / 8. * pow(ln(z), 3) * z * CF * NQCD + (- 2 * ln(z) * Li2(z) * CF * pow(NQCD, -1)) + 3 * ln(z) * Li2(z) * CF * NQCD + (- 2 * ln(z) * Li2(z) * z * CF * pow(NQCD, -1)) + 3 * ln(z) * Li2(z) * z * CF * NQCD + (- Li3(1 - z) * CF * pow(NQCD, -1)) + (- 2 * Li3(1 - z) * CF * NQCD) + (- Li3(1 - z) * z * CF * pow(NQCD, -1)) + (- 2 * Li3(1 - z) * z * CF * NQCD) + 6 * Li3(z) * CF * pow(NQCD, -1) + (- 8 * Li3(z) * CF * NQCD) + 6 * Li3(z) * z * CF * pow(NQCD, -1) + (- 8 * Li3(z) * z * CF * NQCD) + (- 9. / 2. * Li2(z) * CF * pow(NQCD, -1)) + 7. / 2. * Li2(z) * CF * NQCD + (- Li2(z) * z * CF * NQCD) + 10 / (1 - z) * zeta3 * CF * pow(NQCD, -1) + (- 14 / (1 - z) * zeta3 * CF * NQCD) + (- 1. / 4. / (1 - z) * pow(pi, 2) * CF * pow(NQCD, -1)) + 1. / 4. / (1 - z) * pow(pi, 2) * CF * NQCD + (- 1. / 6. / (1 - z) * ln(1 - z) * pow(pi, 2) * CF * pow(NQCD, -1)) +  + (-1. / 6. / (1 - z) * ln(1 - z) * pow(pi, 2) * CF * NQCD) + 1 / (1 - z) * ln(1 - z) * Li2(z) * CF * pow(NQCD, -1) + 1 / (1 - z) * ln(1 - z) * Li2(z) * CF * NQCD + 19. / 2. / (1 - z) * ln(z) * CF * pow(NQCD, -1) + (- 113. / 18. / (1 - z) * ln(z) * CF * NQCD) + (- 5. / 9. / (1 - z) * ln(z) * CF * NF) + 1. / 2. / (1 - z) * ln(z) * pow(pi, 2) * CF * pow(NQCD, -1) + (- 5. / 6. / (1 - z) * ln(z) * pow(pi, 2) * CF * NQCD) + (- 1. / 2. / (1 - z) * ln(z) * pow(ln(1 - z), 2) * CF * pow(NQCD, -1)) + 5. / 2. / (1 - z) * ln(z) * pow(ln(1 - z), 2) * CF * NQCD + (- 9. / 8. / (1 - z) * pow(ln(z), 2) * CF * pow(NQCD, -1)) + 49. / 24. / (1 - z) * pow(ln(z), 2) * CF * NQCD + (- 1. / 6. / (1 - z) * pow(ln(z), 2) * CF * NF) + 1. / 2. / (1 - z) * pow(ln(z), 2) * ln(1 - z) * CF * pow(NQCD, -1) + (- 1. / 2. / (1 - z) * pow(ln(z), 2) * ln(1 - z) * CF * NQCD) + 5. / 3. / (1 - z) * pow(ln(z), 3) * CF * pow(NQCD, -1) + (- 5. / 6. / (1 - z) * pow(ln(z), 3) * CF * NQCD) +  + 4 / (1 - z) * ln(z) * Li2(z) * CF * pow(NQCD, -1) + (- 6 / (1 - z) * ln(z) * Li2(z) * CF * NQCD) + 3 / (1 - z) * Li3(1 - z) * CF * pow(NQCD, -1) + 3 / (1 - z) * Li3(1 - z) * CF * NQCD + (- 10 / (1 - z) * Li3(z) * CF * pow(NQCD, -1)) + 14 / (1 - z) * Li3(z) * CF * NQCD + 3. / 2. / (1 - z) * Li2(z) * CF * pow(NQCD, -1) + (- 3. / 2. / (1 - z) * Li2(z) * CF * NQCD);
    return res;
}

double DL_RG_001(double x, double z, double NF) {
    double res = 0.0;
    res = 7. / 2. * lmua * CF * pow(NQCD, -1) + (-169. / 18. * lmua * CF * NQCD) + 2. / 9. * lmua * CF * NF + 25. / 2. * lmua * z * CF * pow(NQCD, -1) + 149. / 18. * lmua * z * CF * NQCD + (- 22. / 9. * lmua * z * CF * NF) + 1. / 2. * lmua * pow(pi, 2) * CF * pow(NQCD, -1) + (- 5. / 6. * lmua * pow(pi, 2) * CF * NQCD) + 1. / 2. * lmua * pow(pi, 2) * z * CF * pow(NQCD, -1) + (- 5. / 6. * lmua * pow(pi, 2) * z * CF * NQCD) + (- 3. / 2. * lmua * ln(1 - z) * CF * pow(NQCD, -1)) + 3. / 2. * lmua * ln(1 - z) * CF * NQCD + (- 3. / 2. * lmua * ln(1 - z) * z * CF * pow(NQCD, -1)) + 3. / 2. * lmua * ln(1 - z) * z * CF * NQCD + (- 3 * lmua * pow(ln(1 - z), 2) * CF * pow(NQCD, -1)) + 3 * lmua * pow(ln(1 - z), 2) * CF * NQCD + (- 3 * lmua * pow(ln(1 - z), 2) * z * CF * pow(NQCD, -1)) + 3 * lmua * pow(ln(1 - z), 2) * z * CF * NQCD + (- lmua * Li2(z) * CF * pow(NQCD, -1)) + lmua * Li2(z) * CF * NQCD + (- lmua * Li2(z) * z * CF * pow(NQCD, -1)) + lmua * Li2(z) * z * CF * NQCD + (- 17. / 2. * ln(z) * lmua * CF * pow(NQCD, -1)) + 61. / 6. * ln(z) * lmua * CF * NQCD + (- 2. / 3. * ln(z) * lmua * CF * NF) + (- 7. / 2. * ln(z) * lmua * z * CF * pow(NQCD, -1)) + 31. / 6. * ln(z) * lmua * z * CF * NQCD + (- 2. / 3. * ln(z) * lmua * z * CF * NF) + (- 2 * ln(z) * lmua * ln(1 - z) * CF * pow(NQCD, -1)) + 2 * ln(z) * lmua * ln(1 - z) * CF * NQCD + (- 2 * ln(z) * lmua * ln(1 - z) * z * CF * pow(NQCD, -1)) + 2 * ln(z) * lmua * ln(1 - z) * z * CF * NQCD + 4 * pow(ln(z), 2) * lmua * CF * pow(NQCD, -1) + (- 3 * pow(ln(z), 2) * lmua * CF * NQCD) + 4 * pow(ln(z), 2) * lmua * z * CF * pow(NQCD, -1) + (- 3 * pow(ln(z), 2) * lmua * z * CF * NQCD) + 6 / (1 - z) * ln(z) * lmua * CF * pow(NQCD, -1) + (- 40. / 3. / (1 - z) * ln(z) * lmua * CF * NQCD) + 4. / 3. / (1 - z) * ln(z) * lmua * CF * NF + 4 / (1 - z) * ln(z) * lmua * ln(1 - z) * CF * pow(NQCD, -1) + (- 4 / (1 - z) * ln(z) * lmua * ln(1 - z) * CF * NQCD) + (- 6 / (1 - z) * pow(ln(z), 2) * lmua * CF * pow(NQCD, -1)) + 4 / (1 - z) * pow(ln(z), 2) * lmua * CF * NQCD;
    return res;
}

double DL_RG_002(double x, double z, double NF) {
    double res = 0.0;
    res = 5 * pow(lmua, 2) * CF * pow(NQCD, -1) + (- 26. / 3. * pow(lmua, 2) * CF * NQCD) + 2. / 3. * pow(lmua, 2) * CF * NF + pow(lmua, 2) * z * CF * pow(NQCD, -1) + (- 14. / 3. * pow(lmua, 2) * z * CF * NQCD) + 2. / 3. * pow(lmua, 2) * z * CF * NF + 4 * pow(lmua, 2) * ln(1 - z) * CF * pow(NQCD, -1) + (- 4 * pow(lmua, 2) * ln(1 - z) * CF * NQCD) + 4 * pow(lmua, 2) * ln(1 - z) * z * CF * pow(NQCD, -1) + (- 4 * pow(lmua, 2) * ln(1 - z) * z * CF * NQCD) + (- 3 * ln(z) * pow(lmua, 2) * CF * pow(NQCD, -1)) + 3 * ln(z) * pow(lmua, 2) * CF * NQCD + (- 3 * ln(z) * pow(lmua, 2) * z * CF * pow(NQCD, -1)) + 3 * ln(z) * pow(lmua, 2) * z * CF * NQCD + 4 / (1 - z) * ln(z) * pow(lmua, 2) * CF * pow(NQCD, -1) + (- 4 / (1 - z) * ln(z) * pow(lmua, 2) * CF * NQCD);
    return res;
}

double DL_RG_010(double x, double z, double NF) {
    double res = 0.0;
    res = 3. / 2. * lmuf * CF * pow(NQCD, -1) + (- 3. / 2. * lmuf * CF * NQCD) + (- 3. / 2. * lmuf * z * CF * pow(NQCD, -1)) + 3. / 2. * lmuf * z * CF * NQCD + 1. / 3. * lmuf * pow(pi, 2) * CF * pow(NQCD, -1) + (- 1. / 3. * lmuf * pow(pi, 2) * CF * NQCD) + 1. / 3. * lmuf * pow(pi, 2) * z * CF * pow(NQCD, -1) + (- 1. / 3. * lmuf * pow(pi, 2) * z * CF * NQCD) + (- 3. / 2. * lmuf * ln(1 - z) * CF * pow(NQCD, -1)) + 3. / 2. * lmuf * ln(1 - z) * CF * NQCD + (- 3. / 2. * lmuf * ln(1 - z) * z * CF * pow(NQCD, -1)) + 3. / 2. * lmuf * ln(1 - z) * z * CF * NQCD + (- 3. / 2. * ln(z) * lmuf * CF * pow(NQCD, -1)) + 3. / 2. * ln(z) * lmuf * CF * NQCD + (- 3. / 2. * ln(z) * lmuf * z * CF * pow(NQCD, -1)) + 3. / 2. * ln(z) * lmuf * z * CF * NQCD + 3 / (1 - z) * ln(z) * lmuf * CF * pow(NQCD, -1) + (- 3 / (1 - z) * ln(z) * lmuf * CF * NQCD);
    return res;
}

double DL_RG_011(double x, double z, double NF) {
    double res = 0.0;
    res = 3 * lmuf * lmua * CF * pow(NQCD, -1) + (- 3 * lmuf * lmua * CF * NQCD) + 3 * lmuf * lmua * z * CF * pow(NQCD, -1) + (- 3 * lmuf * lmua * z * CF * NQCD);
    return res;
}

double DL_RG_100(double x, double z, double NF) {
    double res = 0.0;
    res = 11. / 3. * lmur * CF * NQCD + (- 2. / 3. * lmur * CF * NF) + (- 11. / 3. * lmur * z * CF * NQCD) + 2. / 3. * lmur * z * CF * NF + (- 11. / 3. * lmur * ln(1 - z) * CF * NQCD) + 2. / 3. * lmur * ln(1 - z) * CF * NF + (- 11. / 3. * lmur * ln(1 - z) * z * CF * NQCD) + 2. / 3. * lmur * ln(1 - z) * z * CF * NF + (- 11. / 3. * ln(z) * lmur * CF * NQCD) + 2. / 3. * ln(z) * lmur * CF * NF + (- 11. / 3. * ln(z) * lmur * z * CF * NQCD) + 2. / 3. * ln(z) * lmur * z * CF * NF + 22. / 3. / (1 - z) * ln(z) * lmur * CF * NQCD + (- 4. / 3. / (1 - z) * ln(z) * lmur * CF * NF);
    return res;
}

double DL_RG_101(double x, double z, double NF) {
    double res = 0.0;
    res = 22. / 3. * lmur * lmua * CF * NQCD + (- 4. / 3. * lmur * lmua * CF * NF) + 22. / 3. * lmur * lmua * z * CF * NQCD + (- 4. / 3. * lmur * lmua * z * CF * NF);
    return res;
}

double D0_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-CF * pow(NQCD, -1)) + 19. / 9. * CF * NQCD + 2. / 9. * CF * NF + (- 7 * z * CF * pow(NQCD, -1)) + (- 14. / 9. * z * CF * NQCD) + 8. / 9. * z * CF * NF + (- 5. / 12. * pow(pi, 2) * CF * pow(NQCD, -1)) + 7. / 12. * pow(pi, 2) * CF * NQCD + (- 5. / 12. * pow(pi, 2) * z * CF * pow(NQCD, -1)) + 7. / 12. * pow(pi, 2) * z * CF * NQCD + 11. / 6. * ln(1 - z) * CF * NQCD + (- 1. / 3. * ln(1 - z) * CF * NF) + 11. / 6. * ln(1 - z) * z * CF * NQCD + (- 1. / 3. * ln(1 - z) * z * CF * NF) + 3. / 2. * pow(ln(1 - z), 2) * CF * pow(NQCD, -1) + (- 3. / 2. * pow(ln(1 - z), 2) * CF * NQCD) + 3. / 2. * pow(ln(1 - z), 2) * z * CF * pow(NQCD, -1) + (- 3. / 2. * pow(ln(1 - z), 2) * z * CF * NQCD) +  + 7. / 2. * ln(z) * CF * pow(NQCD, -1) + (- 5. / 2. * ln(z) * CF * NQCD) + ln(z) * z * CF * pow(NQCD, -1) + ln(z) * ln(1 - z) * CF * pow(NQCD, -1) + (- ln(z) * ln(1 - z) * CF * NQCD) + ln(z) * ln(1 - z) * z * CF * pow(NQCD, -1) + (- ln(z) * ln(1 - z) * z * CF * NQCD) + (- 2 * pow(ln(z), 2) * CF * pow(NQCD, -1)) + 3. / 2. * pow(ln(z), 2) * CF * NQCD + (- 2 * pow(ln(z), 2) * z * CF * pow(NQCD, -1)) + 3. / 2. * pow(ln(z), 2) * z * CF * NQCD + 1. / 2. * Li2(z) * CF * pow(NQCD, -1) + (- 1. / 2. * Li2(z) * CF * NQCD) + 1. / 2. * Li2(z) * z * CF * pow(NQCD, -1) + (- 1. / 2. * Li2(z) * z * CF * NQCD) + (- 3. / 2. / (1 - z) * ln(z) * CF * pow(NQCD, -1)) + 3. / 2. / (1 - z) * ln(z) * CF * NQCD + (- 2 / (1 - z) * ln(z) * ln(1 - z) * CF * pow(NQCD, -1)) + 2 / (1 - z) * ln(z) * ln(1 - z) * CF * NQCD + 3 / (1 - z) * pow(ln(z), 2) * CF * pow(NQCD, -1) + (- 2 / (1 - z) * pow(ln(z), 2) * CF * NQCD);
    return res;
}

double D0_RG_001(double x, double z, double NF) {
    double res = 0.0;
    res = (- 7. / 2. * lmua * CF * pow(NQCD, -1)) + 7. / 2. * lmua * CF * NQCD + 1. / 2. * lmua * z * CF * pow(NQCD, -1) + (- 1. / 2. * lmua * z * CF * NQCD) + (- 4 * lmua * ln(1 - z) * CF * pow(NQCD, -1)) + 4 * lmua * ln(1 - z) * CF * NQCD + (- 4 * lmua * ln(1 - z) * z * CF * pow(NQCD, -1)) + 4 * lmua * ln(1 - z) * z * CF * NQCD + 3 * ln(z) * lmua * CF * pow(NQCD, -1) + (- 3 * ln(z) * lmua * CF * NQCD) + 3 * ln(z) * lmua * z * CF * pow(NQCD, -1) + (- 3 * ln(z) * lmua * z * CF * NQCD) + (- 4 / (1 - z) * ln(z) * lmua * CF * pow(NQCD, -1)) + 4 / (1 - z) * ln(z) * lmua * CF * NQCD;
    return res;
}

double D0_RG_010(double x, double z, double NF) {
    double res = 0.0;
    res = 1. / 2. * lmuf * CF * pow(NQCD, -1) + (- 1. / 2. * lmuf * CF * NQCD) + (- 7. / 2. * lmuf * z * CF * pow(NQCD, -1)) + 7. / 2. * lmuf * z * CF * NQCD + (- 2 * lmuf * ln(1 - z) * CF * pow(NQCD, -1)) + 2 * lmuf * ln(1 - z) * CF * NQCD + (- 2 * lmuf * ln(1 - z) * z * CF * pow(NQCD, -1)) + 2 * lmuf * ln(1 - z) * z * CF * NQCD + (- 2 * ln(z) * lmuf * CF * pow(NQCD, -1)) + 2 * ln(z) * lmuf * CF * NQCD + (- 2 * ln(z) * lmuf * z * CF * pow(NQCD, -1)) + 2 * ln(z) * lmuf * z * CF * NQCD + 4 / (1 - z) * ln(z) * lmuf * CF * pow(NQCD, -1) + (- 4 / (1 - z) * ln(z) * lmuf * CF * NQCD);
    return res;
}

double D0_RG_011(double x, double z, double NF) {
    double res = 0.0;
    res = 4 * lmuf * lmua * CF * pow(NQCD, -1) + (- 4 * lmuf * lmua * CF * NQCD) + 4 * lmuf * lmua * z * CF * pow(NQCD, -1) + (- 4 * lmuf * lmua * z * CF * NQCD);
    return res;
}

double D0_RG_100(double x, double z, double NF) {
    double res = 0.0;
    res = (- 11. / 3. * lmur * CF * NQCD) + 2. / 3. * lmur * CF * NF + (- 11. / 3. * lmur * z * CF * NQCD) + 2. / 3. * lmur * z * CF * NF;
    return res;
}

double D1_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = 11. / 6. * CF * NQCD + (- 1. / 3. * CF * NF) + 11. / 6. * z * CF * NQCD + (- 1. / 3. * z * CF * NF) + 3 * ln(1 - z) * CF * pow(NQCD, -1) + (- 3 * ln(1 - z) * CF * NQCD) + 3 * ln(1 - z) * z * CF * pow(NQCD, -1) + (- 3 * ln(1 - z) * z * CF * NQCD) + (- 1. / 2. * ln(z) * CF * pow(NQCD, -1)) + 1. / 2. * ln(z) * CF * NQCD + (- 1. / 2. * ln(z) * z * CF * pow(NQCD, -1)) + 1. / 2. * ln(z) * z * CF * NQCD;
    return res;
}

double D1_RG_001(double x, double z, double NF) {
    double res = 0.0;
    res = (- 2 * lmua * CF * pow(NQCD, -1)) + 2 * lmua * CF * NQCD + (- 2 * lmua * z * CF * pow(NQCD, -1)) + 2 * lmua * z * CF * NQCD;
    return res;
}

double D1_RG_010(double x, double z, double NF) {
    double res = 0.0;
    res = (- 4 * lmuf * CF * pow(NQCD, -1)) + 4 * lmuf * CF * NQCD + (- 4 * lmuf * z * CF * pow(NQCD, -1)) + 4 * lmuf * z * CF * NQCD;
    return res;
}

double D2_RG_000(double x, double z, double NF) {
    double res = 0.0;
    res = 3. / 2. * CF * pow(NQCD, -1) + (- 3. / 2. * CF * NQCD) + 3. / 2. * z * CF * pow(NQCD, -1) + (- 3. / 2. * z * CF * NQCD);
    return res;
}

double RG_DL_000(double x, double z, double NF) {
    double res = 0.0;
    res = 29. / 4. * CF * pow(NQCD, -1) + (- 91. / 108. * CF * NQCD) + (- 37. / 54. * CF * NF) + (- 31. / 4. * x * CF * pow(NQCD, -1)) + 845. / 108. * x * CF * NQCD + (- 19. / 54. * x * CF * NF) + 11. / 2. * zeta3 * CF * pow(NQCD, -1) + (- 8 * zeta3 * CF * NQCD) + 11. / 2. * zeta3 * x * CF * pow(NQCD, -1) + (- 8 * zeta3 * x * CF * NQCD) + (- 1. / 6. * pow(pi, 2) * CF * pow(NQCD, -1)) + (- 13. / 36. * pow(pi, 2) * CF * NQCD) + 1. / 9. * pow(pi, 2) * CF * NF + 5. / 12. * pow(pi, 2) * x * CF * pow(NQCD, -1) + (- 7. / 9. * pow(pi, 2) * x * CF * NQCD) + 1. / 9. * pow(pi, 2) * x * CF * NF + (- ln(1 - x) * CF * pow(NQCD, -1)) + 19. / 9. * ln(1 - x) * CF * NQCD + 2. / 9. * ln(1 - x) * CF * NF + (- 27. / 4. * ln(1 - x) * x * CF * pow(NQCD, -1)) + (- 47. / 36. * ln(1 - x) * x * CF * NQCD) + 8. / 9. * ln(1 - x) * x * CF * NF + (- 7. / 12. * ln(1 - x) * pow(pi, 2) * CF * pow(NQCD, -1)) + 7. / 12. * ln(1 - x) * pow(pi, 2) * CF * NQCD + (- 7. / 12. * ln(1 - x) * pow(pi, 2) * x * CF * pow(NQCD, -1)) + 7. / 12. * ln(1 - x) * pow(pi, 2) * x * CF * NQCD + 11. / 12. * pow(ln(1 - x), 2) * CF * NQCD + (- 1. / 6. * pow(ln(1 - x), 2) * CF * NF) + 11. / 12. * pow(ln(1 - x), 2) * x * CF * NQCD + (- 1. / 6. * pow(ln(1 - x), 2) * x * CF * NF) + 1. / 2. * pow(ln(1 - x), 3) * CF * pow(NQCD, -1) + (- 1. / 2. * pow(ln(1 - x), 3) * CF * NQCD) + 1. / 2. * pow(ln(1 - x), 3) * x * CF * pow(NQCD, -1) + (- 1. / 2. * pow(ln(1 - x), 3) * x * CF * NQCD) + 1. / 2. * ln(1 - x) * Li2(1 - x) * CF * pow(NQCD, -1) + (- 1. / 2. * ln(1 - x) * Li2(1 - x) * CF * NQCD) + 1. / 2. * ln(1 - x) * Li2(1 - x) * x * CF * pow(NQCD, -1) + (- 1. / 2. * ln(1 - x) * Li2(1 - x) * x * CF * NQCD) + 3. / 2. * ln(1 - x) * Li2(x) * CF * pow(NQCD, -1) + (- 1. / 2. * ln(1 - x) * Li2(x) * CF * NQCD) + 3. / 2. * ln(1 - x) * Li2(x) * x * CF * pow(NQCD, -1) + (- 1. / 2. * ln(1 - x) * Li2(x) * x * CF * NQCD) +  +  + 21. / 4. * ln(x) * CF * pow(NQCD, -1) + 1. / 12. * ln(x) * CF * NQCD + (- 5. / 6. * ln(x) * CF * NF) +  + 11 * ln(x) * x * CF * pow(NQCD, -1) + 13. / 6. * ln(x) * x * CF * NQCD + (- 7. / 6. * ln(x) * x * CF * NF) + 2. / 3. * ln(x) * pow(pi, 2) * CF * pow(NQCD, -1) + (- ln(x) * pow(pi, 2) * CF * NQCD) + 2. / 3. * ln(x) * pow(pi, 2) * x * CF * pow(NQCD, -1) + (- ln(x) * pow(pi, 2) * x * CF * NQCD) + 1. / 2. * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) + (- 7. / 3. * ln(x) * ln(1 - x) * CF * NQCD) + 1. / 3. * ln(x) * ln(1 - x) * CF * NF + (- 1. / 2. * ln(x) * ln(1 - x) * x * CF * pow(NQCD, -1)) + (- 4. / 3. * ln(x) * ln(1 - x) * x * CF * NQCD) + 1. / 3. * ln(x) * ln(1 - x) * x * CF * NF + (- 1. / 2. * ln(x) * pow(ln(1 - x), 2) * CF * pow(NQCD, -1)) + 3. / 2. * ln(x) * pow(ln(1 - x), 2) * CF * NQCD + (- 1. / 2. * ln(x) * pow(ln(1 - x), 2) * x * CF * pow(NQCD, -1)) + 3. / 2. * ln(x) * pow(ln(1 - x), 2) * x * CF * NQCD +  + 1. / 4. * pow(ln(x), 2) * CF * pow(NQCD, -1) + 49. / 24. * pow(ln(x), 2) * CF * NQCD + (- 5. / 12. * pow(ln(x), 2) * CF * NF) + (- 3. / 2. * pow(ln(x), 2) * x * CF * pow(NQCD, -1)) + 55. / 24. * pow(ln(x), 2) * x * CF * NQCD + (- 5. / 12. * pow(ln(x), 2) * x * CF * NF) + 9. / 4. * pow(ln(x), 2) * ln(1 - x) * CF * pow(NQCD, -1) + (- 5. / 4. * pow(ln(x), 2) * ln(1 - x) * CF * NQCD) + 9. / 4. * pow(ln(x), 2) * ln(1 - x) * x * CF * pow(NQCD, -1) + (- 5. / 4. * pow(ln(x), 2) * ln(1 - x) * x * CF * NQCD) + (- 5. / 24. * pow(ln(x), 3) * CF * pow(NQCD, -1)) + 11. / 24. * pow(ln(x), 3) * CF * NQCD + (- 5. / 24. * pow(ln(x), 3) * x * CF * pow(NQCD, -1)) + 11. / 24. * pow(ln(x), 3) * x * CF * NQCD + 2 * ln(x) * Li2(x) * CF * pow(NQCD, -1) + 2 * ln(x) * Li2(x) * x * CF * pow(NQCD, -1) + 2 * Li3(1 - x) * CF * pow(NQCD, -1) + 2 * Li3(1 - x) * CF * NQCD + 2 * Li3(1 - x) * x * CF * pow(NQCD, -1) + 2 * Li3(1 - x) * x * CF * NQCD + (- 7. / 2. * Li3(x) * CF * pow(NQCD, -1)) + 5. / 2. * Li3(x) * CF * NQCD + (- 7. / 2. * Li3(x) * x * CF * pow(NQCD, -1)) + 5. / 2. * Li3(x) * x * CF * NQCD + 5. / 6. * Li2(x) * CF * NQCD + (- 1. / 3. * Li2(x) * CF * NF) + (- 3. / 2. * Li2(x) * x * CF * pow(NQCD, -1)) + 7. / 3. * Li2(x) * x * CF * NQCD + (- 1. / 3. * Li2(x) * x * CF * NF) + (- 7 / (1 - x) * zeta3 * CF * pow(NQCD, -1)) + 5 / (1 - x) * zeta3 * CF * NQCD +  + 1. / 4. / (1 - x) * pow(pi, 2) * CF * pow(NQCD, -1) + 13. / 36. / (1 - x) * pow(pi, 2) * CF * NQCD + (- 1. / 9. / (1 - x) * pow(pi, 2) * CF * NF) + 1. / 6. / (1 - x) * ln(1 - x) * pow(pi, 2) * CF * pow(NQCD, -1) + 1. / 6. / (1 - x) * ln(1 - x) * pow(pi, 2) * CF * NQCD + (- 1 / (1 - x) * ln(1 - x) * Li2(x) * CF * pow(NQCD, -1)) + (- 1 / (1 - x) * ln(1 - x) * Li2(x) * CF * NQCD) + (- 10 / (1 - x) * ln(x) * CF * pow(NQCD, -1)) + (- 5. / 3. / (1 - x) * ln(x) * CF * NQCD) + 5. / 3. / (1 - x) * ln(x) * CF * NF + (- 1 / (1 - x) * ln(x) * pow(pi, 2) * CF * pow(NQCD, -1)) + 5. / 3. / (1 - x) * ln(x) * pow(pi, 2) * CF * NQCD + 11. / 3. / (1 - x) * ln(x) * ln(1 - x) * CF * NQCD + (- 2. / 3. / (1 - x) * ln(x) * ln(1 - x) * CF * NF) + 5. / 2. / (1 - x) * ln(x) * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) + (- 9. / 2. / (1 - x) * ln(x) * pow(ln(1 - x), 2) * CF * NQCD) + (- 9. / 8. / (1 - x) * pow(ln(x), 2) * CF * pow(NQCD, -1)) + (- 83. / 24. / (1 - x) * pow(ln(x), 2) * CF * NQCD) + 5. / 6. / (1 - x) * pow(ln(x), 2) * CF * NF + (- 9. / 2. / (1 - x) * pow(ln(x), 2) * ln(1 - x) * CF * pow(NQCD, -1)) +  + 5. / 2. / (1 - x) * pow(ln(x), 2) * ln(1 - x) * CF * NQCD + (- 1. / 2. / (1 - x) * pow(ln(x), 3) * CF * NQCD) + (- 5 / (1 - x) * ln(x) * Li2(x) * CF * pow(NQCD, -1)) + 1 / (1 - x) * ln(x) * Li2(x) * CF * NQCD + (- 3 / (1 - x) * Li3(1 - x) * CF * pow(NQCD, -1)) + (- 5 / (1 - x) * Li3(1 - x) * CF * NQCD) + 7 / (1 - x) * Li3(x) * CF * pow(NQCD, -1) + (- 5 / (1 - x) * Li3(x) * CF * NQCD) + (- 3. / 2. / (1 - x) * Li2(x) * CF * pow(NQCD, -1)) + (- 13. / 6. / (1 - x) * Li2(x) * CF * NQCD) + 2. / 3. / (1 - x) * Li2(x) * CF * NF;
    return res;
}

double RG_DL_001(double x, double z, double NF) {
    double res = 0.0;
    res = 3. / 2. * lmua * CF * pow(NQCD, -1) + (-3. / 2. * lmua * CF * NQCD) + (- 3. / 2. * lmua * x * CF * pow(NQCD, -1)) + 3. / 2. * lmua * x * CF * NQCD + 1. / 3. * lmua * pow(pi, 2) * CF * pow(NQCD, -1) + (- 1. / 3. * lmua * pow(pi, 2) * CF * NQCD) + 1. / 3. * lmua * pow(pi, 2) * x * CF * pow(NQCD, -1) + (- 1. / 3. * lmua * pow(pi, 2) * x * CF * NQCD) + (- 3. / 2. * lmua * ln(1 - x) * CF * pow(NQCD, -1)) + 3. / 2. * lmua * ln(1 - x) * CF * NQCD + (- 3. / 2. * lmua * ln(1 - x) * x * CF * pow(NQCD, -1)) + 3. / 2. * lmua * ln(1 - x) * x * CF * NQCD + 3. / 2. * ln(x) * lmua * CF * pow(NQCD, -1) + (- 3. / 2. * ln(x) * lmua * CF * NQCD) + 3. / 2. * ln(x) * lmua * x * CF * pow(NQCD, -1) + (- 3. / 2. * ln(x) * lmua * x * CF * NQCD) + (- 3 / (1 - x) * ln(x) * lmua * CF * pow(NQCD, -1)) + 3 / (1 - x) * ln(x) * lmua * CF * NQCD;
    return res;
}

double RG_DL_010(double x, double z, double NF) {
    double res = 0.0;
    res = 7. / 2. * lmuf * CF * pow(NQCD, -1) + (- 169. / 18. * lmuf * CF * NQCD) + 2. / 9. * lmuf * CF * NF + 25. / 2. * lmuf * x * CF * pow(NQCD, -1) + 149. / 18. * lmuf * x * CF * NQCD + (- 22. / 9. * lmuf * x * CF * NF) + 1. / 2. * lmuf * pow(pi, 2) * CF * pow(NQCD, -1) + (- 5. / 6. * lmuf * pow(pi, 2) * CF * NQCD) + 1. / 2. * lmuf * pow(pi, 2) * x * CF * pow(NQCD, -1) + (- 5. / 6. * lmuf * pow(pi, 2) * x * CF * NQCD) + (- 3. / 2. * lmuf * ln(1 - x) * CF * pow(NQCD, -1)) + 3. / 2. * lmuf * ln(1 - x) * CF * NQCD + (- 3. / 2. * lmuf * ln(1 - x) * x * CF * pow(NQCD, -1)) + 3. / 2. * lmuf * ln(1 - x) * x * CF * NQCD + (- 3 * lmuf * pow(ln(1 - x), 2) * CF * pow(NQCD, -1)) + 3 * lmuf * pow(ln(1 - x), 2) * CF * NQCD + (- 3 * lmuf * pow(ln(1 - x), 2) * x * CF * pow(NQCD, -1)) + 3 * lmuf * pow(ln(1 - x), 2) * x * CF * NQCD + (- lmuf * Li2(x) * CF * pow(NQCD, -1)) + lmuf * Li2(x) * CF * NQCD + (- lmuf * Li2(x) * x * CF * pow(NQCD, -1)) + lmuf * Li2(x) * x * CF * NQCD + 3. / 2. * ln(x) * lmuf * CF * pow(NQCD, -1) + 1. / 6. * ln(x) * lmuf * CF * NQCD + (- 2. / 3. * ln(x) * lmuf * CF * NF) + (- 3. / 2. * ln(x) * lmuf * x * CF * pow(NQCD, -1)) + 19. / 6. * ln(x) * lmuf * x * CF * NQCD + (- 2. / 3. * ln(x) * lmuf * x * CF * NF) + 6 * ln(x) * lmuf * ln(1 - x) * CF * pow(NQCD, -1) + (- 6 * ln(x) * lmuf * ln(1 - x) * CF * NQCD) + 6 * ln(x) * lmuf * ln(1 - x) * x * CF * pow(NQCD, -1) + (- 6 * ln(x) * lmuf * ln(1 - x) * x * CF * NQCD) + (- 2 * pow(ln(x), 2) * lmuf * CF * pow(NQCD, -1)) + 3 * pow(ln(x), 2) * lmuf * CF * NQCD + (- 2 * pow(ln(x), 2) * lmuf * x * CF * pow(NQCD, -1)) + 3 * pow(ln(x), 2) * lmuf * x * CF * NQCD + (- 6 / (1 - x) * ln(x) * lmuf * CF * pow(NQCD, -1)) + (- 4. / 3. / (1 - x) * ln(x) * lmuf * CF * NQCD) + 4. / 3. / (1 - x) * ln(x) * lmuf * CF * NF + (- 12 / (1 - x) * ln(x) * lmuf * ln(1 - x) * CF * pow(NQCD, -1)) + 12 / (1 - x) * ln(x) * lmuf * ln(1 - x) * CF * NQCD + 2 / (1 - x) * pow(ln(x), 2) * lmuf * CF * pow(NQCD, -1) + (- 4 / (1 - x) * pow(ln(x), 2) * lmuf * CF * NQCD);
    return res;
}

double RG_DL_011(double x, double z, double NF) {
    double res = 0.0;
    res = 3 * lmuf * lmua * CF * pow(NQCD, -1) + (-3 * lmuf * lmua * CF * NQCD) + 3 * lmuf * lmua * x * CF * pow(NQCD, -1) + (- 3 * lmuf * lmua * x * CF * NQCD);
    return res;
}

double RG_DL_020(double x, double z, double NF) {
    double res = 0.0;
    res = 5 * pow(lmuf, 2) * CF * pow(NQCD, -1) + (- 26. / 3. * pow(lmuf, 2) * CF * NQCD) + 2. / 3. * pow(lmuf, 2) * CF * NF + pow(lmuf, 2) * x * CF * pow(NQCD, -1) + (- 14. / 3. * pow(lmuf, 2) * x * CF * NQCD) + 2. / 3. * pow(lmuf, 2) * x * CF * NF + 4 * pow(lmuf, 2) * ln(1 - x) * CF * pow(NQCD, -1) + (- 4 * pow(lmuf, 2) * ln(1 - x) * CF * NQCD) + 4 * pow(lmuf, 2) * ln(1 - x) * x * CF * pow(NQCD, -1) + (- 4 * pow(lmuf, 2) * ln(1 - x) * x * CF * NQCD) + (- 3 * ln(x) * pow(lmuf, 2) * CF * pow(NQCD, -1)) + 3 * ln(x) * pow(lmuf, 2) * CF * NQCD + (- 3 * ln(x) * pow(lmuf, 2) * x * CF * pow(NQCD, -1)) + 3 * ln(x) * pow(lmuf, 2) * x * CF * NQCD + 4 / (1 - x) * ln(x) * pow(lmuf, 2) * CF * pow(NQCD, -1) + (- 4 / (1 - x) * ln(x) * pow(lmuf, 2) * CF * NQCD);
    return res;
}

double RG_DL_100(double x, double z, double NF) {
    double res = 0.0;
    res = 11. / 3. * lmur * CF * NQCD + (- 2. / 3. * lmur * CF * NF) + (- 11. / 3. * lmur * x * CF * NQCD) + 2. / 3. * lmur * x * CF * NF + (- 11. / 3. * lmur * ln(1 - x) * CF * NQCD) + 2. / 3. * lmur * ln(1 - x) * CF * NF + (- 11. / 3. * lmur * ln(1 - x) * x * CF * NQCD) + 2. / 3. * lmur * ln(1 - x) * x * CF * NF + 11. / 3. * ln(x) * lmur * CF * NQCD + (- 2. / 3. * ln(x) * lmur * CF * NF) + 11. / 3. * ln(x) * lmur * x * CF * NQCD + (- 2. / 3. * ln(x) * lmur * x * CF * NF) + (- 22. / 3. / (1 - x) * ln(x) * lmur * CF * NQCD) + 4. / 3. / (1 - x) * ln(x) * lmur * CF * NF;
    return res;
}

double RG_DL_110(double x, double z, double NF) {
    double res = 0.0;
    res = 22. / 3. * lmur * lmuf * CF * NQCD + (- 4. / 3. * lmur * lmuf * CF * NF) + 22. / 3. * lmur * lmuf * x * CF * NQCD + (- 4. / 3. * lmur * lmuf * x * CF * NF);
    return res;
}

double RG_D0_000(double x, double z, double NF) {
    double res = 0.0;
    res = (-CF * pow(NQCD, -1)) + 19. / 9. * CF * NQCD + 2. / 9. * CF * NF + (- 7 * x * CF * pow(NQCD, -1)) + (- 14. / 9. * x * CF * NQCD) + 8. / 9. * x * CF * NF + (- 5. / 12. * pow(pi, 2) * CF * pow(NQCD, -1)) + 7. / 12. * pow(pi, 2) * CF * NQCD + (- 5. / 12. * pow(pi, 2) * x * CF * pow(NQCD, -1)) + 7. / 12. * pow(pi, 2) * x * CF * NQCD + 11. / 6. * ln(1 - x) * CF * NQCD + (- 1. / 3. * ln(1 - x) * CF * NF) + 11. / 6. * ln(1 - x) * x * CF * NQCD + (- 1. / 3. * ln(1 - x) * x * CF * NF) + 3. / 2. * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) + (- 3. / 2. * pow(ln(1 - x), 2) * CF * NQCD) + 3. / 2. * pow(ln(1 - x), 2) * x * CF * pow(NQCD, -1) + (- 3. / 2. * pow(ln(1 - x), 2) * x * CF * NQCD) +  + (- 8. / 3. * ln(x) * CF * NQCD) + 2. / 3. * ln(x) * CF * NF + 3. / 2. * ln(x) * x * CF * pow(NQCD, -1) + (- 25. / 6. * ln(x) * x * CF * NQCD) + 2. / 3. * ln(x) * x * CF * NF + (- 3 * ln(x) * ln(1 - x) * CF * pow(NQCD, -1)) + 3 * ln(x) * ln(1 - x) * CF * NQCD + (- 3 * ln(x) * ln(1 - x) * x * CF * pow(NQCD, -1)) + 3 * ln(x) * ln(1 - x) * x * CF * NQCD + pow(ln(x), 2) * CF * pow(NQCD, -1) + (- 3. / 2. * pow(ln(x), 2) * CF * NQCD) + pow(ln(x), 2) * x * CF * pow(NQCD, -1) + (- 3. / 2. * pow(ln(x), 2) * x * CF * NQCD) + 1. / 2. * Li2(x) * CF * pow(NQCD, -1) + (- 1. / 2. * Li2(x) * CF * NQCD) + 1. / 2. * Li2(x) * x * CF * pow(NQCD, -1) + (- 1. / 2. * Li2(x) * x * CF * NQCD) + 3. / 2. / (1 - x) * ln(x) * CF * pow(NQCD, -1) + 35. / 6. / (1 - x) * ln(x) * CF * NQCD + (- 4. / 3. / (1 - x) * ln(x) * CF * NF) + 6 / (1 - x) * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) + (- 6 / (1 - x) * ln(x) * ln(1 - x) * CF * NQCD) + (- 1 / (1 - x) * pow(ln(x), 2) * CF * pow(NQCD, -1)) + 2 / (1 - x) * pow(ln(x), 2) * CF * NQCD;
    return res;
}

double RG_D0_001(double x, double z, double NF) {
    double res = 0.0;
    res = 1. / 2. * lmua * CF * pow(NQCD, -1) + (- 1. / 2. * lmua * CF * NQCD) + (- 7. / 2. * lmua * x * CF * pow(NQCD, -1)) + 7. / 2. * lmua * x * CF * NQCD + (- 2 * lmua * ln(1 - x) * CF * pow(NQCD, -1)) + 2 * lmua * ln(1 - x) * CF * NQCD + (- 2 * lmua * ln(1 - x) * x * CF * pow(NQCD, -1)) + 2 * lmua * ln(1 - x) * x * CF * NQCD + 2 * ln(x) * lmua * CF * pow(NQCD, -1) + (- 2 * ln(x) * lmua * CF * NQCD) + 2 * ln(x) * lmua * x * CF * pow(NQCD, -1) + (- 2 * ln(x) * lmua * x * CF * NQCD) + (- 4 / (1 - x) * ln(x) * lmua * CF * pow(NQCD, -1)) + 4 / (1 - x) * ln(x) * lmua * CF * NQCD;
    return res;
}

double RG_D0_010(double x, double z, double NF) {
    double res = 0.0;
    res = (- 7. / 2. * lmuf * CF * pow(NQCD, -1)) + 7. / 2. * lmuf * CF * NQCD + 1. / 2. * lmuf * x * CF * pow(NQCD, -1) + (- 1. / 2. * lmuf * x * CF * NQCD) + (- 4 * lmuf * ln(1 - x) * CF * pow(NQCD, -1)) + 4 * lmuf * ln(1 - x) * CF * NQCD + (- 4 * lmuf * ln(1 - x) * x * CF * pow(NQCD, -1)) + 4 * lmuf * ln(1 - x) * x * CF * NQCD + 3 * ln(x) * lmuf * CF * pow(NQCD, -1) + (- 3 * ln(x) * lmuf * CF * NQCD) + 3 * ln(x) * lmuf * x * CF * pow(NQCD, -1) + (- 3 * ln(x) * lmuf * x * CF * NQCD) + (- 4 / (1 - x) * ln(x) * lmuf * CF * pow(NQCD, -1)) + 4 / (1 - x) * ln(x) * lmuf * CF * NQCD;
    return res;
}

double RG_D0_011(double x, double z, double NF) {
    double res = 0.0;
    res = 4 * lmuf * lmua * CF * pow(NQCD, -1) + (- 4 * lmuf * lmua * CF * NQCD) + 4 * lmuf * lmua * x * CF * pow(NQCD, -1) + (- 4 * lmuf * lmua * x * CF * NQCD);
    return res;
}

double RG_D0_100(double x, double z, double NF) {
    double res = 0.0;
    res = (- 11. / 3. * lmur * CF * NQCD) + 2. / 3. * lmur * CF * NF + (- 11. / 3. * lmur * x * CF * NQCD) + 2. / 3. * lmur * x * CF * NF;
    return res;
}

double RG_D1_000(double x, double z, double NF) {
    double res = 0.0;
    res = 11. / 6. * CF * NQCD + (- 1. / 3. * CF * NF) + 11. / 6. * x * CF * NQCD + (- 1. / 3. * x * CF * NF) + 3 * ln(1 - x) * CF * pow(NQCD, -1) + (- 3 * ln(1 - x) * CF * NQCD) + 3 * ln(1 - x) * x * CF * pow(NQCD, -1) + (- 3 * ln(1 - x) * x * CF * NQCD) + (- 5. / 2. * ln(x) * CF * pow(NQCD, -1)) + 5. / 2. * ln(x) * CF * NQCD + (- 5. / 2. * ln(x) * x * CF * pow(NQCD, -1)) + 5. / 2. * ln(x) * x * CF * NQCD + 4 / (1 - x) * ln(x) * CF * pow(NQCD, -1) + (- 4 / (1 - x) * ln(x) * CF * NQCD);
    return res;
}

double RG_D1_001(double x, double z, double NF) {
    double res = 0.0;
    res = (- 4 * lmua * CF * pow(NQCD, -1)) + 4 * lmua * CF * NQCD + (- 4 * lmua * x * CF * pow(NQCD, -1)) + 4 * lmua * x * CF * NQCD;
    return res;
}

double RG_D1_010(double x, double z, double NF) {
    double res = 0.0;
    res = (- 2 * lmuf * CF * pow(NQCD, -1)) + 2 * lmuf * CF * NQCD + (- 2 * lmuf * x * CF * pow(NQCD, -1)) + 2 * lmuf * x * CF * NQCD;
    return res;
}

double RG_D2_000(double x, double z, double NF) {
    double res = 0.0;
    res = 3. / 2. * CF * pow(NQCD, -1) + (- 3. / 2. * CF * NQCD) + 3. / 2. * x * CF * pow(NQCD, -1) + (- 3. / 2. * x * CF * NQCD);
    return res;
}

double RG_RG_000(double x, double z, double NF) {

    double res = 0.0;
    double tiny = 1E-4;
    double tinyinv = 1. / tiny;

    double u = x + z;
    double v = x - z;

    // x=z
    if (std::abs(v) <= tiny && u >= 2 - tiny) {
        return 0.;
    }
    if (std::abs(v) <= tiny && u <= tiny) {
        return 0.;
    }

    // intersection region of x=z and x=1-z:
    if (std::abs(v) < .99 * tiny && std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double v0 = -tiny;
        double u1 = 1. - tiny;
        double v1 = tiny;
        double u2 = 1. + tiny;
        double v2 = -tiny;

        double x0 = .5 * (u0 + v0);
        double z0 = .5 * (u0 - v0);
        double x1 = .5 * (u1 + v1);
        double z1 = .5 * (u1 - v1);
        double x2 = .5 * (u2 + v2);
        double z2 = .5 * (u2 - v2);

        double pt0 = RG_RG_000(x0, z0, NF);
        double pt1 = RG_RG_000(x1, z1, NF);
        double pt2 = RG_RG_000(x2, z2, NF);

        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if (std::abs(v) < .99 * tiny) {
        double v0 = -tiny;
        double v1 = tiny;

        double x0 = .5 * (u + v0);
        double z0 = .5 * (u - v0);
        double x1 = .5 * (u + v1);
        double z1 = .5 * (u - v1);

        double pt0 = RG_RG_000(x0, z0, NF);
        double pt1 = RG_RG_000(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0);
        return res;
    }

    // x=1-z
    if (std::abs(u - 1.) <= tiny && v <= tiny - 1.) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) <= tiny && v >= 1. - tiny) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double u1 = 1. + tiny;

        double x0 = .5 * (u0 + v);
        double z0 = .5 * (u0 - v);
        double x1 = .5 * (u1 + v);
        double z1 = .5 * (u1 - v);

        double pt0 = RG_RG_000(x0, z0, NF);
        double pt1 = RG_RG_000(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        return res;
    }


    if (z < 1. - x && z < x) {
        double tmp = 0.0;
        tmp = -3 * CF * pow(NQCD, -1) - 6 * z * CF * pow(NQCD, -1) + 3 * x * CF * pow(NQCD, -1) - pow(pi, 2) * CF * pow(NQCD, -1) - 4. / 3. * pow(pi, 2) * z * CF * pow(NQCD, -1) - 1. / 3. * pow(pi, 2) * x * CF * pow(NQCD, -1) - 3 * ln(1 - z) * CF * pow(NQCD, -1) + 4 * ln(1 - z) * x * CF * pow(NQCD, -1) + pow(ln(1 - z), 2) * CF * pow(NQCD, -1) + 4 * pow(ln(1 - z), 2) * z * CF * pow(NQCD, -1) + 3 * pow(ln(1 - z), 2) * x * CF * pow(NQCD, -1) - 2 * ln(1 - z) * ln(1 - z - x) * z * CF * pow(NQCD, -1) - 2 * ln(1 - z) * ln(1 - z - x) * x * CF * pow(NQCD, -1) - 3 * ln(1 - x) * CF * pow(NQCD, -1) + 2 * ln(1 - x) * x * CF * pow(NQCD, -1) + 4 * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) + 10 * ln(1 - x) * ln(1 - z) * z * CF * pow(NQCD, -1) + 6 * ln(1 - x) * ln(1 - z) * x * CF * pow(NQCD, -1) + 4 * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) + 5 * pow(ln(1 - x), 2) * z * CF * pow(NQCD, -1) + pow(ln(1 - x), 2) * x * CF * pow(NQCD, -1) + 6 * ln(x) * CF * pow(NQCD, -1) - 6 * ln(x) * x * CF * pow(NQCD, -1) - 8 * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) - 18 * ln(x) * ln(1 - z) * z * CF * pow(NQCD, -1) - 10 * ln(x) * ln(1 - z) * x * CF * pow(NQCD, -1) + 2 * ln(x) * ln(1 - z - x) * z * CF * pow(NQCD, -1) + 2 * ln(x) * ln(1 - z - x) * x * CF * pow(NQCD, -1) - 10 * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) - 18 * ln(x) * ln(1 - x) * z * CF * pow(NQCD, -1) - 8 * ln(x) * ln(1 - x) * x * CF * pow(NQCD, -1) + 2 * ln(x) * ln(-z + x) * CF * pow(NQCD, -1) + 4 * ln(x) * ln(-z + x) * z * CF * pow(NQCD, -1) + 2 * ln(x) * ln(-z + x) * x * CF * pow(NQCD, -1) + 6 * pow(ln(x), 2) * CF * pow(NQCD, -1) + 12 * pow(ln(x), 2) * z * CF * pow(NQCD, -1) + 6 * pow(ln(x), 2) * x * CF * pow(NQCD, -1) - 10 * ln(x) * ln(z) * CF * pow(NQCD, -1) - 20 * ln(x) * ln(z) * z * CF * pow(NQCD, -1) + -10 * ln(x) * ln(z) * x * CF * pow(NQCD, -1) - 4 * ln(z) * CF * pow(NQCD, -1) + 4 * ln(z) * x * CF * pow(NQCD, -1) + 4 * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) + 12 * ln(z) * ln(1 - z) * z * CF * pow(NQCD, -1) + 8 * ln(z) * ln(1 - z) * x * CF * pow(NQCD, -1) + 8 * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) + 12 * ln(z) * ln(1 - x) * z * CF * pow(NQCD, -1) + 4 * ln(z) * ln(1 - x) * x * CF * pow(NQCD, -1) - 2 * ln(z) * ln(-z + x) * CF * pow(NQCD, -1) - 4 * ln(z) * ln(-z + x) * z * CF * pow(NQCD, -1) - 2 * ln(z) * ln(-z + x) * x * CF * pow(NQCD, -1) + 4 * pow(ln(z), 2) * CF * pow(NQCD, -1) + 8 * pow(ln(z), 2) * z * CF * pow(NQCD, -1) + 4 * pow(ln(z), 2) * x * CF * pow(NQCD, -1) + 2 * Li2(1 / (1 - z) - 1 / (1 - z) * x) * CF * pow(NQCD, -1) - 2 * Li2(1 / (1 - z) - 1 / (1 - z) * x) * x * CF * pow(NQCD, -1) - 2 * Li2(1 / (1 - z) * pow(x, -1) * z - 1 / (1 - z) * z) * CF * pow(NQCD, -1) - 2 * Li2(1 / (1 - z) * pow(x, -1) * z - 1 / (1 - z) * z) * z * CF * pow(NQCD, -1) - 2 * Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * z * CF * pow(NQCD, -1) - 2 * Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * x * CF * pow(NQCD, -1) + 2 * Li2(1 / (1 - x) * z) * z * CF * pow(NQCD, -1) + 2 * Li2(1 / (1 - x) * z) * x * CF * pow(NQCD, -1) - 2 * Li2(z) * CF * pow(NQCD, -1) - 2 * Li2(z) * z * CF * pow(NQCD, -1) + 3 / (1 - z) * CF * pow(NQCD, -1) - 3 / (1 - z) * x * CF * pow(NQCD, -1) + 7. / 6. / (1 - z) * pow(pi, 2) * CF * pow(NQCD, -1) + 1. / 6. / (1 - z) * pow(pi, 2) * x * CF * pow(NQCD, -1) + 2 / (1 - z) * ln(1 - z) * CF * pow(NQCD, -1) - 2 / (1 - z) * ln(1 - z) * x * CF * pow(NQCD, -1) - 5. / 2. / (1 - z) * pow(ln(1 - z), 2) * CF * pow(NQCD, -1) - 3. / 2. / (1 - z) * pow(ln(1 - z), 2) * x * CF * pow(NQCD, -1) + +1 / (1 - z) * ln(1 - z) * ln(1 - z - x) * CF * pow(NQCD, -1) + 1 / (1 - z) * ln(1 - z) * ln(1 - z - x) * x * CF * pow(NQCD, -1) + 1 / (1 - z) * ln(1 - x) * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(1 - x) * x * CF * pow(NQCD, -1) - 7 / (1 - z) * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) - 3 / (1 - z) * ln(1 - x) * ln(1 - z) * x * CF * pow(NQCD, -1) - 9. / 2. / (1 - z) * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) - 1. / 2. / (1 - z) * pow(ln(1 - x), 2) * x * CF * pow(NQCD, -1) - 3 / (1 - z) * ln(x) * CF * pow(NQCD, -1) + 3 / (1 - z) * ln(x) * x * CF * pow(NQCD, -1) + 13 / (1 - z) * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) + 5 / (1 - z) * ln(x) * ln(1 - z) * x * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(x) * ln(1 - z - x) * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(x) * ln(1 - z - x) * x * CF * pow(NQCD, -1) + 14 / (1 - z) * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) + 4 / (1 - z) * ln(x) * ln(1 - x) * x * CF * pow(NQCD, -1) - 3 / (1 - z) * ln(x) * ln(-z + x) * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(x) * ln(-z + x) * x * CF * pow(NQCD, -1) - 9 / (1 - z) * pow(ln(x), 2) * CF * pow(NQCD, -1) - 3 / (1 - z) * pow(ln(x), 2) * x * CF * pow(NQCD, -1) + 15 / (1 - z) * ln(x) * ln(z) * CF * pow(NQCD, -1) + 5 / (1 - z) * ln(x) * ln(z) * x * CF * pow(NQCD, -1) + 2 / (1 - z) * ln(z) * CF * pow(NQCD, -1) - 2 / (1 - z) * ln(z) * x * CF * pow(NQCD, -1) - 8 / (1 - z) * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) - 4 / (1 - z) * ln(z) * ln(1 - z) * x * CF * pow(NQCD, -1) - 10 / (1 - z) * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) - 2 / (1 - z) * ln(z) * ln(1 - x) * x * CF * pow(NQCD, -1) + 3 / (1 - z) * ln(z) * ln(-z + x) * CF * pow(NQCD, -1) + 1 / (1 - z) * ln(z) * ln(-z + x) * x * CF * pow(NQCD, -1) - 6 / (1 - z) * pow(ln(z), 2) * CF * pow(NQCD, -1) + -2 / (1 - z) * pow(ln(z), 2) * x * CF * pow(NQCD, -1) - 1 / (1 - z) * Li2(1 / (1 - z) - 1 / (1 - z) * x) * CF * pow(NQCD, -1) + 1 / (1 - z) * Li2(1 / (1 - z) - 1 / (1 - z) * x) * x * CF * pow(NQCD, -1) + 2 / (1 - z) * Li2(1 / (1 - z) * pow(x, -1) * z - 1 / (1 - z) * z) * CF * pow(NQCD, -1) + 1 / (1 - z) * Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * CF * pow(NQCD, -1) + 1 / (1 - z) * Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * x * CF * pow(NQCD, -1) - 1 / (1 - z) * Li2(1 / (1 - x) * z) * CF * pow(NQCD, -1) - 1 / (1 - z) * Li2(1 / (1 - x) * z) * x * CF * pow(NQCD, -1) + 2 / (1 - z) * Li2(z) * CF * pow(NQCD, -1) + 3 / (1 - x) * z * CF * pow(NQCD, -1) - 3 / (1 - x) * pow(z, 2) * CF * pow(NQCD, -1) + 5. / 6. / (1 - x) * pow(pi, 2) * CF * pow(NQCD, -1) + 5. / 6. / (1 - x) * pow(pi, 2) * z * CF * pow(NQCD, -1) + 1 / (1 - x) * ln(1 - z) * CF * pow(NQCD, -1) - 1 / (1 - x) * ln(1 - z) * z * CF * pow(NQCD, -1) - 7. / 2. / (1 - x) * pow(ln(1 - z), 2) * CF * pow(NQCD, -1) - 7. / 2. / (1 - x) * pow(ln(1 - z), 2) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(1 - z) * ln(1 - z - x) * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(1 - z) * ln(1 - z - x) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(1 - x) * CF * pow(NQCD, -1) - 2 / (1 - x) * ln(1 - x) * z * CF * pow(NQCD, -1) - 8 / (1 - x) * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) - 8 / (1 - x) * ln(1 - x) * ln(1 - z) * z * CF * pow(NQCD, -1) - 3 / (1 - x) * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) - 3 / (1 - x) * pow(ln(1 - x), 2) * z * CF * pow(NQCD, -1) - 3 / (1 - x) * ln(x) * CF * pow(NQCD, -1) + 3 / (1 - x) * ln(x) * z * CF * pow(NQCD, -1) + 14 / (1 - x) * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) + 14 / (1 - x) * ln(x) * ln(1 - z) * z * CF * pow(NQCD, -1) + -2 / (1 - x) * ln(x) * ln(1 - z - x) * CF * pow(NQCD, -1) - 2 / (1 - x) * ln(x) * ln(1 - z - x) * z * CF * pow(NQCD, -1) + 13 / (1 - x) * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) + 13 / (1 - x) * ln(x) * ln(1 - x) * z * CF * pow(NQCD, -1) - 3 / (1 - x) * ln(x) * ln(-z + x) * CF * pow(NQCD, -1) - 3 / (1 - x) * ln(x) * ln(-z + x) * z * CF * pow(NQCD, -1) - 9 / (1 - x) * pow(ln(x), 2) * CF * pow(NQCD, -1) - 9 / (1 - x) * pow(ln(x), 2) * z * CF * pow(NQCD, -1) + 15 / (1 - x) * ln(x) * ln(z) * CF * pow(NQCD, -1) + 15 / (1 - x) * ln(x) * ln(z) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(z) * CF * pow(NQCD, -1) - 2 / (1 - x) * ln(z) * z * CF * pow(NQCD, -1) - 10 / (1 - x) * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) - 10 / (1 - x) * ln(z) * ln(1 - z) * z * CF * pow(NQCD, -1) - 8 / (1 - x) * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) - 8 / (1 - x) * ln(z) * ln(1 - x) * z * CF * pow(NQCD, -1) + 3 / (1 - x) * ln(z) * ln(-z + x) * CF * pow(NQCD, -1) + 3 / (1 - x) * ln(z) * ln(-z + x) * z * CF * pow(NQCD, -1) - 6 / (1 - x) * pow(ln(z), 2) * CF * pow(NQCD, -1) - 6 / (1 - x) * pow(ln(z), 2) * z * CF * pow(NQCD, -1) + 1 / (1 - x) * Li2(1 / (1 - z) - 1 / (1 - z) * x) * CF * pow(NQCD, -1) + 1 / (1 - x) * Li2(1 / (1 - z) - 1 / (1 - z) * x) * z * CF * pow(NQCD, -1) + 1 / (1 - x) * Li2(1 / (1 - z) * pow(x, -1) * z - 1 / (1 - z) * z) * CF * pow(NQCD, -1) + 1 / (1 - x) * Li2(1 / (1 - z) * pow(x, -1) * z - 1 / (1 - z) * z) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * CF * pow(NQCD, -1) + 2 / (1 - x) * Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * z * CF * pow(NQCD, -1) - 2 / (1 - x) * Li2(1 / (1 - x) * z) * CF * pow(NQCD, -1) - 2 / (1 - x) * Li2(1 / (1 - x) * z) * z * CF * pow(NQCD, -1) + +1 / (1 - x) * Li2(z) * CF * pow(NQCD, -1) + 1 / (1 - x) * Li2(z) * z * CF * pow(NQCD, -1) - 4. / 3. / (1 - x) / (1 - z) * pow(pi, 2) * CF * pow(NQCD, -1) + 4 / (1 - x) / (1 - z) * pow(ln(1 - z), 2) * CF * pow(NQCD, -1) - 2 / (1 - x) / (1 - z) * ln(1 - z) * ln(1 - z - x) * CF * pow(NQCD, -1) + 10 / (1 - x) / (1 - z) * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) + 5 / (1 - x) / (1 - z) * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) - 18 / (1 - x) / (1 - z) * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) + 2 / (1 - x) / (1 - z) * ln(x) * ln(1 - z - x) * CF * pow(NQCD, -1) - 18 / (1 - x) / (1 - z) * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) + 4 / (1 - x) / (1 - z) * ln(x) * ln(-z + x) * CF * pow(NQCD, -1) + 12 / (1 - x) / (1 - z) * pow(ln(x), 2) * CF * pow(NQCD, -1) - 20 / (1 - x) / (1 - z) * ln(x) * ln(z) * CF * pow(NQCD, -1) + 12 / (1 - x) / (1 - z) * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) + 12 / (1 - x) / (1 - z) * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) - 4 / (1 - x) / (1 - z) * ln(z) * ln(-z + x) * CF * pow(NQCD, -1) + 8 / (1 - x) / (1 - z) * pow(ln(z), 2) * CF * pow(NQCD, -1) - 2 / (1 - x) / (1 - z) * Li2(1 / (1 - z) * pow(x, -1) * z - 1 / (1 - z) * z) * CF * pow(NQCD, -1) - 2 / (1 - x) / (1 - z) * Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * CF * pow(NQCD, -1) + 2 / (1 - x) / (1 - z) * Li2(1 / (1 - x) * z) * CF * pow(NQCD, -1) - 2 / (1 - x) / (1 - z) * Li2(z) * CF * pow(NQCD, -1);

        res += tmp;
    }
    if (z > 1. - x && z < x) {
        double tmp = 0.0;
        tmp = -3 * CF * pow(NQCD, -1) - 6 * z * CF * pow(NQCD, -1) + 3 * x * CF * pow(NQCD, -1) - pow(pi, 2) * CF * pow(NQCD, -1) - 4. / 3. * pow(pi, 2) * z * CF * pow(NQCD, -1) - 1. / 3. * pow(pi, 2) * x * CF * pow(NQCD, -1) - 3 * ln(1 - z) * CF * pow(NQCD, -1) + 4 * ln(1 - z) * x * CF * pow(NQCD, -1) - 2 * ln(1 - z) * ln(-1 + z + x) * z * CF * pow(NQCD, -1) - 2 * ln(1 - z) * ln(-1 + z + x) * x * CF * pow(NQCD, -1) + pow(ln(1 - z), 2) * CF * pow(NQCD, -1) + 5 * pow(ln(1 - z), 2) * z * CF * pow(NQCD, -1) + 4 * pow(ln(1 - z), 2) * x * CF * pow(NQCD, -1) - 3 * ln(1 - x) * CF * pow(NQCD, -1) + 2 * ln(1 - x) * x * CF * pow(NQCD, -1) + 4 * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) + 8 * ln(1 - x) * ln(1 - z) * z * CF * pow(NQCD, -1) + 4 * ln(1 - x) * ln(1 - z) * x * CF * pow(NQCD, -1) + 4 * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) + 5 * pow(ln(1 - x), 2) * z * CF * pow(NQCD, -1) + pow(ln(1 - x), 2) * x * CF * pow(NQCD, -1) + 6 * ln(x) * CF * pow(NQCD, -1) - 6 * ln(x) * x * CF * pow(NQCD, -1) + 2 * ln(x) * ln(-1 + z + x) * z * CF * pow(NQCD, -1) + 2 * ln(x) * ln(-1 + z + x) * x * CF * pow(NQCD, -1) - 8 * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) - 20 * ln(x) * ln(1 - z) * z * CF * pow(NQCD, -1) - 12 * ln(x) * ln(1 - z) * x * CF * pow(NQCD, -1) - 10 * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) - 16 * ln(x) * ln(1 - x) * z * CF * pow(NQCD, -1) - 6 * ln(x) * ln(1 - x) * x * CF * pow(NQCD, -1) + 2 * ln(x) * ln(-z + x) * CF * pow(NQCD, -1) + 4 * ln(x) * ln(-z + x) * z * CF * pow(NQCD, -1) + 2 * ln(x) * ln(-z + x) * x * CF * pow(NQCD, -1) + 6 * pow(ln(x), 2) * CF * pow(NQCD, -1) + 13 * pow(ln(x), 2) * z * CF * pow(NQCD, -1) + 7 * pow(ln(x), 2) * x * CF * pow(NQCD, -1) - 10 * ln(x) * ln(z) * CF * pow(NQCD, -1) + -22 * ln(x) * ln(z) * z * CF * pow(NQCD, -1) - 12 * ln(x) * ln(z) * x * CF * pow(NQCD, -1) - 4 * ln(z) * CF * pow(NQCD, -1) + 4 * ln(z) * x * CF * pow(NQCD, -1) + 4 * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) + 14 * ln(z) * ln(1 - z) * z * CF * pow(NQCD, -1) + 10 * ln(z) * ln(1 - z) * x * CF * pow(NQCD, -1) + 8 * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) + 12 * ln(z) * ln(1 - x) * z * CF * pow(NQCD, -1) + 4 * ln(z) * ln(1 - x) * x * CF * pow(NQCD, -1) - 2 * ln(z) * ln(-z + x) * CF * pow(NQCD, -1) - 4 * ln(z) * ln(-z + x) * z * CF * pow(NQCD, -1) - 2 * ln(z) * ln(-z + x) * x * CF * pow(NQCD, -1) + 4 * pow(ln(z), 2) * CF * pow(NQCD, -1) + 8 * pow(ln(z), 2) * z * CF * pow(NQCD, -1) + 4 * pow(ln(z), 2) * x * CF * pow(NQCD, -1) - 2 * Li2(pow(z, -1) - x * pow(z, -1)) * z * CF * pow(NQCD, -1) - 2 * Li2(pow(z, -1) - x * pow(z, -1)) * x * CF * pow(NQCD, -1) + 2 * Li2(1 / (1 - z) - 1 / (1 - z) * x) * CF * pow(NQCD, -1) - 2 * Li2(1 / (1 - z) - 1 / (1 - z) * x) * x * CF * pow(NQCD, -1) - 2 * Li2(1 / (1 - z) * pow(x, -1) * z - 1 / (1 - z) * z) * CF * pow(NQCD, -1) - 2 * Li2(1 / (1 - z) * pow(x, -1) * z - 1 / (1 - z) * z) * z * CF * pow(NQCD, -1) + 2 * Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * z * CF * pow(NQCD, -1) + 2 * Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * x * CF * pow(NQCD, -1) - 2 * Li2(z) * CF * pow(NQCD, -1) - 2 * Li2(z) * z * CF * pow(NQCD, -1) + 3 / (1 - z) * CF * pow(NQCD, -1) - 3 / (1 - z) * x * CF * pow(NQCD, -1) + 7. / 6. / (1 - z) * pow(pi, 2) * CF * pow(NQCD, -1) + 1. / 6. / (1 - z) * pow(pi, 2) * x * CF * pow(NQCD, -1) + 2 / (1 - z) * ln(1 - z) * CF * pow(NQCD, -1) - 2 / (1 - z) * ln(1 - z) * x * CF * pow(NQCD, -1) + 1 / (1 - z) * ln(1 - z) * ln(-1 + z + x) * CF * pow(NQCD, -1) + +1 / (1 - z) * ln(1 - z) * ln(-1 + z + x) * x * CF * pow(NQCD, -1) - 3 / (1 - z) * pow(ln(1 - z), 2) * CF * pow(NQCD, -1) - 2 / (1 - z) * pow(ln(1 - z), 2) * x * CF * pow(NQCD, -1) + 1 / (1 - z) * ln(1 - x) * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(1 - x) * x * CF * pow(NQCD, -1) - 6 / (1 - z) * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) - 2 / (1 - z) * ln(1 - x) * ln(1 - z) * x * CF * pow(NQCD, -1) - 9. / 2. / (1 - z) * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) - 1. / 2. / (1 - z) * pow(ln(1 - x), 2) * x * CF * pow(NQCD, -1) - 3 / (1 - z) * ln(x) * CF * pow(NQCD, -1) + 3 / (1 - z) * ln(x) * x * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(x) * ln(-1 + z + x) * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(x) * ln(-1 + z + x) * x * CF * pow(NQCD, -1) + 14 / (1 - z) * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) + 6 / (1 - z) * ln(x) * ln(1 - z) * x * CF * pow(NQCD, -1) + 13 / (1 - z) * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) + 3 / (1 - z) * ln(x) * ln(1 - x) * x * CF * pow(NQCD, -1) - 3 / (1 - z) * ln(x) * ln(-z + x) * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(x) * ln(-z + x) * x * CF * pow(NQCD, -1) - 19. / 2. / (1 - z) * pow(ln(x), 2) * CF * pow(NQCD, -1) - 7. / 2. / (1 - z) * pow(ln(x), 2) * x * CF * pow(NQCD, -1) + 16 / (1 - z) * ln(x) * ln(z) * CF * pow(NQCD, -1) + 6 / (1 - z) * ln(x) * ln(z) * x * CF * pow(NQCD, -1) + 2 / (1 - z) * ln(z) * CF * pow(NQCD, -1) - 2 / (1 - z) * ln(z) * x * CF * pow(NQCD, -1) - 9 / (1 - z) * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) - 5 / (1 - z) * ln(z) * ln(1 - z) * x * CF * pow(NQCD, -1) - 10 / (1 - z) * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) - 2 / (1 - z) * ln(z) * ln(1 - x) * x * CF * pow(NQCD, -1) + 3 / (1 - z) * ln(z) * ln(-z + x) * CF * pow(NQCD, -1) + 1 / (1 - z) * ln(z) * ln(-z + x) * x * CF * pow(NQCD, -1) + -6 / (1 - z) * pow(ln(z), 2) * CF * pow(NQCD, -1) - 2 / (1 - z) * pow(ln(z), 2) * x * CF * pow(NQCD, -1) + 1 / (1 - z) * Li2(pow(z, -1) - x * pow(z, -1)) * CF * pow(NQCD, -1) + 1 / (1 - z) * Li2(pow(z, -1) - x * pow(z, -1)) * x * CF * pow(NQCD, -1) - 1 / (1 - z) * Li2(1 / (1 - z) - 1 / (1 - z) * x) * CF * pow(NQCD, -1) + 1 / (1 - z) * Li2(1 / (1 - z) - 1 / (1 - z) * x) * x * CF * pow(NQCD, -1) + 2 / (1 - z) * Li2(1 / (1 - z) * pow(x, -1) * z - 1 / (1 - z) * z) * CF * pow(NQCD, -1) - 1 / (1 - z) * Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * CF * pow(NQCD, -1) - 1 / (1 - z) * Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * x * CF * pow(NQCD, -1) + 2 / (1 - z) * Li2(z) * CF * pow(NQCD, -1) + 3 / (1 - x) * z * CF * pow(NQCD, -1) - 3 / (1 - x) * pow(z, 2) * CF * pow(NQCD, -1) + 5. / 6. / (1 - x) * pow(pi, 2) * CF * pow(NQCD, -1) + 5. / 6. / (1 - x) * pow(pi, 2) * z * CF * pow(NQCD, -1) + 1 / (1 - x) * ln(1 - z) * CF * pow(NQCD, -1) - 1 / (1 - x) * ln(1 - z) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(1 - z) * ln(-1 + z + x) * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(1 - z) * ln(-1 + z + x) * z * CF * pow(NQCD, -1) - 9. / 2. / (1 - x) * pow(ln(1 - z), 2) * CF * pow(NQCD, -1) - 9. / 2. / (1 - x) * pow(ln(1 - z), 2) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(1 - x) * CF * pow(NQCD, -1) - 2 / (1 - x) * ln(1 - x) * z * CF * pow(NQCD, -1) - 6 / (1 - x) * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) - 6 / (1 - x) * ln(1 - x) * ln(1 - z) * z * CF * pow(NQCD, -1) - 3 / (1 - x) * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) - 3 / (1 - x) * pow(ln(1 - x), 2) * z * CF * pow(NQCD, -1) - 3 / (1 - x) * ln(x) * CF * pow(NQCD, -1) + 3 / (1 - x) * ln(x) * z * CF * pow(NQCD, -1) - 2 / (1 - x) * ln(x) * ln(-1 + z + x) * CF * pow(NQCD, -1) + -2 / (1 - x) * ln(x) * ln(-1 + z + x) * z * CF * pow(NQCD, -1) + 16 / (1 - x) * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) + 16 / (1 - x) * ln(x) * ln(1 - z) * z * CF * pow(NQCD, -1) + 11 / (1 - x) * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) + 11 / (1 - x) * ln(x) * ln(1 - x) * z * CF * pow(NQCD, -1) - 3 / (1 - x) * ln(x) * ln(-z + x) * CF * pow(NQCD, -1) - 3 / (1 - x) * ln(x) * ln(-z + x) * z * CF * pow(NQCD, -1) - 10 / (1 - x) * pow(ln(x), 2) * CF * pow(NQCD, -1) - 10 / (1 - x) * pow(ln(x), 2) * z * CF * pow(NQCD, -1) + 17 / (1 - x) * ln(x) * ln(z) * CF * pow(NQCD, -1) + 17 / (1 - x) * ln(x) * ln(z) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(z) * CF * pow(NQCD, -1) - 2 / (1 - x) * ln(z) * z * CF * pow(NQCD, -1) - 12 / (1 - x) * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) - 12 / (1 - x) * ln(z) * ln(1 - z) * z * CF * pow(NQCD, -1) - 8 / (1 - x) * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) - 8 / (1 - x) * ln(z) * ln(1 - x) * z * CF * pow(NQCD, -1) + 3 / (1 - x) * ln(z) * ln(-z + x) * CF * pow(NQCD, -1) + 3 / (1 - x) * ln(z) * ln(-z + x) * z * CF * pow(NQCD, -1) - 6 / (1 - x) * pow(ln(z), 2) * CF * pow(NQCD, -1) - 6 / (1 - x) * pow(ln(z), 2) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * Li2(pow(z, -1) - x * pow(z, -1)) * CF * pow(NQCD, -1) + 2 / (1 - x) * Li2(pow(z, -1) - x * pow(z, -1)) * z * CF * pow(NQCD, -1) + 1 / (1 - x) * Li2(1 / (1 - z) - 1 / (1 - z) * x) * CF * pow(NQCD, -1) + 1 / (1 - x) * Li2(1 / (1 - z) - 1 / (1 - z) * x) * z * CF * pow(NQCD, -1) + 1 / (1 - x) * Li2(1 / (1 - z) * pow(x, -1) * z - 1 / (1 - z) * z) * CF * pow(NQCD, -1) + 1 / (1 - x) * Li2(1 / (1 - z) * pow(x, -1) * z - 1 / (1 - z) * z) * z * CF * pow(NQCD, -1) - 2 / (1 - x) * Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * CF * pow(NQCD, -1) + -2 / (1 - x) * Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * z * CF * pow(NQCD, -1) + 1 / (1 - x) * Li2(z) * CF * pow(NQCD, -1) + 1 / (1 - x) * Li2(z) * z * CF * pow(NQCD, -1) - 4. / 3. / (1 - x) / (1 - z) * pow(pi, 2) * CF * pow(NQCD, -1) - 2 / (1 - x) / (1 - z) * ln(1 - z) * ln(-1 + z + x) * CF * pow(NQCD, -1) + 5 / (1 - x) / (1 - z) * pow(ln(1 - z), 2) * CF * pow(NQCD, -1) + 8 / (1 - x) / (1 - z) * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) + 5 / (1 - x) / (1 - z) * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) + 2 / (1 - x) / (1 - z) * ln(x) * ln(-1 + z + x) * CF * pow(NQCD, -1) - 20 / (1 - x) / (1 - z) * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) - 16 / (1 - x) / (1 - z) * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) + 4 / (1 - x) / (1 - z) * ln(x) * ln(-z + x) * CF * pow(NQCD, -1) + 13 / (1 - x) / (1 - z) * pow(ln(x), 2) * CF * pow(NQCD, -1) - 22 / (1 - x) / (1 - z) * ln(x) * ln(z) * CF * pow(NQCD, -1) + 14 / (1 - x) / (1 - z) * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) + 12 / (1 - x) / (1 - z) * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) - 4 / (1 - x) / (1 - z) * ln(z) * ln(-z + x) * CF * pow(NQCD, -1) + 8 / (1 - x) / (1 - z) * pow(ln(z), 2) * CF * pow(NQCD, -1) - 2 / (1 - x) / (1 - z) * Li2(pow(z, -1) - x * pow(z, -1)) * CF * pow(NQCD, -1) - 2 / (1 - x) / (1 - z) * Li2(1 / (1 - z) * pow(x, -1) * z - 1 / (1 - z) * z) * CF * pow(NQCD, -1) + 2 / (1 - x) / (1 - z) * Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * CF * pow(NQCD, -1) - 2 / (1 - x) / (1 - z) * Li2(z) * CF * pow(NQCD, -1);

        res += tmp;
    }
    if (z < 1. - x && z > x) {
        double tmp = 0.0;
        tmp = -3 * CF * pow(NQCD, -1) - 6 * z * CF * pow(NQCD, -1) + 3 * x * CF * pow(NQCD, -1) - pow(pi, 2) * CF * pow(NQCD, -1) - 8. / 3. * pow(pi, 2) * z * CF * pow(NQCD, -1) - 5. / 3. * pow(pi, 2) * x * CF * pow(NQCD, -1) - 3 * ln(1 - z) * CF * pow(NQCD, -1) + 4 * ln(1 - z) * x * CF * pow(NQCD, -1) + pow(ln(1 - z), 2) * CF * pow(NQCD, -1) + 6 * pow(ln(1 - z), 2) * z * CF * pow(NQCD, -1) + 5 * pow(ln(1 - z), 2) * x * CF * pow(NQCD, -1) - 2 * ln(1 - z) * ln(1 - z - x) * z * CF * pow(NQCD, -1) - 2 * ln(1 - z) * ln(1 - z - x) * x * CF * pow(NQCD, -1) - 3 * ln(1 - x) * CF * pow(NQCD, -1) + 2 * ln(1 - x) * x * CF * pow(NQCD, -1) + 4 * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) + 6 * ln(1 - x) * ln(1 - z) * z * CF * pow(NQCD, -1) + 2 * ln(1 - x) * ln(1 - z) * x * CF * pow(NQCD, -1) + 4 * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) + 7 * pow(ln(1 - x), 2) * z * CF * pow(NQCD, -1) + 3 * pow(ln(1 - x), 2) * x * CF * pow(NQCD, -1) + 6 * ln(x) * CF * pow(NQCD, -1) - 6 * ln(x) * x * CF * pow(NQCD, -1) - 6 * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) - 18 * ln(x) * ln(1 - z) * z * CF * pow(NQCD, -1) - 12 * ln(x) * ln(1 - z) * x * CF * pow(NQCD, -1) + 2 * ln(x) * ln(1 - z - x) * z * CF * pow(NQCD, -1) + 2 * ln(x) * ln(1 - z - x) * x * CF * pow(NQCD, -1) - 12 * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) - 18 * ln(x) * ln(1 - x) * z * CF * pow(NQCD, -1) - 6 * ln(x) * ln(1 - x) * x * CF * pow(NQCD, -1) + 2 * ln(x) * ln(z - x) * CF * pow(NQCD, -1) + 4 * ln(x) * ln(z - x) * z * CF * pow(NQCD, -1) + 2 * ln(x) * ln(z - x) * x * CF * pow(NQCD, -1) + 7 * pow(ln(x), 2) * CF * pow(NQCD, -1) + 14 * pow(ln(x), 2) * z * CF * pow(NQCD, -1) + 7 * pow(ln(x), 2) * x * CF * pow(NQCD, -1) - 12 * ln(x) * ln(z) * CF * pow(NQCD, -1) - 24 * ln(x) * ln(z) * z * CF * pow(NQCD, -1) + -12 * ln(x) * ln(z) * x * CF * pow(NQCD, -1) - 4 * ln(z) * CF * pow(NQCD, -1) + 4 * ln(z) * x * CF * pow(NQCD, -1) + 2 * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) + 12 * ln(z) * ln(1 - z) * z * CF * pow(NQCD, -1) + 10 * ln(z) * ln(1 - z) * x * CF * pow(NQCD, -1) + 10 * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) + 12 * ln(z) * ln(1 - x) * z * CF * pow(NQCD, -1) + 2 * ln(z) * ln(1 - x) * x * CF * pow(NQCD, -1) - 2 * ln(z) * ln(z - x) * CF * pow(NQCD, -1) - 4 * ln(z) * ln(z - x) * z * CF * pow(NQCD, -1) - 2 * ln(z) * ln(z - x) * x * CF * pow(NQCD, -1) + 5 * pow(ln(z), 2) * CF * pow(NQCD, -1) + 10 * pow(ln(z), 2) * z * CF * pow(NQCD, -1) + 5 * pow(ln(z), 2) * x * CF * pow(NQCD, -1) + 2 * Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * z * CF * pow(NQCD, -1) + 2 * Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * x * CF * pow(NQCD, -1) - 2 * Li2(1 / (1 - x) - 1 / (1 - x) * z) * CF * pow(NQCD, -1) + 2 * Li2(1 / (1 - x) - 1 / (1 - x) * z) * x * CF * pow(NQCD, -1) + 2 * Li2(1 / (1 - x) * z) * z * CF * pow(NQCD, -1) + 2 * Li2(1 / (1 - x) * z) * x * CF * pow(NQCD, -1) + 2 * Li2(1 / (1 - x) * x * pow(z, -1) - 1 / (1 - x) * x) * CF * pow(NQCD, -1) + 2 * Li2(1 / (1 - x) * x * pow(z, -1) - 1 / (1 - x) * x) * z * CF * pow(NQCD, -1) - 2 * Li2(z) * CF * pow(NQCD, -1) - 2 * Li2(z) * z * CF * pow(NQCD, -1) + 3 / (1 - z) * CF * pow(NQCD, -1) - 3 / (1 - z) * x * CF * pow(NQCD, -1) + 11. / 6. / (1 - z) * pow(pi, 2) * CF * pow(NQCD, -1) + 5. / 6. / (1 - z) * pow(pi, 2) * x * CF * pow(NQCD, -1) + 2 / (1 - z) * ln(1 - z) * CF * pow(NQCD, -1) - 2 / (1 - z) * ln(1 - z) * x * CF * pow(NQCD, -1) - 7. / 2. / (1 - z) * pow(ln(1 - z), 2) * CF * pow(NQCD, -1) - 5. / 2. / (1 - z) * pow(ln(1 - z), 2) * x * CF * pow(NQCD, -1) + 1 / (1 - z) * ln(1 - z) * ln(1 - z - x) * CF * pow(NQCD, -1) + +1 / (1 - z) * ln(1 - z) * ln(1 - z - x) * x * CF * pow(NQCD, -1) + 1 / (1 - z) * ln(1 - x) * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(1 - x) * x * CF * pow(NQCD, -1) - 5 / (1 - z) * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(1 - x) * ln(1 - z) * x * CF * pow(NQCD, -1) - 11. / 2. / (1 - z) * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) - 3. / 2. / (1 - z) * pow(ln(1 - x), 2) * x * CF * pow(NQCD, -1) - 3 / (1 - z) * ln(x) * CF * pow(NQCD, -1) + 3 / (1 - z) * ln(x) * x * CF * pow(NQCD, -1) + 12 / (1 - z) * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) + 6 / (1 - z) * ln(x) * ln(1 - z) * x * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(x) * ln(1 - z - x) * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(x) * ln(1 - z - x) * x * CF * pow(NQCD, -1) + 15 / (1 - z) * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) + 3 / (1 - z) * ln(x) * ln(1 - x) * x * CF * pow(NQCD, -1) - 3 / (1 - z) * ln(x) * ln(z - x) * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(x) * ln(z - x) * x * CF * pow(NQCD, -1) - 21. / 2. / (1 - z) * pow(ln(x), 2) * CF * pow(NQCD, -1) - 7. / 2. / (1 - z) * pow(ln(x), 2) * x * CF * pow(NQCD, -1) + 18 / (1 - z) * ln(x) * ln(z) * CF * pow(NQCD, -1) + 6 / (1 - z) * ln(x) * ln(z) * x * CF * pow(NQCD, -1) + 2 / (1 - z) * ln(z) * CF * pow(NQCD, -1) - 2 / (1 - z) * ln(z) * x * CF * pow(NQCD, -1) - 7 / (1 - z) * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) - 5 / (1 - z) * ln(z) * ln(1 - z) * x * CF * pow(NQCD, -1) - 11 / (1 - z) * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(z) * ln(1 - x) * x * CF * pow(NQCD, -1) + 3 / (1 - z) * ln(z) * ln(z - x) * CF * pow(NQCD, -1) + 1 / (1 - z) * ln(z) * ln(z - x) * x * CF * pow(NQCD, -1) - 15. / 2. / (1 - z) * pow(ln(z), 2) * CF * pow(NQCD, -1) - 5. / 2. / (1 - z) * pow(ln(z), 2) * x * CF * pow(NQCD, -1) + -1 / (1 - z) * Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * CF * pow(NQCD, -1) - 1 / (1 - z) * Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * x * CF * pow(NQCD, -1) + 1 / (1 - z) * Li2(1 / (1 - x) - 1 / (1 - x) * z) * CF * pow(NQCD, -1) - 1 / (1 - z) * Li2(1 / (1 - x) - 1 / (1 - x) * z) * x * CF * pow(NQCD, -1) - 1 / (1 - z) * Li2(1 / (1 - x) * z) * CF * pow(NQCD, -1) - 1 / (1 - z) * Li2(1 / (1 - x) * z) * x * CF * pow(NQCD, -1) - 2 / (1 - z) * Li2(1 / (1 - x) * x * pow(z, -1) - 1 / (1 - x) * x) * CF * pow(NQCD, -1) + 2 / (1 - z) * Li2(z) * CF * pow(NQCD, -1) + 3 / (1 - x) * z * CF * pow(NQCD, -1) - 3 / (1 - x) * pow(z, 2) * CF * pow(NQCD, -1) + 13. / 6. / (1 - x) * pow(pi, 2) * CF * pow(NQCD, -1) + 13. / 6. / (1 - x) * pow(pi, 2) * z * CF * pow(NQCD, -1) + 1 / (1 - x) * ln(1 - z) * CF * pow(NQCD, -1) - 1 / (1 - x) * ln(1 - z) * z * CF * pow(NQCD, -1) - 11. / 2. / (1 - x) * pow(ln(1 - z), 2) * CF * pow(NQCD, -1) - 11. / 2. / (1 - x) * pow(ln(1 - z), 2) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(1 - z) * ln(1 - z - x) * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(1 - z) * ln(1 - z - x) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(1 - x) * CF * pow(NQCD, -1) - 2 / (1 - x) * ln(1 - x) * z * CF * pow(NQCD, -1) - 4 / (1 - x) * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) - 4 / (1 - x) * ln(1 - x) * ln(1 - z) * z * CF * pow(NQCD, -1) - 5 / (1 - x) * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) - 5 / (1 - x) * pow(ln(1 - x), 2) * z * CF * pow(NQCD, -1) - 3 / (1 - x) * ln(x) * CF * pow(NQCD, -1) + 3 / (1 - x) * ln(x) * z * CF * pow(NQCD, -1) + 15 / (1 - x) * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) + 15 / (1 - x) * ln(x) * ln(1 - z) * z * CF * pow(NQCD, -1) - 2 / (1 - x) * ln(x) * ln(1 - z - x) * CF * pow(NQCD, -1) + -2 / (1 - x) * ln(x) * ln(1 - z - x) * z * CF * pow(NQCD, -1) + 12 / (1 - x) * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) + 12 / (1 - x) * ln(x) * ln(1 - x) * z * CF * pow(NQCD, -1) - 3 / (1 - x) * ln(x) * ln(z - x) * CF * pow(NQCD, -1) - 3 / (1 - x) * ln(x) * ln(z - x) * z * CF * pow(NQCD, -1) - 21. / 2. / (1 - x) * pow(ln(x), 2) * CF * pow(NQCD, -1) - 21. / 2. / (1 - x) * pow(ln(x), 2) * z * CF * pow(NQCD, -1) + 18 / (1 - x) * ln(x) * ln(z) * CF * pow(NQCD, -1) + 18 / (1 - x) * ln(x) * ln(z) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(z) * CF * pow(NQCD, -1) - 2 / (1 - x) * ln(z) * z * CF * pow(NQCD, -1) - 11 / (1 - x) * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) - 11 / (1 - x) * ln(z) * ln(1 - z) * z * CF * pow(NQCD, -1) - 7 / (1 - x) * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) - 7 / (1 - x) * ln(z) * ln(1 - x) * z * CF * pow(NQCD, -1) + 3 / (1 - x) * ln(z) * ln(z - x) * CF * pow(NQCD, -1) + 3 / (1 - x) * ln(z) * ln(z - x) * z * CF * pow(NQCD, -1) - 15. / 2. / (1 - x) * pow(ln(z), 2) * CF * pow(NQCD, -1) - 15. / 2. / (1 - x) * pow(ln(z), 2) * z * CF * pow(NQCD, -1) - 2 / (1 - x) * Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * CF * pow(NQCD, -1) - 2 / (1 - x) * Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * z * CF * pow(NQCD, -1) - 1 / (1 - x) * Li2(1 / (1 - x) - 1 / (1 - x) * z) * CF * pow(NQCD, -1) - 1 / (1 - x) * Li2(1 / (1 - x) - 1 / (1 - x) * z) * z * CF * pow(NQCD, -1) - 2 / (1 - x) * Li2(1 / (1 - x) * z) * CF * pow(NQCD, -1) - 2 / (1 - x) * Li2(1 / (1 - x) * z) * z * CF * pow(NQCD, -1) - 1 / (1 - x) * Li2(1 / (1 - x) * x * pow(z, -1) - 1 / (1 - x) * x) * CF * pow(NQCD, -1) - 1 / (1 - x) * Li2(1 / (1 - x) * x * pow(z, -1) - 1 / (1 - x) * x) * z * CF * pow(NQCD, -1) + 1 / (1 - x) * Li2(z) * CF * pow(NQCD, -1) + +1 / (1 - x) * Li2(z) * z * CF * pow(NQCD, -1) - 8. / 3. / (1 - x) / (1 - z) * pow(pi, 2) * CF * pow(NQCD, -1) + 6 / (1 - x) / (1 - z) * pow(ln(1 - z), 2) * CF * pow(NQCD, -1) - 2 / (1 - x) / (1 - z) * ln(1 - z) * ln(1 - z - x) * CF * pow(NQCD, -1) + 6 / (1 - x) / (1 - z) * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) + 7 / (1 - x) / (1 - z) * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) - 18 / (1 - x) / (1 - z) * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) + 2 / (1 - x) / (1 - z) * ln(x) * ln(1 - z - x) * CF * pow(NQCD, -1) - 18 / (1 - x) / (1 - z) * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) + 4 / (1 - x) / (1 - z) * ln(x) * ln(z - x) * CF * pow(NQCD, -1) + 14 / (1 - x) / (1 - z) * pow(ln(x), 2) * CF * pow(NQCD, -1) - 24 / (1 - x) / (1 - z) * ln(x) * ln(z) * CF * pow(NQCD, -1) + 12 / (1 - x) / (1 - z) * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) + 12 / (1 - x) / (1 - z) * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) - 4 / (1 - x) / (1 - z) * ln(z) * ln(z - x) * CF * pow(NQCD, -1) + 10 / (1 - x) / (1 - z) * pow(ln(z), 2) * CF * pow(NQCD, -1) + 2 / (1 - x) / (1 - z) * Li2(1 / (1 - z) * x * pow(z, -1) - 1 / (1 - z) * pow(x, 2) * pow(z, -1)) * CF * pow(NQCD, -1) + 2 / (1 - x) / (1 - z) * Li2(1 / (1 - x) * z) * CF * pow(NQCD, -1) + 2 / (1 - x) / (1 - z) * Li2(1 / (1 - x) * x * pow(z, -1) - 1 / (1 - x) * x) * CF * pow(NQCD, -1) - 2 / (1 - x) / (1 - z) * Li2(z) * CF * pow(NQCD, -1);

        res += tmp;
    }
    if (z > 1. - x && z > x) {
        double tmp = 0.0;
        tmp = -3 * CF * pow(NQCD, -1) - 6 * z * CF * pow(NQCD, -1) + 3 * x * CF * pow(NQCD, -1) - pow(pi, 2) * CF * pow(NQCD, -1) - 4. / 3. * pow(pi, 2) * z * CF * pow(NQCD, -1) - 1. / 3. * pow(pi, 2) * x * CF * pow(NQCD, -1) - 3 * ln(1 - z) * CF * pow(NQCD, -1) + 4 * ln(1 - z) * x * CF * pow(NQCD, -1) - 2 * ln(1 - z) * ln(-1 + z + x) * z * CF * pow(NQCD, -1) - 2 * ln(1 - z) * ln(-1 + z + x) * x * CF * pow(NQCD, -1) + pow(ln(1 - z), 2) * CF * pow(NQCD, -1) + 5 * pow(ln(1 - z), 2) * z * CF * pow(NQCD, -1) + 4 * pow(ln(1 - z), 2) * x * CF * pow(NQCD, -1) - 3 * ln(1 - x) * CF * pow(NQCD, -1) + 2 * ln(1 - x) * x * CF * pow(NQCD, -1) + 4 * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) + 8 * ln(1 - x) * ln(1 - z) * z * CF * pow(NQCD, -1) + 4 * ln(1 - x) * ln(1 - z) * x * CF * pow(NQCD, -1) + 4 * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) + 5 * pow(ln(1 - x), 2) * z * CF * pow(NQCD, -1) + pow(ln(1 - x), 2) * x * CF * pow(NQCD, -1) + 6 * ln(x) * CF * pow(NQCD, -1) - 6 * ln(x) * x * CF * pow(NQCD, -1) + 2 * ln(x) * ln(-1 + z + x) * z * CF * pow(NQCD, -1) + 2 * ln(x) * ln(-1 + z + x) * x * CF * pow(NQCD, -1) - 6 * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) - 16 * ln(x) * ln(1 - z) * z * CF * pow(NQCD, -1) - 10 * ln(x) * ln(1 - z) * x * CF * pow(NQCD, -1) - 12 * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) - 20 * ln(x) * ln(1 - x) * z * CF * pow(NQCD, -1) - 8 * ln(x) * ln(1 - x) * x * CF * pow(NQCD, -1) + 2 * ln(x) * ln(z - x) * CF * pow(NQCD, -1) + 4 * ln(x) * ln(z - x) * z * CF * pow(NQCD, -1) + 2 * ln(x) * ln(z - x) * x * CF * pow(NQCD, -1) + 7 * pow(ln(x), 2) * CF * pow(NQCD, -1) + 13 * pow(ln(x), 2) * z * CF * pow(NQCD, -1) + 6 * pow(ln(x), 2) * x * CF * pow(NQCD, -1) - 12 * ln(x) * ln(z) * CF * pow(NQCD, -1) - 22 * ln(x) * ln(z) * z * CF * pow(NQCD, -1) + -10 * ln(x) * ln(z) * x * CF * pow(NQCD, -1) - 4 * ln(z) * CF * pow(NQCD, -1) + 4 * ln(z) * x * CF * pow(NQCD, -1) + 2 * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) + 10 * ln(z) * ln(1 - z) * z * CF * pow(NQCD, -1) + 8 * ln(z) * ln(1 - z) * x * CF * pow(NQCD, -1) + 10 * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) + 16 * ln(z) * ln(1 - x) * z * CF * pow(NQCD, -1) + 6 * ln(z) * ln(1 - x) * x * CF * pow(NQCD, -1) - 2 * ln(z) * ln(z - x) * CF * pow(NQCD, -1) - 4 * ln(z) * ln(z - x) * z * CF * pow(NQCD, -1) - 2 * ln(z) * ln(z - x) * x * CF * pow(NQCD, -1) + 5 * pow(ln(z), 2) * CF * pow(NQCD, -1) + 8 * pow(ln(z), 2) * z * CF * pow(NQCD, -1) + 3 * pow(ln(z), 2) * x * CF * pow(NQCD, -1) - 2 * Li2(pow(z, -1) - x * pow(z, -1)) * z * CF * pow(NQCD, -1) - 2 * Li2(pow(z, -1) - x * pow(z, -1)) * x * CF * pow(NQCD, -1) - 2 * Li2(1 / (1 - x) - 1 / (1 - x) * z) * CF * pow(NQCD, -1) + 2 * Li2(1 / (1 - x) - 1 / (1 - x) * z) * x * CF * pow(NQCD, -1) - 2 * Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * z * CF * pow(NQCD, -1) - 2 * Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * x * CF * pow(NQCD, -1) + 2 * Li2(1 / (1 - x) * x * pow(z, -1) - 1 / (1 - x) * x) * CF * pow(NQCD, -1) + 2 * Li2(1 / (1 - x) * x * pow(z, -1) - 1 / (1 - x) * x) * z * CF * pow(NQCD, -1) - 2 * Li2(z) * CF * pow(NQCD, -1) - 2 * Li2(z) * z * CF * pow(NQCD, -1) + 3 / (1 - z) * CF * pow(NQCD, -1) - 3 / (1 - z) * x * CF * pow(NQCD, -1) + 7. / 6. / (1 - z) * pow(pi, 2) * CF * pow(NQCD, -1) + 1. / 6. / (1 - z) * pow(pi, 2) * x * CF * pow(NQCD, -1) + 2 / (1 - z) * ln(1 - z) * CF * pow(NQCD, -1) - 2 / (1 - z) * ln(1 - z) * x * CF * pow(NQCD, -1) + 1 / (1 - z) * ln(1 - z) * ln(-1 + z + x) * CF * pow(NQCD, -1) + 1 / (1 - z) * ln(1 - z) * ln(-1 + z + x) * x * CF * pow(NQCD, -1) + -3 / (1 - z) * pow(ln(1 - z), 2) * CF * pow(NQCD, -1) - 2 / (1 - z) * pow(ln(1 - z), 2) * x * CF * pow(NQCD, -1) + 1 / (1 - z) * ln(1 - x) * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(1 - x) * x * CF * pow(NQCD, -1) - 6 / (1 - z) * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) - 2 / (1 - z) * ln(1 - x) * ln(1 - z) * x * CF * pow(NQCD, -1) - 9. / 2. / (1 - z) * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) - 1. / 2. / (1 - z) * pow(ln(1 - x), 2) * x * CF * pow(NQCD, -1) - 3 / (1 - z) * ln(x) * CF * pow(NQCD, -1) + 3 / (1 - z) * ln(x) * x * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(x) * ln(-1 + z + x) * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(x) * ln(-1 + z + x) * x * CF * pow(NQCD, -1) + 11 / (1 - z) * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) + 5 / (1 - z) * ln(x) * ln(1 - z) * x * CF * pow(NQCD, -1) + 16 / (1 - z) * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) + 4 / (1 - z) * ln(x) * ln(1 - x) * x * CF * pow(NQCD, -1) - 3 / (1 - z) * ln(x) * ln(z - x) * CF * pow(NQCD, -1) - 1 / (1 - z) * ln(x) * ln(z - x) * x * CF * pow(NQCD, -1) - 10 / (1 - z) * pow(ln(x), 2) * CF * pow(NQCD, -1) - 3 / (1 - z) * pow(ln(x), 2) * x * CF * pow(NQCD, -1) + 17 / (1 - z) * ln(x) * ln(z) * CF * pow(NQCD, -1) + 5 / (1 - z) * ln(x) * ln(z) * x * CF * pow(NQCD, -1) + 2 / (1 - z) * ln(z) * CF * pow(NQCD, -1) - 2 / (1 - z) * ln(z) * x * CF * pow(NQCD, -1) - 6 / (1 - z) * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) - 4 / (1 - z) * ln(z) * ln(1 - z) * x * CF * pow(NQCD, -1) - 13 / (1 - z) * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) - 3 / (1 - z) * ln(z) * ln(1 - x) * x * CF * pow(NQCD, -1) + 3 / (1 - z) * ln(z) * ln(z - x) * CF * pow(NQCD, -1) + 1 / (1 - z) * ln(z) * ln(z - x) * x * CF * pow(NQCD, -1) - 13. / 2. / (1 - z) * pow(ln(z), 2) * CF * pow(NQCD, -1) - 3. / 2. / (1 - z) * pow(ln(z), 2) * x * CF * pow(NQCD, -1) + +1 / (1 - z) * Li2(pow(z, -1) - x * pow(z, -1)) * CF * pow(NQCD, -1) + 1 / (1 - z) * Li2(pow(z, -1) - x * pow(z, -1)) * x * CF * pow(NQCD, -1) + 1 / (1 - z) * Li2(1 / (1 - x) - 1 / (1 - x) * z) * CF * pow(NQCD, -1) - 1 / (1 - z) * Li2(1 / (1 - x) - 1 / (1 - x) * z) * x * CF * pow(NQCD, -1) + 1 / (1 - z) * Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * CF * pow(NQCD, -1) + 1 / (1 - z) * Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * x * CF * pow(NQCD, -1) - 2 / (1 - z) * Li2(1 / (1 - x) * x * pow(z, -1) - 1 / (1 - x) * x) * CF * pow(NQCD, -1) + 2 / (1 - z) * Li2(z) * CF * pow(NQCD, -1) + 3 / (1 - x) * z * CF * pow(NQCD, -1) - 3 / (1 - x) * pow(z, 2) * CF * pow(NQCD, -1) + 5. / 6. / (1 - x) * pow(pi, 2) * CF * pow(NQCD, -1) + 5. / 6. / (1 - x) * pow(pi, 2) * z * CF * pow(NQCD, -1) + 1 / (1 - x) * ln(1 - z) * CF * pow(NQCD, -1) - 1 / (1 - x) * ln(1 - z) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(1 - z) * ln(-1 + z + x) * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(1 - z) * ln(-1 + z + x) * z * CF * pow(NQCD, -1) - 9. / 2. / (1 - x) * pow(ln(1 - z), 2) * CF * pow(NQCD, -1) - 9. / 2. / (1 - x) * pow(ln(1 - z), 2) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(1 - x) * CF * pow(NQCD, -1) - 2 / (1 - x) * ln(1 - x) * z * CF * pow(NQCD, -1) - 6 / (1 - x) * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) - 6 / (1 - x) * ln(1 - x) * ln(1 - z) * z * CF * pow(NQCD, -1) - 3 / (1 - x) * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) - 3 / (1 - x) * pow(ln(1 - x), 2) * z * CF * pow(NQCD, -1) - 3 / (1 - x) * ln(x) * CF * pow(NQCD, -1) + 3 / (1 - x) * ln(x) * z * CF * pow(NQCD, -1) - 2 / (1 - x) * ln(x) * ln(-1 + z + x) * CF * pow(NQCD, -1) - 2 / (1 - x) * ln(x) * ln(-1 + z + x) * z * CF * pow(NQCD, -1) + +13 / (1 - x) * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) + 13 / (1 - x) * ln(x) * ln(1 - z) * z * CF * pow(NQCD, -1) + 14 / (1 - x) * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) + 14 / (1 - x) * ln(x) * ln(1 - x) * z * CF * pow(NQCD, -1) - 3 / (1 - x) * ln(x) * ln(z - x) * CF * pow(NQCD, -1) - 3 / (1 - x) * ln(x) * ln(z - x) * z * CF * pow(NQCD, -1) - 19. / 2. / (1 - x) * pow(ln(x), 2) * CF * pow(NQCD, -1) - 19. / 2. / (1 - x) * pow(ln(x), 2) * z * CF * pow(NQCD, -1) + 16 / (1 - x) * ln(x) * ln(z) * CF * pow(NQCD, -1) + 16 / (1 - x) * ln(x) * ln(z) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * ln(z) * CF * pow(NQCD, -1) - 2 / (1 - x) * ln(z) * z * CF * pow(NQCD, -1) - 9 / (1 - x) * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) - 9 / (1 - x) * ln(z) * ln(1 - z) * z * CF * pow(NQCD, -1) - 11 / (1 - x) * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) - 11 / (1 - x) * ln(z) * ln(1 - x) * z * CF * pow(NQCD, -1) + 3 / (1 - x) * ln(z) * ln(z - x) * CF * pow(NQCD, -1) + 3 / (1 - x) * ln(z) * ln(z - x) * z * CF * pow(NQCD, -1) - 11. / 2. / (1 - x) * pow(ln(z), 2) * CF * pow(NQCD, -1) - 11. / 2. / (1 - x) * pow(ln(z), 2) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * Li2(pow(z, -1) - x * pow(z, -1)) * CF * pow(NQCD, -1) + 2 / (1 - x) * Li2(pow(z, -1) - x * pow(z, -1)) * z * CF * pow(NQCD, -1) - 1 / (1 - x) * Li2(1 / (1 - x) - 1 / (1 - x) * z) * CF * pow(NQCD, -1) - 1 / (1 - x) * Li2(1 / (1 - x) - 1 / (1 - x) * z) * z * CF * pow(NQCD, -1) + 2 / (1 - x) * Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * CF * pow(NQCD, -1) + 2 / (1 - x) * Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * z * CF * pow(NQCD, -1) - 1 / (1 - x) * Li2(1 / (1 - x) * x * pow(z, -1) - 1 / (1 - x) * x) * CF * pow(NQCD, -1) + -1 / (1 - x) * Li2(1 / (1 - x) * x * pow(z, -1) - 1 / (1 - x) * x) * z * CF * pow(NQCD, -1) + 1 / (1 - x) * Li2(z) * CF * pow(NQCD, -1) + 1 / (1 - x) * Li2(z) * z * CF * pow(NQCD, -1) - 4. / 3. / (1 - x) / (1 - z) * pow(pi, 2) * CF * pow(NQCD, -1) - 2 / (1 - x) / (1 - z) * ln(1 - z) * ln(-1 + z + x) * CF * pow(NQCD, -1) + 5 / (1 - x) / (1 - z) * pow(ln(1 - z), 2) * CF * pow(NQCD, -1) + 8 / (1 - x) / (1 - z) * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) + 5 / (1 - x) / (1 - z) * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) + 2 / (1 - x) / (1 - z) * ln(x) * ln(-1 + z + x) * CF * pow(NQCD, -1) - 16 / (1 - x) / (1 - z) * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) - 20 / (1 - x) / (1 - z) * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) + 4 / (1 - x) / (1 - z) * ln(x) * ln(z - x) * CF * pow(NQCD, -1) + 13 / (1 - x) / (1 - z) * pow(ln(x), 2) * CF * pow(NQCD, -1) - 22 / (1 - x) / (1 - z) * ln(x) * ln(z) * CF * pow(NQCD, -1) + 10 / (1 - x) / (1 - z) * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) + 16 / (1 - x) / (1 - z) * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) - 4 / (1 - x) / (1 - z) * ln(z) * ln(z - x) * CF * pow(NQCD, -1) + 8 / (1 - x) / (1 - z) * pow(ln(z), 2) * CF * pow(NQCD, -1) - 2 / (1 - x) / (1 - z) * Li2(pow(z, -1) - x * pow(z, -1)) * CF * pow(NQCD, -1) - 2 / (1 - x) / (1 - z) * Li2(1 / (1 - x) * pow(x, -1) * z - 1 / (1 - x) * pow(x, -1) * pow(z, 2)) * CF * pow(NQCD, -1) + 2 / (1 - x) / (1 - z) * Li2(1 / (1 - x) * x * pow(z, -1) - 1 / (1 - x) * x) * CF * pow(NQCD, -1) - 2 / (1 - x) / (1 - z) * Li2(z) * CF * pow(NQCD, -1);

        res += tmp;
    }
    if (z > x) {
        double tmp = 0.0;
        tmp = 0;

        res += tmp;
    }
    if (z < x) {
        double tmp = 0.0;
        tmp = 0;

        res += tmp;
    }
    if (z < 1. - x) {
        double tmp = 0.0;
        tmp = 4 * CF * NQCD + z * CF * NQCD - 2 * x * CF * NQCD + 4. / 3. * pow(pi, 2) * z * CF * NQCD + 4. / 3. * pow(pi, 2) * x * CF * NQCD - 2 * ln(1 - z) * CF * NQCD + 2 * ln(1 - z) * x * CF * NQCD - 5 * pow(ln(1 - z), 2) * z * CF * NQCD - 5 * pow(ln(1 - z), 2) * x * CF * NQCD + 2 * ln(1 - z) * ln(1 - z - x) * z * CF * NQCD + 2 * ln(1 - z) * ln(1 - z - x) * x * CF * NQCD - 2 * ln(1 - x) * CF * NQCD + 2 * ln(1 - x) * x * CF * NQCD - 10 * ln(1 - x) * ln(1 - z) * z * CF * NQCD - 10 * ln(1 - x) * ln(1 - z) * x * CF * NQCD - 4 * pow(ln(1 - x), 2) * z * CF * NQCD - 4 * pow(ln(1 - x), 2) * x * CF * NQCD + 3 * ln(x) * CF * NQCD - 3 * ln(x) * x * CF * NQCD + 12 * ln(x) * ln(1 - z) * z * CF * NQCD + 12 * ln(x) * ln(1 - z) * x * CF * NQCD - 2 * ln(x) * ln(1 - z - x) * z * CF * NQCD - 2 * ln(x) * ln(1 - z - x) * x * CF * NQCD + 12 * ln(x) * ln(1 - x) * z * CF * NQCD + 12 * ln(x) * ln(1 - x) * x * CF * NQCD - 7 * pow(ln(x), 2) * z * CF * NQCD - 7 * pow(ln(x), 2) * x * CF * NQCD + 6 * ln(x) * ln(z) * z * CF * NQCD + 6 * ln(x) * ln(z) * x * CF * NQCD - ln(z) * CF * NQCD + ln(z) * x * CF * NQCD - 4 * ln(z) * ln(1 - z) * z * CF * NQCD - 4 * ln(z) * ln(1 - z) * x * CF * NQCD - 4 * ln(z) * ln(1 - x) * z * CF * NQCD - 4 * ln(z) * ln(1 - x) * x * CF * NQCD - pow(ln(z), 2) * z * CF * NQCD - pow(ln(z), 2) * x * CF * NQCD + 2 * Li2(1 / (1 - x) * z) * z * CF * NQCD + 2 * Li2(1 / (1 - x) * z) * x * CF * NQCD - 2 * Li2(1 / (1 - x) / (1 - z) * x * z) * z * CF * NQCD - 2 * Li2(1 / (1 - x) / (1 - z) * x * z) * x * CF * NQCD - 2 * Li2(z) * z * CF * NQCD - 2 * Li2(z) * x * CF * NQCD - 2. / 3. / (1 - z) * pow(pi, 2) * CF * NQCD - 2. / 3. / (1 - z) * pow(pi, 2) * x * CF * NQCD - 2 / (1 - z) * ln(1 - z) * CF * NQCD + 2 / (1 - z) * ln(1 - z) * x * CF * NQCD + 5. / 2. / (1 - z) * pow(ln(1 - z), 2) * CF * NQCD + 5. / 2. / (1 - z) * pow(ln(1 - z), 2) * x * CF * NQCD + -1 / (1 - z) * ln(1 - z) * ln(1 - z - x) * CF * NQCD - 1 / (1 - z) * ln(1 - z) * ln(1 - z - x) * x * CF * NQCD - 2 / (1 - z) * ln(1 - x) * CF * NQCD + 2 / (1 - z) * ln(1 - x) * x * CF * NQCD + 5 / (1 - z) * ln(1 - x) * ln(1 - z) * CF * NQCD + 5 / (1 - z) * ln(1 - x) * ln(1 - z) * x * CF * NQCD + 2 / (1 - z) * pow(ln(1 - x), 2) * CF * NQCD + 2 / (1 - z) * pow(ln(1 - x), 2) * x * CF * NQCD + 3 / (1 - z) * ln(x) * CF * NQCD - 3 / (1 - z) * ln(x) * x * CF * NQCD - 6 / (1 - z) * ln(x) * ln(1 - z) * CF * NQCD - 6 / (1 - z) * ln(x) * ln(1 - z) * x * CF * NQCD + 1 / (1 - z) * ln(x) * ln(1 - z - x) * CF * NQCD + 1 / (1 - z) * ln(x) * ln(1 - z - x) * x * CF * NQCD - 6 / (1 - z) * ln(x) * ln(1 - x) * CF * NQCD - 6 / (1 - z) * ln(x) * ln(1 - x) * x * CF * NQCD + 7. / 2. / (1 - z) * pow(ln(x), 2) * CF * NQCD + 7. / 2. / (1 - z) * pow(ln(x), 2) * x * CF * NQCD - 3 / (1 - z) * ln(x) * ln(z) * CF * NQCD - 3 / (1 - z) * ln(x) * ln(z) * x * CF * NQCD - 1 / (1 - z) * ln(z) * CF * NQCD + 1 / (1 - z) * ln(z) * x * CF * NQCD + 2 / (1 - z) * ln(z) * ln(1 - z) * CF * NQCD + 2 / (1 - z) * ln(z) * ln(1 - z) * x * CF * NQCD + 2 / (1 - z) * ln(z) * ln(1 - x) * CF * NQCD + 2 / (1 - z) * ln(z) * ln(1 - x) * x * CF * NQCD + 1. / 2. / (1 - z) * pow(ln(z), 2) * CF * NQCD + 1. / 2. / (1 - z) * pow(ln(z), 2) * x * CF * NQCD - 1 / (1 - z) * Li2(1 / (1 - x) * z) * CF * NQCD - 1 / (1 - z) * Li2(1 / (1 - x) * z) * x * CF * NQCD + 1 / (1 - z) * Li2(1 / (1 - x) / (1 - z) * x * z) * CF * NQCD + 1 / (1 - z) * Li2(1 / (1 - x) / (1 - z) * x * z) * x * CF * NQCD + 1 / (1 - z) * Li2(z) * CF * NQCD + 1 / (1 - z) * Li2(z) * x * CF * NQCD - 2. / 3. / (1 - x) * pow(pi, 2) * CF * NQCD - 2. / 3. / (1 - x) * pow(pi, 2) * z * CF * NQCD - 2 / (1 - x) * ln(1 - z) * CF * NQCD + 2 / (1 - x) * ln(1 - z) * z * CF * NQCD + 5. / 2. / (1 - x) * pow(ln(1 - z), 2) * CF * NQCD + +5. / 2. / (1 - x) * pow(ln(1 - z), 2) * z * CF * NQCD - 1 / (1 - x) * ln(1 - z) * ln(1 - z - x) * CF * NQCD - 1 / (1 - x) * ln(1 - z) * ln(1 - z - x) * z * CF * NQCD - 2 / (1 - x) * ln(1 - x) * CF * NQCD + 2 / (1 - x) * ln(1 - x) * z * CF * NQCD + 5 / (1 - x) * ln(1 - x) * ln(1 - z) * CF * NQCD + 5 / (1 - x) * ln(1 - x) * ln(1 - z) * z * CF * NQCD + 2 / (1 - x) * pow(ln(1 - x), 2) * CF * NQCD + 2 / (1 - x) * pow(ln(1 - x), 2) * z * CF * NQCD + 3 / (1 - x) * ln(x) * CF * NQCD - 3 / (1 - x) * ln(x) * z * CF * NQCD - 6 / (1 - x) * ln(x) * ln(1 - z) * CF * NQCD - 6 / (1 - x) * ln(x) * ln(1 - z) * z * CF * NQCD + 1 / (1 - x) * ln(x) * ln(1 - z - x) * CF * NQCD + 1 / (1 - x) * ln(x) * ln(1 - z - x) * z * CF * NQCD - 6 / (1 - x) * ln(x) * ln(1 - x) * CF * NQCD - 6 / (1 - x) * ln(x) * ln(1 - x) * z * CF * NQCD + 7. / 2. / (1 - x) * pow(ln(x), 2) * CF * NQCD + 7. / 2. / (1 - x) * pow(ln(x), 2) * z * CF * NQCD - 3 / (1 - x) * ln(x) * ln(z) * CF * NQCD - 3 / (1 - x) * ln(x) * ln(z) * z * CF * NQCD - 1 / (1 - x) * ln(z) * CF * NQCD + 1 / (1 - x) * ln(z) * z * CF * NQCD + 2 / (1 - x) * ln(z) * ln(1 - z) * CF * NQCD + 2 / (1 - x) * ln(z) * ln(1 - z) * z * CF * NQCD + 2 / (1 - x) * ln(z) * ln(1 - x) * CF * NQCD + 2 / (1 - x) * ln(z) * ln(1 - x) * z * CF * NQCD + 1. / 2. / (1 - x) * pow(ln(z), 2) * CF * NQCD + 1. / 2. / (1 - x) * pow(ln(z), 2) * z * CF * NQCD - 1 / (1 - x) * Li2(1 / (1 - x) * z) * CF * NQCD - 1 / (1 - x) * Li2(1 / (1 - x) * z) * z * CF * NQCD + 1 / (1 - x) * Li2(1 / (1 - x) / (1 - z) * x * z) * CF * NQCD + 1 / (1 - x) * Li2(1 / (1 - x) / (1 - z) * x * z) * z * CF * NQCD + 1 / (1 - x) * Li2(z) * CF * NQCD + 1 / (1 - x) * Li2(z) * z * CF * NQCD + 4. / 3. / (1 - x) / (1 - z) * pow(pi, 2) * CF * NQCD - 5 / (1 - x) / (1 - z) * pow(ln(1 - z), 2) * CF * NQCD + 2 / (1 - x) / (1 - z) * ln(1 - z) * ln(1 - z - x) * CF * NQCD + -10 / (1 - x) / (1 - z) * ln(1 - x) * ln(1 - z) * CF * NQCD - 4 / (1 - x) / (1 - z) * pow(ln(1 - x), 2) * CF * NQCD + 12 / (1 - x) / (1 - z) * ln(x) * ln(1 - z) * CF * NQCD - 2 / (1 - x) / (1 - z) * ln(x) * ln(1 - z - x) * CF * NQCD + 12 / (1 - x) / (1 - z) * ln(x) * ln(1 - x) * CF * NQCD - 7 / (1 - x) / (1 - z) * pow(ln(x), 2) * CF * NQCD + 6 / (1 - x) / (1 - z) * ln(x) * ln(z) * CF * NQCD - 4 / (1 - x) / (1 - z) * ln(z) * ln(1 - z) * CF * NQCD - 4 / (1 - x) / (1 - z) * ln(z) * ln(1 - x) * CF * NQCD - 1 / (1 - x) / (1 - z) * pow(ln(z), 2) * CF * NQCD + 2 / (1 - x) / (1 - z) * Li2(1 / (1 - x) * z) * CF * NQCD - 2 / (1 - x) / (1 - z) * Li2(1 / (1 - x) / (1 - z) * x * z) * CF * NQCD - 2 / (1 - x) / (1 - z) * Li2(z) * CF * NQCD;

        res += tmp;
    }
    if (z > 1. - x) {
        double tmp = 0.0;
        tmp = 4 * CF * NQCD + z * CF * NQCD - 2 * x * CF * NQCD + 4. / 3. * pow(pi, 2) * z * CF * NQCD + 4. / 3. * pow(pi, 2) * x * CF * NQCD - 2 * ln(1 - z) * CF * NQCD + 2 * ln(1 - z) * x * CF * NQCD + 2 * ln(1 - z) * ln(-1 + z + x) * z * CF * NQCD + 2 * ln(1 - z) * ln(-1 + z + x) * x * CF * NQCD - 4 * pow(ln(1 - z), 2) * z * CF * NQCD - 4 * pow(ln(1 - z), 2) * x * CF * NQCD - 2 * ln(1 - x) * CF * NQCD + 2 * ln(1 - x) * x * CF * NQCD - 8 * ln(1 - x) * ln(1 - z) * z * CF * NQCD - 8 * ln(1 - x) * ln(1 - z) * x * CF * NQCD - 4 * pow(ln(1 - x), 2) * z * CF * NQCD - 4 * pow(ln(1 - x), 2) * x * CF * NQCD + 3 * ln(x) * CF * NQCD - 3 * ln(x) * x * CF * NQCD - 2 * ln(x) * ln(-1 + z + x) * z * CF * NQCD - 2 * ln(x) * ln(-1 + z + x) * x * CF * NQCD + 10 * ln(x) * ln(1 - z) * z * CF * NQCD + 10 * ln(x) * ln(1 - z) * x * CF * NQCD + 10 * ln(x) * ln(1 - x) * z * CF * NQCD + 10 * ln(x) * ln(1 - x) * x * CF * NQCD - 6 * pow(ln(x), 2) * z * CF * NQCD - 6 * pow(ln(x), 2) * x * CF * NQCD + 8 * ln(x) * ln(z) * z * CF * NQCD + 8 * ln(x) * ln(z) * x * CF * NQCD - ln(z) * CF * NQCD + ln(z) * x * CF * NQCD - 6 * ln(z) * ln(1 - z) * z * CF * NQCD - 6 * ln(z) * ln(1 - z) * x * CF * NQCD - 4 * ln(z) * ln(1 - x) * z * CF * NQCD - 4 * ln(z) * ln(1 - x) * x * CF * NQCD - pow(ln(z), 2) * z * CF * NQCD - pow(ln(z), 2) * x * CF * NQCD + 2 * Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * z * CF * NQCD + 2 * Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * CF * NQCD - 2 * Li2(pow(z, -1) - x * pow(z, -1)) * z * CF * NQCD - 2 * Li2(pow(z, -1) - x * pow(z, -1)) * x * CF * NQCD - 2 * Li2(z) * z * CF * NQCD - 2 * Li2(z) * x * CF * NQCD - 2. / 3. / (1 - z) * pow(pi, 2) * CF * NQCD - 2. / 3. / (1 - z) * pow(pi, 2) * x * CF * NQCD - 2 / (1 - z) * ln(1 - z) * CF * NQCD + 2 / (1 - z) * ln(1 - z) * x * CF * NQCD + -1 / (1 - z) * ln(1 - z) * ln(-1 + z + x) * CF * NQCD - 1 / (1 - z) * ln(1 - z) * ln(-1 + z + x) * x * CF * NQCD + 2 / (1 - z) * pow(ln(1 - z), 2) * CF * NQCD + 2 / (1 - z) * pow(ln(1 - z), 2) * x * CF * NQCD - 2 / (1 - z) * ln(1 - x) * CF * NQCD + 2 / (1 - z) * ln(1 - x) * x * CF * NQCD + 4 / (1 - z) * ln(1 - x) * ln(1 - z) * CF * NQCD + 4 / (1 - z) * ln(1 - x) * ln(1 - z) * x * CF * NQCD + 2 / (1 - z) * pow(ln(1 - x), 2) * CF * NQCD + 2 / (1 - z) * pow(ln(1 - x), 2) * x * CF * NQCD + 3 / (1 - z) * ln(x) * CF * NQCD - 3 / (1 - z) * ln(x) * x * CF * NQCD + 1 / (1 - z) * ln(x) * ln(-1 + z + x) * CF * NQCD + 1 / (1 - z) * ln(x) * ln(-1 + z + x) * x * CF * NQCD - 5 / (1 - z) * ln(x) * ln(1 - z) * CF * NQCD - 5 / (1 - z) * ln(x) * ln(1 - z) * x * CF * NQCD - 5 / (1 - z) * ln(x) * ln(1 - x) * CF * NQCD - 5 / (1 - z) * ln(x) * ln(1 - x) * x * CF * NQCD + 3 / (1 - z) * pow(ln(x), 2) * CF * NQCD + 3 / (1 - z) * pow(ln(x), 2) * x * CF * NQCD - 4 / (1 - z) * ln(x) * ln(z) * CF * NQCD - 4 / (1 - z) * ln(x) * ln(z) * x * CF * NQCD - 1 / (1 - z) * ln(z) * CF * NQCD + 1 / (1 - z) * ln(z) * x * CF * NQCD + 3 / (1 - z) * ln(z) * ln(1 - z) * CF * NQCD + 3 / (1 - z) * ln(z) * ln(1 - z) * x * CF * NQCD + 2 / (1 - z) * ln(z) * ln(1 - x) * CF * NQCD + 2 / (1 - z) * ln(z) * ln(1 - x) * x * CF * NQCD + 1. / 2. / (1 - z) * pow(ln(z), 2) * CF * NQCD + 1. / 2. / (1 - z) * pow(ln(z), 2) * x * CF * NQCD - 1 / (1 - z) * Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * CF * NQCD - 1 / (1 - z) * Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * x * CF * NQCD + 1 / (1 - z) * Li2(pow(z, -1) - x * pow(z, -1)) * CF * NQCD + 1 / (1 - z) * Li2(pow(z, -1) - x * pow(z, -1)) * x * CF * NQCD + 1 / (1 - z) * Li2(z) * CF * NQCD + 1 / (1 - z) * Li2(z) * x * CF * NQCD + -2. / 3. / (1 - x) * pow(pi, 2) * CF * NQCD - 2. / 3. / (1 - x) * pow(pi, 2) * z * CF * NQCD - 2 / (1 - x) * ln(1 - z) * CF * NQCD + 2 / (1 - x) * ln(1 - z) * z * CF * NQCD - 1 / (1 - x) * ln(1 - z) * ln(-1 + z + x) * CF * NQCD - 1 / (1 - x) * ln(1 - z) * ln(-1 + z + x) * z * CF * NQCD + 2 / (1 - x) * pow(ln(1 - z), 2) * CF * NQCD + 2 / (1 - x) * pow(ln(1 - z), 2) * z * CF * NQCD - 2 / (1 - x) * ln(1 - x) * CF * NQCD + 2 / (1 - x) * ln(1 - x) * z * CF * NQCD + 4 / (1 - x) * ln(1 - x) * ln(1 - z) * CF * NQCD + 4 / (1 - x) * ln(1 - x) * ln(1 - z) * z * CF * NQCD + 2 / (1 - x) * pow(ln(1 - x), 2) * CF * NQCD + 2 / (1 - x) * pow(ln(1 - x), 2) * z * CF * NQCD + 3 / (1 - x) * ln(x) * CF * NQCD - 3 / (1 - x) * ln(x) * z * CF * NQCD + 1 / (1 - x) * ln(x) * ln(-1 + z + x) * CF * NQCD + 1 / (1 - x) * ln(x) * ln(-1 + z + x) * z * CF * NQCD - 5 / (1 - x) * ln(x) * ln(1 - z) * CF * NQCD - 5 / (1 - x) * ln(x) * ln(1 - z) * z * CF * NQCD - 5 / (1 - x) * ln(x) * ln(1 - x) * CF * NQCD - 5 / (1 - x) * ln(x) * ln(1 - x) * z * CF * NQCD + 3 / (1 - x) * pow(ln(x), 2) * CF * NQCD + 3 / (1 - x) * pow(ln(x), 2) * z * CF * NQCD - 4 / (1 - x) * ln(x) * ln(z) * CF * NQCD - 4 / (1 - x) * ln(x) * ln(z) * z * CF * NQCD - 1 / (1 - x) * ln(z) * CF * NQCD + 1 / (1 - x) * ln(z) * z * CF * NQCD + 3 / (1 - x) * ln(z) * ln(1 - z) * CF * NQCD + 3 / (1 - x) * ln(z) * ln(1 - z) * z * CF * NQCD + 2 / (1 - x) * ln(z) * ln(1 - x) * CF * NQCD + 2 / (1 - x) * ln(z) * ln(1 - x) * z * CF * NQCD + 1. / 2. / (1 - x) * pow(ln(z), 2) * CF * NQCD + 1. / 2. / (1 - x) * pow(ln(z), 2) * z * CF * NQCD - 1 / (1 - x) * Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * CF * NQCD - 1 / (1 - x) * Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * z * CF * NQCD + 1 / (1 - x) * Li2(pow(z, -1) - x * pow(z, -1)) * CF * NQCD + +1 / (1 - x) * Li2(pow(z, -1) - x * pow(z, -1)) * z * CF * NQCD + 1 / (1 - x) * Li2(z) * CF * NQCD + 1 / (1 - x) * Li2(z) * z * CF * NQCD + 4. / 3. / (1 - x) / (1 - z) * pow(pi, 2) * CF * NQCD + 2 / (1 - x) / (1 - z) * ln(1 - z) * ln(-1 + z + x) * CF * NQCD - 4 / (1 - x) / (1 - z) * pow(ln(1 - z), 2) * CF * NQCD - 8 / (1 - x) / (1 - z) * ln(1 - x) * ln(1 - z) * CF * NQCD - 4 / (1 - x) / (1 - z) * pow(ln(1 - x), 2) * CF * NQCD - 2 / (1 - x) / (1 - z) * ln(x) * ln(-1 + z + x) * CF * NQCD + 10 / (1 - x) / (1 - z) * ln(x) * ln(1 - z) * CF * NQCD + 10 / (1 - x) / (1 - z) * ln(x) * ln(1 - x) * CF * NQCD - 6 / (1 - x) / (1 - z) * pow(ln(x), 2) * CF * NQCD + 8 / (1 - x) / (1 - z) * ln(x) * ln(z) * CF * NQCD - 6 / (1 - x) / (1 - z) * ln(z) * ln(1 - z) * CF * NQCD - 4 / (1 - x) / (1 - z) * ln(z) * ln(1 - x) * CF * NQCD - 1 / (1 - x) / (1 - z) * pow(ln(z), 2) * CF * NQCD + 2 / (1 - x) / (1 - z) * Li2(1 + pow(x, -1) * pow(z, -1) - pow(x, -1) - pow(z, -1)) * CF * NQCD - 2 / (1 - x) / (1 - z) * Li2(pow(z, -1) - x * pow(z, -1)) * CF * NQCD - 2 / (1 - x) / (1 - z) * Li2(z) * CF * NQCD;

        res += tmp;
    }
    
    if (z != x && z != 1. - x) {
        double tmp = 0.0;
        tmp = (-9. / 2. * CF * pow(NQCD, -1)) + (- 31. / 6. * CF * NQCD) + 2. / 3. * CF * NF + 16 * z * CF * pow(NQCD, -1) + (- 14. / 9. * z * CF * NQCD) + (- 10. / 9. * z * CF * NF) + 12 * x * CF * pow(NQCD, -1) + 37. / 9. * x * CF * NQCD + (- 16. / 9. * x * CF * NF) + 1. / 2. * x * z * CF * pow(NQCD, -1) + (- 1. / 2. * x * z * CF * NQCD) + 7. / 6. * pow(pi, 2) * CF * pow(NQCD, -1) + (- 1. / 6. * pow(pi, 2) * CF * NQCD) + 5. / 2. * pow(pi, 2) * z * CF * pow(NQCD, -1) + (- 13. / 6. * pow(pi, 2) * z * CF * NQCD) + 3. / 2. * pow(pi, 2) * x * CF * pow(NQCD, -1) + (- 13. / 6. * pow(pi, 2) * x * CF * NQCD) + 1. / 6. * pow(pi, 2) * x * z * CF * pow(NQCD, -1) + (- 1. / 6. * pow(pi, 2) * x * z * CF * NQCD) + ln(1 - z) * CF * pow(NQCD, -1) + 4 * ln(1 - z) * CF * NQCD + 2 * ln(1 - z) * z * CF * pow(NQCD, -1) + (- 17. / 3. * ln(1 - z) * z * CF * NQCD) + 2. / 3. * ln(1 - z) * z * CF * NF + (- 2 * ln(1 - z) * x * CF * pow(NQCD, -1)) + (- 23. / 3. * ln(1 - z) * x * CF * NQCD) + 2. / 3. * ln(1 - z) * x * CF * NF + (- 2 * ln(1 - z) * x * z * CF * pow(NQCD, -1)) + 2 * ln(1 - z) * x * z * CF * NQCD + (- 3. / 2. * pow(ln(1 - z), 2) * CF * pow(NQCD, -1)) + 1. / 2. * pow(ln(1 - z), 2) * CF * NQCD + (- 13. / 2. * pow(ln(1 - z), 2) * z * CF * pow(NQCD, -1)) + 11. / 2. * pow(ln(1 - z), 2) * z * CF * NQCD + (- 11. / 2. * pow(ln(1 - z), 2) * x * CF * pow(NQCD, -1)) + 11. / 2. * pow(ln(1 - z), 2) * x * CF * NQCD + (- 1. / 2. * pow(ln(1 - z), 2) * x * z * CF * pow(NQCD, -1)) + 1. / 2. * pow(ln(1 - z), 2) * x * z * CF * NQCD + 3. / 2. * ln(1 - x) * CF * pow(NQCD, -1) + 5. / 2. * ln(1 - x) * CF * NQCD + 1. / 2. * ln(1 - x) * z * CF * pow(NQCD, -1) + (- 25. / 6. * ln(1 - x) * z * CF * NQCD) + 2. / 3. * ln(1 - x) * z * CF * NF + (- 1. / 2. * ln(1 - x) * x * CF * pow(NQCD, -1)) + (- 37. / 6. * ln(1 - x) * x * CF * NQCD) + 2. / 3. * ln(1 - x) * x * CF * NF + (- 1. / 2. * ln(1 - x) * x * z * CF * pow(NQCD, -1)) + 1. / 2. * ln(1 - x) * x * z * CF * NQCD +  + (-5 * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1)) + ln(1 - x) * ln(1 - z) * CF * NQCD + (- 11 * ln(1 - x) * ln(1 - z) * z * CF * pow(NQCD, -1)) + 11 * ln(1 - x) * ln(1 - z) * z * CF * NQCD + (- 7 * ln(1 - x) * ln(1 - z) * x * CF * pow(NQCD, -1)) + 11 * ln(1 - x) * ln(1 - z) * x * CF * NQCD + (- ln(1 - x) * ln(1 - z) * x * z * CF * pow(NQCD, -1)) + ln(1 - x) * ln(1 - z) * x * z * CF * NQCD + (- 9. / 2. * pow(ln(1 - x), 2) * CF * pow(NQCD, -1)) + 1. / 2. * pow(ln(1 - x), 2) * CF * NQCD + (- 13. / 2. * pow(ln(1 - x), 2) * z * CF * pow(NQCD, -1)) + 11. / 2. * pow(ln(1 - x), 2) * z * CF * NQCD + (- 5. / 2. * pow(ln(1 - x), 2) * x * CF * pow(NQCD, -1)) + 11. / 2. * pow(ln(1 - x), 2) * x * CF * NQCD + (- 1. / 2. * pow(ln(1 - x), 2) * x * z * CF * pow(NQCD, -1)) + 1. / 2. * pow(ln(1 - x), 2) * x * z * CF * NQCD +  +  + (- 13. / 2. * ln(x) * CF * pow(NQCD, -1)) + (- 7. / 2. * ln(x) * CF * NQCD) + (- 5. / 2. * ln(x) * z * CF * pow(NQCD, -1)) + 47. / 6. * ln(x) * z * CF * NQCD + (- 4. / 3. * ln(x) * z * CF * NF) + 3. / 2. * ln(x) * x * CF * pow(NQCD, -1) + 71. / 6. * ln(x) * x * CF * NQCD + (- 4. / 3. * ln(x) * x * CF * NF) + 1. / 2. * ln(x) * x * z * CF * pow(NQCD, -1) + (- 1. / 2. * ln(x) * x * z * CF * NQCD) + 7 * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) + (- ln(x) * ln(1 - z) * CF * NQCD) + 20 * ln(x) * ln(1 - z) * z * CF * pow(NQCD, -1) + (- 14 * ln(x) * ln(1 - z) * z * CF * NQCD) + 14 * ln(x) * ln(1 - z) * x * CF * pow(NQCD, -1) + (- 14 * ln(x) * ln(1 - z) * x * CF * NQCD) + ln(x) * ln(1 - z) * x * z * CF * pow(NQCD, -1) + (- ln(x) * ln(1 - z) * x * z * CF * NQCD) + 15 * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) + (- ln(x) * ln(1 - x) * CF * NQCD) + 23 * ln(x) * ln(1 - x) * z * CF * pow(NQCD, -1) + (- 13 * ln(x) * ln(1 - x) * z * CF * NQCD) + 9 * ln(x) * ln(1 - x) * x * CF * pow(NQCD, -1) + (- 13 * ln(x) * ln(1 - x) * x * CF * NQCD) + ln(x) * ln(1 - x) * x * z * CF * pow(NQCD, -1) + (- ln(x) * ln(1 - x) * x * z * CF * NQCD) + (- 2 * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1)) + 2 * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1) +  + (- 17. / 2. * pow(ln(x), 2) * CF * pow(NQCD, -1)) + 1. / 2. * pow(ln(x), 2) * CF * NQCD + (- 33. / 2. * pow(ln(x), 2) * z * CF * pow(NQCD, -1)) + 17. / 2. * pow(ln(x), 2) * z * CF * NQCD + (- 17. / 2. * pow(ln(x), 2) * x * CF * pow(NQCD, -1)) + 17. / 2. * pow(ln(x), 2) * x * CF * NQCD + (- 1. / 2. * pow(ln(x), 2) * x * z * CF * pow(NQCD, -1)) + 1. / 2. * pow(ln(x), 2) * x * z * CF * NQCD + 8 * ln(x) * ln(z) * CF * pow(NQCD, -1) + 17 * ln(x) * ln(z) * z * CF * pow(NQCD, -1) + (- 5 * ln(x) * ln(z) * z * CF * NQCD) + 9 * ln(x) * ln(z) * x * CF * pow(NQCD, -1) + (- 5 * ln(x) * ln(z) * x * CF * NQCD) + ln(z) * CF * pow(NQCD, -1) + 2 * ln(z) * CF * NQCD + 2 * ln(z) * z * CF * pow(NQCD, -1) + (- ln(z) * x * CF * pow(NQCD, -1)) + (- ln(z) * x * CF * NQCD) + (- 6 * ln(z) * ln(1 - z) * CF * pow(NQCD, -1)) + (- 18 * ln(z) * ln(1 - z) * z * CF * pow(NQCD, -1)) + 6 * ln(z) * ln(1 - z) * z * CF * NQCD + (- 12 * ln(z) * ln(1 - z) * x * CF * pow(NQCD, -1)) + 6 * ln(z) * ln(1 - z) * x * CF * NQCD +  + (-6 * ln(z) * ln(1 - x) * CF * pow(NQCD, -1)) + (- 11 * ln(z) * ln(1 - x) * z * CF * pow(NQCD, -1)) + 3 * ln(z) * ln(1 - x) * z * CF * NQCD + (- 5 * ln(z) * ln(1 - x) * x * CF * pow(NQCD, -1)) + 3 * ln(z) * ln(1 - x) * x * CF * NQCD + (- 1. / 2. * pow(ln(z), 2) * CF * pow(NQCD, -1)) + (- 1. / 2. * pow(ln(z), 2) * CF * NQCD) + (- 3. / 2. * pow(ln(z), 2) * z * CF * pow(NQCD, -1)) + (- 1. / 2. * pow(ln(z), 2) * z * CF * NQCD) + (- 1. / 2. * pow(ln(z), 2) * x * CF * pow(NQCD, -1)) + (- 1. / 2. * pow(ln(z), 2) * x * CF * NQCD) + 1. / 2. * pow(ln(z), 2) * x * z * CF * pow(NQCD, -1) + (- 1. / 2. * pow(ln(z), 2) * x * z * CF * NQCD) + (- 2 * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1)) + 2 * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1) +  + 2 * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1) + (- 2 * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1)) + 4 * Li2(1 - x * pow(z, -1)) * CF * pow(NQCD, -1) + 8 * Li2(1 - x * pow(z, -1)) * z * CF * pow(NQCD, -1) + 4 * Li2(1 - x * pow(z, -1)) * x * CF * pow(NQCD, -1) + 4 * Li2(x) * CF * pow(NQCD, -1) + 3 * Li2(x) * z * CF * pow(NQCD, -1) + Li2(x) * z * CF * NQCD + (- Li2(x) * x * CF * pow(NQCD, -1)) + Li2(x) * x * CF * NQCD + (- 2 * Li2(z) * CF * pow(NQCD, -1)) + (- 7 * Li2(z) * z * CF * pow(NQCD, -1)) + 3 * Li2(z) * z * CF * NQCD + (- 5 * Li2(z) * x * CF * pow(NQCD, -1)) + 3 * Li2(z) * x * CF * NQCD + 1. / 2. / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(1 - z) * z * CF * pow(NQCD, -1) + (- 1. / 2. / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(1 - z) * z * CF * NQCD) + (- 1. / 2. / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(1 - z) * pow(z, 2) * CF * pow(NQCD, -1)) + 1. / 2. / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(1 - z) * pow(z, 2) * CF * NQCD + (- 1. / 2. / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(x) * z * CF * pow(NQCD, -1)) + 1. / 2. / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(x) * z * CF * NQCD + 1. / 2. / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(x) * pow(z, 2) * CF * pow(NQCD, -1) + (- 1. / 2. / (1 - 2 * z + pow(z, 2) - 2 * x + 2 * x * z + pow(x, 2)) * ln(x) * pow(z, 2) * CF * NQCD) + (- 3 / (1 - z) * CF * pow(NQCD, -1)) + 3 / (1 - z) * x * CF * pow(NQCD, -1) + (- 4. / 3. / (1 - z) * pow(pi, 2) * CF * pow(NQCD, -1)) + 1. / 2. / (1 - z) * pow(pi, 2) * CF * NQCD +  + (-1. / 3. / (1 - z) * pow(pi, 2) * x * CF * pow(NQCD, -1)) + 1. / 2. / (1 - z) * pow(pi, 2) * x * CF * NQCD + (- 2 / (1 - z) * ln(1 - z) * CF * pow(NQCD, -1)) + 2 / (1 - z) * ln(1 - z) * CF * NQCD + 2 / (1 - z) * ln(1 - z) * x * CF * pow(NQCD, -1) + (- 2 / (1 - z) * ln(1 - z) * x * CF * NQCD) + 3 / (1 - z) * pow(ln(1 - z), 2) * CF * pow(NQCD, -1) + (- 2 / (1 - z) * pow(ln(1 - z), 2) * CF * NQCD) + 2 / (1 - z) * pow(ln(1 - z), 2) * x * CF * pow(NQCD, -1) + (- 2 / (1 - z) * pow(ln(1 - z), 2) * x * CF * NQCD) + (- 1 / (1 - z) * ln(1 - x) * CF * pow(NQCD, -1)) + 2 / (1 - z) * ln(1 - x) * CF * NQCD + 1 / (1 - z) * ln(1 - x) * x * CF * pow(NQCD, -1) + (- 2 / (1 - z) * ln(1 - x) * x * CF * NQCD) + 6 / (1 - z) * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) + (- 4 / (1 - z) * ln(1 - x) * ln(1 - z) * CF * NQCD) + 2 / (1 - z) * ln(1 - x) * ln(1 - z) * x * CF * pow(NQCD, -1) + (- 4 / (1 - z) * ln(1 - x) * ln(1 - z) * x * CF * NQCD) + 9. / 2. / (1 - z) * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) + (- 2 / (1 - z) * pow(ln(1 - x), 2) * CF * NQCD) + 1. / 2. / (1 - z) * pow(ln(1 - x), 2) * x * CF * pow(NQCD, -1) + (- 2 / (1 - z) * pow(ln(1 - x), 2) * x * CF * NQCD) + 3 / (1 - z) * ln(x) * CF * pow(NQCD, -1) + (- 3 / (1 - z) * ln(x) * CF * NQCD) + (- 3 / (1 - z) * ln(x) * x * CF * pow(NQCD, -1)) + 3 / (1 - z) * ln(x) * x * CF * NQCD + (- 12 / (1 - z) * ln(x) * ln(1 - z) * CF * pow(NQCD, -1)) + 6 / (1 - z) * ln(x) * ln(1 - z) * CF * NQCD + (- 6 / (1 - z) * ln(x) * ln(1 - z) * x * CF * pow(NQCD, -1)) + 6 / (1 - z) * ln(x) * ln(1 - z) * x * CF * NQCD + (- 17 / (1 - z) * ln(x) * ln(1 - x) * CF * pow(NQCD, -1)) + 5 / (1 - z) * ln(x) * ln(1 - x) * CF * NQCD + (- 3 / (1 - z) * ln(x) * ln(1 - x) * x * CF * pow(NQCD, -1)) + 5 / (1 - z) * ln(x) * ln(1 - x) * x * CF * NQCD + 1 / (1 - z) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1) +  + (-1 / (1 - z) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1)) + 25. / 2. / (1 - z) * pow(ln(x), 2) * CF * pow(NQCD, -1) + (- 4 / (1 - z) * pow(ln(x), 2) * CF * NQCD) + 9. / 2. / (1 - z) * pow(ln(x), 2) * x * CF * pow(NQCD, -1) + (- 4 / (1 - z) * pow(ln(x), 2) * x * CF * NQCD) + (- 14 / (1 - z) * ln(x) * ln(z) * CF * pow(NQCD, -1)) + 4 / (1 - z) * ln(x) * ln(z) * CF * NQCD + (- 6 / (1 - z) * ln(x) * ln(z) * x * CF * pow(NQCD, -1)) + 4 / (1 - z) * ln(x) * ln(z) * x * CF * NQCD + (- 2 / (1 - z) * ln(z) * CF * pow(NQCD, -1)) + 2 / (1 - z) * ln(z) * CF * NQCD + 2 / (1 - z) * ln(z) * x * CF * pow(NQCD, -1) + (- 2 / (1 - z) * ln(z) * x * CF * NQCD) + 11 / (1 - z) * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) + (- 2 / (1 - z) * ln(z) * ln(1 - z) * CF * NQCD) + 5 / (1 - z) * ln(z) * ln(1 - z) * x * CF * pow(NQCD, -1) + (- 2 / (1 - z) * ln(z) * ln(1 - z) * x * CF * NQCD) + 9 / (1 - z) * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) + (- 2 / (1 - z) * ln(z) * ln(1 - x) * CF * NQCD) + 3 / (1 - z) * ln(z) * ln(1 - x) * x * CF * pow(NQCD, -1) + (- 2 / (1 - z) * ln(z) * ln(1 - x) * x * CF * NQCD) + 3. / 2. / (1 - z) * pow(ln(z), 2) * CF * pow(NQCD, -1) + 1. / 2. / (1 - z) * pow(ln(z), 2) * x * CF * pow(NQCD, -1) + 1 / (1 - z) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1) +  + (-1 / (1 - z) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1)) + (- 1 / (1 - z) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1)) + 1 / (1 - z) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1) + (- 5 / (1 - z) * Li2(1 - x * pow(z, -1)) * CF * pow(NQCD, -1)) + (- 1 / (1 - z) * Li2(1 - x * pow(z, -1)) * CF * NQCD) + (- 1 / (1 - z) * Li2(1 - x * pow(z, -1)) * x * CF * pow(NQCD, -1)) + (- 1 / (1 - z) * Li2(1 - x * pow(z, -1)) * x * CF * NQCD) + (- 4 / (1 - z) * Li2(x) * CF * pow(NQCD, -1)) + 3 / (1 - z) * Li2(z) * CF * pow(NQCD, -1) + 1 / (1 - z) * Li2(z) * x * CF * pow(NQCD, -1) + (- 1. / 2. / (1 - z - x) * z * CF * pow(NQCD, -1)) + 1. / 2. / (1 - z - x) * z * CF * NQCD + (- 1. / 2. / (1 - z - x) * ln(1 - z) * CF * pow(NQCD, -1)) + 3. / 2. / (1 - z - x) * ln(1 - z) * CF * NQCD + (- 3. / 2. / (1 - z - x) * ln(1 - z) * z * CF * pow(NQCD, -1)) + 1. / 2. / (1 - z - x) * ln(1 - z) * z * CF * NQCD + 1. / 2. / (1 - z - x) * ln(x) * CF * pow(NQCD, -1) + (- 3. / 2. / (1 - z - x) * ln(x) * CF * NQCD) + 3. / 2. / (1 - z - x) * ln(x) * z * CF * pow(NQCD, -1) + (- 1. / 2. / (1 - z - x) * ln(x) * z * CF * NQCD) + 4 / (1 - 2 * x + pow(x, 2)) / (1 - z) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1) + (- 4 / (1 - 2 * x + pow(x, 2)) / (1 - z) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1)) + 4 / (1 - 2 * x + pow(x, 2)) / (1 - z) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1) +  + (-4 / (1 - 2 * x + pow(x, 2)) / (1 - z) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1)) + (- 4 / (1 - 2 * x + pow(x, 2)) / (1 - z) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1)) + 4 / (1 - 2 * x + pow(x, 2)) / (1 - z) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1) + (- 16 / (1 - 2 * x + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * CF * pow(NQCD, -1)) + 16 / (1 - 2 * x + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * CF * pow(NQCD, -1) + (- 16 / (1 - 2 * x + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * CF * pow(NQCD, -1)) + 16 / (1 - 2 * x + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * CF * pow(NQCD, -1) + 16 / (1 - 2 * x + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * CF * pow(NQCD, -1) + (- 16 / (1 - 2 * x + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * CF * pow(NQCD, -1)) + (- 3 / (1 - x) * z * CF * pow(NQCD, -1)) + 3 / (1 - x) * pow(z, 2) * CF * pow(NQCD, -1) +  + (-4. / 3. / (1 - x) * pow(pi, 2) * CF * pow(NQCD, -1)) + 1. / 2. / (1 - x) * pow(pi, 2) * CF * NQCD + (- 4. / 3. / (1 - x) * pow(pi, 2) * z * CF * pow(NQCD, -1)) + 1. / 2. / (1 - x) * pow(pi, 2) * z * CF * NQCD + (- 1 / (1 - x) * ln(1 - z) * CF * pow(NQCD, -1)) + 2 / (1 - x) * ln(1 - z) * CF * NQCD + 1 / (1 - x) * ln(1 - z) * z * CF * pow(NQCD, -1) + (- 2 / (1 - x) * ln(1 - z) * z * CF * NQCD) + 9. / 2. / (1 - x) * pow(ln(1 - z), 2) * CF * pow(NQCD, -1) + (- 2 / (1 - x) * pow(ln(1 - z), 2) * CF * NQCD) + 9. / 2. / (1 - x) * pow(ln(1 - z), 2) * z * CF * pow(NQCD, -1) + (- 2 / (1 - x) * pow(ln(1 - z), 2) * z * CF * NQCD) + (- 2 / (1 - x) * ln(1 - x) * CF * pow(NQCD, -1)) + 2 / (1 - x) * ln(1 - x) * CF * NQCD + 2 / (1 - x) * ln(1 - x) * z * CF * pow(NQCD, -1) + (- 2 / (1 - x) * ln(1 - x) * z * CF * NQCD) + 6 / (1 - x) * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1) + (- 4 / (1 - x) * ln(1 - x) * ln(1 - z) * CF * NQCD) + 6 / (1 - x) * ln(1 - x) * ln(1 - z) * z * CF * pow(NQCD, -1) + (- 4 / (1 - x) * ln(1 - x) * ln(1 - z) * z * CF * NQCD) + 3 / (1 - x) * pow(ln(1 - x), 2) * CF * pow(NQCD, -1) + (- 2 / (1 - x) * pow(ln(1 - x), 2) * CF * NQCD) + 3 / (1 - x) * pow(ln(1 - x), 2) * z * CF * pow(NQCD, -1) + (- 2 / (1 - x) * pow(ln(1 - x), 2) * z * CF * NQCD) + 1 / (1 - x) * ln(x) * CF * pow(NQCD, -1) + (- 11. / 2. / (1 - x) * ln(x) * CF * NQCD) + 1 / (1 - x) * ln(x) * CF * NF + (- 5 / (1 - x) * ln(x) * z * CF * pow(NQCD, -1)) + (- 1. / 2. / (1 - x) * ln(x) * z * CF * NQCD) + 1 / (1 - x) * ln(x) * z * CF * NF + (- 16 / (1 - x) * ln(x) * ln(1 - z) * CF * pow(NQCD, -1)) + 8 / (1 - x) * ln(x) * ln(1 - z) * CF * NQCD + (- 16 / (1 - x) * ln(x) * ln(1 - z) * z * CF * pow(NQCD, -1)) + 8 / (1 - x) * ln(x) * ln(1 - z) * z * CF * NQCD + (- 17 / (1 - x) * ln(x) * ln(1 - x) * CF * pow(NQCD, -1)) + 8 / (1 - x) * ln(x) * ln(1 - x) * CF * NQCD +  + (-17 / (1 - x) * ln(x) * ln(1 - x) * z * CF * pow(NQCD, -1)) + 8 / (1 - x) * ln(x) * ln(1 - x) * z * CF * NQCD + 13 / (1 - x) * pow(ln(x), 2) * CF * pow(NQCD, -1) + (- 5 / (1 - x) * pow(ln(x), 2) * CF * NQCD) + 13 / (1 - x) * pow(ln(x), 2) * z * CF * pow(NQCD, -1) + (- 5 / (1 - x) * pow(ln(x), 2) * z * CF * NQCD) + (- 27. / 2. / (1 - x) * ln(x) * ln(z) * CF * pow(NQCD, -1)) + 7. / 2. / (1 - x) * ln(x) * ln(z) * CF * NQCD + (- 27. / 2. / (1 - x) * ln(x) * ln(z) * z * CF * pow(NQCD, -1)) + 7. / 2. / (1 - x) * ln(x) * ln(z) * z * CF * NQCD + (- 2 / (1 - x) * ln(z) * CF * pow(NQCD, -1)) + 1 / (1 - x) * ln(z) * CF * NQCD + 2 / (1 - x) * ln(z) * z * CF * pow(NQCD, -1) + (- 1 / (1 - x) * ln(z) * z * CF * NQCD) + 13 / (1 - x) * ln(z) * ln(1 - z) * CF * pow(NQCD, -1) + (- 1 / (1 - x) * ln(z) * ln(1 - z) * CF * NQCD) + 13 / (1 - x) * ln(z) * ln(1 - z) * z * CF * pow(NQCD, -1) + (- 1 / (1 - x) * ln(z) * ln(1 - z) * z * CF * NQCD) + 8 / (1 - x) * ln(z) * ln(1 - x) * CF * pow(NQCD, -1) + (- 2 / (1 - x) * ln(z) * ln(1 - x) * CF * NQCD) + 8 / (1 - x) * ln(z) * ln(1 - x) * z * CF * pow(NQCD, -1) + (- 2 / (1 - x) * ln(z) * ln(1 - x) * z * CF * NQCD) + 3 / (1 - x) * pow(ln(z), 2) * CF * pow(NQCD, -1) + (- 1 / (1 - x) * pow(ln(z), 2) * CF * NQCD) + 3 / (1 - x) * pow(ln(z), 2) * z * CF * pow(NQCD, -1) + (- 1 / (1 - x) * pow(ln(z), 2) * z * CF * NQCD) +  + (-6 / (1 - x) * Li2(1 - x * pow(z, -1)) * CF * pow(NQCD, -1)) + (- 1 / (1 - x) * Li2(1 - x * pow(z, -1)) * CF * NQCD) + (- 6 / (1 - x) * Li2(1 - x * pow(z, -1)) * z * CF * pow(NQCD, -1)) + (- 1 / (1 - x) * Li2(1 - x * pow(z, -1)) * z * CF * NQCD) + (- 3 / (1 - x) * Li2(x) * CF * pow(NQCD, -1)) + (- 3 / (1 - x) * Li2(x) * z * CF * pow(NQCD, -1)) + 5 / (1 - x) * Li2(z) * CF * pow(NQCD, -1) + 5 / (1 - x) * Li2(z) * z * CF * pow(NQCD, -1) + 5. / 3. / (1 - x) / (1 - z) * pow(pi, 2) * CF * pow(NQCD, -1) + (- 1 / (1 - x) / (1 - z) * pow(pi, 2) * CF * NQCD) + (- 5 / (1 - x) / (1 - z) * pow(ln(1 - z), 2) * CF * pow(NQCD, -1)) + 4 / (1 - x) / (1 - z) * pow(ln(1 - z), 2) * CF * NQCD + (- 8 / (1 - x) / (1 - z) * ln(1 - x) * ln(1 - z) * CF * pow(NQCD, -1)) + 8 / (1 - x) / (1 - z) * ln(1 - x) * ln(1 - z) * CF * NQCD + (- 5 / (1 - x) / (1 - z) * pow(ln(1 - x), 2) * CF * pow(NQCD, -1)) + 4 / (1 - x) / (1 - z) * pow(ln(1 - x), 2) * CF * NQCD + 18 / (1 - x) / (1 - z) * ln(x) * ln(1 - z) * CF * pow(NQCD, -1) + (- 12 / (1 - x) / (1 - z) * ln(x) * ln(1 - z) * CF * NQCD) + 20 / (1 - x) / (1 - z) * ln(x) * ln(1 - x) * CF * pow(NQCD, -1) + (- 10 / (1 - x) / (1 - z) * ln(x) * ln(1 - x) * CF * NQCD) + (- 4 / (1 - x) / (1 - z) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1)) + 4 / (1 - x) / (1 - z) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1) + (- 17 / (1 - x) / (1 - z) * pow(ln(x), 2) * CF * pow(NQCD, -1)) + 8 / (1 - x) / (1 - z) * pow(ln(x), 2) * CF * NQCD + 20 / (1 - x) / (1 - z) * ln(x) * ln(z) * CF * pow(NQCD, -1) + (- 8 / (1 - x) / (1 - z) * ln(x) * ln(z) * CF * NQCD) + 3. / 2. / (1 - x) / (1 - z) * ln(z) * CF * pow(NQCD, -1) +  + (-3. / 2. / (1 - x) / (1 - z) * ln(z) * CF * NQCD) + (- 14 / (1 - x) / (1 - z) * ln(z) * ln(1 - z) * CF * pow(NQCD, -1)) + 2 / (1 - x) / (1 - z) * ln(z) * ln(1 - z) * CF * NQCD + (- 12 / (1 - x) / (1 - z) * ln(z) * ln(1 - x) * CF * pow(NQCD, -1)) + 4 / (1 - x) / (1 - z) * ln(z) * ln(1 - x) * CF * NQCD + (- 5 / (1 - x) / (1 - z) * pow(ln(z), 2) * CF * pow(NQCD, -1)) + 2 / (1 - x) / (1 - z) * pow(ln(z), 2) * CF * NQCD + (- 4 / (1 - x) / (1 - z) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1)) + 4 / (1 - x) / (1 - z) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1) + 4 / (1 - x) / (1 - z) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1) + (- 4 / (1 - x) / (1 - z) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * CF * pow(NQCD, -1)) + 6 / (1 - x) / (1 - z) * Li2(1 - x * pow(z, -1)) * CF * pow(NQCD, -1) + 2 / (1 - x) / (1 - z) * Li2(1 - x * pow(z, -1)) * CF * NQCD + 4 / (1 - x) / (1 - z) * Li2(x) * CF * pow(NQCD, -1) + (- 4 / (1 - x) / (1 - z) * Li2(z) * CF * pow(NQCD, -1)) + (- 3. / 2. / (1 - x) / (z - x) * ln(x) * CF * pow(NQCD, -1)) + 3. / 2. / (1 - x) / (z - x) * ln(x) * CF * NQCD + 3. / 2. / (1 - x) / (z - x) * ln(z) * CF * pow(NQCD, -1) + (- 3. / 2. / (1 - x) / (z - x) * ln(z) * CF * NQCD) + 32 / (1 - x) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * CF * pow(NQCD, -1) + (- 32 / (1 - x) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * CF * pow(NQCD, -1)) +  + 32 / (1 - x) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * CF * pow(NQCD, -1) + (- 32 / (1 - x) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * CF * pow(NQCD, -1)) + (- 32 / (1 - x) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * CF * pow(NQCD, -1)) + 32 / (1 - x) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * CF * pow(NQCD, -1) + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * z * CF * pow(NQCD, -1)) + (- 6 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * x * z * CF * pow(NQCD, -1)) + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * x * pow(z, 2) * CF * pow(NQCD, -1) + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * CF * pow(NQCD, -1)) + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * z * CF * pow(NQCD, -1)) + 60 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * pow(z, 2) * CF * pow(NQCD, -1) + (- 48 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * pow(z, 3) * CF * pow(NQCD, -1)) + (- 2 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * CF * pow(NQCD, -1)) + 24 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * z * CF * pow(NQCD, -1) + (- 28 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(x) * x * pow(z, 2) * CF * pow(NQCD, -1)) + (- 4 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * z * CF * pow(NQCD, -1)) + (- 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * pow(z, 2) * CF * pow(NQCD, -1)) + 48 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * pow(z, 3) * CF * pow(NQCD, -1) + (- 12 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * x * z * CF * pow(NQCD, -1)) +  + 28 / (1 + 2 * x - 4 * x * z + pow(x, 2)) * ln(z) * x * pow(z, 2) * CF * pow(NQCD, -1) + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF * pow(NQCD, -1)) + (- 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF * pow(NQCD, -1)) + 144 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * CF * pow(NQCD, -1) + (- 96 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 4) * CF * pow(NQCD, -1)) + (- 16 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF * pow(NQCD, -1)) + 80 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * CF * pow(NQCD, -1) + (- 72 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * CF * pow(NQCD, -1)) + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF * pow(NQCD, -1) + 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF * pow(NQCD, -1) +  + (-144 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * CF * pow(NQCD, -1)) + 96 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 4) * CF * pow(NQCD, -1) + 16 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF * pow(NQCD, -1) + (- 80 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * CF * pow(NQCD, -1)) + 72 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * CF * pow(NQCD, -1) + (- 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * CF * pow(NQCD, -1)) + (- 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF * pow(NQCD, -1)) + 144 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 3) * CF * pow(NQCD, -1) + (- 96 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 4) * CF * pow(NQCD, -1)) +  + (-16 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * CF * pow(NQCD, -1)) + 80 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * CF * pow(NQCD, -1) + (- 72 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * CF * pow(NQCD, -1)) + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * CF * pow(NQCD, -1) + 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF * pow(NQCD, -1) + (- 144 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 3) * CF * pow(NQCD, -1)) + 96 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 4) * CF * pow(NQCD, -1) + 16 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * CF * pow(NQCD, -1) +  + (-80 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * CF * pow(NQCD, -1)) + 72 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * CF * pow(NQCD, -1) + 8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF * pow(NQCD, -1) + 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF * pow(NQCD, -1) + (- 144 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * CF * pow(NQCD, -1)) + 96 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 4) * CF * pow(NQCD, -1) + 16 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF * pow(NQCD, -1) + (- 80 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * CF * pow(NQCD, -1)) + 72 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * CF * pow(NQCD, -1) +  + (-8 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF * pow(NQCD, -1)) + (- 36 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF * pow(NQCD, -1)) + 144 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * CF * pow(NQCD, -1) + (- 96 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 4) * CF * pow(NQCD, -1)) + (- 16 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF * pow(NQCD, -1)) + 80 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * CF * pow(NQCD, -1) + (- 72 / (1 + 2 * x - 4 * x * z + pow(x, 2)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * CF * pow(NQCD, -1)) + 12 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) * ln(x) * z * CF * pow(NQCD, -1) + (- 60 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) * ln(x) * pow(z, 2) * CF * pow(NQCD, -1)) +  + 48 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) * ln(x) * pow(z, 3) * CF * pow(NQCD, -1) + 12 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) * ln(x) * x * z * CF * pow(NQCD, -1) + (- 156 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) * ln(x) * x * pow(z, 2) * CF * pow(NQCD, -1)) + 336 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) * ln(x) * x * pow(z, 3) * CF * pow(NQCD, -1) + (- 192 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) * ln(x) * x * pow(z, 4) * CF * pow(NQCD, -1)) + 36 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) * ln(z) * pow(z, 2) * CF * pow(NQCD, -1) + (- 48 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) * ln(z) * pow(z, 3) * CF * pow(NQCD, -1)) + 60 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) * ln(z) * x * pow(z, 2) * CF * pow(NQCD, -1) + (- 240 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) * ln(z) * x * pow(z, 3) * CF * pow(NQCD, -1)) + 192 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) * ln(z) * x * pow(z, 4) * CF * pow(NQCD, -1) +  + 48 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF * pow(NQCD, -1) + (- 144 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * CF * pow(NQCD, -1)) + 96 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 4) * CF * pow(NQCD, -1) + 72 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * CF * pow(NQCD, -1) + (- 456 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * CF * pow(NQCD, -1)) + 768 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 4) * CF * pow(NQCD, -1) +  + (-384 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 5) * CF * pow(NQCD, -1)) + (- 48 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF * pow(NQCD, -1)) + 144 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * CF * pow(NQCD, -1) + (- 96 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 4) * CF * pow(NQCD, -1)) + (- 72 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * CF * pow(NQCD, -1)) + 456 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * CF * pow(NQCD, -1) +  + (-768 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 4) * CF * pow(NQCD, -1)) + 384 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 5) * CF * pow(NQCD, -1) + 48 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF * pow(NQCD, -1) + (- 144 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 3) * CF * pow(NQCD, -1)) + 96 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 4) * CF * pow(NQCD, -1) + 72 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * CF * pow(NQCD, -1) +  + (-456 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * CF * pow(NQCD, -1)) + 768 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 4) * CF * pow(NQCD, -1) + (- 384 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 5) * CF * pow(NQCD, -1)) + (- 48 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF * pow(NQCD, -1)) + 144 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 3) * CF * pow(NQCD, -1) + (- 96 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 4) * CF * pow(NQCD, -1)) +  + (-72 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 2) * CF * pow(NQCD, -1)) + 456 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 3) * CF * pow(NQCD, -1) + (- 768 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 4) * CF * pow(NQCD, -1)) + 384 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * pow(z, 5) * CF * pow(NQCD, -1) + (- 48 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF * pow(NQCD, -1)) + 144 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * CF * pow(NQCD, -1) +  + (-96 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 4) * CF * pow(NQCD, -1)) + (- 72 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * CF * pow(NQCD, -1)) + 456 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * CF * pow(NQCD, -1) + (- 768 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 4) * CF * pow(NQCD, -1)) + 384 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 5) * CF * pow(NQCD, -1) + 48 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF * pow(NQCD, -1) +  + (-144 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 3) * CF * pow(NQCD, -1)) + 96 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 4) * CF * pow(NQCD, -1) + 72 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 2) * CF * pow(NQCD, -1) + (- 456 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 3) * CF * pow(NQCD, -1)) + 768 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 4) * CF * pow(NQCD, -1) + (- 384 / (1 + 4 * x - 8 * x * z + 6 * pow(x, 2) - 16 * pow(x, 2) * z + 16 * pow(x, 2) * pow(z, 2) + 4 * pow(x, 3) - 8 * pow(x, 3) * z + pow(x, 4)) / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * pow(z, 5) * CF * pow(NQCD, -1)) +  + (-1. / 2. / (z - x) * z * CF * pow(NQCD, -1)) + (- 1. / 2. / (z - x) * z * CF * NQCD) + 1 / (z - x) * pow(z, 2) * CF * pow(NQCD, -1) + 1 / (z - x) * pow(z, 2) * CF * NQCD + 3. / 2. / (z - x) * ln(x) * CF * pow(NQCD, -1) + (- 3. / 2. / (z - x) * ln(x) * CF * NQCD) + 5. / 2. / (z - x) * ln(x) * z * CF * pow(NQCD, -1) + (- 1. / 2. / (z - x) * ln(x) * z * CF * NQCD) + (- 4 / (z - x) * ln(x) * pow(z, 2) * CF * NQCD) + (- 3. / 2. / (z - x) * ln(z) * CF * pow(NQCD, -1)) + 3. / 2. / (z - x) * ln(z) * CF * NQCD + (- 5. / 2. / (z - x) * ln(z) * z * CF * pow(NQCD, -1)) + 1. / 2. / (z - x) * ln(z) * z * CF * NQCD + 4 / (z - x) * ln(z) * pow(z, 2) * CF * NQCD + (- 1. / 2. / (pow(z, 2) - 2 * x * z + pow(x, 2)) * ln(x) * pow(z, 2) * CF * pow(NQCD, -1)) + (- 1. / 2. / (pow(z, 2) - 2 * x * z + pow(x, 2)) * ln(x) * pow(z, 2) * CF * NQCD) + 1 / (pow(z, 2) - 2 * x * z + pow(x, 2)) * ln(x) * pow(z, 3) * CF * pow(NQCD, -1) + 1 / (pow(z, 2) - 2 * x * z + pow(x, 2)) * ln(x) * pow(z, 3) * CF * NQCD + 1. / 2. / (pow(z, 2) - 2 * x * z + pow(x, 2)) * ln(z) * pow(z, 2) * CF * pow(NQCD, -1) + 1. / 2. / (pow(z, 2) - 2 * x * z + pow(x, 2)) * ln(z) * pow(z, 2) * CF * NQCD + (- 1 / (pow(z, 2) - 2 * x * z + pow(x, 2)) * ln(z) * pow(z, 3) * CF * pow(NQCD, -1)) + (- 1 / (pow(z, 2) - 2 * x * z + pow(x, 2)) * ln(z) * pow(z, 3) * CF * NQCD) + (- 16 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * CF * pow(NQCD, -1)) + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF * pow(NQCD, -1) + (- 12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF * pow(NQCD, -1)) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * CF * pow(NQCD, -1)) +  + (-8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x - mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF * pow(NQCD, -1)) + 16 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * CF * pow(NQCD, -1) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF * pow(NQCD, -1)) + 12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF * pow(NQCD, -1) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * CF * pow(NQCD, -1) + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * ln(x) * ln(1 + x + mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF * pow(NQCD, -1) + (- 16 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * CF * pow(NQCD, -1)) + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * CF * pow(NQCD, -1) + (- 12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF * pow(NQCD, -1)) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * CF * pow(NQCD, -1)) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * CF * pow(NQCD, -1)) +  + 16 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * CF * pow(NQCD, -1) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * z * CF * pow(NQCD, -1)) + 12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * pow(z, 2) * CF * pow(NQCD, -1) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * CF * pow(NQCD, -1) + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * pow(x, -1) + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2)) * pow(x, -1)) * x * z * CF * pow(NQCD, -1) + 16 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * CF * pow(NQCD, -1) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF * pow(NQCD, -1)) + 12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF * pow(NQCD, -1) + 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * CF * pow(NQCD, -1) + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x - 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF * pow(NQCD, -1) + (- 16 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * CF * pow(NQCD, -1)) +  + 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * z * CF * pow(NQCD, -1) + (- 12 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * pow(z, 2) * CF * pow(NQCD, -1)) + (- 2 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * CF * pow(NQCD, -1)) + (- 8 / (mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * Li2(1. / 2. - 1. / 2. * x + 1. / 2. * mysqrt(1 + 2 * x - 4 * x * z + pow(x, 2))) * x * z * CF * pow(NQCD, -1));
        res += tmp;
    }

    return res;
}

double RG_RG_001(double x, double z, double NF) {

    double res = 0.0;
    double tiny = 1E-4;
    double tinyinv = 1. / tiny;

    double u = x + z;
    double v = x - z;

    // x=z
    if (std::abs(v) <= tiny && u >= 2 - tiny) {
        return 0.;
    }
    if (std::abs(v) <= tiny && u <= tiny) {
        return 0.;
    }

    // intersection region of x=z and x=1-z:
    if (std::abs(v) < .99 * tiny && std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double v0 = -tiny;
        double u1 = 1. - tiny;
        double v1 = tiny;
        double u2 = 1. + tiny;
        double v2 = -tiny;

        double x0 = .5 * (u0 + v0);
        double z0 = .5 * (u0 - v0);
        double x1 = .5 * (u1 + v1);
        double z1 = .5 * (u1 - v1);
        double x2 = .5 * (u2 + v2);
        double z2 = .5 * (u2 - v2);

        double pt0 = RG_RG_001(x0, z0, NF);
        double pt1 = RG_RG_001(x1, z1, NF);
        double pt2 = RG_RG_001(x2, z2, NF);

        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if (std::abs(v) < .99 * tiny) {
        double v0 = -tiny;
        double v1 = tiny;

        double x0 = .5 * (u + v0);
        double z0 = .5 * (u - v0);
        double x1 = .5 * (u + v1);
        double z1 = .5 * (u - v1);

        double pt0 = RG_RG_001(x0, z0, NF);
        double pt1 = RG_RG_001(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0);
        return res;
    }

    // x=1-z
    if (std::abs(u - 1.) <= tiny && v <= tiny - 1.) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) <= tiny && v >= 1. - tiny) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double u1 = 1. + tiny;

        double x0 = .5 * (u0 + v);
        double z0 = .5 * (u0 - v);
        double x1 = .5 * (u1 + v);
        double z1 = .5 * (u1 - v);

        double pt0 = RG_RG_001(x0, z0, NF);
        double pt1 = RG_RG_001(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if (z != x && z != 1. - x) {
        double tmp = 0.0;
        tmp = 2 * lmua * CF * pow(NQCD, -1) + (- 2 * lmua * CF * NQCD) + (- lmua * z * CF * pow(NQCD, -1)) + lmua * z * CF * NQCD + 3 * lmua * x * CF * pow(NQCD, -1) + (- 3 * lmua * x * CF * NQCD) + 2 * lmua * x * z * CF * pow(NQCD, -1) + (- 2 * lmua * x * z * CF * NQCD) + lmua * ln(1 - z) * CF * pow(NQCD, -1) + (- lmua * ln(1 - z) * CF * NQCD) + 5 * lmua * ln(1 - z) * z * CF * pow(NQCD, -1) + (- 5 * lmua * ln(1 - z) * z * CF * NQCD) + 5 * lmua * ln(1 - z) * x * CF * pow(NQCD, -1) + (- 5 * lmua * ln(1 - z) * x * CF * NQCD) + lmua * ln(1 - z) * x * z * CF * pow(NQCD, -1) + (- lmua * ln(1 - z) * x * z * CF * NQCD) + lmua * ln(1 - x) * CF * pow(NQCD, -1) + (- lmua * ln(1 - x) * CF * NQCD) + lmua * ln(1 - x) * z * CF * pow(NQCD, -1) + (-lmua * ln(1 - x) * z * CF * NQCD) + lmua * ln(1 - x) * x * CF * pow(NQCD, -1) + (- lmua * ln(1 - x) * x * CF * NQCD) + lmua * ln(1 - x) * x * z * CF * pow(NQCD, -1) + (- lmua * ln(1 - x) * x * z * CF * NQCD) + (-ln(x) * lmua * CF * pow(NQCD, -1)) + ln(x) * lmua * CF * NQCD + (- ln(x) * lmua * z * CF * pow(NQCD, -1)) + ln(x) * lmua * z * CF * NQCD + (- ln(x) * lmua * x * CF * pow(NQCD, -1)) + ln(x) * lmua * x * CF * NQCD + (- ln(x) * lmua * x * z * CF * pow(NQCD, -1)) + ln(x) * lmua * x * z * CF * NQCD + (- ln(z) * lmua * CF * pow(NQCD, -1)) + ln(z) * lmua * CF * NQCD + (- 3 * ln(z) * lmua * z * CF * pow(NQCD, -1)) + 3 * ln(z) * lmua * z * CF * NQCD + (- 3 * ln(z) * lmua * x * CF * pow(NQCD, -1)) + 3 * ln(z) * lmua * x * CF * NQCD + (- ln(z) * lmua * x * z * CF * pow(NQCD, -1)) + ln(z) * lmua * x * z * CF * NQCD + 2 / (1 - z) * ln(z) * lmua * CF * pow(NQCD, -1) + (- 2 / (1 - z) * ln(z) * lmua * CF * NQCD) + 2 / (1 - z) * ln(z) * lmua * x * CF * pow(NQCD, -1) + (- 2 / (1 - z) * ln(z) * lmua * x * CF * NQCD) + 2 / (1 - x) * ln(x) * lmua * CF * pow(NQCD, -1) + (- 2 / (1 - x) * ln(x) * lmua * CF * NQCD) + 2 / (1 - x) * ln(x) * lmua * z * CF * pow(NQCD, -1) + (- 2 / (1 - x) * ln(x) * lmua * z * CF * NQCD);
        res += tmp;
    }

    return res;
}

double RG_RG_010(double x, double z, double NF) {

    double res = 0.0;
    double tiny = 1E-4;
    double tinyinv = 1. / tiny;

    double u = x + z;
    double v = x - z;

    // x=z
    if (std::abs(v) <= tiny && u >= 2 - tiny) {
        return 0.;
    }
    if (std::abs(v) <= tiny && u <= tiny) {
        return 0.;
    }

    // intersection region of x=z and x=1-z:
    if (std::abs(v) < .99 * tiny && std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double v0 = -tiny;
        double u1 = 1. - tiny;
        double v1 = tiny;
        double u2 = 1. + tiny;
        double v2 = -tiny;

        double x0 = .5 * (u0 + v0);
        double z0 = .5 * (u0 - v0);
        double x1 = .5 * (u1 + v1);
        double z1 = .5 * (u1 - v1);
        double x2 = .5 * (u2 + v2);
        double z2 = .5 * (u2 - v2);

        double pt0 = RG_RG_010(x0, z0, NF);
        double pt1 = RG_RG_010(x1, z1, NF);
        double pt2 = RG_RG_010(x2, z2, NF);

        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if (std::abs(v) < .99 * tiny) {
        double v0 = -tiny;
        double v1 = tiny;

        double x0 = .5 * (u + v0);
        double z0 = .5 * (u - v0);
        double x1 = .5 * (u + v1);
        double z1 = .5 * (u - v1);

        double pt0 = RG_RG_010(x0, z0, NF);
        double pt1 = RG_RG_010(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0);
        return res;
    }

    // x=1-z
    if (std::abs(u - 1.) <= tiny && v <= tiny - 1.) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) <= tiny && v >= 1. - tiny) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double u1 = 1. + tiny;

        double x0 = .5 * (u0 + v);
        double z0 = .5 * (u0 - v);
        double x1 = .5 * (u1 + v);
        double z1 = .5 * (u1 - v);

        double pt0 = RG_RG_010(x0, z0, NF);
        double pt1 = RG_RG_010(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if (z != x && z != 1. - x) {
        double tmp = 0.0;
        tmp = 2 * lmuf * CF * pow(NQCD, -1) + (- 2 * lmuf * CF * NQCD) + 3 * lmuf * z * CF * pow(NQCD, -1) + (- 3 * lmuf * z * CF * NQCD) + (- lmuf * x * CF * pow(NQCD, -1)) + lmuf * x * CF * NQCD + 2 * lmuf * x * z * CF * pow(NQCD, -1) + (- 2 * lmuf * x * z * CF * NQCD) + lmuf * ln(1 - z) * CF * pow(NQCD, -1) + (- lmuf * ln(1 - z) * CF * NQCD) + lmuf * ln(1 - z) * z * CF * pow(NQCD, -1) + (- lmuf * ln(1 - z) * z * CF * NQCD) + lmuf * ln(1 - z) * x * CF * pow(NQCD, -1) + (- lmuf * ln(1 - z) * x * CF * NQCD) + lmuf * ln(1 - z) * x * z * CF * pow(NQCD, -1) + (- lmuf * ln(1 - z) * x * z * CF * NQCD) + lmuf * ln(1 - x) * CF * pow(NQCD, -1) + (- lmuf * ln(1 - x) * CF * NQCD) + 5 * lmuf * ln(1 - x) * z * CF * pow(NQCD, -1) + (- 5 * lmuf * ln(1 - x) * z * CF * NQCD) + 5 * lmuf * ln(1 - x) * x * CF * pow(NQCD, -1) + (- 5 * lmuf * ln(1 - x) * x * CF * NQCD) + lmuf * ln(1 - x) * x * z * CF * pow(NQCD, -1) + (- lmuf * ln(1 - x) * x * z * CF * NQCD) + (- ln(x) * lmuf * CF * pow(NQCD, -1)) + ln(x) * lmuf * CF * NQCD + (- 3 * ln(x) * lmuf * z * CF * pow(NQCD, -1)) + 3 * ln(x) * lmuf * z * CF * NQCD + (- 3 * ln(x) * lmuf * x * CF * pow(NQCD, -1)) + 3 * ln(x) * lmuf * x * CF * NQCD + (- ln(x) * lmuf * x * z * CF * pow(NQCD, -1)) + ln(x) * lmuf * x * z * CF * NQCD + ln(z) * lmuf * CF * pow(NQCD, -1) + (- ln(z) * lmuf * CF * NQCD) + ln(z) * lmuf * z * CF * pow(NQCD, -1) + (- ln(z) * lmuf * z * CF * NQCD) + ln(z) * lmuf * x * CF * pow(NQCD, -1) + (- ln(z) * lmuf * x * CF * NQCD) + ln(z) * lmuf * x * z * CF * pow(NQCD, -1) + (- ln(z) * lmuf * x * z * CF * NQCD) + (- 2 / (1 - z) * ln(z) * lmuf * CF * pow(NQCD, -1)) + 2 / (1 - z) * ln(z) * lmuf * CF * NQCD + (- 2 / (1 - z) * ln(z) * lmuf * x * CF * pow(NQCD, -1)) + 2 / (1 - z) * ln(z) * lmuf * x * CF * NQCD + 2 / (1 - x) * ln(x) * lmuf * CF * pow(NQCD, -1) + (- 2 / (1 - x) * ln(x) * lmuf * CF * NQCD) + 2 / (1 - x) * ln(x) * lmuf * z * CF * pow(NQCD, -1) + (- 2 / (1 - x) * ln(x) * lmuf * z * CF * NQCD);
        res += tmp;
    }

    return res;
}

double RG_RG_011(double x, double z, double NF) {

    double res = 0.0;
    double tiny = 1E-4;
    double tinyinv = 1. / tiny;

    double u = x + z;
    double v = x - z;

    // x=z
    if (std::abs(v) <= tiny && u >= 2 - tiny) {
        return 0.;
    }
    if (std::abs(v) <= tiny && u <= tiny) {
        return 0.;
    }

    // intersection region of x=z and x=1-z:
    if (std::abs(v) < .99 * tiny && std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double v0 = -tiny;
        double u1 = 1. - tiny;
        double v1 = tiny;
        double u2 = 1. + tiny;
        double v2 = -tiny;

        double x0 = .5 * (u0 + v0);
        double z0 = .5 * (u0 - v0);
        double x1 = .5 * (u1 + v1);
        double z1 = .5 * (u1 - v1);
        double x2 = .5 * (u2 + v2);
        double z2 = .5 * (u2 - v2);

        double pt0 = RG_RG_011(x0, z0, NF);
        double pt1 = RG_RG_011(x1, z1, NF);
        double pt2 = RG_RG_011(x2, z2, NF);

        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if (std::abs(v) < .99 * tiny) {
        double v0 = -tiny;
        double v1 = tiny;

        double x0 = .5 * (u + v0);
        double z0 = .5 * (u - v0);
        double x1 = .5 * (u + v1);
        double z1 = .5 * (u - v1);

        double pt0 = RG_RG_011(x0, z0, NF);
        double pt1 = RG_RG_011(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0);
        return res;
    }

    // x=1-z
    if (std::abs(u - 1.) <= tiny && v <= tiny - 1.) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) <= tiny && v >= 1. - tiny) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double u1 = 1. + tiny;

        double x0 = .5 * (u0 + v);
        double z0 = .5 * (u0 - v);
        double x1 = .5 * (u1 + v);
        double z1 = .5 * (u1 - v);

        double pt0 = RG_RG_011(x0, z0, NF);
        double pt1 = RG_RG_011(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if (z != x && z != 1. - x) {
        double tmp = 0.0;
        tmp = (- 2 * lmuf * lmua * CF * pow(NQCD, -1)) + 2 * lmuf * lmua * CF * NQCD + (- 2 * lmuf * lmua * z * CF * pow(NQCD, -1)) + 2 * lmuf * lmua * z * CF * NQCD + (- 2 * lmuf * lmua * x * CF * pow(NQCD, -1)) + 2 * lmuf * lmua * x * CF * NQCD + (- 2 * lmuf * lmua * x * z * CF * pow(NQCD, -1)) + 2 * lmuf * lmua * x * z * CF * NQCD;
        res += tmp;
    }

    return res;
}

double RG_RG_100(double x, double z, double NF) {

    double res = 0.0;
    double tiny = 1E-4;
    double tinyinv = 1. / tiny;

    double u = x + z;
    double v = x - z;

    // x=z
    if (std::abs(v) <= tiny && u >= 2 - tiny) {
        return 0.;
    }
    if (std::abs(v) <= tiny && u <= tiny) {
        return 0.;
    }

    // intersection region of x=z and x=1-z:
    if (std::abs(v) < .99 * tiny && std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double v0 = -tiny;
        double u1 = 1. - tiny;
        double v1 = tiny;
        double u2 = 1. + tiny;
        double v2 = -tiny;

        double x0 = .5 * (u0 + v0);
        double z0 = .5 * (u0 - v0);
        double x1 = .5 * (u1 + v1);
        double z1 = .5 * (u1 - v1);
        double x2 = .5 * (u2 + v2);
        double z2 = .5 * (u2 - v2);

        double pt0 = RG_RG_100(x0, z0, NF);
        double pt1 = RG_RG_100(x1, z1, NF);
        double pt2 = RG_RG_100(x2, z2, NF);

        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0) + .5 * (pt2 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if (std::abs(v) < .99 * tiny) {
        double v0 = -tiny;
        double v1 = tiny;

        double x0 = .5 * (u + v0);
        double z0 = .5 * (u - v0);
        double x1 = .5 * (u + v1);
        double z1 = .5 * (u - v1);

        double pt0 = RG_RG_100(x0, z0, NF);
        double pt1 = RG_RG_100(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (v - v0);
        return res;
    }

    // x=1-z
    if (std::abs(u - 1.) <= tiny && v <= tiny - 1.) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) <= tiny && v >= 1. - tiny) {
        res = 0.;
        return res;
    }
    if (std::abs(u - 1.) < .99 * tiny) {
        double u0 = 1. - tiny;
        double u1 = 1. + tiny;

        double x0 = .5 * (u0 + v);
        double z0 = .5 * (u0 - v);
        double x1 = .5 * (u1 + v);
        double z1 = .5 * (u1 - v);

        double pt0 = RG_RG_100(x0, z0, NF);
        double pt1 = RG_RG_100(x1, z1, NF);
        res = pt0 + .5 * (pt1 - pt0) * tinyinv * (u - u0);
        return res;
    }
    if (z != x && z != 1. - x) {
        double tmp = 0.0;
        tmp = 22. / 3. * lmur * z * CF * NQCD + (- 4. / 3. * lmur * z * CF * NF) + 22. / 3. * lmur * x * CF * NQCD + (- 4. / 3. * lmur * x * CF * NF);
        res += tmp;
    }

    return res;
}

/*
  Branch extraction report:
  Created helper functions for:
  - D0_D0: 000, 001, 010, 011, 100
  - D0_D1: 000, 001, 010
  - D0_D2: 000
  - D0_DL: 000, 001, 010, 011, 020, 110
  - D0_RG: 000, 001, 010, 011, 100
  - D1_D0: 000, 001, 010
  - D1_D1: 000
  - D1_DL: 000, 001, 010, 020, 100
  - D1_RG: 000, 001, 010
  - D2_D0: 000
  - D2_DL: 000, 010
  - D2_RG: 000
  - D3_DL: 000
  - DL_D0: 000, 001, 002, 010, 011, 101
  - DL_D1: 000, 001, 002, 010, 100
  - DL_D2: 000, 001
  - DL_D3: 000
  - DL_DL: 000, 001, 002, 010, 011, 020, 100, 101, 110
  - DL_RG: 000, 001, 002, 010, 011, 100, 101
  - RG_D0: 000, 001, 010, 011, 100
  - RG_D1: 000, 001, 010
  - RG_D2: 000
  - RG_DL: 000, 001, 010, 011, 020, 100, 110
  - RG_RG: 000, 001, 010, 011, 100
*/

/*
  Inverted Branch Report (By Number):
  - 000: D0_D0, D0_D1, D0_D2, D0_DL, D0_RG, D1_D0, D1_D1, D1_DL, D1_RG, D2_D0, D2_DL, D2_RG, D3_DL, DL_D0, DL_D1, DL_D2, DL_D3, DL_DL, DL_RG, RG_D0, RG_D1, RG_D2, RG_DL, RG_RG
  - 001: D0_D0, D0_D1, D0_DL, D0_RG, D1_D0, D1_DL, D1_RG, DL_D0, DL_D1, DL_D2, DL_DL, DL_RG, RG_D0, RG_D1, RG_DL, RG_RG
  - 002: DL_D0, DL_D1, DL_DL, DL_RG
  - 010: D0_D0, D0_D1, D0_DL, D0_RG, D1_D0, D1_DL, D1_RG, D2_DL, DL_D0, DL_D1, DL_DL, DL_RG, RG_D0, RG_D1, RG_DL, RG_RG
  - 011: D0_D0, D0_DL, D0_RG, DL_D0, DL_DL, DL_RG, RG_D0, RG_DL, RG_RG
  - 020: D0_DL, D1_DL, DL_DL, RG_DL
  - 100: D0_D0, D0_RG, D1_DL, DL_D1, DL_DL, DL_RG, RG_D0, RG_DL, RG_RG
  - 101: DL_D0, DL_DL, DL_RG
  - 110: D0_DL, DL_DL, RG_DL
*/
