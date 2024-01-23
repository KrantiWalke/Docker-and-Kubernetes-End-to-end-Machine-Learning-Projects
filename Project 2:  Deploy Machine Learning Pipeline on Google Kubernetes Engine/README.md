# Deploy Machine Learning Pipeline on Google Kubernetes Engine

## 👉 Learning Goals:
- What is a Container, What is Docker, What is Kubernetes, and What is Google Kubernetes Engine?
- Build a Docker image and upload it on Google Container Registry (GCR).
- Create clusters and deploy machine learning pipeline with Flask app as a web service.
- See a web app in action that uses a trained machine learning pipeline to predict on new data points in real-time.

Read the complete post: https://medium.com/@moez_62905/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b

# Machine Learning Pipeline Deployment on GKE

## Description
This project demonstrates how to build, containerize, and deploy a machine learning pipeline on Google Kubernetes Engine (GKE). It involves training a machine learning model using PyCaret, building a web application with Flask for predictions, containerizing the application using Docker, and deploying it on GKE.

## Prerequisites
- Python (with PyCaret library)
- Flask
- Docker
- Google Cloud Platform account
- Basic understanding of Kubernetes

## Installation & Setup
### 1. Install Required Libraries
'''
pip install pycaret flask
'''


### 2. Set Up Google Cloud Platform
- Sign up for a GCP account.
- Create a new project in GCP Console.
- Configure Google Cloud SDK.

### 3. Clone Repository
'''
git clone https://github.com/pycaret/pycaret-deployment-google.git
'''


## Usage
### Training Machine Learning Model
- Navigate to the training script.
- Run the script to train the model and save the pipeline.

### Building Flask Application
- Explore the Flask application code in the repository.
- Run the Flask app locally for testing.

### Containerizing with Docker
- Build a Docker image of the Flask application.
- Push the image to Google Container Registry.

### Deploying on Google Kubernetes Engine
- Create a cluster in GKE.
- Deploy the application to the cluster.
- Expose the application to the internet.

## Accessing the Web Application
- Use the external IP provided by GKE to access the web application.
- Enter the required information in the web form to get predictions.


