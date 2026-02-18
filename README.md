------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🧠 Model Architecture

3 Convolutional Layers

MaxPooling Layers

Dropout Regularization

Dense Fully Connected Layer

Softmax Output (7 classes)

Final Validation Accuracy: ~56%
###

HTML / CSS





⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/FaceEmotionDetection.git
cd FaceEmotionDetection

2️⃣ Create Virtual Environment (Python 3.10 recommended)
py -3.10 -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt


Or manually:

pip install tensorflow opencv-python flask numpy

▶️ Run Web App
python app.py


Open browser:

http://127.0.0.1:5000/


Press Q to stop if using OpenCV version.

🎓 How It Works

Webcam captures frame

Face detected using Haar Cascade

Face resized to 48x48 grayscale

CNN predicts emotion

Emotion + confidence displayed in real-time

💼 Resume Description

Developed a real-time facial emotion detection web application using CNN trained on FER-2013 dataset, integrated with Flask backend for live browser-based emotion classification with confidence scoring.

🔮 Future Improvements

Circular UI webcam frame

Emotion analytics dashboard

Model optimization (70%+ accuracy)

Cloud deployment (Render / AWS)

REST API integration

📜 License

This project is for educational and research purposes.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
