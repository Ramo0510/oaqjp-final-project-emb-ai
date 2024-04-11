import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyzes emotions in the given text using the Watson NLP API.

    Args:
        text_to_analyze (str): The text to analyze for detecting emotions.

    Returns:
        str: The analyzed text with detected emotions.
    """
    # URL of the API for emotion detection
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
     # Headers required for the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Input data format
    data = {"raw_document": {"text": text_to_analyze}}
    
    # Sending POST request to the API for emotion detection
    response = requests.post(url, headers=headers, json=data)

    # Convert the JSON response text into a dictionary
    formatted_response = json.loads(response.text)

    # Extract the required emotions with their scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Output format as requested
    output_formatting = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

    return output_formatting