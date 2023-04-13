import time


def contagem_regressiva(segundos):

    while segundos > 0:
        
        minutes = int(segundos / 60)     

        seconds = int(segundos % 60)

        cronometro = f'{minutes} : {seconds}'

        print(cronometro)#, end='\r')

        time.sleep(1)
    
        segundos -= 1
    
    print("Tempo esgotado!")




segundos = input("Digite aqui o tempo em segundos: ")

contagem_regressiva(int(segundos))



