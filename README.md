# FastAPI Backend – Practice 2026

This repository contains a FastAPI-based backend application designed for
containerization and CI-driven Docker image builds.

The primary responsibility of this repository is:
- Maintain backend application code
- Build immutable Docker images
- Push images to a container registry (ECR) via CI pipeline

---

## Repository Responsibility

- Owns FastAPI application code
- Owns Dockerfile and dependency definitions
- Produces versioned Docker images
- Does NOT contain Kubernetes manifests

Deployment configuration is intentionally kept in a separate GitOps repository.

---

## High-Level Flow

1. Application or Dockerfile changes are committed
2. CI pipeline builds a new Docker image
3. Image is pushed to the container registry
4. Image SHA is later consumed by the Kubernetes GitOps repo

---

## Folder Structure Overview

- `app/` – FastAPI application source
- `Dockerfile` – Container image definition
- `requirements.txt` – Python dependencies
- `.github/workflows/` – CI pipeline configuration

---

## Notes

- This repository follows real-world separation of concerns
- Designed for repeated practice of Docker and CI workflows
- Kubernetes and deployment logic are managed externally
