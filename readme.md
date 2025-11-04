# Movie Recommendation System using LLM

## Tech Stack

- LLM Groq  
- Hugging Face Transformers  
- Chroma DB  
- GCP VM  
- Docker  
- Minikube  
- Kubectl  

---

## Project Setup

### 1. Build the Virtual Environment

Before writing any code, create a virtual environment.

Steps:

1. Create a new folder in your local machine.  
2. Open the terminal inside the folder and run the following commands:

```bash
python -m venv venv
source venv/bin/activate
```

3. Create a `.env` file inside the root directory and add the following credentials:

```
GROQ_API_KEY=<your_groq_api_key>
HUGGINGFACE_TOKEN=<your_hugging_face_token>
```

4. Create the following folder structure:

```
data/               # Add dataset here
src/                # Create __init__.py inside
config/             # Create __init__.py inside
utils/              # Create __init__.py inside
pipeline/           # Create __init__.py inside
setup.py            # Project setup and management script
```

5. Run the following command to install the project in editable mode:

```bash
pip install -e .
```

6. Inside the `utils` folder, create the following Python scripts:

- `logger.py`
- `custom_exception.py`

---

## Dockerization

To containerize the application:

1. Create a `Dockerfile` in the root directory.  
2. Create a `kubernetes.yaml` file for Kubernetes deployment.  

Example structure:

```
Dockerfile
kubernetes.yaml
```

---

## GCP Environment Setup

### 1. Create a VM Instance

Use the following configuration:

- Machine Series: E2  
- Machine Type: Standard  
- Memory: 16 GB RAM  
- Boot Disk: 256 GB  
- Image: Ubuntu 24.04 LTS  
- Networking: Enable HTTP and HTTPS traffic  

---

### 2. Install Docker and Kubernetes Tools

Run the following commands in the SSH terminal of the VM:

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu   $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" |   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker

docker run hello-world

curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
minikube start

curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo snap install kubectl --classic
kubectl version --client
```

---

### 3. Clone the Repository

Clone the project repository into your VM instance:

```bash
git clone <repo_url>
cd Movie-Recommender-System
```

---

### 4. Connect GitHub with VS Code and VM

Run the following commands in the VM terminal:

```bash
git config --global user.email "JThilinaDK123@gmail.com"
git config --global user.name "JThilinaDK123"
```

To push and pull changes between VS Code and the VM:

```bash
git add .
git commit -m "commit"
git push origin main
git pull origin main
```

If prompted for a password, create a new GitHub token and use it as your password.  
The token must have permissions for:
- repo  
- admin:org  
- admin:public_key  
- admin:org_hook  

---

## Build and Deploy the Application on GCP VM

Once all dependencies are set up, run the following commands inside the project directory.

### Build Docker Image

```bash
eval $(minikube docker-env)
docker build -t llmops-app:latest .
```

### Deploy using Kubernetes

```bash
kubectl create secret generic llmops-secrets \
 --from-literal=GROQ_API_KEY="" \
 --from-literal=HUGGINGFACEHUB_API_TOKEN=""

kubectl apply -f kubernetes.yaml
```

### Verify Deployment

```bash
kubectl get pods
kubectl get services
minikube tunnel
```

### Open another SSH terminal

```bash
kubectl port-forward svc/llmops-service 8501:80 --address 0.0.0.0
```

Once the pod is running and the service is exposed, the Movie Recommendation LLM application will be deployed successfully.

---

## Summary

This project integrates a Large Language Model (LLM)-based movie recommendation system with containerization and orchestration tools.  
It is deployed on a GCP virtual machine with Docker and Kubernetes for production-level scalability and efficiency.

---
