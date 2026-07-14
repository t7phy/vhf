import os

config_template = """QCDParameter:
  NFlavor: 5
  EvolveOrder: 3
  HardOrder: 3
  AlphaSOrder: 3
  mc: 1.3
  mb: 4.75
  mt: {top_mass}
  Qini: 1.295
  AlphaS: {alpha_s}
  AlphaS_Q0: 91.19
  Evolution: Hoppet #Hoppet/APFEL/APFELxx
  EvolutionOption: Default #Default/QED/smallx
LMPenalty:
  - penalty: [1, ratioPDF, [1], [10.0, 1.0, 0.2, 1e-8]]
  - penalty: [2, ratioPDF, [1], [100.0, 0.85, 0.2, 1e-5]]
  - penalty: [3, ratioPDF, [1], [10.0, 1.0, 0.0, 0.6]]
  - penalty: [4, ratioPDF, [1], [10.0, 1.0, 0.0, 0.9]]
  - penalty: [5, LargeCoefficient, [1], [0.01]]
  - penalty: [6, SystematicShift, [504, 25, 514, 23], [0.5, 0.5]]
PDFInput:
  PDFInputType: None #None/CTEQ/LHAPDF
  PDFInput: CT18NNLO
  PDFiSet: 0
Algorithm:
  Name: Migrad #Simplex/Migrad/Minimize/Fumili...
  MaxCall: 100000
  Tolerance: 1e-6
  LFit: 30
Thread:
  nDISThread: 55
  nVBPThread: 15
ErrorSet:
  dmeasTol: 0.008
  Tolerance: 100.0
  Tier2Type: CTEQ
  CalcLevel: Full #PDFOnly/Full"""

