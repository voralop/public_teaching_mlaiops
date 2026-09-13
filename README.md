# Lab 1 — Reproducible Training

* **Student ID**: 6688045
* **Project ID**: itcs355-6688045
* **Region**: asia-southeast1

## Model Performance & Reproducibility
expected test_roc_auc: 0.848 ± 0.010

## Engineering Trade-off Analysis
Under time pressure, I would drop controlled seeds first. Dropping controlled seeds means exact metric values will fluctuate slightly between runs due to the stochastic nature of model initialization or data shuffling. However, the model architecture, environment (digest-pinned image), and library versions (hashed dependencies) remain identical. In contrast, dropping environment or dependency pinning would be far worse. It could break the build entirely, cause runtime crashes, or lead to massive behavioral shifts due to incompatible package updates, which would completely halt production rather than just causing minor metric variance.

## Verification Checklist
- [x] Environment configured and validated (`cloud.env` & `make cloud-check`)
- [x] Hash-pinned dependencies (`requirements.txt` with `--require-hashes`)
- [x] Digest-pinned Docker base image (`Dockerfile`)
- [x] DVC remote configured and data pushed to GCS
- [x] Container image built and pushed to Artifact Registry
- [x] Training runs executed and tracked in MLflow
- [x] End-to-end reproducibility verified (`make verify`)
