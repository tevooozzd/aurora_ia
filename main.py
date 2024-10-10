import speech_recognition as sr
import pyttsx3
from main_iniciando import iniciando_sexta_feira



engine = pyttsx3.init()

def iniciar_sexta_feira():
    reconhecer_fala = sr.Recognizer()
    with sr.Microphone() as microfone:
        reconhecer_fala.adjust_for_ambient_noise(microfone)
        print("SEXTA FEIRA: Pode falar!")
        audio = reconhecer_fala.listen(microfone)

        try:
            texto = reconhecer_fala.recognize_google(audio, language='pt-BR')
            print(f"VOCÊ DISSE: {texto}")
            iniciando_sexta_feira(texto)  
        except sr.UnknownValueError:
            erro_segunda_feira()

def erro_segunda_feira():
    seg_iniciar_erro = "Nao entendi!"
    engine.say(seg_iniciar_erro)
    print(f"SEXTA FEIRA: Não entendi!")
    engine.runAndWait()

iniciar_sexta_feira()