datalist_template = """GlobalPath:
  data: /mnt/home/fuyao3/FittingCode/da/data2025c/
  applgrid: /mnt/home/fuyao3/FittingCode/ApplGridtables/
  fastnlo: /mnt/home/fuyao3/FittingCode/fastNLOtables/
  pineappl: /mnt/research/CTEQ-TEA/top_grids/{top_dir}/
DataInformation:
  LHCb7ZWrap: #245
    Path: LHCb7ZWrap_up2025
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: LHC
    subType: LHCb7ZWrap
    ApplGrid:
      - 245_1.root
      - 245_2.root
      - 245_3.root
    ApplRange:
      - [1, 1, 17]
    FastNLO:
    KFactor: [5, 8]
    Systematic:
    Normalization:
  LHCb8ZResKF: #246
    Path: LHCb8ZResKF_up2025
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: LHC
    subType: LHCb8ZResKF
    ApplGrid:
      - 246_1_KP_2018.1010.root
    ApplRange:
      - [1, 1, 17]
    FastNLO:
    KFactor: [6, 8]
    Systematic:
    Normalization:
  ATL7ZW: #248
    Path: ATL7ZW_up2025
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: LHC
    subType: ATL7ZW
    ApplGrid:
      - 248_40-6-15-3-Z0_zypeak_cc_xfitter_2018.0618.root
      - 248_40-6-15-3-Wplus_wyl_xfitter_2018.0618.root
      - 248_40-6-15-3-Wminus_wyl_xfitter_2018.0618.root
    ApplRange:
    FastNLO:
    KFactor: [8]
    Systematic:
    Normalization:
  CMS8Wxa: #249
    Path: CMS8Wxa_up2025
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: LHC
    subType: CMS8Wxa
    ApplGrid:
      - 249_Wplus_applgrid_Pt25_xfitter_2018.0618.root
      - 249_Wminus_applgrid_Pt25_xfitter_2018.0618.root
    ApplRange:
    FastNLO:
    KFactor: [9]
    Systematic:
    Normalization:
  LHCb8WZ: #250
    Path: LHCb8WZ_up2025
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: LHC
    subType: LHCb8WZ
    ApplGrid:
      - 250_1.root
      - 250_2.root
      - 250_3.root
    ApplRange:
    FastNLO:
    KFactor: [5, 10]
    Systematic:
    Normalization:
  ATL8ZpT: #253
    Path: ATL8ZpT
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: LHC
    subType: ATL8ZpT
    ApplGrid:
      - 253_4.root
      - 253_5.root
      - 253_6.root
    ApplRange:
    FastNLO:
    KFactor: [6]
    Systematic:
      - [0, 0, 0]
      - [1, 100, 1]
    Normalization:
  ATL7jtR6u: #544
    Path: ATL7jtR6u
    DataType: Jet
    CalcMode: ApplGrid
    Collider: LHC
    subType: ATL7jtR6u
    ApplGrid:
      - 510_1.root
      - 510_2.root
      - 510_3.root
      - 510_4.root
      - 510_5.root
      - 510_6.root
    ApplRange:
    FastNLO:
    KFactor: [5]
    Systematic:
      - [0, 0, 0]
      - [1, 73, 1]
    Normalization:
  CMS8pTtyt: #573
    Path: CMS8pTtyt
    DataType: Jet
    CalcMode: PineAPPL
    Collider: LHC
    subType: CMS8pTtyt
    ApplGrid:
    ApplRange:
    FastNLO:
    PineAPPL:
      - [CMS_TTBAR_8TEV_2L_DIF_PTT-YT.pineappl.lz4, CMS_TTBAR_8TEV_2L_DIF_PTT-YT-INTEGRATED.pineappl.lz4, ratio]
    KFactor:
    Systematic:
    Normalization:
  ATL8ttcoma: #580
    Path: ATL8ttcoma
    DataType: Jet
    CalcMode: PineAPPL
    Collider: LHC
    subType: ATL8ttcoma
    ApplGrid:
    ApplRange:
    FastNLO:
    PineAPPL:
      - [ATLAS_TTBAR_8TEV_LJ_DIF_PTT.pineappl.lz4]
      - [ATLAS_TTBAR_8TEV_LJ_DIF_MTTBAR.pineappl.lz4]
    KFactor:
    Systematic:
    Normalization:
  cdf2jtCor2: #504
    Path: cdf2jtCor2
    DataType: Jet
    CalcMode: FastNLO
    Collider: Tev
    subType: cdf2jtCor2
    ApplGrid:
    ApplRange:
    FastNLO:
      - fnt2007midp.tab
    KFactor:
    Systematic:
    Normalization:
  d02jtCor2: #514
    Path: d02jtCor2
    DataType: Jet
    CalcMode: FastNLO
    Collider: Tev
    subType: d02jtCor2
    ApplGrid:
    ApplRange:
    FastNLO:
      - fnt2009midp.tab
    KFactor:
    Systematic:
    Normalization:
  HERAIpII: #160
    Path: HERAIpII
    DataType: DIS
    CalcMode: CTEQ
    Collider:
    subType: HERAIpII
    ApplGrid:
    ApplRange:
    FastNLO:
    KFactor:
    Systematic:
    Normalization:
  BcdF2pCor: #101
    Path: BcdF2pCor
    DataType: DIS
    CalcMode: CTEQ
    Collider:
    subType: BcdF2pCor
    ApplGrid:
    ApplRange:
    FastNLO:
    KFactor:
    Systematic:
    Normalization: [[71, N71], [0.9676, 0.1, 1.0]]
  BcdF2dCor: #102
    Path: BcdF2dCor
    DataType: DIS
    CalcMode: CTEQ
    Collider:
    subType: BcdF2dCor
    ApplGrid:
    ApplRange:
    FastNLO:
    KFactor:
    Systematic:
    Normalization: [[71, N71], [0.9676, 1.0, 0.0]]
  NmcRatCor: #104
    Path: NmcRatCor
    DataType: DIS
    CalcMode: CTEQ
    Collider:
    subType: NmcRatCor
    ApplGrid:
    ApplRange:
    FastNLO:
    KFactor:
    Systematic:
    Normalization:
  NuTvNuChXN: #124
    Path: NuTvNuChXN
    DataType: DIS
    CalcMode: CTEQ
    Collider:
    subType: NuTvNuChXN
    ApplGrid:
    ApplRange:
    FastNLO:
    KFactor:
    Systematic:
    Normalization:
  NuTvNbChXN: #125
    Path: NuTvNbChXN
    DataType: DIS
    CalcMode: CTEQ
    Collider:
    subType: NuTvNbChXN
    ApplGrid:
    ApplRange:
    FastNLO:
    KFactor:
    Systematic:
    Normalization:
  CcfrNuChXN: #126
    Path: CcfrNuChXN
    DataType: DIS
    CalcMode: CTEQ
    Collider:
    subType: CcfrNuChXN
    ApplGrid:
    ApplRange:
    FastNLO:
    KFactor:
    Systematic:
    Normalization:
  CcfrNbChXN: #127
    Path: CcfrNbChXN
    DataType: DIS
    CalcMode: CTEQ
    Collider:
    subType: CcfrNbChXN
    ApplGrid:
    ApplRange:
    FastNLO:
    KFactor:
    Systematic:
    Normalization:
  Hn1X0ccom: #148
    Path: Hn1X0ccom
    DataType: DIS
    CalcMode: CTEQ
    Collider:
    subType: Hn1X0ccom
    ApplGrid:
    ApplRange:
    FastNLO:
    KFactor:
    Systematic:
    Normalization:
  Hn1X0bcom: #149
    Path: Hn1X0bcom
    DataType: DIS
    CalcMode: CTEQ
    Collider:
    subType: Hn1X0bcom
    ApplGrid:
    ApplRange:
    FastNLO:
    KFactor:
    Systematic:
    Normalization:
  e605: #201
    Path: e605_up2025
    DataType: DrellYan
    CalcMode: CTEQ_DY
    Collider:
    subType: e605
    ApplGrid:
    ApplRange:
    FastNLO:
    KFactor: [2]
    Systematic:
    Normalization:
  e866f: #203
    Path: e866f_up2025
    DataType: DrellYan
    CalcMode: CTEQ_DY
    Collider:
    subType: e866f_up2025
    ApplGrid:
    ApplRange:
    FastNLO:
    KFactor: []
    Systematic:
    Normalization:
  e866ppxf: #204
    Path: e866ppxf_up2025
    DataType: DrellYan
    CalcMode: CTEQ_DY
    Collider:
    subType: e866ppxf
    ApplGrid:
    ApplRange:
    FastNLO:
    KFactor: [2]
    Systematic:
    Normalization:
  e906aF: #206
    Path: e906aF_up2025
    DataType: DrellYan
    CalcMode: CTEQ_DY
    Collider:
    subType: e906aF_up2025
    ApplGrid:
    ApplRange:
    FastNLO:
    KFactor: []
    Systematic:
    Normalization:
  cdfLasy: #225
    Path: cdfLasy_up2025
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: Tev
    subType: cdfLasy
    ApplGrid:
      - 225_mcfm_grid_Wp_CDF1Wp_etal_2020.0819.root
      - 225_mcfm_grid_Wm_CDF1Wm_etal_2020.0819.root
    ApplRange:
    FastNLO:
    KFactor:
    Systematic:
    Normalization:
  cdfLasy2: #227
    Path: cdfLasy2_up2025
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: Tev
    subType: cdfLasy2
    ApplGrid:
      - 227_mcfm_grid_Wp_CDF1Wp_etal_2020.0819.root
      - 227_mcfm_grid_Wm_CDF1Wm_etal_2020.0819.root
    ApplRange:
    FastNLO:
    KFactor:
    Systematic:
    Normalization:
  d02Masy1: #234
    Path: d02Masy1_up2025
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: Tev
    subType: d02Masy1
    ApplGrid:
      - 234_mcfm_grid_Wp_D02Wp_etal_2020.0819.root
      - 234_mcfm_grid_Wm_D02Wm_etal_2020.0819.root
    ApplRange:
    FastNLO:
    KFactor:
    Systematic:
    Normalization:
  ZyD02a: #260
    Path: ZyD02a_up2025
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: Tev
    subType: ZyD02a_up
    ApplGrid:
      - 260_grid-40-6-15-3-Z0_zyd0_2020.0819.root
    ApplRange:
    FastNLO:
    KFactor: [3, 5]
    Systematic:
    Normalization:
  ZyCDF2: #261
    Path: ZyCDF2_up2025
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: Tev
    subType: ZyCDF2_up
    ApplGrid:
      - 261_grid-40-6-15-3-ZyCDF2_Yao.root
    ApplRange:
    FastNLO:
    KFactor: [3, 4]
    Systematic:
    Normalization:
  CMS7Masy2: #266
    Path: CMS7Masy2_up2025
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: LHC
    subType: CMS7Masy2
    ApplGrid:
      - 266_mcfm_grid_Wp_CMS7Wp_etal_2020.0819.root
      - 266_mcfm_grid_Wm_CMS7Wm_etal_2020.0819.root
    ApplRange:
    FastNLO:
    KFactor:
    Systematic:
    Normalization:
  CMS7Easy: #267
    Path: CMS7Easy_up2025
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: LHC
    subType: CMS7Easy
    ApplGrid:
      - 267_CMS-PAS-SMP-12-001-Wplus_eta4_2020.0819.root
      - 267_CMS-PAS-SMP-12-001-Wminus_eta3_2020.0819.root
    ApplRange:
    FastNLO:
    KFactor:
    Systematic:
    Normalization:
  d02Easy5: #281
    Path: d02Easy5_up2025
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: Tev
    subType: d02Easy5
    ApplGrid:
      - 281_grid-40-6-15-3-Wplus_wly_pt25_el_2020.0819.root
      - 281_grid-40-6-15-3-Wminus_wly_pt25_el_2020.0819.root
    ApplRange:
    FastNLO:
    KFactor:
    Systematic:
    Normalization:
  ATL8W_new3: #211
    Path: ATL8W_new3_Yao
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: LHC
    subType: CommonDY
    ApplGrid:
      - ATL8Wp_mcfm_grid_Wp_etal.root
      - ATL8Wm_mcfm_grid_Wm_etal.root
    ApplRange:
    FastNLO:
    KFactor: [1, 2]
    Systematic:
    Normalization:
  CMS13Zmu_new2: #212
    Path: CMS13Zmu_new2_Yao
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: LHC
    subType: CommonDY
    ApplGrid:
      - CMS13Z_mcfm_grid_Zonly_yll.root
    ApplRange:
    FastNLO:
    KFactor: [1, 2]
    Systematic:
    Normalization:
  LHCb13Zy2_Decom.data: #218
    Path: LHCb13Zy2_Decom.data_up2025_Yao
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: LHC
    subType: CommonDY
    ApplGrid:
      - LHCb13Z_mcfm_grid_Zonly_yll.root
    ApplRange:
      - [1, 2, 17]
    FastNLO:
    KFactor: [1, 2]
    Systematic:
    Normalization:
  ATL8Z3d: #214
    Path: ATL8Z3d_Yao
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: LHC
    subType: ATL8Z3d
    ApplGrid:
      - 66_80.root
      - 80_91.root
      - 91_102.root
      - 102_116.root
      - 116_150.root
      - 150_200.root
    ApplRange:
    FastNLO:
    KFactor: [1, 2]
    Systematic:
    Normalization:
  ATL5WZunc.data: #215
    Path: ATL5WZunc.data_up2025_Yao
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: LHC
    subType: CommonDY
    ApplGrid:
      - ATL5Wp_mcfm_grid_Wp_etal.root
      - ATL5Wm_mcfm_grid_Wm_etal.root
      - ATL5Z_mcfm_grid_Zonly_yll.root
    ApplRange:
    FastNLO:
    KFactor: [1, 2]
    Systematic:
    Normalization:
  LHCb8W_Lastm2.data: #217
    Path: LHCb8W_Lastm2.data_up2025_Yao
    DataType: DrellYan
    CalcMode: ApplGrid
    Collider: LHC
    subType: CommonDY
    ApplGrid:
      - LHCb8Wp_mcfm_grid_Wp_etal.root
      - LHCb8Wm_mcfm_grid_Wm_etal.root
    ApplRange:
      - [1, 1, 7]
      - [2, 1, 7]
    FastNLO:
    KFactor: [1, 2]
    Systematic:
    Normalization:
  ATL13ytt_HTO2: #521
    Path: ATL13ytt_HTO2
    DataType: Jet
    CalcMode: PineAPPL
    Collider: LHC
    subType: CommonJet
    ApplGrid:
    ApplRange:
    FastNLO:
    PineAPPL:
      - [ATLAS_TTBAR_13TEV_HADR_DIF_YTTBAR.pineappl.lz4]
    KFactor: # [2, 3] for APPLgrid, kfactors should be applied, check if PineAPPL needs the same kfactors
    Systematic:
    Normalization:
  CMS13ytt_HTO2: #528
    Path: CMS13ytt_HTO2
    DataType: Jet
    CalcMode: PineAPPL
    Collider: LHC
    subType: CommonJet
    ApplGrid:
    ApplRange:
    FastNLO:
    PineAPPL:
      - [CMS_TTBAR_13TEV_2L_DIF_YTTBAR.pineappl.lz4]
    KFactor: # [2, 3] for APPLgrid, kfactors should be applied, check if PineAPPL needs the same kfactors
    Systematic:
    Normalization:
  ATL13LepJ_MttYttYBHTtt_HTO2: #587
    Path: ATL13LepJ_MttYttYBHTtt
    DataType: Jet
    CalcMode: PineAPPL
    Collider: LHC
    subType: CommonJet
    ApplGrid:
    ApplRange:
    FastNLO:
    PineAPPL:
      - [ATLAS_TTBAR_13TEV_LJ_DIF_MTTBAR.pineappl.lz4]
      - [ATLAS_TTBAR_13TEV_LJ_DIF_YTTBAR.pineappl.lz4]
      - [ATLAS_TTBAR_13TEV_LJ_DIF_YBTTB.pineappl.lz4]
      - [ATLAS_TTBAR_13TEV_LJ_DIF_HTTTB.pineappl.lz4]
    KFactor: # [2, 3] for APPLgrid, kfactors should be applied, check if PineAPPL needs the same kfactors
    Systematic:
    Normalization:
  CMS13lj21mtt_HTO2: #581
    Path: CMS13lj21mtt_HTO2
    DataType: Jet
    CalcMode: PineAPPL
    Collider: LHC
    subType: CMS13lj21mtt_HTO2
    ApplGrid:
    ApplRange:
    FastNLO:
    PineAPPL:
      - [CMS_TTBAR_13TEV_LJ_DIF_MTTBAR.pineappl.lz4]
    KFactor: # [2, 3] for APPLgrid, kfactors should be applied, check if PineAPPL needs the same kfactors
    Systematic:
    Normalization:
  ATL8_Inc_pTjDecor: #553
    Path: ATL8_Inc_pTjDecor
    DataType: Jet
    CalcMode: ApplGrid
    Collider: LHC
    subType: CommonJet1000NNLO
    ApplGrid:
      - atlas-incjets-appl-arxiv-1706.03192-xsec006.root
      - atlas-incjets-appl-arxiv-1706.03192-xsec007.root
      - atlas-incjets-appl-arxiv-1706.03192-xsec008.root
      - atlas-incjets-appl-arxiv-1706.03192-xsec009.root
      - atlas-incjets-appl-arxiv-1706.03192-xsec010.root
      - atlas-incjets-appl-arxiv-1706.03192-xsec011.root
    ApplRange:
    FastNLO:
    KFactor: [2, 3]
    Systematic:
      - [0, 0, 0]
      - [1, 336, 1]
    Normalization:
  ATL13_Inc_pTjDecor: #554
    Path: ATL13_Inc_pTjDecor
    DataType: Jet
    CalcMode: ApplGrid
    Collider: LHC
    subType: CommonJet1000NNLO
    ApplGrid:
      - atlas-incjets-appl-arxiv-1711.02692-xsec006.root
      - atlas-incjets-appl-arxiv-1711.02692-xsec007.root
      - atlas-incjets-appl-arxiv-1711.02692-xsec008.root
      - atlas-incjets-appl-arxiv-1711.02692-xsec009.root
      - atlas-incjets-appl-arxiv-1711.02692-xsec010.root
      - atlas-incjets-appl-arxiv-1711.02692-xsec011.root
    ApplRange:
    FastNLO:
    KFactor: [2, 3]
    Systematic:
      - [0, 0, 0]
      - [1, 342, 1]
    Normalization:
  CMS13IncJpTj_v1: #555
    Path: CMS13IncJpTj_v1
    DataType: Jet
    CalcMode: ApplGrid
    Collider: LHC
    subType: CommonJet1000NNLO
    ApplGrid:
      - cms-incjets-appl-arxiv-2111.10431-xsec012.root
      - cms-incjets-appl-arxiv-2111.10431-xsec013.root
      - cms-incjets-appl-arxiv-2111.10431-xsec014.root
      - cms-incjets-appl-arxiv-2111.10431-xsec015.root
    ApplRange:
      - [3, 1, 19]
      - [4, 1, 16]
    FastNLO:
    KFactor: [2, 3]
    Systematic:
      - [0, 0, 0]
      - [1, 31, 1]
    Normalization:
    CorrMatrix:
      - StatCorrMatrices/CMS13IncJetStatCor
  CMS7jtR7y6_v1: #556
    Path: CMS7jtR7y6_v1
    DataType: Jet
    CalcMode: FastNLO
    Collider: LHC
    subType: CMS7jtR7y6_v1
    ApplGrid:
    ApplRange:
    FastNLO:
      - fnl2332e_v23_fix_I1298810.tab
    KFactor: [6]
    Systematic:
      - [0, 0, 0]
      - [1, 26, 1]
    Normalization:
    CorrMatrix:
      - StatCorrMatrices/CMS7IncJetStatCor
  CMS8jtR7_v1: #557
    Path: CMS8jtR7_v1
    DataType: Jet
    CalcMode: FastNLO
    Collider: LHC
    subType: CMS8jtR7_v1
    ApplGrid:
    ApplRange:
    FastNLO:
      - fnl3332_I1487277.tab
    KFactor: [3]
    Systematic:
      - [0, 0, 0]
      - [1, 31, 1]
    Normalization:
    CorrMatrix:
      - StatCorrMatrices/CMS8IncJetStatCor"""

