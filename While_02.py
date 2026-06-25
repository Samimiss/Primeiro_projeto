# Exercício 2: Somador de Números até o Zero (while)
# Enunciado: Desenvolva um programa que peça para o usuário digitar vários números inteiros. O programa deve somar
# todos esses números. A repetição só deve parar quando o usuário digitar exatamente o número 0.
# No final, exiba a soma total.

n = 0
while True:
    n1 = int(input('digite um numero: '))
    if n1 == 0:
        break
    else:
        n = n + n1

print(n)