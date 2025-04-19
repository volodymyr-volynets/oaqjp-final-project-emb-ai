''' Final Project
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    ''' Index page
    '''
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_func():
    ''' EmotionDetector API
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
