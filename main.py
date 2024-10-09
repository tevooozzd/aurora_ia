import speech_recognition as sr
import os
import webbrowser
import pyttsx3

########################################################
pesquisar_e_sinonimos = {
    'sobre': 1.8,
    'me ajude a encontrar': 1.9,

    'pesquisar': 1.0,
    'pesquise': 1.0,
    'pesquisa': 1.0,

    'buscar': 1.1,
    'busca': 1.1,
    'busque': 1.1,

    'procurar': 1.2,
    'procura': 1.2,
    'procure': 1.2,

    'encontrar': 1.3,
    'encontre': 1.3,
    'encontra': 1.3,

    'investigar': 1.4,
    'investigue': 1.4,
    'investiga': 1.4,

    'analisar': 1.5,
    'analise': 1.5,
    'analisa': 1.5,

    'consultar': 1.6,
    'consulte': 1.6,
    'consulta': 1.6,
}

########################################################


########################################################



########################################################





########################################################
def start_iris():
    rec = sr.Recognizer() 
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print("SEXTA-FEIRA: Pode falar")
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language='pt-BR').lower()
        print(f"Você disse: {texto}")
        print('----------------------------------------------')
    try:
        if any(palavra in texto for palavra in dic_start_seg):
            iris_start_answer = "Sexta-feira está ativa agora, vamos prosseguir!"
            print(f'{iris_start_answer.upper()} \nAGUARDE ATE A MENSAGEM DE VOZ TERMINAR!')
            print('----------------------------------------------')
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
        print("SEXTA-FEIRA: Pode falar")
        audio = rec.listen(mic)
    try:
        texto = rec.recognize_google(audio, language='pt-BR').lower()
        print(f"VOCÊ DISSE: {texto}")
        print('----------------------------------------------')
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


########################################################

def search_aurora(searchi):

    iris_search_voice = "Você deseja que eu leia, ou te redirecione para a aba? (Responde com leia ou  redirecione)"
    engine = pyttsx3.init()
    engine.setProperty('voice', engine.getProperty('voices')[0].id)
    engine.say(iris_search_voice)
    engine.runAndWait()

    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print("SEXTA FEIRA: Pode Falar")
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language='pt-BR').lower()
    if 'leia' in texto:
        print(f"VOCÊ DISSE: {texto}")
    elif 'redirecione' in texto:
        print(f"VOCÊ DISSE: {texto}")
        webbrowser.open(f"https://www.google.com/search?q={searchi}")

search_term = ""

if und_user_au:
    for sinonimo in pesquisar_e_sinonimos:
        if sinonimo in und_user_au:
            search_term = und_user_au.split(sinonimo, 1)[-1].strip()
            if search_term:
                for social in sociais:
                    if search_term.endswith(social):
                        search_term = search_term[:-len(social)].strip()  
                        break  

                search_term = search_term.lstrip(',').strip() 
                search_aurora(search_term)
            break
