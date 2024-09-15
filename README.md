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
