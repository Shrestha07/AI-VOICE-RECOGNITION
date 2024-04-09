import speech_recognition as sr
import wolframalpha
import wikipedia
import webbrowser
import time
import os
import numpy as np
from twilio.rest import Client

# Twilio credentials
account_sid = "ACbdadadf551ad32a15b587bd25c87109f"
auth_token ="f2f0645b75268af0237ed83c9b78946d"
client = Client(account_sid, auth_token)
call = client.calls.create(
  url="http://demo.twilio.com/docs/voice.xml",
  to="+919163662012",
  from_="+14432216537"
)

# WolframAlpha credentials
app_id = 'your_app_id'
client = wolframalpha.Client(app_id)

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query

# Function to get a response from WolframAlpha
def get_wolfram_response(query):
    res = client.query(query)
    try:
        answer = next(res.results).text
    except StopIteration:
        answer = "I didn't understand"
        

if __name__ == "__main__":
    ai = ChatBot(name="Dev")
    while True:
        ai.speech_to_text()
        if ai.wake_up(ai.text) is True:
            res = "Hello I am Dev the AI, what can I do for you?"
        elif "time" in ai.text:
            res = ai.action_time()
        elif any(i in ai.text for i in ["thank","thanks"]):
            res = np.random.choice(
                  ["you're welcome!","anytime"])