#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 11:15:41 2024

@author: gustavo
"""

import numpy as np, os
import matplotlib.pyplot as plt
import Biblioteca_General as bbg

def Get_carpetas_scp():
    # print(os.listdir(os.getcwd()+'/Experimentos/'+nombre_carpeta_principal))
    carpetas_scp = list()
    for carpeta in os.listdir(os.getcwd()+'/Experimentos/'+nombre_carpeta_principal):
        # if 'scp' == carpeta[:3]:# and '-1' not in carpeta:
        if 'scp' == carpeta[:3] and 'vast' not in carpeta:
            carpetas_scp.append(carpeta)
    return carpetas_scp


# nombre_carpeta_principal = 'MSSEG2016_Unet_Dice_loss_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_GDL_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_CBL_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_BSL_LC_0.8_0.9_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_Boundary_loss_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_HD_loss_2.0_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_ABL_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'

# nombre_carpeta_principal = 'ISBI2015_Unet_GDL_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_Boundary_loss_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_HD_loss_2.0_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_ABL_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_CBL_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'ISBI2015_Unet_BSL_LC_0.6_0.9_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'A-ISBI2015_Unet_BSL_LC_0.7_0.9_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'A-ISBI2015_Unet_BSL_LC_0.8_0.9_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'ISBI2015_Unet_BSL_LC_0.9_0.9_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'

# nombre_carpeta_principal = 'MSSEG2016_Unet_BSL_LC_0.6_0.9_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_BSL_LC_0.7_0.9_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_BSL_LC_0.8_0.9_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_BSL_LC_0.9_0.9_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'

nombre_carpeta_principal = 'WMH2017_Unet_GDL_bmT_e200_b16_Adam_da0.0_mpF_es200-200_ut1'
# nombre_carpeta_principal = 'WMH2017_Unet_CBL_bmT_e200_b16_Adam_da0.0_mpF_es200-200_ut1'
nombre_carpeta_principal = 'WMH2017_Unet_ABL_bmT_e200_b16_Adam_da0.0_mpF_es200-200_ut1'
nombre_carpeta_principal = 'WMH2017_Unet_Boundary_loss_bmT_e200_b16_Adam_da0.0_mpF_es200-200_ut1'
# nombre_carpeta_principal = 'WMH2017_Unet_HD_loss_2.0_bmT_e200_b16_Adam_da0.0_mpF_es200-200_ut1'

nombre_carpeta_principal = 'WMH2017_Unet_BSL_LC_0.6_0.9_bmT_e200_b16_Adam_da0.0_mpF_es200-200_ut1'
nombre_carpeta_principal = 'WMH2017_Unet_BSL_LC_0.7_0.9_bmT_e200_b16_Adam_da0.0_mpF_es200-200_ut1'
nombre_carpeta_principal = 'WMH2017_Unet_BSL_LC_0.8_0.9_bmT_e200_b16_Adam_da0.0_mpF_es200-200_ut1'
nombre_carpeta_principal = 'WMH2017_Unet_BSL_LC_0.9_0.9_bmT_e200_b16_Adam_da0.0_mpF_es200-200_ut1'

nombre_carpeta_principal = 'MSSEG2016_Unet_ABL_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'A-ISBI2015_Unet_ABL_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'ISBI2015_Unet_ABL_bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'

                           # 'MSSEG2016_Unet_MD_loss-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u4-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u4-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u10-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u4-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u10-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'

nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_B-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u4-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_B-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u4-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_B-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u4-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'


nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_B_w1sq1-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_B_w2sq1-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_B_w1sq2-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_B_w2sq2-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'

nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_B_w1sq1-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_B_w2sq1-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_B_w1sq2-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_B_w2sq2-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'

nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_B_w1.0p0.5sq1-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_B_w1.0p1.5sq1-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_B_w1.0p0.5sq1-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_B_w1.0p1.5sq1-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'

nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p0.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p1.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p1.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p2.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p2.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p3.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'

# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p0.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p1.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p1.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p2.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p2.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p3.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'

# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p0.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p1.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p1.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p2.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p2.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p3.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'

# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p0.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p1.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p1.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p2.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p2.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p3.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'

# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p0.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p1.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p1.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p2.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p2.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p3.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'

# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p0.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p1.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p1.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p2.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p2.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p3.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'



# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p0.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p1.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p0.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p1.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es200-200_ut1'

# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p3.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p2.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p2.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
print(nombre_carpeta_principal)
print('-'*70)

carpetas_scp = Get_carpetas_scp()[:]
print(f'#carpetas_scp={len(carpetas_scp)}')
# =============================================================================
# Seleccionar carpetas scp que no estén vacias
# =============================================================================
# lista=list()
def Get_carpetas_scp():
    # print(os.listdir(os.getcwd()+'/Experimentos/'+nombre_carpeta_principal))
    carpetas_scp = list()
    for carpeta in os.listdir(os.getcwd()+'/Experimentos/'+nombre_carpeta_principal):
        # if 'scp' == carpeta[:3]:# and '-1' not in carpeta:
        if 'scp' == carpeta[:3] and 'vast' not in carpeta:
            contenido=os.listdir(os.path.join(os.getcwd(),'Experimentos',nombre_carpeta_principal,carpeta))
            # print(f'contenido:{contenido}')
            if len(contenido)>0:
                carpetas_scp.append(carpeta)
    return carpetas_scp

carpetas_scp = Get_carpetas_scp()
print(f'#carpetas_scp={len(carpetas_scp)}')
# N=len(carpetas_scp)

if 'ISBI2015' in nombre_carpeta_principal:
    # N_val = 4; N_test = 4
    folds = getattr(bbg,'ISBI2015_5folds'+'_trainvaltest')
    pacientes_train, pacientes_val, pacientes_test = folds[0]
    N_val  = len(pacientes_val)
    N_test = len(pacientes_test)
elif 'MSSEG2016' in nombre_carpeta_principal:
    # N_val = 3; N_test = 3
    folds = getattr(bbg,'MSSEG2016_5folds'+'_trainvaltest')
    pacientes_train, pacientes_val, pacientes_test = folds[0]
    N_val  = len(pacientes_val)
    N_test = len(pacientes_test)
elif 'WMH2017' in nombre_carpeta_principal:
    # N_val = 12; N_test = 12
    training,validation,testing = getattr(bbg,'WMH2017_trainvaltest')
    N_val = len(validation)
    N_test = len(testing)
N = N_val + N_test
# print(f'#N = N_val + N_test={N}')

d_metricas = {}
for carpeta_scp in carpetas_scp[:]:
    # print(f'carpeta_scp:{carpeta_scp}')
    path_training = os.path.join(os.getcwd(),'Experimentos',nombre_carpeta_principal,carpeta_scp,'entrenamiento.txt')
    # print(f'path_training:{path_training}')
    archivo = open(path_training,'r')
    for linea in archivo:
        if ':' in linea and '_' in linea:
            llave,valor = linea.split(':')
            if llave not in d_metricas:
                d_metricas[llave] = []
            # print(f'llave:{llave}')
            d_metricas[llave].append(list(map(float,valor.split(','))))
    archivo.close()

dA = {}
dB = {}
for llave in d_metricas:
    # print(llave,len(d_metricas[llave]))
    if llave not in dA:
        dA[llave] = []
    for i in range(len(d_metricas[llave])):
        ultima_epoca = len(d_metricas[llave][i])-1
        # print(ultima_epoca, d_metricas[llave][i][ultima_epoca])
        dA[llave].append(d_metricas[llave][i][ultima_epoca])
    d_metricas[llave]={'mean':np.mean(dA[llave],0), 'std':np.std(dA[llave],0)}

# =============================================================================
# Obtener tabla de resultados umbralizados
# =============================================================================
# Metricas test
# =============================================================================
print(f'#N={len(carpetas_scp)}')
print('validation-testing:')
metricas = ['HD95_test', 'ASSD_test', 'TPR_test', 'PPV_test', 'F1_test', 'RVD_test','AUC_PR_test']
s=''
for metrica in metricas:
    # media = str(round(d_metricas[metrica]['mean'][epoca-1],4)).ljust(6,'0')
    # std = str(round(d_metricas[metrica]['std'][epoca-1],4)).ljust(6,'0')
    media = str(round(d_metricas[metrica]['mean'],4)).ljust(6,'0')
    std = str(round(d_metricas[metrica]['std'],4)).ljust(6,'0')
    if metrica != metricas[-1]:
        s+=media+'('+std+')'+' & '
    else:
        s+=media+'('+std+')'
            
# print(f'{epoca} épocas:')
m = ''
for metrica in metricas:
    m += '    '+metrica.ljust(12,' ')+'|'
print(m)
print('-'*120)
print(s)