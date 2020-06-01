#AudioBook converter
import os
import speech_recognition as sr
import pyttsx3
import datetime
from tkinter import*
import tkinter as tk

root = tk.Tk()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate = 5

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss!")
    elif hour>=12 and hour<18:
        speak("Good afternoon Boss!")
    else:
        speak("Good Evening Boss!")
        
def readText():
    text1 = input_text.get()
    speak(text1)
    
#wishMe()
#creating canvas
canvas = tk.Canvas(root,height=720,width=1280,bg="#006871").pack()
root.title("Audiobook App")

#creating a frame
frame = tk.Frame(root,bg="black")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

#labels
Label(frame,text="Welcome to this application!",font =16,fg="white",bg="black").pack()#place(x=80,y=50)
Label(frame,text="Enter Text to read:",fg="white",bg="black").place(x=60,y=75)

#crating entry box
input_text=StringVar()
Entry(frame,text="",textvar=input_text,width=115).place(x=60,y=100)

#creating a button
Button(frame,text = "Submit",width =6,command=readText,height="1",font=8).place(x=60,y=150)
root.mainloop()