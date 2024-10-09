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
            au_start_answer = "Aurora está ativa agora, como posso ajudar?!"
            engine = pyttsx3.init()
            engine.setProperty('voice', engine.getProperty('voices')[0].id)
            engine.say(au_start_answer)
            engine.runAndWait()
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


und_user_au = ''
if st_au:
    und_user_au = understanding_user_aurora()
    if und_user_au:
        print(f"User input: {und_user_au}")




def search_aurora(searchi):
    print("Lets search this for you my brother!")
    time.sleep(1.5)
    url = f"https://www.google.com/search?q={searchi}"
    webbrowser.open(url)


search_term = ''
if und_user_au:
    for sinonimo in pesquisar_e_sinonimos:
        if sinonimo in und_user_au:
            search_term = und_user_au.split(sinonimo, 1)[-1].strip() 
            if search_term: 
                search_aurora(search_term)
            break 
