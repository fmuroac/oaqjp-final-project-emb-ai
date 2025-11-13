"""
Flask server for Emotion Detector application.
Provides routes for home and emotion detection.
"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def home():
    """Return welcome message with usage instructions."""
    return "Welcome to the Emotion Detector app! Use /emotionDetector?textToAnalyze=your_text"

@app.route("/emotionDetector")
def emotion_detector_route():
    """Process text input and return detected dominant emotion and score."""
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Invalid input! Please provide text to analyze."

    response = emotion_detector(text_to_analyze)
    if not response:
        return "Error processing the request."

    label = response.get('label') or response.get('dominant_emotion')
    score = response.get(label)if label else None

    if label is None or score is None:
        return "Could not determine dominant emotion."

    return  (
        f"The given text has been identified as '{label.capitalize()}' "
        f"with a score of {score:.4f}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
