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
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p3.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'

# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p0.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p1.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p1.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p2.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p2.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p3.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'

# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p0.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p1.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p1.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p2.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p2.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p3.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d15u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'

# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p0.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p1.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p1.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p2.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p2.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
# nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p3.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'

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

nombre_carpeta_principal = 'ISBI2015_Unet_MD_loss_C_w1.0p3.0-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d5u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'

nombre_carpeta_principal = 'MSSEG2016_Unet_MD_loss_C_w1.0p1.5-A5GL11_r5a1pmGL0.3g1.0p0.9_FLAIR_d10u0-bmT_e200_b16_Adam_da0.0_mpT_es40-30_ut1'
print(nombre_carpeta_principal)
print('-'*70)

carpetas_scp = Get_carpetas_scp()[:]
print(f'#carpetas_scp={len(carpetas_scp)}')
# =============================================================================
# Seleccionar carpetas scp que no estén vacias
# =============================================================================
# lista=list()
def Get_carpetas_scp_B():
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

carpetas_scp = Get_carpetas_scp_B()
print(f'#carpetas_scp={len(carpetas_scp)}')




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
            d_metricas[llave].append(list(map(float,valor.split(','))))
    archivo.close()
for llave in d_metricas:
    d_metricas[llave]=np.array(d_metricas[llave],dtype=np.float32)
d_metricas_N = dict(d_metricas) # copia de diccionario de métricas sin umbralizar.
# =============================================================================
# 
# =============================================================================
d_metricas['dice_val_test'] = (d_metricas['dice_val']*N_val + d_metricas['dice_test']*N_test)/N
d_metricas['loss_val_test'] = (d_metricas['loss_val']*N_val + d_metricas['loss_test']*N_test)/N
d_metricas['HD'] = (d_metricas['HD_val']*N_val + d_metricas['HD_test']*N_test)/N
d_metricas['HD95'] = (d_metricas['HD95_val']*N_val + d_metricas['HD95_test']*N_test)/N
d_metricas['HD90'] = (d_metricas['HD90_val']*N_val + d_metricas['HD90_test']*N_test)/N
d_metricas['ASSD'] = (d_metricas['ASSD_val']*N_val + d_metricas['ASSD_test']*N_test)/N
d_metricas['ASSD95'] = (d_metricas['ASSD95_val']*N_val + d_metricas['ASSD95_test']*N_test)/N
d_metricas['RVD'] = (d_metricas['RVD_val']*N_val + d_metricas['RVD_test']*N_test)/N
d_metricas['F1'] = (d_metricas['F1_val']*N_val + d_metricas['F1_test']*N_test)/N
d_metricas['TPR'] = (d_metricas['TPR_val']*N_val + d_metricas['TPR_test']*N_test)/N
d_metricas['PPV'] = (d_metricas['PPV_val']*N_val + d_metricas['PPV_test']*N_test)/N
d_metricas['AUC_ROC'] = (d_metricas['AUC_ROC_val']*N_val + d_metricas['AUC_ROC_test']*N_test)/N
d_metricas['AUC_PR'] = (d_metricas['AUC_PR_val']*N_val + d_metricas['AUC_PR_test']*N_test)/N
d_metricas['F2'] = (d_metricas['F2_val']*N_val + d_metricas['F2_test']*N_test)/N
for llave in d_metricas:
    d_metricas[llave]={'mean':np.mean(d_metricas[llave],0), 'std':np.std(d_metricas[llave],0)}
# d_sinthr = dict(d_metricas) # copia de diccionario de métricas sin umbralizar.

fig, ax = plt.subplots(1, 1, figsize = (15,5))
xticks = np.arange(0, 200, 5)
yticks = np.arange(0, 1, 0.025)
ax.plot(d_metricas['dice_train']['mean']);plt.axis([0,200,0,1])
ax.plot(d_metricas['dice_val_test']['mean']);plt.axis([0,200,0,1])
ax.plot(d_metricas['dice_val']['mean']);plt.axis([0,200,0,1])
ax.plot(d_metricas['dice_test']['mean']);plt.axis([0,200,0,1])
ax.plot(d_metricas['loss_val_test']['mean']);plt.axis([0,200,0,1])
ax.plot(d_metricas['loss_val']['mean']);plt.axis([0,200,0,1])
ax.plot(d_metricas['loss_test']['mean']);plt.axis([0,200,0,1])
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.yaxis.tick_right()
ax.grid()
ax.set_title('epocas/dice')
plt.legend(["train", 'val-test', "val", "test"], loc="upper left", fontsize=20)

