import speech_recognition as sr
import os
import time
import webbrowser
from gtts import gTTS
import pyttsx3



########################################################
pesquisar_e_sinonimos = [
    "pesquisar", "pesquisa", "pesquise",
    "buscar", "busque", "busca",
    "procurar", "procure", "procura",
    "encontrar", "encontre", "encontra",
    "investigar", "investigue", "investiga",
    "analisar", "analise", "analisa",
    "examinar", "examine", "examina",
    "estudar", "estude", "estuda",
    "consultar", "consulte", "consulta",
    "explorar", "explore", "explora",
    "averiguar", "averigüe", "averigua"
]

########################################################


########################################################
def start_iris():
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Pode falar")
        audio = rec.listen(mic)

    try:
        texto = rec.recognize_google(audio, language='pt-BR').lower()
        if 'segunda' in texto:
            os.system('cls' if os.name == 'nt' else 'clear')
            iris_start_answer = "Segunda-feira está ativa agora, vamos prosseguir!"
            engine = pyttsx3.init()
            engine.setProperty('voice', engine.getProperty('voices')[0].id)
            engine.say(iris_start_answer)
            engine.runAndWait()
            return True
    except sr.UnknownValueError:

        iris_start_error = "Não entendi, tente novamente!"
        engine = pyttsx3.init()
        engine.setProperty('voice', engine.getProperty('voices')[0].id)
        engine.say(iris_start_error)
        engine.runAndWait()
        return False

st_au = start_iris()

########################################################

def understanding_user_iris():

    au_start_answer = "Como posso te ajudar chefe?!"

    engine = pyttsx3.init()
    engine.setProperty('voice', engine.getProperty('voices')[0].id)
    engine.say(au_start_answer)
    engine.runAndWait()

    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Pode falar")
        audio = rec.listen(mic)
    try:
        texto = rec.recognize_google(audio, language='pt-BR').lower()
        return texto
    except sr.UnknownValueError:
        iris_start_error = "Não entendi, tente novamente!"
        engine = pyttsx3.init()
        engine.setProperty('voice', engine.getProperty('voices')[0].id)
        engine.say(iris_start_error)
        engine.runAndWait()
        return ''

und_user_au = ''
if st_au:
    und_user_au = understanding_user_iris()
    print(und_user_au)



########################################################

def search_aurora(searchi):
    iris_search_voice = "Vamos achar isso para você!"
    engine = pyttsx3.init()
    engine.setProperty('voice', engine.getProperty('voices')[0].id)
    engine.say(iris_search_voice)
    engine.runAndWait()
    url = f"https://www.google.com/search?q={searchi}"
    webbrowser.open(url)


search_term = ""
if und_user_au:
    for sinonimo in pesquisar_e_sinonimos:
        if sinonimo in und_user_au:
            search_term = und_user_au.split(sinonimo, 1)[-1].strip()
            if search_term:  
                search_aurora(search_term)
            break

