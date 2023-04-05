# pip install PyAudio
#pip install SpeechRecognition

# ! Don't use a VM, or be sure you can use it, otherwise the script will not find your microphone
import speech_recognition as sr

r = sr.Recognizer()

# use the default microphone as the audio source
listening = True

while line != 1 or line != 2:
    print("Select a language :\n\t1 - for english\n\t2 - for french\n")
    line = fileinput.input()
    if line == 1:
        print("Welcolm to The Speaking Bot, please speak with me\n")
        while (listening):
            with sr.Microphone() as source:
                audio = r.listen(source)

                # audio is containing the sentence spoken

                if (audio == "stop"):
                    listening = False
            try:
                sentence = r.recognize_google(audio)
                print("You said: " + sentence)
            except sr.UnknownValueError:
                print("I could not understand your speech")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

    if line == 2:
        print("Bienvenu avec The Speaking Bot. Je vous en pris, parlez moi\n")
        while (listening):
            with sr.Microphone() as source:
                audio = r.listen(source)

                # audio is containing the sentence spoken

                if (audio == "stop"):
                    listening = False
            try:
                sentence = r.recognize_google(audio)
                print("You said: " + sentence)
            except sr.UnknownValueError:
                print("I could not understand your speech")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