# =============================================================================
# Obtener tabla de resultados umbralizados
# =============================================================================
# Metricas val-test
# =============================================================================
N = d_metricas_N['dice_val'].shape[0]
print(f'#N={N}')
print('validation-testing:')
metricas = ['HD95', 'ASSD', 'TPR', 'PPV', 'F1', 'RVD','AUC_PR']
# metricas = ['HD95', 'HD90', 'ASSD', 'TPR', 'PPV', 'F1', 'RVD','AUC_PR']

for epoca in [200]:
    s=''
    for metrica in metricas:
        media = str(round(d_metricas[metrica]['mean'][epoca-1],4)).ljust(6,'0')
        std = str(round(d_metricas[metrica]['std'][epoca-1],4)).ljust(6,'0')
        if metrica != metricas[-1]:
            s+=media+'('+std+')'+' & '
        else:
            s+=media+'('+std+')'
    print(f'{epoca} épocas:')
    m = ''
    for metrica in metricas:
        m += '    '+metrica.ljust(12,' ')+'|'
    print(m)
    print('-'*120)
    print(s)

# =============================================================================
# Utilizando early-stopping
# =============================================================================
start_es = 40
paciencia = 30

metricas = ['HD95_val', 'HD90_val', 'ASSD_val', 'TPR_val', 'PPV_val', 'F1_val', 'RVD_val','AUC_PR_val']
metricas += ['HD95_test', 'HD90_test', 'ASSD_test', 'TPR_test', 'PPV_test', 'F1_test', 'RVD_test','AUC_PR_test']
# lista_es = []
d_es = {}
N = d_metricas_N['dice_val'].shape[0]
# print(f'N dice_val:{N}')
epocas = d_metricas_N['dice_val'].shape[1]# 200
# print(f'epocas:{epocas}')
# for n in range(d_metricas_N['dice_val'].shape[0]):
for n in range(N):
    # print(d_metricas_N['dice_val'][n])
    maximo_f1_val = 0
    contador = 0
    epoca_fin = epocas
    for epoca in range(1,d_metricas_N['dice_val'].shape[1]):
        # print(epoca)
        if epoca >= start_es:
            contador += 1
            f1_val = d_metricas_N['dice_val'][n][epoca]
            # print(f'epoca:{epoca}, f1_val:{f1_val}')
            if f1_val > maximo_f1_val:
                maximo_f1_val = f1_val
                contador = 0
            if contador==paciencia:
                epoca_fin = epoca
                break
    # print(f'epoca_fin:{epoca_fin}')
    for metrica in metricas:
        if metrica not in d_es:
            d_es[metrica] = []
        d_es[metrica].append(d_metricas_N[metrica][n][epoca_fin])

for llave in d_es:
    d_es[llave]={'mean':np.mean(d_es[llave],0), 'std':np.std(d_es[llave],0)}

metricas = ['HD95_test', 'ASSD_test', 'TPR_test', 'PPV_test', 'F1_test', 'RVD_test','AUC_PR_test']
# for epoca in [epoca_fin]:
s=''
for metrica in metricas:
    media = str(round(d_es[metrica]['mean'],4)).ljust(6,'0')
    std = str(round(d_es[metrica]['std'],4)).ljust(6,'0')
    if metrica != metricas[-1]:
        s+=media+'('+std+')'+' & '
    else:
        s+=media+'('+std+')'
# print(f'{epoca} épocas:')
m = ''
for metrica in metricas:
    m += ' '+metrica.ljust(15,' ')+'|'
print('\n',m)
print('-'*120)
print(s)
