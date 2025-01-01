from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion detector")

@app.route('/emotionDetector')
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows all emotions and the dominant one.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    emotion_scores = ", ".join([f"'{emotion}': {score}" for emotion, score in emotions.items() if emotion != "dominant_emotion"])
    dominant_emotion = emotions['dominant_emotion']
    
    return f"For the given statement, the system response is {emotion_scores}. The dominant emotion is {dominant_emotion}."
   
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
