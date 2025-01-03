"""
This module provides a function to detect emotions in text.
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotions within a given text using the Watson NLP library
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1'
        '/NlpService/EmotionPredict'
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_json, timeout=10)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion_scores = formatted_response["emotionPredictions"][0]["emotion"]
        emotion = {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness':  emotion_scores['sadness']
        }
        dominant_emotion = max(emotion, key=emotion.get)
        emotion['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
        emotion = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else :
        response.raise_for_status()

    return emotion
