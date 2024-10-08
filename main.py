import speech_recognition as sr
import time


def start_aurora():
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Fale em 3...")
        time.sleep(1)
        print("Fale em 2...")
        time.sleep(1)
        print("Fale em 1...")
        time.sleep(1)
        audio = rec.listen(mic)

    try:
        texto = rec.recognize_google(audio, language='pt-BR')
        texto = texto.lower()
        print(f"Você disse: {texto}")
        return texto  # Retorna o texto para uso posterior
    except sr.UnknownValueError:
        print("Não entendi.")
        return ""
    except sr.RequestError:
        print("Erro ao conectar ao serviço de reconhecimento.")
        return ""


start_aurora()





