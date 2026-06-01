# cicd-pipeline — End-to-End CI/CD for Flask on Kubernetes (EKS)

[![CI](https://github.com/rohioffl/cicd-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/rohioffl/cicd-pipeline/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Stack](https://img.shields.io/badge/stack-Jenkins%20%7C%20Docker%20%7C%20Ansible%20%7C%20K8s-blue)](#tech-stack)

A complete CI/CD pipeline implementation for deploying a Python Flask application to AWS Elastic Kubernetes Service (EKS), built with Jenkins scripted pipelines, Docker, Ansible, and Kubernetes.

## Table of Contents

- [What This Does](#what-this-does)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Pipeline Stages](#pipeline-stages)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Project Structure](#project-structure)

## What This Does

Automates the full software delivery lifecycle for a Flask application:
1. **Build** — Docker image build triggered on git push
2. **Test** — Automated test execution inside the container
3. **Push** — Image pushed to container registry
4. **Deploy** — Ansible deploys to Kubernetes (EKS)
5. **Verify** — Health check confirms successful rollout

## Architecture

```
Git Push
   |
   v
Jenkins Pipeline
   |-- Build Docker Image
   |-- Run Tests
   |-- Push to Registry
   |
   v
Ansible Playbook
   |
   v
AWS EKS (Kubernetes)
   |-- Deployment
   |-- Service (LoadBalancer)
   |-- Health Check
```

## Tech Stack

| Tool | Role |
|------|------|
| Jenkins | CI/CD orchestration (scripted pipeline) |
| Docker | Application containerization |
| Ansible | Configuration management + deployment |
| Kubernetes | Container orchestration |
| AWS EKS | Managed Kubernetes cluster |
| Python/Flask | Application framework |

## Pipeline Stages

```groovy
pipeline {
    stages {
        stage('Checkout')    // Pull latest code
        stage('Build')       // Docker build
        stage('Test')        // pytest inside container
        stage('Push')        // Push to registry
        stage('Deploy')      // Ansible → EKS
        stage('Verify')      // Health check
    }
}
```

## Prerequisites

- Jenkins with Docker + Ansible plugins
- AWS CLI configured with EKS access
- `kubectl` configured for the target cluster
- Container registry credentials in Jenkins

## Setup

1. **Fork/clone this repository**
2. **Configure Jenkins job** — point to this repo's Jenkinsfile
3. **Set credentials** in Jenkins:
   - AWS credentials
   - Container registry credentials
4. **Update `k8s/deployment.yaml`** with your image registry
5. **Run the pipeline**

## Project Structure

```
cicd-pipeline/
├── Jenkinsfile          # Jenkins scripted pipeline
├── Dockerfile           # Application container
├── ansible/
│   ├── playbook.yml     # Deployment playbook
│   └── inventory        # Target hosts
├── k8s/
│   ├── deployment.yaml  # K8s Deployment manifest
│   └── service.yaml     # K8s Service manifest
├── app/                 # Flask application
└── tests/               # Test suite
```

## Related

- [GitHub Repository](https://github.com/rohioffl/cicd-pipeline)
- [LinkedIn Project Post](https://linkedin.com/in/rohioffl)

---

**Author:** Rohit P T | Cloud Automation Engineer @ Ankercloud
