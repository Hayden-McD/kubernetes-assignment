#!/bin/bash

# Remove existing tarball if it exists (to save space and speeds up deployment)
rm -rf Images/app-image.tar

# Build the new Flask application Docker image
docker build -t app-image -f Dockerfile.web .

# Check if Images folder exists, if not create it.
mkdir -p Images

# Tarball the image and save to images directory
docker save app-image:latest > Images/app-image.tar

# Import the image into microk8s
microk8s ctr image import Images/app-image.tar

# Restart Kubernetes deployment to use new iamge
kubectl rollout restart deployment flask-deployment
