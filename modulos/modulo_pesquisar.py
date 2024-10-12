import requests
import speech_recognition as sr
import pyttsx3
from bs4 import BeautifulSoup
import webbrowser
from googlesearch import search



def pesquisar_sexta(pesquisarsite):

    segunda_pesquisar_voz = "Você deseja que eu leia, ou te redirecione para a aba? (Responde com leia ou redirecione)"

    engine = pyttsx3.init()
    engine.setProperty('voice', engine.getProperty('voices')[0].id)
    engine.say(segunda_pesquisar_voz)
    engine.runAndWait()

    receconhecer = sr.Recognizer()
    with sr.Microphone() as mic:
        receconhecer.adjust_for_ambient_noise(mic)
        print("SEXTA FEIRA: Pode Falar")
        audio = receconhecer.listen(mic)
        texto = receconhecer.recognize_google(audio, language='pt-BR').lower()
    
        if 'leia' in texto:
            print(f"VOCÊ DISSE: {texto}")
            for url in search(pesquisarsite, num_results=1):

                print('--------------------------------------------------')
                print(f"Pesquisando sobre: {texto}")
                ler_site(url)
                return
            
        elif 'redirecione' in texto:
            print(f"VOCÊ DISSE: {texto}")
            webbrowser.open(f"https://www.google.com/search?q={pesquisarsite}")
            return


def ler_site(url):
    try:
        resposta = requests.get(url)
        resposta.raise_for_status() 
        sopa = BeautifulSoup(resposta.text, 'html.parser')
        

        paragrafos = sopa.find_all('p')
        
        texto = ' '.join(paragrafo.get_text(strip=True) for paragrafo in paragrafos)

        if texto:
            engine = pyttsx3.init()
            engine.say(texto)
            engine.runAndWait()
        else:
            print("Nenhum parágrafo encontrado.")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site: {e}")

########################################################
