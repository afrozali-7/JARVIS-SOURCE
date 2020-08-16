# This module is used to create JARVIS
import pyttsx3

# # datetime is used to show current time and date
# import datetime

# # SpeechRecogition is used taking command from user.
# import speech_recognition as sr

# # Here i am importing wikipedia for taking any information using wikipedia
# import wikipedia

# # This module is used for importing information from web browser
# import webbrowser

# # We can import any files from System
# import os

# # This module is used for sending mail to anyone
# import smtplib


# # SAPI5 is used for taking any command from user inside system
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')

# # This print function i used for printing voices.
# engine.setProperty('voice', voices[1].id)


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# # I am using this function for jarvis wish me on time like morning,evening,etc.


# def wishme():
#     hour = int(datetime.datetime.now().hour)
#     # I am if else sytatement here for showing time .
#     if hour >= 0 and hour < 12:
#         speak("Good Morning!")

#     elif hour >= 12 and hour < 18:
#         speak("Good Afternoon!")

#     else:
#         speak("Good Evening!")

# # After completion of wish jarvis ask me how can i help you!

#     speak("Hi Afroz, what can i do for you")


# def hear():
#     # This command is used for taking input from mic and recognise and give output.
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")
#         # This is using google for recognizing our voicces.
#         query = r.recognize_google(audio, language='eng-in')
#         # User query will be printed through this code.
#         print(f"User said: {query}\n")

#     except Exception as e:
#         # print(e)
#         print("Speak again please...")
#         return("none")  # Here none string will be return.
#     return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail', 'password')
#     server.sendmail('yourmail.com', to, content)
#     server.close()



# if __name__ == "__main__":
#     wishme()
#     while True:
#     # if 1:
#         # This will convert user query into lowercase text.
#         query = hear().lower()

#         # Logic for executing task based on query
#         if 'wikipedia' in query:
#             speak('Searching  Wikipedia...')
#             query = query.replace("wikipedia", "")
#             results = wikipedia.summary(query, sentences=2)
#             speak("According to wikipedia")
#             print(results)
#             speak(results)

#         # Now i am using this code for opening YouTube
#         elif 'open youtube' in query:
#             webbrowser.open("https://www.youtube.com")

#         # This is use to open Google. 
#         elif 'open google' in query:
#             webbrowser.open("https://www.google.com")

#         #This is used for opening Facebook.
#         elif 'open stackoverflow' in query:
#             webbrowser.open("https://www.stackoverflow.com") 

#         # This is used to open Instagram
#         elif 'open instagram' in query:
#             webbrowser.open("https://www.instagram.com") 

#         # This code is used to open my personal blogging website        
#         elif 'open mywebsite' in query:
#             webbrowser.open("https://www.afroztech.blogspot.com")  

#         # This one is for opening twitter
#         elif 'open twitter' in query:
#             webbrowser.open("https://www.twitter.com") 

#         # This is use for opening my university website
#         elif 'open my university website' in query:
#             webbrowser.open("https://www.pdm.ac.in")  

#         # This is used to open wikipedia in browser
#         elif 'open wikipedia' in query:
#             webbrowser.open("https://www.wikipedia.org")    

#         # This is for opening Gmail in browser
#         elif 'open gmail' in query:
#             webbrowser.open("https://www.gmail.com")

#         # This is for opening Whatsweb in browser
#         elif 'open whatsapp' in query:
#             webbrowser.open("https://web.whatsapp.com/")

#         # This one is for playing Music from System
#         elif 'play music' in query:
#             music_dir = 'F:\\songs'
#             songs = os.listdir(music_dir)
#             print(songs)
#             os.startfile(os.path.join(music_dir, songs[0]))

#         # For time inquery
#         elif 'the time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f"Sir The time is{strTime}")
#             print(strTime)
        
#         # for opening anything form system
#         elif 'open code' in query:
#             Path = "C:\\Users\\afroz\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#             os.startfile(Path)

