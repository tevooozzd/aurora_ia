
################## - Importações das bibliotecas  #############################


import speech_recognition as sr
import pyttsx3
import time

########## - Mensagem do sistema para fala ########################
def mensagem_de_fala():
    print("=" * 30)
    print("SEXTA FEIRA: Pode falar!")
    print("=" * 30)







########## - Captura de som  ######################## (Ativa o microfone e reconhece a fala do usuario com o idioma 'pt-BR')

engine = pyttsx3.init()

def captura_som_sexta():
    reconhecer = sr.Recognizer()
    with sr.Microphone() as microfone:
        reconhecer.adjust_for_ambient_noise(microfone)

        for x in range(2):
            mensagem_de_fala()

            try:

                audio = reconhecer.listen(microfone, timeout=8, phrase_time_limit=8)
                texto = reconhecer.recognize_google(audio, language='pt-BR').lower()
                verificacao_som_sexta(texto)  
                break  





################# - Sistema de erros na captura de som #################### (Caso não capture o som, ou não entender a fala)
            except sr.WaitTimeoutError:

                if x == 0: 

                    print("SISTEMA: O sistema da sexta-feira foi ativado, mas não houve o reconhecimento de som, você tem mais uma tentativa!")
                    engine.say("O sistema da sexta-feira foi ativado, mas não houve o reconhecimento de som, você tem mais uma tentativa!")
                    time.sleep(1)

                elif x == 1:
                    print("SISTEMA: Não houve reconhecimento de som nas tentativas. Por favor, tente novamente mais tarde, ou inicie novamente!")
                    engine.say("Não houve reconhecimento de som nas tentativas. Por favor, tente novamente mais tarde, ou inicie novamente!")
                    time.sleep(1)
                engine.runAndWait()


            except sr.UnknownValueError:

                if x == 0:
                    print("SISTEMA: O sistema da sexta-feira foi ativado, porém não foi identificado o som, você tem mais uma tentativa!")
                    engine.say("O sistema da sexta-feira foi ativado, porém não foi identificado o som, você tem mais uma tentativa!")
                    engine.runAndWait()

                elif x == 1:
                    print("SISTEMA: Não houve o entendimento do som nas tentativas. Por favor tente novamente mais tarde, ou incie o progama novamente")
                    engine.say("SISTEMA: Não houve o entendimento do som nas tentativas. Por favor tente novamente mais tarde, ou incie o progama novamente")
                    engine.runAndWait()







########## - Verificação de som ######################## (Verificar se o chamado pelo nome da IA aconteceu, para não ativar por qualquer coisa, como o da SIRI)



verificacao_sexta = {
    'sexta', 'sexta feira', 'cesta', 'ceista',
}




def verificacao_som_sexta(texto):  

        if any(palavra in texto for palavra in  verificacao_sexta):
            from second import entendendo_frase_sexta
            entendendo_frase_sexta(texto)
        else:
            
            print("SISTEMA: Se você está tentando utilizar a SEXTA-FEIRA, chame ela pelo nome, vamos tentar novamente!")
            engine.say("Se você está tentando utilizar a SEXTA-FEIRA, chame ela pelo nome, vamos tentar novamente!")
            engine.runAndWait()

            captura_som_sexta()

captura_som_sexta()




