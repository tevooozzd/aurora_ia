
from datetime import datetime
import pyttsx3
from entendendo_sexta import entender_user_sexta

# BIBLIOTECA DE PALAVRAS CHAVES PARA INICIAR O PROGRAMA
dic_iniciar_seg = { 
    'cesta': 0,
    'sexta ': 0,
    'sexta-feira': 0,
    'sexta': 0,
}

engine = pyttsx3.init()

def iniciando_sexta_feira(texto):
    
    if any(palavra in texto for palavra in dic_iniciar_seg):
        saudacao = saudacao_por_hora()
        agora = datetime.now()
        horario = agora.strftime("%H horas e %M minutos")

        engine.say(f"{saudacao} SEXTA-FEIRA ESTÁ ATIVA!")
        engine.runAndWait()

        engine.say(f"Agora são {horario}")
        engine.runAndWait()

        entender_user_sexta()

    else:
        seg_iniciada_erro = "Se você está tentando falar comigo, me chame pelo nome e aguarde!"
        engine.say(seg_iniciada_erro)
        engine.runAndWait()

def saudacao_por_hora():
    agora = datetime.now()
    hora = agora.hour
    if 5 <= hora < 12:
        return "Bom dia!"
    elif 12 <= hora < 18:
        return "Boa tarde!"
    else:
        return "Boa noite"

