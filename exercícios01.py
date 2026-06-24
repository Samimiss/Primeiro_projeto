#Exercício 1: A Tabuada Automatizada (Básico)
#Enunciado: Desenvolva um programa que peça para o usuário digitar um número inteiro. Utilizando o laço for e
# a função range(), exiba a tabuada desse número de 1 a 10 no terminal.
#Exemplo de saída esperada: 5 x 1 = 5, 5 x 2 = 10...

num = int(input("Digite um número: "))
print("Tabuada")

for i in range (1 , 11) :
     print(f"{num} x {i} = {num*i}")