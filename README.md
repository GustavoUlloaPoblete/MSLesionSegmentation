# MSLesionSegmentation
Multiple sclerosis lesions segmentation based on CNN with Mahalanobis loss function

## Instructions

Training:
```
python Entrenar.py loss:MD_loss_C epocas:20 batch_size:16 opt:Adam DS:MSSEG2016 red:Unet gpu:0 tasa_da:0.0 \
  mixed_precision:T alpha_TL:0.3 folds:MSSEG2016_5folds metric:Dice_metric gamma:1.0 alpha_HD:2.0 ES:T \
  patience:30 start_es:40 potencia_assd:nan beta_ASL:2.0 w_SEL:0.1 p_assd:nan umbral_vol_training:1 \
  alpha_BS:0.8 beta_BS_LC:0.9 wa_ABL:1.0 batch_loss:T gamma_CBL:2.0 sc:A5GL11 canal:FLAIR r:5 ady:1 \
  ce:GL par_ce:0.3 dist:10 prototipo:prototipo_mediana gamma_MDF:1.0 percentil:0.9 umbral_cc:0 \
  parMD_weight:1.0 parMD_sq:1 umbral_P_MDF:150 parMD_pot:1.5 parMD_quantil:1.0 tarea:training \
  k:0 corrida:mineria_gpu0-1
```
