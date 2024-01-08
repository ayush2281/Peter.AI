import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data) 
            return data  # Return the recognized text
        except sr.UnknownValueError:
            print("Not Understanding")
            # return "data"

def speechtxt(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 165)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    data1 = sptext().lower()  # Call sptext once and store the result
    
    if "hello peter" in data1:
        name = "hello ayush"
        speechtxt(name)
    elif "how old are you" in data1:
        age="you are 21 year old" 
        print(age)
        speechtxt(age)   
    elif "i am talking about your age" in data1:
        age  = "I don't have a specific age, but I'm always evolving with each interaction, just like fine wine getting better over time"
        print(age) 
        speechtxt(age)
    elif 'time' in data1 and data1:
        time = datetime.datetime.now().strftime("%I-%M-%p")
        speechtxt(time)
    elif 'youtube' in data1:
        webbrowser.open("https://www.youtube.com/watch?v=LsUdoy7EH7M")
    
    elif 'instagram'in data1:
        webbrowser.open("https://www.instagram.com/ayush_rathod1299/?hl=en")
    elif "joke" in data1:
        joke_1=pyjokes.get_joke(language="en",category="neutral")
        print(joke_1)
        speechtxt(joke_1)
        
        



    


    # else:
        # print("Thank you")

