# Badger Gif App

## Overview

This project presents a **Flask-based, Dockerized web application** integrated with **GitHub Actions CI/CD** for automation. The application dynamically serves a random badger GIF from a **MySQL database** and keeps track of visitor counts. The infrastructure is managed using **Terraform** to provision a **Google Kubernetes Engine (GKE) cluster**, and **Helm** for Kubernetes deployments.

### Features

- **Flask Web Application**
- **GitHub Actions CI/CD**
- **Dockerized Deployment**
- **MySQL Database for GIF storage & visitor tracking**
- **Infrastructure as Code (Terraform) for GKE provisioning**
- **Kubernetes Deployment using Helm**

---

## Project Architecture Diagram

(Insert Image of the Architecture here)

### CI/CD Pipeline Flow

1. **Code Push & CI/CD Pipeline Trigger**

   - GitHub Actions detects a push to the repository and triggers the pipeline.

2. **Building & Pushing Docker Image**

   - The Flask app is containerized using Docker and pushed to Docker Hub.

3. **Testing with Docker Compose**

   - The application is tested locally before deployment to Kubernetes.

4. **Updating Helm Chart**

   - Helm templates are updated to include the new Docker image.

5. **Infrastructure Provisioning with Terraform**

   - GKE is provisioned using Terraform, with **S3 as a backend** for tfstate.

6. **Deployment to Kubernetes**

   - Helm deploys the updated application to GKE.

---

## Setup Instructions

### Required Tools

- **Python & Flask**
- **Docker**
- **Terraform**
- **Kubernetes (Minikube for local testing)**
- **Helm**
- **GitHub Actions**

### 🔑 Required Secrets & Variables

#### GitHub Secrets:

- `DOCKER_USERNAME`: Docker Hub username
- `DOCKER_PASSWORD`: Docker Hub token
- `MYSQL_ROOT_PASSWORD`: MySQL root password
- `MYSQL_DATABASE`: MySQL database name
- `MYSQL_USER`: MySQL user
- `MYSQL_PASSWORD`: MySQL password
- `AWS_ACCESS_KEY_ID`: AWS credentials for Terraform backend
- `AWS_SECRET_ACCESS_KEY`: AWS secret key
- `GCP_PROJECT_ID`: GCP project ID
- `GCP_CREDENTIALS`: GCP service account key

#### GitHub Variables:

- `FLASK_ENV`: Flask environment
- `DB_HOST`: Database host
- `DB_USER`: Database user
- `DB_PASSWORD`: Database password
- `DB_NAME`: Database name
- `PORT`: Flask application port

---

## Deployment Steps

### Local Testing

```sh
docker-compose up --build
curl http://localhost:5001
```

### Deploying with Terraform

```sh
terraform init
terraform apply -auto-approve
```

### Deploying with Helm

```sh
helm repo add my-repo <helm-repo-url>
helm install my-release my-repo/flask-app --version 1.0.0
```

---

## Cleanup

To remove deployed resources:

```sh
helm uninstall my-release
terraform destroy -auto-approve Security Considerations
```

**GitHub Secrets**: Secure credential storage.

- **Kubernetes Secrets**: Secure environment variable storage.
- **HTTPS Enforcement**: Secure communication.
- **IAM Role Restrictions**: Minimum privilege policies applied.

---

## Conclusion

This project automates the deployment of a Flask web application using Kubernetes, Helm, and Terraform.&#x20;

---

![final project diagram drawio](https://github.com/user-attachments/assets/1beed81d-c3e1-4486-9554-6e638852316f)


