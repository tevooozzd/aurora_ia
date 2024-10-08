import speech_recognition as sr
import os
import time
import webbrowser





def start_aurora():
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        audio = rec.listen(mic)

    try:
        texto = rec.recognize_google(audio, language='pt-BR').lower()
        if 'aurora' in texto:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Aurora, is ONLINE!")
            time.sleep(1)
            print("Let's go!")
            return texto.upper 
    except sr.UnknownValueError:
        print("I don't understand sorry.")
        return ""








def understanding_user_aurora():
    print("How can i help boss?")
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        audio = rec.listen(mic)


    try:
        texto = rec.recognize_google(audio, language='pt-BR').lower()
        time.sleep(1)
        print(f"You said  {texto.upper()}")
    except sr.UnknownValueError:
        print("I don't understand sorry.")
        return ""
