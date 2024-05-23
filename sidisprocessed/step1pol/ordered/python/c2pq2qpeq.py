def C2Pq2qpEq(inx, inz, cx, cz,                 Q, muR, muF, muA):
      res = (0.0)

      rln2 = (ln(2.0))

      LMUR = (2 * log(muR / Q))
      LMUF = (2 * log(muF / Q))
      LMUA = (2 * log(muA / Q))

      NC = (3.0)
      CF = (4.0 / 3.0)
      TR = (0.5)

      if cx == "D" and cz == "D":
      
            res = (0)

            return res
      
      if cx == "D" and cz == "0":
      
            res = (0)

            return res
      
      if cx == "D" and cz == "1":
      
            res = (0)

            return res
      
      if cx == "D" and cz == "2":
      
            res = (0)

            return res
      
      if cx == "D" and cz == "3":
      
            res = (0)

            return res
      
      if cx == "0" and cz == "D":
      
            res = (0)

            return res
      
      if cx == "0" and cz == "0":
      
            res = (0)

            return res
      
      if cx == "0" and cz == "1":
      
            res = (0)

            return res
      
      if cx == "0" and cz == "2":
      
            res = (0)

            return res
      
      if cx == "0" and cz == "3":
      
            res = (0)

            return res
      
      if cx == "1" and cz == "D":
      
            res = (0)

            return res
      
      if cx == "1" and cz == "0":
      
            res = (0)

            return res
      
      if cx == "1" and cz == "1":
      
            res = (0)

            return res
      
      if cx == "1" and cz == "2":
      
            res = (0)

            return res
      
      if cx == "1" and cz == "3":
      
            res = (0)

            return res
      
      if cx == "2" and cz == "D":
      
            res = (0)

            return res
      
      if cx == "2" and cz == "0":
      
            res = (0)

            return res
      
      if cx == "2" and cz == "1":
      
            res = (0)

            return res
      
      if cx == "2" and cz == "2":
      
            res = (0)

            return res
      
      if cx == "2" and cz == "3":
      
            res = (0)

            return res
      
      if cx == "3" and cz == "D":
      
            res = (0)

            return res
      
      if cx == "3" and cz == "0":
      
            res = (0)

            return res
      
      if cx == "3" and cz == "1":
      
            res = (0)

            return res
      
      if cx == "3" and cz == "2":
      
            res = (0)

            return res
      
      if cx == "3" and cz == "3":
      
            res = (0)

            return res
      
      if cx == "D" and cz == "R":
      
            z = (inz)
            omz = (1. - z)
            opz = (1. + z)
            # Split orders:
            res = (0)
            # Order 000:
            res += ( +(-1) * 107. / 108. * pow(z, -1) * CF + (-1) * 11. / 9. * CF + (-1) * 4. / 9. * z * CF + 287. / 108. * pow(z, 2) * CF + 2 * zeta3 * CF + 2 * zeta3 * z * CF + (-1) * 1. / 6. * pow(pi, 2) * CF + (-1) * 1. / 4. * pow(pi, 2) * z * CF + (-1) * 7. / 18. * ln(z) * pow(z, -1) * CF + (-1) * 5 * ln(z) * CF + (-1) * 9. / 2. * ln(z) * z * CF + (-1) * 31. / 18. * ln(z) * pow(z, 2) * CF + 1. / 6. * ln(z) * pow(pi, 2) * CF + 1. / 6. * ln(z) * pow(pi, 2) * z * CF + 1. / 3. * pow(ln(z), 2) * pow(z, -1) * CF + (-1) * 1. / 8. * pow(ln(z), 2) * CF + (-1) * 5. / 8. * pow(ln(z), 2) * z * CF + 5. / 12. * pow(ln(z), 3) * CF + 5. / 12. * pow(ln(z), 3) * z * CF + 0)
            res += ( (-1) * 3. / 2. * ln(z) * pow(ln(omz), 2) * CF + (-1) * 3. / 2. * ln(z) * pow(ln(omz), 2) * z * CF + (-1) * 7. / 18. * ln(omz) * pow(z, -1) * CF + (-1) * 10. / 3. * ln(omz) * CF + 7. / 3. * ln(omz) * z * CF + 25. / 18. * ln(omz) * pow(z, 2) * CF + 1. / 3. * ln(omz) * pow(pi, 2) * CF + 1. / 3. * ln(omz) * pow(pi, 2) * z * CF + 1. / 3. * pow(ln(omz), 2) * pow(z, -1) * CF + 1. / 4. * pow(ln(omz), 2) * CF + (-1) * 1. / 4. * pow(ln(omz), 2) * z * CF + (-1) * 1. / 3. * pow(ln(omz), 2) * pow(z, 2) * CF + (-1) * ln(omz) * Li2(1 - z) * CF + (-1) * ln(omz) * Li2(1 - z) * z * CF + (-1) * 2 * ln(omz) * Li2(z) * CF + (-1) * 2 * ln(omz) * Li2(z) * z * CF + (-1) * Li3(1 - z) * CF + (-1) * Li3(1 - z) * z * CF + (-1) * 2 * Li3(z) * CF + (-1) * 2 * Li3(z) * z * CF + 0)
            res += ( (-1) * 2. / 3. * Li2(z) * pow(z, -1) * CF + 1. / 2. * Li2(z) * CF + 2 * Li2(z) * z * CF + 2. / 3. * Li2(z) * pow(z, 2) * CF + 0)
            # Order 001:
            res += ( 7. / 18. * pow(z, -1) * LMUA * CF + 10. / 3. * LMUA * CF + (-1) * 7. / 3. * z * LMUA * CF + (-1) * 25. / 18. * pow(z, 2) * LMUA * CF + (-1) * 1. / 6. * pow(pi, 2) * LMUA * CF + (-1) * 1. / 6. * pow(pi, 2) * z * LMUA * CF + (-1) * 2. / 3. * ln(z) * pow(z, -1) * LMUA * CF + 1. / 2. * ln(z) * LMUA * CF + 2 * ln(z) * z * LMUA * CF + 2. / 3. * ln(z) * pow(z, 2) * LMUA * CF + (-1) * pow(ln(z), 2) * LMUA * CF + (-1) * pow(ln(z), 2) * z * LMUA * CF + (-1) * 2. / 3. * ln(omz) * pow(z, -1) * LMUA * CF + (-1) * 1. / 2. * ln(omz) * LMUA * CF + 1. / 2. * ln(omz) * z * LMUA * CF + 2. / 3. * ln(omz) * pow(z, 2) * LMUA * CF + Li2(z) * LMUA * CF + Li2(z) * z * LMUA * CF + 0)
            # Order 002:
            res += ( 1. / 3. * pow(z, -1) * pow(LMUA, 2) * CF + 1. / 4. * pow(LMUA, 2) * CF + (-1) * 1. / 4. * z * pow(LMUA, 2) * CF + (-1) * 1. / 3. * pow(z, 2) * pow(LMUA, 2) * CF + 1. / 2. * ln(z) * pow(LMUA, 2) * CF + 1. / 2. * ln(z) * z * pow(LMUA, 2) * CF + 0)

            return res
      
      if cx == "0" and cz == "R":
      
            z = (inz)
            omz = (1. - z)
            opz = (1. + z)
            # Split orders:
            res = (0)
            # Order 000:
            res += ( +(-1) * 107. / 108. * pow(z, -1) * CF + (-1) * 11. / 9. * CF + (-1) * 4. / 9. * z * CF + 287. / 108. * pow(z, 2) * CF + 2 * zeta3 * CF + 2 * zeta3 * z * CF + (-1) * 1. / 6. * pow(pi, 2) * CF + (-1) * 1. / 4. * pow(pi, 2) * z * CF + (-1) * 7. / 18. * ln(z) * pow(z, -1) * CF + (-1) * 5 * ln(z) * CF + (-1) * 9. / 2. * ln(z) * z * CF + (-1) * 31. / 18. * ln(z) * pow(z, 2) * CF + 1. / 6. * ln(z) * pow(pi, 2) * CF + 1. / 6. * ln(z) * pow(pi, 2) * z * CF + 1. / 3. * pow(ln(z), 2) * pow(z, -1) * CF + (-1) * 1. / 8. * pow(ln(z), 2) * CF + (-1) * 5. / 8. * pow(ln(z), 2) * z * CF + 5. / 12. * pow(ln(z), 3) * CF + 5. / 12. * pow(ln(z), 3) * z * CF + 0)
            res += ( (-1) * 3. / 2. * ln(z) * pow(ln(omz), 2) * CF + (-1) * 3. / 2. * ln(z) * pow(ln(omz), 2) * z * CF + (-1) * 7. / 18. * ln(omz) * pow(z, -1) * CF + (-1) * 10. / 3. * ln(omz) * CF + 7. / 3. * ln(omz) * z * CF + 25. / 18. * ln(omz) * pow(z, 2) * CF + 1. / 3. * ln(omz) * pow(pi, 2) * CF + 1. / 3. * ln(omz) * pow(pi, 2) * z * CF + 1. / 3. * pow(ln(omz), 2) * pow(z, -1) * CF + 1. / 4. * pow(ln(omz), 2) * CF + (-1) * 1. / 4. * pow(ln(omz), 2) * z * CF + (-1) * 1. / 3. * pow(ln(omz), 2) * pow(z, 2) * CF + (-1) * ln(omz) * Li2(1 - z) * CF + (-1) * ln(omz) * Li2(1 - z) * z * CF + (-1) * 2 * ln(omz) * Li2(z) * CF + (-1) * 2 * ln(omz) * Li2(z) * z * CF + (-1) * Li3(1 - z) * CF + (-1) * Li3(1 - z) * z * CF + (-1) * 2 * Li3(z) * CF + (-1) * 2 * Li3(z) * z * CF + 0)
            res += ( (-1) * 2. / 3. * Li2(z) * pow(z, -1) * CF + 1. / 2. * Li2(z) * CF + 2 * Li2(z) * z * CF + 2. / 3. * Li2(z) * pow(z, 2) * CF + 0)
            # Order 001:
            res += ( 7. / 18. * pow(z, -1) * LMUA * CF + 10. / 3. * LMUA * CF + (-1) * 7. / 3. * z * LMUA * CF + (-1) * 25. / 18. * pow(z, 2) * LMUA * CF + (-1) * 1. / 6. * pow(pi, 2) * LMUA * CF + (-1) * 1. / 6. * pow(pi, 2) * z * LMUA * CF + (-1) * 2. / 3. * ln(z) * pow(z, -1) * LMUA * CF + 1. / 2. * ln(z) * LMUA * CF + 2 * ln(z) * z * LMUA * CF + 2. / 3. * ln(z) * pow(z, 2) * LMUA * CF + (-1) * pow(ln(z), 2) * LMUA * CF + (-1) * pow(ln(z), 2) * z * LMUA * CF + (-1) * 2. / 3. * ln(omz) * pow(z, -1) * LMUA * CF + (-1) * 1. / 2. * ln(omz) * LMUA * CF + 1. / 2. * ln(omz) * z * LMUA * CF + 2. / 3. * ln(omz) * pow(z, 2) * LMUA * CF + Li2(z) * LMUA * CF + Li2(z) * z * LMUA * CF + 0)
            # Order 002:
            res += ( 1. / 3. * pow(z, -1) * pow(LMUA, 2) * CF + 1. / 4. * pow(LMUA, 2) * CF + (-1) * 1. / 4. * z * pow(LMUA, 2) * CF + (-1) * 1. / 3. * pow(z, 2) * pow(LMUA, 2) * CF + 1. / 2. * ln(z) * pow(LMUA, 2) * CF + 1. / 2. * ln(z) * z * pow(LMUA, 2) * CF + 0)

            return res
      
      if cx == "1" and cz == "R":
      
            z = (inz)
            omz = (1. - z)
            opz = (1. + z)
            res = (2. / 3. * pow(z, -1) * CF + 1. / 2. * CF - 1. / 2. * z * CF - 2. / 3. * pow(z, 2) * CF + ln(z) * CF + ln(z) * z * CF)

            return res
      
      if cx == "2" and cz == "R":
      
            z = (inz)
            omz = (1. - z)
            opz = (1. + z)
            res = (0)

            return res
      
      if cx == "3" and cz == "R":
      
            z = (inz)
            omz = (1. - z)
            opz = (1. + z)
            res = (0)

            return res
      
      if cx == "R" and cz == "D":
      
            x = (inx)
            omx = (1. - x)
            opx = (1. + x)
            op6xpxsq = (1. + 6. * x + x * x)
            res = (0)

            return res
      
      if cx == "R" and cz == "0":
      
            x = (inx)
            omx = (1. - x)
            opx = (1. + x)
            op6xpxsq = (1. + 6. * x + x * x)
            res = (0)

            return res
      
      if cx == "R" and cz == "1":
      
            x = (inx)
            omx = (1. - x)
            opx = (1. + x)
            op6xpxsq = (1. + 6. * x + x * x)
            res = (0)

            return res
      
      if cx == "R" and cz == "2":
      
            x = (inx)
            omx = (1. - x)
            opx = (1. + x)
            op6xpxsq = (1. + 6. * x + x * x)
            res = (0)

            return res
      
      if cx == "R" and cz == "3":
      
            x = (inx)
            omx = (1. - x)
            opx = (1. + x)
            op6xpxsq = (1. + 6. * x + x * x)
            res = (0)

            return res
      
      if cx == "R" and cz == "R":
      
            x = (inx)
            z = (inz)
            omz = (1. - z)
            opz = (1. + z)
            omx = (1. - x)
            opx = (1. + x)
            op6xpxsq = (1. + 6. * x + x * x)
            xmz = (x - z)
            omxmz = (1. - x - z)
            poly2 = (1 + 2 * x + x * x - 4 * x * z)
            sqrtxz1 = (mysqrt(1 - 2 * z + z * z + 4 * x * z))
            sqrtxz2 = (mysqrt(poly2))
            sqrtxz3 = (mysqrt(x / z))
            if z < 1. - x and z < x:
            
                  tmp = (0.0)
                  tmp = (0)

                  res += ( tmp)
            
            if z > 1. - x and z < x:
            
                  tmp = (0.0)
                  tmp = (0)

                  res += ( tmp)
            
            if z < 1. - x and z > x:
            
                  tmp = (0.0)
                  tmp = (0)

                  res += ( tmp)
            
            if z > 1. - x and z > x:
            
                  tmp = (0.0)
                  tmp = (0)

                  res += ( tmp)
            
            if z > x:
            
                  tmp = (0.0)
                  tmp = (0)

                  res += ( tmp)
            
            if z < x:
            
                  tmp = (0.0)
                  tmp = (0)

                  res += ( tmp)
            
            if z < 1. - x:
            
                  tmp = (0.0)
                  tmp = (0)

                  res += ( tmp)
            
            if z > 1. - x:
            
                  tmp = (0.0)
                  tmp = (0)

                  res += ( tmp)
            
            if z != x and z != 1. - x:
            
                  tmp = (0.0)
                  # Split orders:
                  tmp = (0)
                  # Order 000:
                  tmp += ( +(-1) * 5. / 36. * pow(z, -1) * CF + 2. / 3. * CF + 37. / 12. * z * CF + (-1) * 65. / 18. * pow(z, 2) * CF + 19. / 36. * x * pow(z, -1) * CF + 5. / 3. * x * CF + (-1) * 47. / 12. * x * z * CF + 31. / 18. * x * pow(z, 2) * CF + (-1) * 1. / 6. * pow(pi, 2) * CF + (-1) * 1. / 3. * pow(pi, 2) * z * CF + (-1) * 1. / 6. * pow(pi, 2) * x * CF + (-1) * 4. / 3. * ln(x) * pow(z, -1) * CF * pow(omx, -1) + 2. / 3. * ln(x) * pow(z, -1) * CF + (-1) * 5. / 2. * ln(x) * CF * pow(omx, -1) + 3 * ln(x) * CF + 5. / 2. * ln(x) * z * CF * pow(omx, -1) + (-1) * ln(x) * z * CF + 4. / 3. * ln(x) * pow(z, 2) * CF * pow(omx, -1) + (-1) * 8. / 3. * ln(x) * pow(z, 2) * CF + 0)
                  tmp += ( 2. / 3. * ln(x) * x * pow(z, -1) * CF + ln(x) * x * CF + (-1) * 3 * ln(x) * x * z * CF + 4. / 3. * ln(x) * x * pow(z, 2) * CF + (-1) * 3 * ln(x) * ln(z) * CF * pow(omx, -1) + 2 * ln(x) * ln(z) * CF + (-1) * 3 * ln(x) * ln(z) * z * CF * pow(omx, -1) + 4 * ln(x) * ln(z) * z * CF + 2 * ln(x) * ln(z) * x * CF + (-1) * 1. / 3. * ln(z) * pow(z, -1) * CF + (-1) * 5. / 2. * ln(z) * CF + 3. / 2. * ln(z) * z * CF + 4. / 3. * ln(z) * pow(z, 2) * CF + (-1) * 1. / 3. * ln(z) * x * pow(z, -1) * CF + 1. / 2. * ln(z) * x * CF + 3. / 2. * ln(z) * x * z * CF + (-1) * 2. / 3. * ln(z) * x * pow(z, 2) * CF + (-1) * pow(ln(z), 2) * CF + (-1) * 2 * pow(ln(z), 2) * z * CF + (-1) * pow(ln(z), 2) * x * CF + 0)
                  tmp += ( (-1) * ln(z) * ln(omx) * CF + (-1) * 2 * ln(z) * ln(omx) * z * CF + (-1) * ln(z) * ln(omx) * x * CF + (-1) * 1. / 3. * ln(omx) * pow(z, -1) * CF + (-1) * 3. / 2. * ln(omx) * CF + 1. / 2. * ln(omx) * z * CF + 4. / 3. * ln(omx) * pow(z, 2) * CF + (-1) * 1. / 3. * ln(omx) * x * pow(z, -1) * CF + (-1) * 1. / 2. * ln(omx) * x * CF + 3. / 2. * ln(omx) * x * z * CF + (-1) * 2. / 3. * ln(omx) * x * pow(z, 2) * CF + (-1) * 1. / 3. * ln(omz) * pow(z, -1) * CF + (-1) * 3. / 2. * ln(omz) * CF + 1. / 2. * ln(omz) * z * CF + 4. / 3. * ln(omz) * pow(z, 2) * CF + (-1) * 1. / 3. * ln(omz) * x * pow(z, -1) * CF + (-1) * 1. / 2. * ln(omz) * x * CF + 3. / 2. * ln(omz) * x * z * CF + (-1) * 2. / 3. * ln(omz) * x * pow(z, 2) * CF + Li2(z) * CF + 0)
                  tmp += ( 2 * Li2(z) * z * CF + Li2(z) * x * CF + 0)
                  # Order 001:
                  tmp += ( 1. / 3. * pow(z, -1) * LMUA * CF + 3. / 2. * LMUA * CF + (-1) * 1. / 2. * z * LMUA * CF + (-1) * 4. / 3. * pow(z, 2) * LMUA * CF + 1. / 3. * x * pow(z, -1) * LMUA * CF + 1. / 2. * x * LMUA * CF + (-1) * 3. / 2. * x * z * LMUA * CF + 2. / 3. * x * pow(z, 2) * LMUA * CF + ln(z) * LMUA * CF + 2 * ln(z) * z * LMUA * CF + ln(z) * x * LMUA * CF + 0)

                  res += ( tmp)
            
            return res
      
