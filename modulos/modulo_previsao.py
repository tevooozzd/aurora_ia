import requests
import speech_recognition as sr
import pyttsx3
import time


engine = pyttsx3.init()

def obter_localizacao_previsao_tempo():
    engine.say("Deseja obter pela sua localização?")
    engine.runAndWait()

    engine.say("Ou de outro lugar?")
    engine.runAndWait()
    time.sleep(0.6)
    engine.say("Caso seja de outro lugar, diga somente o nome da cidade ou país porfavor!")
    engine.runAndWait()

    reconhecer = sr.Recognizer()
    
    with sr.Microphone() as mic:
        reconhecer.adjust_for_ambient_noise(mic)
        print("SEXTA-FEIRA: Pode falar")
        audio = reconhecer.listen(mic)
        texto = reconhecer.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {texto}")
        
        if 'minha' in texto:  
            url = 'https://ipinfo.io/json'
            resposta = requests.get(url)
            if resposta.status_code == 200:
                dados = resposta.json()
                cidade = dados.get('city')
                return cidade
            else:
                print("SEXTA FEIRA: Não entendi ")
        else:
            return texto













def obter_previsao_tempo(localizacao, chave_api):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={localizacao}&appid={chave_api}&units=metric&lang=pt"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        temperatura = dados['main']['temp']
        descricao = dados['weather'][0]['description']

        print(f"SEXTA-FEIRA: Previsão do tempo em {localizacao}: {temperatura} graus Celsius, {descricao}.")
        
        engine.say(f"Previsão do tempo em {localizacao}: {temperatura} graus Celsius, {descricao}.")
        engine.runAndWait()

        time.sleep(0.7)

        engine.say("Deseja algo mais, caso sim, responda com sim?")
        engine.runAndWait()

        reconhecer = sr.Recognizer()
        with sr.Microphone() as microfone:
            reconhecer.adjust_for_ambient_noise(microfone)
            print("PODE FALAR")
            audio = reconhecer.listen(microfone, timeout=10)














            try:
                texto = reconhecer.recognize_google(audio, language='pt-BR')

                if 'sim' in texto:
                    print(f"VOCÊ DISSE: '{texto.upper()}', continuando...")
                    from entendendo_sexta import entender_user_sexta
                    entender_user_sexta()
                else:
                    entender_user_sexta()
                    print(f"VOCÊ DISSE: '{texto.upper()}', fechando sexta-feira...")
                    engine.say("Você disse 'não' ou não respondeu, parando a segunda-feira em 3 segundos")
                    return 
                
            except sr.UnknownValueError:
                seg_iniciada_erro = "Não entendi, tente novamente!"
                engine.say(seg_iniciada_erro)
                engine.runAndWait()



    else:
        print("Erro ao obter previsão do tempo:", resposta.status_code)










if __name__ == "__main__":
    chave_api = '6a8b46a1e363c39ece0c59e7de2d2d44'
    localizacao = obter_localizacao_previsao_tempo()
    if localizacao: 
        obter_previsao_tempo(localizacao, chave_api)
