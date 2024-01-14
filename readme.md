
# MNIST Digit Classifier Flask App

## Introduction

This project involves a Flask web application that serves a pre-trained TensorFlow model to classify handwritten digits. The MNIST dataset, which is a collection of 70,000 grayscale images of handwritten digits (0 through 9), is used for training the model. Users can upload an image of a handwritten digit to the app, and the app will return the digit's classification along with the probability of the prediction.

## Problem Statement

Handwriting digit recognition is a classic problem in the field of machine learning and computer vision. This project demonstrates a practical application of a convolutional neural network (CNN) to solve this problem. The Flask web app provides an easy-to-use interface for users to test the model's capabilities with their own images of handwritten digits.

## Prerequisites

Before running the application, ensure you have the following installed:
- Docker
- Git (optional, for cloning the repository)

## Installation and Running the App

Follow these steps to get the application up and running:

### Step 1: Clone the Repository

(Optional) If you have Git installed, clone the repository to your local machine. Alternatively, you can download the source code directly.

```bash
git clone https://github.com/dawei7/ml_zoomcamp_capstone2
cd ml_zoomcamp_capstone2
```

### Step 2: Build the Docker Image

Navigate to the directory containing the Dockerfile and run the following command to build the Docker image:

```bash
docker build -t mnist-flask-app .
```

This command creates a Docker image named `mnist-flask-app` containing the Flask application and all necessary dependencies.

### Step 3: Run the Docker Container

Start the container from the image:

```bash
docker run -p 5000:5000 mnist-flask-app
```

This command runs the Flask application inside a Docker container and makes it accessible at `http://localhost:5000`.

### Step 4: Access the Web Application

Open a web browser and go to `http://localhost:5000`. You should see the interface for uploading an image of a handwritten digit.

### Step 5: Upload an Image

Use the web interface to upload an image of a handwritten digit. The application will process the image and display the predicted digit along with the confidence level of the prediction.

## Usage Notes

- The application expects grayscale images of handwritten digits, similar to those in the MNIST dataset.
- For best results, use images where digits are centered and occupy most of the image area.

## Conclusion

This application demonstrates a simple yet effective way to deploy a machine learning model for digit recognition using Flask and Docker, making it accessible for users to interact with the model through a web interface.