parameters_template = """Parameter:
  - parameter: [ 1,  A1glu,   0.53101,  0.05,   0.0,   1.0]
  - parameter: [ 2,  A2glu,   3.14810,  0.05,   0.0,   5.0]
  - parameter: [ 3,  A3glu,   3.03140,  0.05,   0.0,   5.0]
  - parameter: [ 4,  A4glu,  -1.70494,  0.05,  -2.0,   0.0]
  - parameter: [10,  gluM,        0.0,  0.01,  -0.5,   0.5]
  - parameter: [11,  A1uvl,   0.76317,  0.05,   0.0,   1.0]
  - parameter: [12,  A2uvl,   3.03609,  0.05,   0.0,   5.0]
  - parameter: [13,  A3uvl,   1.50192,  0.05,   0.0,   5.0]
  - parameter: [14,  A4uvl,  -0.14666,  0.05,  -1.0,   0.0]
  - parameter: [15,  A5uvl,   1.67108,  0.05,   0.0,   5.0]
  - parameter: [23,  A3dvl,   2.61407,  0.05,   0.0,   5.0]
  - parameter: [24,  A4dvl,   1.82746,  0.05,   0.0,   5.0]
  - parameter: [25,  A5dvl,   2.72032,  0.05,   0.0,   5.0]
  - parameter: [26,  A6dvl,   2.72032,  0.05,   0.0,   5.0]
  - parameter: [41,  A1dou,   0.61791,  0.05,   0.0,   1.0]
  - parameter: [42,  A2dou,   0.19493,  0.05,   0.0,   1.0]
  - parameter: [43,  A3dou,   0.87087,  0.05,   0.0,   1.0]
  - parameter: [44,  A4dou,   0.26669,  0.05,   0.0,   1.0]
  - parameter: [45,  A5dou,   0.73317,  0.05,   0.0,   1.0]
  - parameter: [51,  A1dpu,  -0.02194,  0.05,  -1.0,   0.0]
  - parameter: [52,  A2dpu,   7.73657,  0.05,   5.0,  10.0]
  - parameter: [53,  A3dpu,   7.73657,  0.05,   5.0,  10.0]
  - parameter: [54,  A4dpu,   0.29223,  0.05,   0.0,   1.0]
  - parameter: [55,  A5dpu,   0.64695,  0.05,   0.0,   1.0]
  - parameter: [56,  A6dpu,   0.47492,  0.05,   0.0,   1.0]
  - parameter: [57,  A7dpu,   0.74137,  0.05,   0.0,   1.0]
  - parameter: [60,  strM,        0.0,  0.05,  -0.5,   0.5]
  - parameter: [62,  A2str,  10.30986,  0.05,   7.0,  12.0]
  - parameter: [63,  A3str,  10.30986,  0.05,   7.0,  12.0]
  - parameter: [64,  A4str,   0.46599,  0.05,   0.0,   1.0]
  - parameter: [65,  A5str,   0.22525,  0.05,   0.0,   1.0]
  - parameter: [66,  A6str,  10.30986,  0.05,   7.0,  12.0]
  - parameter: [67,  A7str,  10.30986,  0.05,   7.0,  12.0]
  - parameter: [71,  N71,      0.9876,  0.05,   0.9,   1.1]
PDFParameterization: # IFun = 1(CT18), 2(CT18As)
  IFun: 1
ShapeMatch:
  - parameter: [dv,    310, [ 11, 12, 23, 24, 25, 26,  0,  0,  0,  0,  0,  0,  0,  0,  0]]
  - parameter: [uv,    705, [ 11, 12, 13, 14, 15,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]
  - parameter: [gluon, 406, [  1,  2,  3,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]
  - parameter: [dmu,   205, [ 51, 52, 53, 54, 55, 56, 57, 41, 42, 43, 44, 45,  0,  0,  0]]
  - parameter: [dpu,   204, [ 51, 52, 53, 54, 55, 56, 57, 41, 42, 43, 44, 45,  0,  0,  0]]
  - parameter: [str,  3319, [ 51, 62, 63, 64, 65, 66, 67,  0,  0,  0,  0,  0,  0,  0,  0]]
CentralValue:
             # flavor  momentum        B0        shape parameters
  - parameter: [dv,    0.1391770,  0.0000000,  [ 0.75757,   3.60004,   2.54686,   1.65865,   1.89857,  -0.76193,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.97000,   0.00000]]
  - parameter: [uv,    0.3334066,  0.0000000,  [ 0.75757,   3.60004,  -0.55434,  -1.14161,  -0.57956,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.97000,   0.00000]]
  - parameter: [gluon, 0.3596852,  0.0000000,  [ 1.96973,   2.34865,   5.25003,  -2.14729,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000]]
  - parameter: [dmu,   0.0000000,  0.0000000,  [-0.01387,   9.70880,   8.84105,   0.96692,  -0.22663,   1.01288,  -0.13518,  -0.44589,  -0.05599,   0.73140,   0.04178,  -1.24042,   0.00000,   0.80000,   0.00000]]
  - parameter: [dpu,   0.1300072,  0.0000000,  [-0.01387,   9.70880,   8.84105,   0.96692,  -0.22663,   1.01288,  -0.13518,  -0.44589,  -0.05599,   0.73140,   0.04178,  -1.24042,   0.00000,   0.80000,   0.00000]]
  - parameter: [str,   0.0377240,  0.6747229,  [-0.01387,   7.81588,   0.57651,  -0.87419,   2.09825,  -2.01794,   3.30087,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000,   0.00000]]
OtherParameters:
  - parameter: [10, gluM, GluonMomentum]
  - parameter: [60, strM, StrangeB0]
  - parameter: [71,  N71, Normalization, [BcdF2pCor, BcdF2dCor]]
#  - parameter: [31, alphas, AlphaS]"""

