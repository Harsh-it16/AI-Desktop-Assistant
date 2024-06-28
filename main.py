import os
import subprocess

import speech_recognition as sr
import win32com.client
import webbrowser
import openai
import datetime
from config import apikey

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n ******************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        text += response[["choices"][0], ["text"]]
        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        with open(os.startfile(r"C:\Users\thebr\PycharmProjects\jarvis A.I\Openai\ {''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w")) as f:
            f.write(text)
    except Exception as e:
        return "Some error occurred. Sorry from Jerry"


# def chat(query):
#     global chatStr
#     print(chatStr)
#     openai.api_key = apikey
#     chatStr += f"Harry: {}"
def sayquery(text):
    # while True:
    # print("Enter the word you want to speak")
    # s = "hello brother"
    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said:{query}")
            return query
        except Exception as e:
            return "Some error occurred. Sorry from Jarvis"


if __name__ == '__main__':
    print("Welcome to Jerry A.I")
    sayquery("hello I am Jerry AI")
    # say("hello brother")
    while True:
        print("Listening.....")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                sayquery(f"Opening {site[0]} Sir")
                webbrowser.open(site[1])

        # sayquery(query)
        if "open music" in query:

            os.startfile(r"C:\Users\thebr\Music\MITRAZ - Kabhi Na Kabhi (OFFICIAL MUSIC VIDEO).mp3")

        elif "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            sayquery(f"Sir time is {strfTime}")

        elif "open edge".lower() in query.lower():

            os.startfile(r"C:\Users\thebr\OneDrive\Desktop\Personal - Edge.lnk")

        elif "open videos".lower() in query.lower():

            os.startfile(r"C:\Users\thebr\Videos")

        elif "Using Artificial Intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jerry Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        # else:
        #     print("Chatting....")
        #     chat(query)
