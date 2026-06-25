#Exercício 1: O Contador Regressivo de Lançamento (while)
#Enunciado: Crie um script que simule a contagem regressiva para o lançamento de um foguete.
#O programa deve começar em 10 e ir até 0, aguardando 1 segundo entre cada número (Dica: use a função time.sleep(1)
#da biblioteca time). Ao final, exiba a mensagem: "Decolar!".
import time as tm


cont_reg = 10
while True:
    print(cont_reg)
    if cont_reg == 0:
        print('decolar!')
        break
    cont_reg = cont_reg -1
    tm.sleep(1)
