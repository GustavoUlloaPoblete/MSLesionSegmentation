# MSLesionSegmentation
https://github.com/GustavoUlloaPoblete/MSLesionSegmentation

Title of the paper (submitted for peer review):

**"MRI Boundary-Aware Segmentation of Multiple Sclerosis Lesion Using a Novel Mahalanobis Distance Map"**

Authors:

- Gustavo Ulloa-Poblete, Departamento de Informática, Universidad Técnica Federico Santa María, Valparaíso 2390123, Chile; gustavo.ulloa@usm.cl
- Alejandro Veloz: School of Biomedical Engineering, Universidad de Valparaíso, Chile; alejandro.veloz@uv.cl
- Sebastián Sánchez; Departamento de Informática, Universidad Técnica Federico Santa María, Valparaíso 2390123, Chile; sebastian.sanchezl@sansano.usm.cl
- Héctor Allende, Departamento de Informática, Universidad Técnica Federico Santa María, Valparaíso 2390123, Chile; hallende@inf.utfsm.cl


**Brief explanation of the paper submitted for peer review (different from the abstract):**

In this work, we address the challenging task of accurately segmenting multiple sclerosis (MS) lesions in MRIs. We propose a new Mahalanobis distance loss function for Convolutional neural networks (CNN). Unlike traditional loss functions, this loss function also incorporates texture information from the neighborhood of boundary pixels. To achieve this, we introduce the Mahalanobis distance map (MDM). Unlike traditional DTM and SDF maps used in current loss functions, the MDM also considers radiomic texture features. This allows to CNN, especifically U-Net to better identify those tricky, ambiguous lesion boundaries, mimicking how a human expert would think. The results are highly promising, showing our method outperforms existing approaches in both overall accuracy and boundary quality.

### Dependencies

This project requires the following libraries:
* `numpy`
* `torch`
* `scipy`
* `sklearn`
* `skimage`
* `SimpleITK`
* `os`, `sys`, `time`

### Use and reproduction

Use the main.py script, where you configure the training parameters such as:
- epochs
- MDM $\lambda$
- servers to be used
- dataset
- loss function
- radiomic characteristics

Preprocessed training data sets are required, and for efficiency, it is desirable (but not mandatory) to have the Mahalanobis distance maps already saved on the hard drive.

#### Data Sets used (last accessed on 26 August 2025)
- ISBI-MS: Publicly available at https://www.kaggle.com/datasets/marwa96/isbi-ms-dataset/data;
- MSSEG: Publicly available at https://portal.fli-iam.irisa.fr/msseg-challenge/

#### Mini tutorial to generate a Mahalanobis distance map
To learn how to generate a Mahalanobis distance map using a simulated toy image, open the following file in Jupyter Notebook or JupyterLab:

src/tutorial.ipyb

