from distutils.cmd import Command
#from errno import
import time
from email import message
from socket import timeout
from typing import final
import pyttsx3
import requests
from requests.api import head
import speech_recognition as sr
import datetime
import os
from plyer import notification
import datetime
from datetime import datetime
import winsound
#from textblob import Word
import re

keyWord = 'samuel'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',200)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def recognize_speech():

    microphone = sr.Microphone()

    recognizer = sr.Recognizer()

    with microphone as source:

        audio= recognizer.listen(source,phrase_time_limit=6)

    response = ""

    #speak("Identifying speech..")

    try:

        response = recognizer.query = recognizer.recognize_google(audio, language="en-in")

    except:

        response="Error"

    return response






def reminder(query):
    command = query
    command = command.replace(".","")
    number = "\d"
    y = re.findall(number,command)
    am= "pm|am"
    done = re.findall(am,command)
    done = "".join(done)
    x = "".join(y)
    if x == "":
        speak("please specify time for reminder")
        command = takecommand()
        res = ([int(i) for i in command.split() if i.isdigit()])
            #print(res)
        a = ""    
        for i in res: 
            a = str(i)
            #print(a)
        b = "10"
        c = "11"
        d = "12"

        if len(a) > 1:
            if a != b and a!= c and a!= d :
                number = "\d"
                ok_1 = re.findall(number,command)
                m = "12"
                b = ":" 
                ok_1 = list(ok_1)
                pqr = "".join(ok_1)
                #print("pqr",pqr)
                if len(pqr)>3 :
                    n = -2
                elif len(pqr) == 3 and pqr[0:2] > m :
                    n = -2
                else :
                    n = -1
                ok_1.insert(n,b)
                res= "".join(ok_1)
                

                am= "pm|am"
                done = re.findall(am,command)
                #print(type(done))
                space = [" "]
                time = ok_1 + space + done
                #print(time)
                final_try = ""
                final = (final_try.join(time))
               
            
            else :
                number = "\d"
                ok = re.findall(number,command) 
                b = ":"  
                n= -1
                ok = list(a)
                ok.insert(n,b)
                res= "".join(ok)
                am= "pm|am"
                done = re.findall(am,command)
                #print(type(done))
                space = [" "]
                time = ok + space + done
                #print(time)
                final_try = ""
                final = (final_try.join(time))
                final = final.replace(":","")
                
        elif len(a) > 2 and a[-2:-1] != "0" :
            b = ":"  
            n= -2
            ok = list(a)
            ok.insert(n,b)
            res= "".join(ok)
        
            am= "pm|am"
            done = re.findall(am,command)
            #print(type(done))
            space = [" "]
            time = ok + space + done
            #print(time)
            final_try = ""
            final = (final_try.join(time))
            final = final.replace(":","")
            

        elif len(a) == 1 :
            number = "\d"
            ok = re.findall(number,command) 
            am= "pm|am"
            done = re.findall(am,command)
            #print(type(done))
            space = [" "]
            time = ok + space + done
            #print(time)
            final_try = ""
            final = (final_try.join(time))
            final = final.replace(":","")

        am= "pm|am"
        done = re.findall(am,command)
        done = "".join(done)
        
    else :
        command = command

    if ":" in command:
        number = "\d+\:*?\d+"
        ok = re.findall(number,command)
        print((ok))
        am= "pm|am"
        done = re.findall(am,command)
        #print(type(done))
        space = [" "]
        time = ok + space + done
        #print(time)
        final_try = ""
        final = (final_try.join(time))
        if final[-5:-3]== "00":
            final = final.replace(":","")
            final = final.replace("00","")

        else :
            final = final

        
    elif ":" not in command:
        res = ([int(i) for i in command.split() if i.isdigit()])
            #print(res)
        a = ""    
        for i in res: 
            a = str(i)
            #print(a)
        b = "10"
        c = "11"
        d = "12"

        if len(a) > 1:
            if a != b and a!= c and a!= d :
                number = "\d"
                ok_1 = re.findall(number,command)
                m = "12"
                b = ":" 
                ok_1 = list(ok_1)
                pqr = "".join(ok_1)
                #print("pqr",pqr)
                if len(pqr)>3 :
                    n = -2
                elif len(pqr) == 3 and pqr[0:2] > m :
                    n = -2
                else :
                    n = -1
                ok_1.insert(n,b)
                res= "".join(ok_1)
                

                am= "pm|am"
                done = re.findall(am,command)
                #print(type(done))
                space = [" "]
                time = ok_1 + space + done
                #print(time)
                final_try = ""
                final = (final_try.join(time))
               
            
            else :
                number = "\d"
                ok = re.findall(number,command) 
                b = ":"  
                n= -1
                ok = list(a)
                ok.insert(n,b)
                res= "".join(ok)
                am= "pm|am"
                done = re.findall(am,command)
                #print(type(done))
                space = [" "]
                time = ok + space + done
                #print(time)
                final_try = ""
                final = (final_try.join(time))
                final = final.replace(":","")
                
        elif len(a) > 2 and a[-2:-1] != "0" :
            b = ":"  
            n= -2
            ok = list(a)
            ok.insert(n,b)
            res= "".join(ok)
        
            am= "pm|am"
            done = re.findall(am,command)
            #print(type(done))
            space = [" "]
            time = ok + space + done
            #print(time)
            final_try = ""
            final = (final_try.join(time))
            final = final.replace(":","")
            

        elif len(a) == 1 :
            number = "\d"
            ok = re.findall(number,command) 
            am= "pm|am"
            done = re.findall(am,command)
            #print(type(done))
            space = [" "]
            time = ok + space + done
            #print(time)
            final_try = ""
            final = (final_try.join(time))
            final = final.replace(":","")


    title = command.partition("for")[2]
    patt  = f"[0-9]"
    title = re.sub(patt,"",title)
    title = title.replace("am","")
    title = title.replace("pm","")
    title = title.replace("at","")
    title = title.replace(":","")
    if title == "" :
        speak("good , can i get title of reminder")
        title = takecommand()
    else :
        title = title

    
    speak(f"great, i will reminde you at {final} for {title}")
    while True:
        local_time_1 = datetime.today().strftime("%I:%M %p").lower()
        
    
        if local_time_1[0:1]=="0" and local_time_1[3:5] != "00" and local_time_1[4:5] != "0":
            local_time = local_time_1[1:]
            local_time = local_time_1.replace("0","")
            #print("1",local_time)
        elif local_time_1[0:1]=="0"  and local_time_1[3:5] == "00" and local_time_1[0:2] != "10":        
            local_1= local_time_1.replace("0","")
            local_time = local_1
            local_time = local_time.replace(":","")
            #print("2",local_time)
        elif local_time_1[3:5] == "00" and local_time_1[0:2] != "10":
            local_1= local_time_1.replace("0","")
            local_time = local_1
            local_time = local_time.replace(":","")
        elif local_time_1[0:2]== "10"  and local_time_1[3:5] == "00":
            local_time = local_time_1[0:1]
            #print("4",local_time)
        elif local_time_1[0:2]!= "10"  and local_time_1[3:5] != "00" and local_time_1[3:4] == "0":
            test_time = ""
            for i in range(len(local_time_1)):
                if i != 3 :
                    test_time = test_time + local_time_1[i]
            local_time = test_time           
            #print("5",local_time)
        elif local_time_1[0:1]=="0" and local_time_1[3:4] != "0" :
            local_time = local_time_1[1:]          
            #print("6",local_time)
        elif local_time_1[3:4]== "0":
            local_time = local_time_1
        else :
            local_time = local_time_1          
            #print("7",local_time)
        if final == local_time :
            #playsound('/your/path/to/file/beep-07.mp3)
            winsound.PlaySound('abc',winsound.SND_LOOP)
            #time.sleep(1)
            notification.notify(                
                title= title,
                message="reminder",
                timeout=1.2
            )
            speak(f"Time for {title}, to stop the reminder say stop")
            command = recognize_speech()
            if "stop" in command or "stop it" in command:
                speak("reminder has been stopped")
                break  
        elif final < local_time:
                break

                

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    r = sr.Recognizer()
    text="no res"
    with sr.Microphone() as source:
        while True:
            audio = r.listen(source,timeout=5,phrase_time_limit=5)
            if keyWord.lower() in text.lower():
                speak("yes How can I help you?")
                voice = recognize_speech().lower()
                print(voice)
                print("listning...")
                r.pause_threshold = 1
        

            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language= 'en-in')
                print(f"user said: {query}")

            except Exception as e:
                speak("Say that again please...")
                return "none"
            return query

def wish():
    hour = int(datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("i am samuel.  please tell me how can i help you")
    print("listening")

if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()
        

        if "set reminder" in query or "set alarm" in query or "alarm set karo" in query:
            reminder(query)

        elif "thank you" in query:
            speak("welcome")
        
        elif "good job" in query:
            speak("its my duty")
     