#         # This code is for opening Firefox
#         elif 'open firefox' in query:
#             Path2 = "C:\\Program Files\\Mozilla Firefox\\firefox.exe" 
#             os.startfile(Path2)

#         # This is for opening MS Word
#         elif 'open word' in query:
#             Path3 = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
#             os.startfile(Path3)

#         # This is opening Powerpoint
#         elif 'open powerpoint' in query:
#             Path4 = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
#             os.startfile(Path4)

#         # This is for opening MS Excel
#         elif 'open excel' in query:
#             Path5 = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
#             os.startfile(Path5)

#         elif 'email to India' in query:
#             try:
#                 speak("What should i write in Mail?")
#                 content = hear() #This give our voices into  strings.
#                 to = "aliafroz936@gmail.com" 
#                 sendEmail(to, content)
#                 speak("Email has been sent")
#             except Exception as e:
#                 print(e)
#                 speak("Sorry , I am not able to send the mail")



#         # This is use for sending Email
#         elif 'email to Raman' in query:
#             try:
#                 speak("What should i write in Mail?")
#                 content = hear() #This give our voices into  strings.
#                 to = "modulusmod@gmail.com" 
#                 sendEmail(to, content)
#                 speak("Email has been sent")
#             except Exception as e:
#                 print(e)
#                 speak("Sorry , I am not able to send the mail")  



#         # This is use for sending Email
#         elif 'email to Parul Mam' in query:
#             try:
#                 speak("What should i write in Mail?")
#                 content = hear() #This give our voices into  strings.
#                 to = "parul2_engg@pdm.ac.in" 
#                 sendEmail(to, content)
#                 speak("Email has been sent")
#             except Exception as e:
#                 print(e)
#                 speak("Sorry , I am not able to send the mail")



#         # This is use for sending Email
#         elif 'email to Deep Mam' in query:
#             try:
#                 speak("What should i write in Mail?")
#                 content = hear() #This give our voices into  strings.
#                 to = "deepinder.kaur@pdm.ac.in" 
#                 sendEmail(to, content)
#                 speak("Email has been sent")
#             except Exception as e:
#                 print(e)
#                 speak("Sorry , I am not able to send the mail")



#         # This is use for sending Email
#         elif 'email to Vanshika Mam' in query:
#             try:
#                 speak("What should i write in Mail?")
#                 content = hear() #This give our voices into  strings.
#                 to = "vashisht238@gmail.com" 
#                 sendEmail(to, content)
#                 speak("Email has been sent")
#             except Exception as e:
#                 print(e)
#                 speak("Sorry , I am not able to send the mail")



#         # This is use for sending Email
#         elif 'email to Naman Mam' in query:
#             try:
#                 speak("What should i write in Mail?")
#                 content = hear() #This give our voices into  strings.
#                 to = "Kakkarnaman92@gmail.com" 
#                 sendEmail(to, content)
#                 speak("Email has been sent")
#             except Exception as e:
#                 print(e)
#                 speak("Sorry , I am not able to send the mail")



#         # This is use for sending Email
#         elif 'email to Jagjit Sir' in query:
#             try:
#                 speak("What should i write in Mail?")
#                 content = hear() #This give our voices into  strings.
#                 to = "	jagjit_engg@pdm.ac.in" 
#                 sendEmail(to, content)
#                 speak("Email has been sent")
#             except Exception as e:
#                 print(e)
#                 speak("Sorry , I am not able to send the mail")



#         # This is use for sending Email
#         elif 'email to Rehan' in query:
#             try:
#                 speak("What should i write in Mail?")
#                 content = hear() #This give our voices into  strings.
#                 to = "wahidhussain868@gmail.com" 
#                 sendEmail(to, content)
#                 speak("Email has been sent")
#             except Exception as e:
#                 print(e)
#                 speak("Sorry , I am not able to send the mail")
