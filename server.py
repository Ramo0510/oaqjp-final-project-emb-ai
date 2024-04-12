'''
Import module and intiate the app
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned contains the detected emotions
        and the dominant emotion for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!."

    emotions = emotion_detector(text_to_analyze)
    dominant_emotion = emotions['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Formatting the output as requested
    output = "For the given statement, the system response is "
    for emotion, score in emotions.items():
        if emotion != 'dominant_emotion':
            output += f"'{emotion}': {score}, "
    output += f"and the dominant emotion is {dominant_emotion.capitalize()}."

    return output

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
     # This function executes the Flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
