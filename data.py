bad_stocks = ['AFIL01', 'ECJM', 'SUNY', 'UNON', 'MCPL', 'EXEN', 'MABR', 'MDGS', 'MEDI', 'APOS', 'ASPR', 'BGI', 'ANCN',
              'SPIR',
              'GBPR', 'VTLC-M', 'LDER', 'MAXM', 'MRP', 'PNTR', 'TALD', 'NNDM', 'RDHL', 'ADO', 'SMOG', 'JTI', 'HAIN',
              'BLLCF',
              'ALD_t3', 'ALMD_t7', 'ANSL_t7', 'APOP_t1', 'AURA_t5', 'AVRT_t5', 'BCNV_t1', 'BIG_t4', 'BRAN_t4',
              'CLPT_t11',
              'CLPT_t12', 'CLPT_t7', 'CLPT_t8', 'CLPT_t9', 'CNFI_t10', 'DISI_t5', 'DISI_t6', 'ECJM_t9', 'ENDY_t5',
              'ENRG_t2',
              'FNTS_t1', 'ILDA_t6', 'INM_t2', 'ISCN_t4', 'ITMR_t4', 'KDST_t2', 'KDST_t3', 'MBMX_t5', 'MCTC_t20',
              'MDGS_t9',
              'MDNp_t15', 'MDVI_t2', 'MGOR_t2', 'MNPR_t1', 'MNPR_t2', 'MYDS_t4', 'OPAL_t2', 'RTIp_t14', 'RTIp_t17',
              'RTIp_t18',
              'RTPTp_t1', 'RTPTp_t2', 'SAFE_t2', 'SKLN_t2', 'SLARL_t3', 'SLGN_t5', 'SPRG_t1', 'SPRG_t2', 'STCM_t1',
              'TGTR_t3',
              'TMD_t1', 'VCTR_t1', 'XENA_t4', 'XENA_t5', 'YBOX_t1', 'ZRAH_t8', 'MNPR', 'ARCS', 'ELDT_p3', 'CHR_t5',
              'INCR_t3',
              'MLD_t1', 'MLD_t2', 'OPAL_t3', 'ORBTC6', 'RIT1_tb7', 'MCC', 'IFF', 'INRI', 'ISOP_t6', 'ISOP_t7',
              'ISOP_t8']

another_bad_stocks = ['ALMO', 'FNTS', 'BVC', 'ISRAp', 'CHR', 'PHOE1', 'FCRE', 'RTENp', 'MDINp', 'OPCT', 'HAML', 'ORMP',
                      'EMIT', 'LPHLp', 'TFR', 'SCOP1', 'ARKO', 'TATTF', 'FATTAL', 'ELLO', 'APIO', 'ASPF', 'TDGN',
                      'PTXp', 'RATIp', 'XTL', 'KRNV', 'TGBR', 'RTPTp', 'PLTF', 'CTPL', 'DIFI', 'DEDRp', 'GLEXp',
                      'ZLKL1', 'GFC', 'MBMX', 'KTOV', 'GIVOp', 'GLRS', 'VNTZ', 'ELWS_t2', 'DLMT', 'KMNK', 'GODM',
                      'ISOP', 'ARYT1', 'NERZ', 'RANI_t1', 'BIMC', 'SEFA', 'MRIN_t1', 'APLY', 'BBYL', 'LUZN_t4', 'GIBU',
                      'IGLD', 'SHOM_t1', 'MCTC', 'CNBT', 'NVPTp', 'IBLD', 'PLAZ']

good_stocks = """NVMI.TA      901
PRGO.TA      902
MEDN.TA      902
CAST.TA      903
WTS.TA       903
ICL.TA       903
CLIS.TA      903
FIBI.TA      903
MGDL.TA      903
PTNR.TA      903
PIU.TA       903
ORTC.TA      903
FORTY.TA     903
PLSN.TA      903
FOX.TA       903
NTO.TA       903
NSTR.TA      903
QLTU.TA      903
DLEKG.TA     903
AZRM.TA      903
ALRPR.TA     903
ALBA.TA      904
TDRN.TA      906
BIRM.TA      907
CFX.TA       907
SRAC.TA      907
GAGR.TA      908
INFR.TA      908
AVER.TA      908
BEZQ.TA      908
HAMAT.TA     908
ININ.TA      908
DANE.TA      908
RIMO.TA      908
LEOF.TA      908
KNFM.TA      908
ISTA.TA      908
EQTL.TA      908
ALHE.TA      908
DISI.TA      908
MMHD.TA      908
ELCO.TA      908
HAP.TA       908
ELTR.TA      908
INTL.TA      908
UNCR.TA      908
WLFD.TA      908
LAPD.TA      908
LBTL.TA      908
DLEA.TA      908
FIBIH.TA     908
TOPS.TA      908
ELWS.TA      908
LHIS.TA      908
ESLT.TA      908
SKBN.TA      908
BSEN.TA      908
MISH.TA      908
EMTC.TA      908
LEVI.TA      908
BYSD.TA      908
NFTA.TA      908
AUDC.TA      908
MGIC.TA      908
SNEL.TA      908
HRON.TA      908
PTCH.TA      908
ANGL.TA      908
ARAN.TA      908
VILR.TA      908
TNPV.TA      908
POLI.TA      908
TEVA.TA      908
NICE.TA      908
VISN.TA      908
BRAN.TA      908
FBRT.TA      908
TSEM.TA      908
LUZN.TA      908
TGTR.TA      908
AVLN.TA      908
DELT.TA      908
SNCM.TA      908
INTR.TA      908
JBNK.TA      908
AVIV.TA      908
REKA.TA      908
PTBL.TA      908
MYDS.TA      908
ELRN.TA      908
DSCT.TA      908
HARL.TA      908
SANO1.TA     908
CMDR.TA      918
AVRT.TA      930
TREN.TA      931
RLCO.TA      935
ISCN.TA      936
ENLT.TA      936
MNRV.TA      936
TAYA.TA      939
ORBI.TA      940
SHOM.TA      944
EXPO.TA      945
TUZA.TA      946
ANLT.TA      946
HOD.TA       946
YBOX.TA      946
PRTC.TA      946
MTRX.TA      946
RSEL.TA      946
CMER.TA      946
AURA.TA      946
LUDN.TA      946
GSFI.TA      946
KAFR.TA      951
ROBO.TA      959
PLCR.TA     1019
TEDE.TA     1033
KLIL.TA     1040
IBI.TA      1040
PAYT.TA     1040
ONE.TA      1040
AICS.TA     1040
BRIL.TA     1040
EMCO.TA     1040
ASGR.TA     1040
MLTM.TA     1040
RPAC.TA     1040
CDEV.TA     1040
NAWI.TA     1040
AMAN.TA     1040
GZT.TA      1040
PLRM.TA     1040
AYAL.TA     1040
NISA.TA     1040
ASHO.TA     1040
MTDS.TA     1040
QNCO.TA     1040
SMNIN.TA    1040
SEMG.TA     1040
TLSY.TA     1040
IES.TA      1040
WSMK.TA     1040
KRUR.TA     1040
ELDAV.TA    1040
ZUR.TA      1040
EMDV.TA     1040
AFID.TA     1040
PEN.TA      1040
FRSX.TA     1040
"""
