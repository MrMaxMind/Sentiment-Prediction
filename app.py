from flask import Flask, request, render_template
from transformers import pipeline
import os

app = Flask(__name__)

# Load the emotion analysis pipeline from Hugging Face
emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        
        # Perform emotion analysis
        result = emotion_pipeline(text)

        # Sort emotions by highest score (confidence)
        sorted_emotions = sorted(result[0], key=lambda x: x['score'], reverse=True)

        # Get the top emotion and score
        top_emotion = sorted_emotions[0]['label']
        top_score = sorted_emotions[0]['score']

        return render_template('index.html', text=text, sentiment=top_emotion, score=round(top_score, 2))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
