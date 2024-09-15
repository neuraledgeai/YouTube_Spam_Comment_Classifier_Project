# YouTube Spam Comment Classifier

This project leverages a machine learning model to classify YouTube comments as either Spam or Not Spam. It’s built with a **Random Forest classifier**, tuned via **GridSearchCV**, and features a real-time classifier interface using **Streamlit**. You can adjust the spam detection threshold to explore how it influences predictions.

## Purpose
- Building a text classification model.
- Tuning model parameters with **GridSearchCV**.
- Understanding threshold adjustment for prediction probabilities.
- Deploying a machine learning model using **Streamlit** for live predictions.

## Features
- **Real-Time Classification**: Input a YouTube comment and see the model classify it as spam or not.
- **Threshold Tuning**: Adjust the spam detection threshold to fine-tune the sensitivity of the model.
- **Interactive Interface**: Explore the model through an intuitive, easy-to-use web interface.

## How It Works

The core of this project is a **Random Forest** model trained on a dataset of YouTube comments. The model classifies comments based on patterns learned during training. By adjusting the **spam detection threshold**, you can control the sensitivity of the classifier:

- **Higher Threshold**: More strict, fewer false positives (fewer comments incorrectly labeled as spam).
- **Lower Threshold**: More lenient, catches more potential spam but may lead to more false positives.

## Access the Full Project

For anyone interested in the full, detailed steps of this project, including everything from data importing, exploration, splitting, model building, tuning, evaluation, and prediction function to saving the model, please refer to the `YouTube_Spam_Comment_Classification.ipynb file`. This notebook is the heart of the project, containing all the comprehensive steps for creating the model.

Additionally, check out the **streamlit_app.py file**, which is designed to serve as the main backend for deploying the model as a web app. The app allows users to test comments in real time and classify them as "Spam" or "Not Spam" with adjustable threshold settings.

## Live Model in Action

Want to try the live model in action? Visit the web app here:
[YouTube Spam Comments Classifier Web App](https://youtube-spam-comments-classifier-project.streamlit.app)

*This project has been proudly contributed to the open-source community and is intended to serve as both an educational resource and a demonstration of the capabilities of machine learning in real-world applications. Whether you're here to learn, experiment, or build upon this work, we hope this project proves to be valuable.*
