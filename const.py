import pandas as pd

bad_stocks = ['AFIL01', 'ECJM', 'SUNY', 'UNON', 'MCPL', 'EXEN', 'MABR', 'MDGS', 'MEDI', 'APOS', 'ASPR', 'BGI', 'ANCN',
              'SPIR',
              'GBPR', 'VTLC-M', 'LDER', 'MAXM', 'MRP', 'PNTR', 'TALD', 'NNDM', 'RDHL', 'ADO', 'SMOG', 'JTI', 'HAIN',
              'BLLCF',
              'ALD_t3', 'ALMD_t7', 'ANSL_t7', 'APOP_t1', 'AURA_t5', 'AVRT_t5', 'BCNV_t1', 'BIG_t4', 'BRAN_t4',
              'CLPT_t11', 'CLPT_t12', 'CLPT_t7', 'CLPT_t8', 'CLPT_t9', 'CNFI_t10', 'DISI_t5', 'DISI_t6', 'ECJM_t9',
              'ENDY_t5',
              'ENRG_t2', 'FNTS_t1', 'ILDA_t6', 'INM_t2', 'ISCN_t4', 'ITMR_t4', 'KDST_t2', 'KDST_t3', 'MBMX_t5',
              'MCTC_t20',
              'MDGS_t9', 'MDNp_t15', 'MDVI_t2', 'MGOR_t2', 'MNPR_t1', 'MNPR_t2', 'MYDS_t4', 'OPAL_t2', 'RTIp_t14',
              'RTIp_t17',
              'RTIp_t18', 'RTPTp_t1', 'RTPTp_t2', 'SAFE_t2', 'SKLN_t2', 'SLARL_t3', 'SLGN_t5', 'SPRG_t1', 'SPRG_t2',
              'STCM_t1',
              'TGTR_t3', 'TMD_t1', 'VCTR_t1', 'XENA_t4', 'XENA_t5', 'YBOX_t1', 'ZRAH_t8', 'MNPR', 'ARCS', 'ELDT_p3',
              'CHR_t5',
              'INCR_t3', 'MLD_t1', 'MLD_t2', 'OPAL_t3', 'ORBTC6', 'RIT1_tb7', 'MCC', 'IFF', 'INRI', 'ISOP_t6',
              'ISOP_t7',
              'ISOP_t8', 'ALMO', 'FNTS', 'BVC', 'ISRAp', 'CHR', 'PHOE1', 'FCRE', 'RTENp', 'MDINp', 'OPCT', 'HAML',
              'ORMP', 'EMIT', 'LPHLp', 'TFR', 'SCOP1', 'ARKO', 'TATTF', 'FATTAL', 'ELLO', 'APIO', 'ASPF', 'TDGN',
              'PTXp', 'RATIp', 'XTL', 'KRNV', 'TGBR', 'RTPTp', 'PLTF', 'CTPL', 'DIFI', 'DEDRp', 'GLEXp',
              'ZLKL1', 'GFC', 'MBMX', 'KTOV', 'GIVOp', 'GLRS', 'VNTZ', 'ELWS_t2', 'DLMT', 'KMNK', 'GODM',
              'ISOP', 'ARYT1', 'NERZ', 'RANI_t1', 'BIMC', 'SEFA', 'MRIN_t1', 'APLY', 'BBYL', 'LUZN_t4', 'GIBU',
              'IGLD', 'SHOM_t1', 'MCTC', 'CNBT', 'NVPTp', 'IBLD', 'PLAZ', 'MSLA', 'SLGN', 'HNMR', 'BYAR',
              'XENA', 'SHNP', 'AFID']

risk_free = pd.read_csv('..\\Data\\risk_free_return.csv')
risk_free.Date = pd.to_datetime(risk_free.Date)
RISK_FREE = risk_free.set_index('Date')[['return']] / 100
