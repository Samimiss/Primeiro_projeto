#Exercício 3: Classificador de Temperatura
#Enunciado: Crie um programa que receba a temperatura atual de uma cidade (em graus Celsius)
#e classifique o clima baseado nas regras abaixo usando
# if, elif e else: • Menor que 15°C: "Clima Frio"• Entre 15°C e 25°C: "Clima Agradável"• Maior que 25°C: "Clima Quente"


temp_atual=float(input("Temperatura da cidade: "))

if temp_atual < 15:
    print("Clima frio!!")
elif temp_atual >= 15 and temp_atual < 25:
    print("Clima agradável!")

else :
    print("Clima Quente!!!")

