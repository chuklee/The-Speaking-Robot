# pip install PyAudio
#pip install SpeechRecognition

# ! Don't use a VM, or be sure you can use it, otherwise the script will not find your microphone
import speech_recognition as sr
import fileinput

r = sr.Recognizer()

# use the default microphone as the audio source
listening = True

line = input("Select a language :\n\t1 - for english\n\t2 - for french\n")
while line != "1" or line != "2" and listening == True:
    if listening == False and line == "1":
        print("Thank you for using The Speaking Bot, see you soon")
        exit()

    elif listening == False and line == "2":
        print("Merci d'avoir utiliser The Speaking Bot, à bientôt") 
        exit()

    elif line == "1":
        print("Welcolm to The Speaking Bot, please speak with me\n")
        while (listening):
            with sr.Microphone() as source:
                audio = r.listen(source)

                # audio is containing the sentence spoken


            try:
                sentence = r.recognize_google(audio)
                print("\t debug : " + sentence)
                if sentence == "stop":
                    listening = False
            except sr.UnknownValueError:
                print("I could not understand your speech")
                sentence = ""
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                sentence = ""

    elif line == "2":
        print("Bienvenu avec The Speaking Bot. Je vous en pris, parlez moi\n")
        while (listening):
            with sr.Microphone() as source:
                audio = r.listen(source)

                # audio is containing the sentence spoken

            try:
                sentence = r.recognize_google(audio, language="fr-FR")
                print("\t debug : " + sentence)
                if (sentence == "stoppe"):
                    listening = False
            except sr.UnknownValueError:
                print("I could not understand your speech")
                sentence = ""
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                sentence = ""
    
    else:
        line = input("Select a language :\n\t1 - for english\n\t2 - for french\n")
