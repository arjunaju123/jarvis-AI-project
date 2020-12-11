


import pyttsx3
# It works offline, unlike other text-to-speech libraries.
# Rather than saving the text as audio file, pyttsx actually speaks it there.
# This makes it more reliable to use for voice-based projects.
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
#https://www.tutorialspoint.com/python/python_sending_email.htm
# Simple Mail Transfer Protocol (SMTP) is a protocol,
# which handles sending e-mail and routing e-mail between mail servers.
#
# Python provides smtplib module, which defines an SMTP client session object that can be used to send mail to
# any Internet machine with an SMTP or ESMTP listener daemon(A daemon is a type of program on Unix-like operating systems that runs unobtrusively in the background, rather than under the direct control of a user, waiting to be activated by the occurance of a specific event or condition)
engine=pyttsx3.init('sapi5')

# The Speech Application Programming Interface or SAPI is an API developed by Microsoft
# to allow the use of speech recognition and speech synthesis within Windows applications.
# pyttsx is a cross-platform text to speech library which is platform independent.
# The major advantage of using this library for text-to-speech conversion is that it works offline.
# However, pyttsx supports only Python 2.x.
# Hence, we will see pyttsx3 which is modified to work on both Python 2.x and Python 3.x with the same code.

# Usage –
# First we need to import the library and then initialise it using init() function. This function may take 2 arguments.
# init(driverName string, debug bool)
#
# drivername : [Name of available driver] sapi5 on Windows | nsss on MacOS
# debug: to enable or disable debug output
# After initialisation, we will make the program speak the text using say() function. This method may also take 2 arguments.
# say(text unicode, name string)
#
# text : Any text you wish to hear.
# name : To set a name for this speech. (optional)
# Finally, to run the speech we use runAndWait() All the say() texts won’t be said unless the interpreter encounters runAndWait().

# importing the pyttsx library
# import pyttsx3
#
# # initialisation
# engine = pyttsx3.init()
#
# # testing
# engine.say("My first code on text-to-speech")
# engine.say("Thank you, Geeksforgeeks")
# engine.runAndWait()
voices=engine.getProperty('voices')
# print(voices[0].id)
#
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

# pyttsx3.init([driverName : string, debug : bool]) – Gets a reference to an engine instance that will use the given driver.
# If the requested driver is already in use by another engine instance, that engine is returned. Otherwise, a new engine is created.
# getProperty(name : string) – Gets the current value of an engine property.
# setProperty(name, value) – Queues a command to set an engine property. The new property value affects all utterances queued after this command.
# say(text : unicode, name : string) – Queues a command to speak an utterance.
# The speech is output according to the properties set before this command in the queue.
# runAndWait() – Blocks while processing all currently queued commands.
# Invokes callbacks for engine notifications appropriately. Returns when all commands queued before this call are emptied from the queue.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    time=datetime.datetime.now().hour
    if(time>0 and time<12):
        speak("good morning")
    elif(time>12 and time<18):
        speak("good afternoon")
    else:
        speak("good evening")

    speak("Iam jarvis, Please tell me how can i help you")

def takecommand():
# it takes microphone input from the user and returns a string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("say that again please")
        return "none"
    return query

def sentemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("your email id@gmail.com","your password")
    server.sendmail('your email id@gmail.com',to,content)
    server.close()

# Here is a simple syntax to create one SMTP object, which can later be used to send an e-mail −
#
# smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )

# Here is the detail of the parameters −
#
# host − This is the host running your SMTP server. You can specify IP address of the host or a domain name like tutorialspoint.com. This is optional argument.
#
# port − If you are providing host argument, then you need to specify a port, where SMTP server is listening. Usually this port would be 25.
#
# local_hostname − If your SMTP server is running on your local machine, then you can specify just localhost as of this option.
# An SMTP object has an instance method called sendmail, which is typically used to do the work of mailing a message. It takes three parameters −
#
# The sender − A string with the address of the sender.
#
# The receivers − A list of strings, one for each recipient.
#
# The message − A message as a string formatted as specified in the various RFCs.

# To send the mail you use smtpObj to connect to the SMTP server on the local machine(if it is on the local machine)( smtpObj = smtplib.SMTP('localhost')) and
# then use the sendmail method along with the message, the from address,
# and the destination address as parameters (even though the from and to addresses are within the e-mail itself,
# these aren't always used to route mail).
#
# If you are not running an SMTP server on your local machine, you can use smtplib client to communicate
# with a remote SMTP server. Unless you are using a webmail service (such as Hotmail or Yahoo! Mail),
# your e-mail provider must have provided you with outgoing mail server details that you can supply them, as follows −

#smtplib.SMTP('mail.your-domain.com', 25)



if __name__=="__main__":
    wishme()
    while True:
    #if 1:
        query = takecommand().lower()

        #logic for executing tasks based on query
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia..")
            print(results)
            speak(results)
            
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "open geeksforgeeks" in query:
            webbrowser.open("geeksforgeeks.com")

        elif "open w3schools" in query:
            webbrowser.open("w3schools.com")

        elif "open github" in query:
            webbrowser.open("github.com")

        elif "open programiz" in query:
            webbrowser.open("programiz.com")

        elif "open coursera" in query:
            webbrowser.open("coursera.com")

        elif "open email" in query:
            webbrowser.open("gmail.com")
            
        elif "play music" in query:
            music_dir = 'C:\\Users\\54721\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif "the time" in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {time}")

        elif "open code" in query:
            path="C:\\Users\\54721\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif "email to arjun" in query:
            try:
                speak("what should i say?")
                content=takecommand()
                to="your email id@gmail.com"
                sentemail(to,content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("sorry,arjun..iam not able to sent this email")

        elif "finish" in query:
            exit()







