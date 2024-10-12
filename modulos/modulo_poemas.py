import pyttsx3
import speech_recognition as sr
import webbrowser
import requests
from bs4 import BeautifulSoup
import time



temas_poemas = { 
    "amor": "", "felicidade": "", "solidão": "", 
    "natureza": "", "esperança": "", "saudade": "", 
    "liberdade": "", "tempo": "", "amizade": "", 
    "luta": "", "tristeza": "", "sonhos": "", 
    "música": "", "mudança": "", "mistério": "", 
    "paz": "", "coragem": "", "destino": "", 
    "aventura": "", "conhecimento": "", "sinceridade": "",
    "nostalgia": "", "futuro": "", "memórias": "", 
    "silêncio": "", "criação": "", "reflexão": "", 
    "crescimento": "", "solidariedade": "", "sensibilidade": "", 
    "luz": "", "escuridão": "", "verdade": "", 
    "justiça": "", "maturidade": "", "harmonia": "", 
    "tradição": "", "transformação": "", "união": "", 
    "insegurança": "", "força": "", "sabedoria": "", 
    "superação": "", "determinação": "", "esperança": "", 
    "autenticidade": "", "fidelidade": "", "comunidade": "", 
    "sustentabilidade": "", "tolerância": "", "crescimento pessoal": "",
    "compaixão": "", "gratidão": "", "alegria": "", 
    "autoestima": "", "inspiração": "", "tranquilidade": "",
    "conexão": "", "foco": "", "perseverança": "", 
    "bondade": "", "resiliência": "", "liberdade de expressão": "",
    "solidariedade": "", "autoajuda": "", "empatia": "",
    "transformação pessoal": "", "equilíbrio": "", "realização": "",
    "reflexão interior": "", "esperança renovada": ""
}

###############################################################



repeticao = {
    'sim',
    'por favor',
    'porfavor',
    'recite',
    'recitar',
    'recita',
    'obvio',
    'concerteza'
    
}















engine = pyttsx3.init()








#################################################################################



def entendendo_escolhapoema():
########################################################### - Mensagem de início perguntando sobre qual tipo o usúario quer
    engine.say("Que tipo de poema você deseja?")
    engine.runAndWait()
    print("SEXTA FEIRA: Que tipo de poema você deseja?")

########################################################## - Captação do audio
    reconhecer = sr.Recognizer()
    with sr.Microphone() as microfone:
        reconhecer.adjust_for_ambient_noise(microfone)
        print("SEXTA FEIRA: Pode falar!")
        audio =  reconhecer.listen(microfone)

#################################################### - Se tiver qualquer (tema) no texto, vai redirecionar para o recitando poemas

        try:
                    texto = reconhecer.recognize_google(audio, language = 'pt-BR').lower()
                    print(f"VOCÊ DISSE: {texto}")

                    if any(palavra in texto for palavra in temas_poemas):
                        recitando_poemas(texto)

                    else:
                        engine.say("Desculpa, não entendi, você deseja que eu recite um poena ou faça uma pesquisa sobre poema?")
                        engine.runAndWait()

                        print("SEXTA FEIRA: Desculpa, não entendi, você deseja que eu recite um poena ou faça uma pesquisa sobre poema?")
                        return


        except sr.UnknownValueError:
            iniciando_entendimento_poema_erro = "Desculpa, não entendi!"
            engine.say(iniciando_entendimento_poema_erro)
            engine.runAndWait()





############################################################################ - Pega o input do usuario sobre qual tema ele quer (texto)

def recitando_poemas(texto):

############################################################## - Transforma espaços em branco em ' _ ', e faz a requisição para o
    texto_formatado = texto.replace(" ", "_")  
    url = f'https://www.pensador.com/{texto_formatado}/'
    header = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0 (Edition std-2)'}
    resposta = requests.get(url, headers=header)



############################################## - Se a requisição for igual a (200) ou ("SIM") vai entrar no site e pegar as frases
    if resposta.status_code == 200:  

        site = BeautifulSoup(resposta.text, 'html.parser')
        leitura_poema = site.find_all('p', class_='frase fr0')
        leitura_autor = site.find_all('span', class_='author-name')
        poemas_recitados = set()

############################################## - Pega os poemas e fala

        for poema, autor in zip(leitura_poema, leitura_autor):
            resultado_autor = f"Poema do autor: `{autor.get_text()}"
            resultado_poema = f"{poema.get_text()}"

######################################################################
            if resultado_poema not in poemas_recitados:  

                print(f"SEXTA FEIRA: {resultado_autor}, {resultado_poema}")
                
                engine.say(f"{resultado_autor}")
                engine.runAndWait()

                engine.say(f"{resultado_poema}")
                engine.runAndWait()
#####################################################################################

                poemas_recitados.add(resultado_poema)

                time.sleep(1)
                engine.say("Deseja que eu recite outro?")
                engine.runAndWait()
####################################################

                reconhecer = sr.Recognizer()
                with sr.Microphone() as microfone:
                    reconhecer.adjust_for_ambient_noise(microfone)
                    audio = reconhecer.listen(microfone)

########################################################


                try:
                    texto = reconhecer.recognize_google(audio, language='pt-BR').lower()

                    if any(palavra in texto for palavra in repeticao):
                        entendendo_escolhapoema()

                    else:
                        break


                except sr.UnknownValueError:
                    engine.say("Desculpa, não entendi!")
                    engine.runAndWait()

#######################################################################

            else:
                print("Esse poema já foi recitado, procurando outro...")
                continue

    else:
        engine.say(f"Erro ao acessar o site: {resposta.status_code}")
        engine.runAndWait()


