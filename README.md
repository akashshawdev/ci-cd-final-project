# CI/CD Final Project

## Project Name: Continuous Integration and Continuous Delivery (CI/CD) Pipeline

### Author
Student Project – IBM Skills Network / Coursera

### Description
This project demonstrates a complete CI/CD pipeline for a Python-based web application.
It covers:
- **Continuous Integration** using GitHub Actions (linting with flake8, unit tests with nose)
- **Continuous Delivery** using OpenShift Pipelines powered by Tekton

### Repository Structure
```
ci-cd-final-project/
├── .github/
│   └── workflows/
│       └── workflow.yml        # GitHub Actions CI pipeline
├── .tekton/
│   └── tasks.yml               # Tekton tasks for CD pipeline
├── service/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── tests/
│   ├── __init__.py
│   └── test_routes.py
├── requirements.txt
└── README.md
```

### CI Pipeline (GitHub Actions)
The CI pipeline runs on every push and pull request to the `main` branch and performs:
1. **Lint** – flake8 code quality checks
2. **Test** – unit tests with nose and coverage reporting
3. **Build** – Docker image creation and tagging

### CD Pipeline (OpenShift / Tekton)
The CD pipeline automates deployment to an OpenShift cluster through:
1. **Cleanup** – removes previous workspace artifacts
2. **Clone** – fetches source code from GitHub
3. **Lint** – runs flake8 linting
4. **Test** – runs unit tests with nose
5. **Build & Push** – builds container image and pushes to registry
6. **Deploy** – deploys application to OpenShift cluster

### Tech Stack
- **Language:** Python 3.9
- **Framework:** Flask
- **Linting:** flake8
- **Testing:** nose, coverage
- **CI:** GitHub Actions
- **CD:** OpenShift Pipelines (Tekton)
- **Container Registry:** OpenShift Internal Registry
