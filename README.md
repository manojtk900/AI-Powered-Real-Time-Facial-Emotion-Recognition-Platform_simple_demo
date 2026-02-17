🎭 Real-Time Facial Emotion Detection Web App

A real-time facial emotion detection system built using TensorFlow, OpenCV, and Flask, trained on the FER-2013 dataset and deployed as a live web application.

📸 Demo

Real-time webcam emotion detection with confidence percentage display.

🚀 Features

🎥 Live webcam streaming in browser

🧠 CNN model trained on FER-2013 dataset

😄 Detects 7 emotions:

Angry

Disgust

Fear

Happy

Neutral

Sad

Surprise

📊 Confidence percentage display

🌐 Flask web deployment

⚡ Real-time face detection using Haar Cascades

🛠️ Tech Stack

Python 3.10

TensorFlow / Keras

OpenCV

Flask



##
📂 Project Structure
FaceEmotionDetection/
│
├── train/                     # Training dataset
├── test/                      # Validation dataset
├── model.h5                   # Trained CNN model
├── train_model.py             # Model training script
├── app.py                     # Flask backend
├── templates/
│     └── index.html           # Frontend UI
├── real_time_detection.py     # OpenCV version
└── requirements.txt

🧠 Model Architecture

3 Convolutional Layers

MaxPooling Layers

Dropout Regularization

Dense Fully Connected Layer

Softmax Output (7 classes)

Final Validation Accuracy: ~56%
###

HTML / CSS
