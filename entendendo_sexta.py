import speech_recognition as sr
from bs4 import BeautifulSoup
import pyttsx3
from googlesearch import search
import time
########################################################


# BIBLIOTECA DE PALAVRAS CHAVES PARA PERGUNTAS, DÚVIDAS, QUESTÕES, CURIOSIDADES E ETC

pesquisar_e_sinonimos = {
    'oque'
    'quem'
    'quanto'
    'o que'
    'quando'
    'sobre': 1.8,
    'me ajude a encontrar': 1.9,
    'para mim': 1.9,
    'para': 1.9,
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
    'investigar': 1.4,
    'analisar': 1.5,
    'consultar': 1.6,
}

########################################################

# BIBLIOTECA DE PALAVRAS CHAVES PARA INICIAR O PROGRAMA

dic_iniciar_seg = { 
    'cesta': 0,
    'sexta ': 0,
    'sexta-feira': 0,
    'sexta': 0,
}

########################################################

# BIBLIOTECA DE PALAVRAS CHAVES PARA QUESTÕES SOCIAIS (EDUCAÇÃO, PEDI FAVORES ETC)

sociais = {
    'por favor': 1.6,
    'com licença': 1.6,
    'obrigado': 1.7,
    'obrigada': 1.7,
    'por gentileza': 1.6,
    'por obséquio': 1.6,
}

########################################################
previsao_tempo = {
    'qual é a previsão': 1.8,
    'previsão': 1.9,
    'tempo para hoje': 1.7,
    'vai chover hoje?': 1.6,
    'como está o clima?': 1.8,
    'qual a temperatura?': 1.5,
    'está frio lá fora?': 1.6,
    'como vai estar amanhã?': 1.7,
    'algum alerta de tempestade?': 1.9,
    'vai fazer sol hoje?': 1.5,
    'como será o clima esta semana?': 1.7,
}






########################################################


engine = pyttsx3.init()

def entender_user_sexta():
    time.sleep(0.6)
    engine.say("Como posso ajudar chefe?")
    engine.runAndWait()




    reconhecer = sr.Recognizer()
    with sr.Microphone() as mic:
        reconhecer.adjust_for_ambient_noise(mic)
        print("SEXTA-FEIRA: Pode falar")
        audio = reconhecer.listen(mic)
    try:
        texto = reconhecer.recognize_google(audio, language='pt-BR').lower()
        print(f"VOCÊ DISSE: {texto}")
        print('----------------------------------------------')

        for palavra in sociais:
            texto = texto.replace(palavra, '')




        if any(palavra in texto for palavra in previsao_tempo):
            from modulo_previsao import obter_localizacao_previsao_tempo
            obter_localizacao_previsao_tempo()

        elif any(palavra in texto for palavra in pesquisar_e_sinonimos):
            for sinonimo in pesquisar_e_sinonimos:
                if sinonimo in texto:
                    from modulo_pesquisar import pesquisar_sexta
                    pesquisar_sexta(texto)





    except sr.UnknownValueError:
        seg_iniciada_erro = "Não entendi, tente novamente!"
        engine.say(seg_iniciada_erro)
        engine.runAndWait()
        return ''
    
if __name__ == "__main__":
    entender_user_sexta()
