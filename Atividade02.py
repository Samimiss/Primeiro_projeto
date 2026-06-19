#Exercício 2: Radar de Velocidade Eletrônico
#Enunciado: Desenvolva um script que leia a velocidade de um carro em km/h. Se o carro ultrapassar 80 km/h,
#exiba uma mensagem dizendo que ele foi multado. Se ele estiver dentro do limite, exiba uma mensagem de "Boa viagem,
#dirija com segurança!".

velocidade=float(input("Velocidade do carro (km/h): "))


if velocidade > 80:
    print("Você vacilou. Multa!")
else:
    print("Boa viagem, dirija com segurança! ")