# Living Survey: cancer

## Introduction

This document collects the scientific literature regarding **cancer**.

## AI-Driven Cancer Detection and Diagnosis

Recent advances in deep learning have significantly improved the detection and classification of various cancers across multiple imaging modalities. For breast cancer, lightweight architectures integrating CNNs with Compact Convolutional Transformers have demonstrated robust generalization with minimal parameters, achieving near-perfect accuracy while maintaining clinical trust through explainable AI integration [^2609.18212]. Similarly, interpretable few-shot learning frameworks like ProtoCAM have shown substantial improvements in classifying breast lesions in ultrasound imaging under data-scarce conditions [^2609.13340]. Terahertz imaging has also been enhanced by physics-based triple Debye dielectric modeling, which quantitatively predicts broadband tissue interactions and improves malignant tissue contrast [^2609.12701].

In the realm of neuro-oncology, NeuroTS-Net introduces a three-dimensional encoder-decoder architecture for multi-class semantic segmentation of pediatric brain tumors in multi-modal MRI, outperforming baseline methods in preserving fine boundary information and modeling broader tumor context [^2609.16873]. For prostate cancer management, a unified vision-language model has been proposed for PSMA PET/CT report generation, visual question answering, and lesion segmentation, achieving higher Dice scores than specialized segmentation models [^2609.15603]. Additionally, weakly supervised spatial grounding techniques align micro-ultrasound and histopathology features for prostate cancer grading, significantly improving macro AUC over unimodal baselines [^2609.15150]. Cervical cancer screening has also benefited from dual cross-attention frameworks that mimic expert visual reasoning for automated CIN grading and Swede score prediction [^2609.12827].

Computational pathology standards are evolving with the adoption of DICOM for sharing image-derived data, facilitating larger collaborative datasets for model development [^2609.14530]. Furthermore, machine unlearning frameworks like GRIN+ address the "privacy-efficiency-utility" trilemma in imbalanced medical datasets, ensuring robust diagnostic accuracy while complying with data erasure regulations for skin, brain, and breast cancer data [^2609.15571].

## AI for Cancer Treatment, Prognosis, and Personalized Medicine

Predicting treatment response and patient survival is critical for personalized oncology. A causal multi-modal AI model has been developed to predict personalized chemosensitivity in breast cancer, outperforming standard recurrence-score tests and potentially reducing unnecessary chemotherapy by 30% while maintaining recurrence-free rates [^2609.13567]. For tumor survival prediction, a graph-guided Mixture of Experts (MoE) framework leverages clinical data, cell slides, and genomics to manage multi-modal inputs and missing data, improving predictive accuracy over vanilla ensembles [^2609.14072].

In the context of immunotherapy, multi-omic prognostic modeling across over 10,000 checkpoint blockade treatment cases enables systematic dissection of tumor-immune ecosystems, identifying prognostic cellular programs across diverse cancer types [^10.5281_zenodo.18706180]. Additionally, autonomous robotic systems guided by conditional occupancy networks have demonstrated the first vision-guided, margin-negative tumor resections for partial nephrectomy in patient-derived phantoms, maintaining intraoperative tracking despite tissue deformation [^2609.16186].

## Computational Oncology, Genomics, and Liquid Biopsy

The integration of multi-omics and liquid biopsy techniques is revolutionizing early cancer detection and mechanistic understanding. Semi-supervised learning combined with XGBoost has enabled the construction of a multi-stage hepatocellular carcinoma (HCC) dataset using genomic biomarkers, achieving high classification accuracy [^2609.17100]. SHAP-based explainable AI further identified DNAJB14 as a key prognostic biomarker for HCC, with functional validation confirming its role in tumor migration and invasion [^2609.15638].

Pan-cancer analyses continue to yield valuable insights. A pan-cancer co-expression network has highlighted hub genes with potential for predicting drug responses [^10.5281_zenodo.2574643]. Single-cell spatially resolved atlases have mapped pan-cancer metastatic brain tumors [^10.5281_zenodo.21782885, ^10.5281_zenodo.21816284]. In renal cell carcinoma, spatial multi-omics revealed that lung metastases harbor cancer-associated fibroblast lymphocyte exclusion sites that form a confined tumor microenvironment [^10.5281_zenodo.18767278]. Urinary proteomics from breast cancer patients has also identified potential non-invasive biomarkers [^10.5281_zenodo.20393677], while comprehensive RNA-seq analysis has further characterized colorectal cancer molecular subtypes in large cohorts [^10.5281_zenodo.8307739].

Liquid biopsy approaches using cell-free DNA (cfDNA) have established comprehensive atlases of nucleosome positioning signatures across repetitive elements in tumors, enabling robust pan-cancer and tissue-specific diagnostics [^10.5526_err-00042900]. Specific applications include analyzing nucleosome repositioning in glioblastoma multiforme for early detection [^10.5526_err-00042862], and identifying DEK oncogene's tumor-promoting chromatin remodeling roles in metastatic melanoma [^10.17638_03194520].

## Nanoparticles, Theranostics, and Environmental Factors

Theranostic nanoparticles are being engineered for enhanced cancer imaging and therapy. Shape- and cation-engineered ferrite nanoparticles have shown promising hemocompatibility and heating capabilities for ovarian cancer tumor-mimicking phantoms, balancing T2 contrast with magnetic hyperthermia [^2609.14720].

Beyond molecular interventions, lifestyle and environmental factors play a significant role in oncology. Dietary polyunsaturated fatty acids have been shown to mediate the antitumor effects of fasting by inducing lipid peroxidation and ferroptosis in breast cancer models [^10.21954_ou.ro.00108036]. Furthermore, topoisomerase II catalytic inhibitors have been developed as non-genotoxic cancer therapies [^10.14288_1.0451818], while the built environment's association with cancer risk highlights the importance of spatial epidemiology [^10.14288_1.0451801].

## Drug Discovery and Molecular Targeting

Understanding molecular pathways is crucial for developing targeted therapies. Dynamic mitochondrial protein succinylation induced by omega-3 polyunsaturated fatty acids has been shown to elicit growth inhibition and lethality in prostate cancer cells by disrupting mitochondrial homeostasis [^10.17638_03195029]. Additionally, deubiquitinating enzymes (DUBs) have been identified as critical regulators of YAP/TAZ activity in mesothelioma and head and neck squamous cell carcinoma, with USP42 emerging as a promising therapeutic target to modulate Hippo signaling [^10.17638_03193849].

## Autonomous Scientific Discovery in Oncology

The application of multi-agent AI systems is accelerating hypothesis generation in cancer research. HypoEvolve utilizes a generational genetic algorithm to coordinate specialized LLM agents for drug repurposing across 34 cancer types, achieving superior selectivity scores against external biological evidence compared to single-pass generation [^2609.15938].
