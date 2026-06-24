#Exercício 3: O Somador de Números Ímpares (Básico)
#Enunciado: Crie um programa que calcule e exiba a soma de todos os números ímpares que
#são múltiplos de 3 e que se encontram no intervalo de 1 até 100.

soma=0
for i in range (3 ,100,3 ) :
    if i %2 != 0:
        soma += i
print("A soma dos múltiplos de 3 é igual: ",  soma)
