import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import smtplib
import time
import pyjokes
import pyautogui

# Initialize TTS engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Could not connect to the internet.")
        return ""

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_password")  # Replace with your actual email and app password
    server.sendmail("your_email@gmail.com", to, content)
    server.quit()

def process_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "open" in command:
        if "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "github" in command:
            speak("Opening GitHub")
            webbrowser.open("https://www.github.com")
        elif "facebook" in command:
            speak("Opening facebook")
            webbrowser.open("https://www.facebook.com")
        else:
            speak("Which website do you want to open?")

    elif "launch" in command:
        if "notepad" in command:
            speak("Launching Notepad")
            os.system("notepad.exe")
        elif "calculator" in command:
            speak("Launching Calculator")
            os.system("calc.exe")
        else:
            speak("Application not recognized.")

    elif "play music" in command:
        speak("What music would you like to play?")
        music_query = listen()
        if music_query:
            speak(f"Playing {music_query} on YouTube.")
            webbrowser.open(f"https://www.youtube.com/results?search_query={music_query}")
        else:
            speak("I didn't catch the song name.")


    elif "remind me" in command:
        speak("What should I remind you about?")
        reminder = listen()
        speak("In how many seconds?")
        try:
            seconds = int(listen())
            speak(f"Reminder set for {seconds} seconds.")
            time.sleep(seconds)
            speak(f"Reminder: {reminder}")
        except:
            speak("Sorry, I couldn't set the reminder.")

    elif "calculate" in command:
        speak("What should I calculate?")
        question = listen()
        try:
            result = eval(question)
            speak(f"The answer is {result}")
        except:
            speak("I couldn't calculate that.")

    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)

    elif "type" in command:
        text = command.replace("type", "").strip()
        if text:
            speak("Typing now.")
            pyautogui.write(text)
        else:
            speak("What should I type?")

    elif "exit" in command or "quit" in command:
        speak("thankyou for connecting us")
        exit()

    else:
        speak("I didn't understand that command.")

# Main Loop
if __name__ == "__main__":
    speak("Hello! I am your friend aman .")
    while True:
        command = listen()
        if command:
            process_command(command)
