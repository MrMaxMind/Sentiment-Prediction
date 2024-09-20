# **Sentiment Prediction Web App**

Welcome to the **Sentiment Prediction Web App** repository. This project aims to classify text into different sentiment categories such as joy, anger, fear, and love using a pre-trained language model. Below are instructions for setting up the project, its features, and deployment on Render using Docker.

---

<div align="center">
  <img src="./Sentiment-Analysis.jpeg" alt="Sentiment Analysis Image" style="border:none;">
</div>

---

## 🚀 **Overview**

This project is built to predict the sentiment of user-input text using a pre-trained Hugging Face model. Users can input any text, and the model will predict the sentiment along with the confidence score. The project includes a Flask backend, a simple HTML-based frontend, and uses Docker for deployment on Render.

---

## ✨ **Features**

- **Text Preprocessing**: Cleans and tokenizes input text using BERT tokenizer.
- **Model Prediction**: Uses the `"j-hartmann/emotion-english-distilroberta-base"` model from Hugging Face to predict emotions from input text.
- **Web Application**: Provides an interactive web interface for users to input text and view sentiment predictions.
- **Render Deployment**: Easily deploy the app using Render’s cloud platform with Docker containerization.

---

## 📂 **Contents**

- `app.py`: Flask backend for loading the model and handling predictions.
- `templates/index.html`: Frontend HTML form for user input.
- `static/style.css`: Custom CSS for styling the frontend.
- `requirements.txt`: List of required Python dependencies.
- `Dockerfile`: Configuration file for Docker to containerize the web app.

---

## 🛠️  **Getting Started**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/Sentiment-Prediction.git
   cd Sentiment Prediction
2. **Install the required packages**:
   Ensure you have Python 3.x installed. Install dependencies by running:
   ```bash
   pip install -r requirements.txt

3. **Run the Flask App**:
   To start the web app locally:
   ```bash
   python3 app.py
   Open your web browser and go to `http://127.0.0.1:5000/`

---

## 🚢 **Deployment Instructions**

### 1. Model Training: 

The app uses a pre-trained Hugging Face model, so no additional training is required. The model will be downloaded automatically when the app is run.

### 2. Deploy the App on Render:

- Push your project to GitHub.
- Create a new web service on Render, connecting it to your GitHub repository.
- Ensure app.py is set as the entry point and requirements.txt includes all dependencies.

### 3. Configure the Environment:

- Add the necessary environment variables if required.
- Deploy the app, and Render will automatically start your service.

---

## 🔍 **Key Insights**

- Successfully implemented a pre-trained model to classify user inputs into various sentiments.
- Simple, user-friendly frontend designed to input text and display prediction results.
- Deployed on Render using Docker, making it easy to scale and maintain.-

---

## 🛠️ **Tools and Libraries**

- `Flask`: For the web backend and handling HTTP requests.
- `Transformers (Hugging Face)`: For loading and using the sentiment prediction model.
- `Pandas`: For data manipulation if needed.
- `HTML, CSS`: For creating and styling the frontend interface.
- `Docker`: For containerizing the application to deploy on Render.

---

## 🤝 **Contributing**
If you have suggestions or improvements, feel free to open an issue or create a pull request.

---

## ⭐ **Thank You!**

Thank you for visiting! If you find this project useful, please consider starring the repository. Happy coding!
