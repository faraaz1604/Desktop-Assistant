import sys
from cv2 import data
import pyttsx3
import requests
from requests.api import head
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as py
import smtplib
import sys
import pyjokes 
import pyautogui
import instaloader 
import json
import time
from bs4 import BeautifulSoup
import pywikihow
from wikipedia.wikipedia import search
import pywikihow
from pywikihow import search_wikihow
import psutil
import numpy as np





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voice', voices[2].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert voice into text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"Good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"Good afternoon, its {tt}")
    else:
        speak(f"Good evening , its {tt}")
    speak("I am Ruby. how can i help you?")

# to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('enter email', '*******') #password enter kar wahan (******)
    server.sendmail('enter email',to,content)
    server.close()


# for news updates
def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=e1a2b90f19484faebfc0d821cbc9cb7b'

    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    #print articles
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eight","ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is : {head[i]}")




def TaskExecution():
    pyautogui.press('esc')
    speak("verification Successful")
    speak("Welcome back faraaz Sir")
    wish()
    while True:
        query = takeCommand().lower()

        # logic builiding from here to perform tasks

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open code" in query:
            apath = "C:\\Users\\Faraaz\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open movies" in query:
            bpath = "D:\movies"
            os.startfile(bpath)

        elif "open camera" in query:
            vid = cv2.VideoCapture(0)
            
            while(True):
                
               
                ret, frame = vid.read()
            
               
                cv2.imshow('frame', frame)
                
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            
            
            vid.release()
           
            cv2.destroyAllWindows()  


        elif "play music" in query:
            music_dir = "E:\\Music"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs) --> to play random songs and make songs[8] as rd in below line
            os.startfile(os.path.join(music_dir, songs[8]))

        
        elif  "ip address" in query:
            ip = get('http://api.ipify.org').text
            speak(f"your IP address is {ip}")
               
        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")


        elif "open google" in query:
            speak("Sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "my website" in query:
            webbrowser.open("mohamedfaraaz.epizy.com")       

        elif "send message" in query:
            py.sendwhatmsg("+919606236046","hello faraaz",12,35)

        elif "play youtube song" in query:
            py.playonyt("DA DA DA ") 

        elif "email to faraaz" in query:
            try:
                speak("What should i say? sir")
                content = takeCommand().lower()
                to = "mohamedfaraaz007@gmial.com" 
                sendEmail(to,content)
                speak("Email has been sent successfully")

            except Exception as e:
                print(e)
                speak("Sorry Sir! I am not able to sent this email")

        elif "quit" in query:
            speak("Thanks for spending time with me Sir, you are the best, come back soon ")
            sys.exit()

        elif "volume up" in query:
            pyautogui.press("Volumeup")

        elif "volume down" in query:
            pyautogui.press("Volumedown")

        elif "volume mute" in query or "mute" in query:
            pyautogui.press("Volumemute")    
        
        
        elif "weather" in query:
            speak("Sir Enter the City name")       
            api_key = "fc6b0b1f0f5691c48c246a82eed8993a"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = input("Enter city name : ")
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
 
    
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                current_temperature-273.15
                speak(f" Temperature  = " +
                                str(current_temperature)+"degree Celsius" +
                    "\n atmospheric pressure  = " +
                                str(current_pressure)+"hpa" +
                    "\n humidity  = " +
                                str(current_humidity)+"percentage" +
                    "\n Over all condition will be " +
                                str(weather_description))
        
            else:
                speak(" City Not Found ")

                

        
          
#to close any application
        elif "close notepad" in query:
            speak("Okay sir, Closing notepad")
            os.system("taskkill /f /im notepad.exe")

#to set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = 'E:\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

#to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
    

        elif "shutdown" in query:
            speak("Okay sir, shuting down the system")
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            speak("Okay sir, restarting the system")
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            speak("Okay sir, system sleeping now")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "tell me news" in query:
            speak("please wait sir,fetteching the latest news")
            news()

        #---------------------------------------to find my location--------------------------------------------------------------------
        elif "where am i " in query or "where are we " in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"Sir i am not sure,but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("Sorry Sir, Due to network issue i am not able to find excat location")
                pass
        #-------------------------------to check a insta profile---------------------------------------------------------------
        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir please enter the user name you would like to check ")
            name = input("Enter UserName here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir here is the profile of the user {name}")
            speak("Sir would you like to download profile picture of this account.")
            condition = takeCommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("I am done Sir,profile picture is saved in our main folder. now i am ready for next task")
            else:
                pass        

    #----------------------------------to take screenshot-------------------------------------------------------
        elif " screenshot" in query or "take a screenshot" in query:
            speak("Sir,please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("please hold the screen for few seconds,i am taking screenshot")
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i have taken the screenshot sir it is saved in our main folder sir")

        elif "activate how to do mode" in query:
            speak("How to do mode is activated")
            while True:
                speak("what are you looking for? Sir")
                how = takeCommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("okay sir, closing how to do mode")
                        break
                    else:
                        from pywikihow import search_wikihow
                        speak("How to do mode is activated please tell me what you want to know ")
                        how = takeCommand()
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am not able to find this")

        elif "how much power is left" in query or "how much power we have" in query or "battery" in query:
            battery = psutil.sensors_battery()
            precentage = battery.percent
            speak(f"Sir the system is currently running on {precentage} percentage battery")

        elif "girlfriend" in query:
            speak("which one sir? ")
            music_dir = "E:\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[9]))
            import cv2
            import numpy as np
            from PIL import Image

            maskPath = 'mask.png'

            harcasPath = 'haarcascade_frontalface_default.xml'

            faceCascade = cv2.CascadeClassifier(harcasPath)

            mask = Image.open(maskPath)

            def thug_mask(image):
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                faces = faceCascade.detectMultiScale(gray, 2.1)

                background = Image.fromarray(image)

                for (x, y, w, h) in faces:
                    resized_mask = mask.resize((w, h), Image.ANTIALIAS)

                    offset = (x, y)
                    background.paste(resized_mask, offset, mask=resized_mask)
                
                return np.asarray(background)

            cap = cv2.VideoCapture(0)

            while True:
                _, frame = cap.read()

                cv2.imshow("Thug Life Filter", thug_mask(frame))

                if cv2.waitKey(1) == 27:
                    break

            cap.release()

            cv2.destroyAllWindows()


import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
recognizer.read('trainer/trainer.yml')   #load trained model
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


id = 2 #number of persons you want to Recognize


names = ['','faraaz']  #names, leave first empty bcz counter starts from 0


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
cam.set(3, 640) # set video FrameWidht
cam.set(4, 480) # set video FrameHeight

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

# flag = True

while True:

    ret, img =cam.read() #read the frames using the above created object

    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

    faces = faceCascade.detectMultiScale( 
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

        # Check if accuracy is less them 100 ==> "0" is perfect match 
        if (accuracy < 100):
            id = names[id]
            accuracy = "  {0}%".format(round(100 - accuracy))
            TaskExecution()

        else:
            id = "unknown"
            accuracy = "  {0}%".format(round(100 - accuracy))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(1) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("Thanks for using this program, have a good day.")
cam.release()
cv2.destroyAllWindows()
   