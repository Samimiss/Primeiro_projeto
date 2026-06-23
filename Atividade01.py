# Exrcicio número 1:
#O Verificador de ParidadeEnunciado: Escreva um programa que receba um número inteiro do usuário. Utilizando a estrutura if/else,
# verifique se o número é Par ou Ímpar e exiba uma mensagem correspondente no terminal.
from queue import PriorityQueue

#Dica: Use o operador de módulo % para verificar o resto da divisão por 2.


num=int(input("Digite o número: "))
if num % 2 == 0 :
    print("Este número é par!")
else:
    print("Este número é ímpar!")
