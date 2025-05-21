import pyttsx3 as tts
# pyttsx3 is a text-to-speech conversion library in Python.
#libraries in python are collections of modules that provide additional functionality and features.
print("Text-to-speech conversion using pyttsx3")

text=input("Enter the text you want to convert to speech: ")
engine = tts.init()
engine.say(text)
engine.runAndWait()