job_scripts_template = """#!/bin/bash --login
#SBATCH --job-name={job_name}   # job name
#SBATCH --nodes=1               # total number of nodes
#SBATCH --ntasks-per-node=1     # total number of tasks requested
#SBATCH --cpus-per-task=30       # total number of tasks requested
#SBATCH --threads-per-core=1    # one core each thread
#SBATCH --mem=60G            # job memory limit
#SBATCH --time=30:00:00             # run time (hh:mm:ss) - 3:00:00 hours
#SBATCH --output=%x-%j.out      # queue (partition) 
source ~/setup.sh
source ~/dragonwell/venv/bin/activate
cd {fit_dir}
PDFFit_Minuit2"""


top_mass_list = [
    (170.0, "fill_dir", "170"),
    (171.25, "fill_dir", "171p25"),
    (172.5, "fill_dir", "172p5"),
    (173.75, "fill_dir", "173p75"),
    (175.0, "fill_dir", "175"),
]

alpha_s_list = [0.116, 0.117, 0.118, 0.119, 0.120]

gluon_params = []

path = "/mnt/home/shar1157/ct_top_fits/"
job_path = "/mnt/home/shar1157/ct_top_fits/jobs/"

for top_mass in top_mass_list:
    for alpha_s in alpha_s_list:

        fit_dir = f"{path}fit_mt{top_mass[2]}_as{str(alpha_s).replace('0.', '')}_para_defCT"

        os.mkdir(f"{fit_dir}")

        config = config_template.format(top_mass=top_mass[0], alpha_s=alpha_s)
        with open(f"{fit_dir}/Config.yml", "w") as f:
            f.write(config)

        datalist = datalist_template.format(top_dir=top_mass[1])
        with open(f"{fit_dir}/DataList.yml", "w") as f:
            f.write(datalist)

        parameters = parameters_template
        with open(f"{fit_dir}/Parameters.yml", "w") as f:
            f.write(parameters)

        job_script = job_scripts_template.format(job_name=f"fit_{top_mass[2]}_{str(alpha_s).replace('0.', '')}_defCT", fit_dir=fit_dir)
        with open(f"{job_path}fit_{top_mass[2]}_{str(alpha_s).replace('0.', '')}_defCT.sh", "w") as f:
            f.write(job_script)



