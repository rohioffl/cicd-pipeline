CI/CD Pipeline Project

CI Pipeline
Table of Contents

    Introduction
    Features
    Prerequisites
    Installation
    Usage
    Testing
    CI/CD Pipeline
    Dockerization
    Contributing

Introduction

This project demonstrates a complete CI/CD pipeline for a Python application using GitHub Actions and Docker. The CI/CD pipeline automates the process of testing and deploying code to ensure reliability and efficiency.
Features

    Automated Testing: Runs unit tests using pytest on every push and pull request.
    Dockerized Deployment: Builds and runs the application in a Docker container.
    Continuous Integration: Uses GitHub Actions for automated testing.
    Continuous Deployment: Can be extended to deploy to various environments.

Prerequisites

Before you begin, ensure you have the following tools installed:

    Docker
    Python 3.8+
    Git

Installation

    Clone the Repository

    bash

git clone https://github.com/rohioffl/cicd-pipeline.git
cd cicd-pipeline

Create a Virtual Environment and Activate it

bash

python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

Install Dependencies

bash

    pip install -r requirements.txt

Usage

    Run the Application Locally

    bash

python src/main.py

Build and Run with Docker

bash

    docker build -t cicd-pipeline .
    docker run -d -p 8000:8000 cicd-pipeline

    This will start the application and expose it on port 8000.

Testing

To run tests, use the following command:

bash

pytest

Test coverage is automatically reported in the GitHub Actions workflow.
CI/CD Pipeline

The CI/CD pipeline is defined using GitHub Actions. It includes the following key steps:

    Checkout Code: Retrieves the latest code from the repository.
    Set Up Python: Configures the Python environment.
    Install Dependencies: Installs the necessary Python packages.
    Run Tests: Executes the test suite.

The workflow configuration is found in .github/workflows/ci.yml:

yaml

name: CI Pipeline

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: |
        pytest

Dockerization

The application is containerized using Docker. The Dockerfile includes steps to set up and run the application:

dockerfile

FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]

Building the Docker Image

bash

docker build -t cicd-pipeline .

Running the Docker Container

bash

docker run -d -p 8000:8000 cicd-pipeline

Contributing

Contributions are welcome! Please follow these steps:

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes.
    Commit your changes (git commit -m 'Add some feature').
    Push to the branch (git push origin feature-branch).
    Open a pull request.
