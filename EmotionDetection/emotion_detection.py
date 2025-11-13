import requests  # Import the requests library to handle HTTP requests
import json #Impport the jason libraries to handle the jason file
def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json=myobj, headers=header)
    if response.status_code == 200:
        data = response.json()
        # Extract emotion scores from the response
        emotion_data = data['emotionPredictions'][0]['emotion']
        # Create scores dictionary
        scores = {
            'anger': emotion_data.get('anger', 0),
            'disgust': emotion_data.get('disgust', 0),
            'fear': emotion_data.get('fear', 0),
            'joy': emotion_data.get('joy', 0),
            'sadness': emotion_data.get('sadness', 0)
        }
        # Find dominant emotion
        dominant_emotion = max(scores, key=scores.get)
        # Return formatted dictionary
        return {
            'anger': scores['anger'],
            'disgust': scores['disgust'],
            'fear': scores['fear'],
            'joy': scores['joy'],
            'sadness': scores['sadness'],
            'The dominant emotion is': dominant_emotion.capitalize()
        }
    elif response.status_code == 400:
        return{
            'anger': scores['None'],
            'disgust': scores['None'],
            'fear': scores['None'],
            'joy': scores['None'],
            'sadness': scores['None'],
            'The dominant emotion is': ['None']
        }
    else:
        return None