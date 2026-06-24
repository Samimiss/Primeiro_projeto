#Exercício 2: Contador de Intervalos Customizado (Básico)
#Enunciado: Escreva um script que solicite três valores ao usuário: um valor inicial,
#um valor final e um valor de passo (de quanto em quanto a contagem deve andar).
#Use o laço for para exibir a contagem na tela.
#Exemplo: Inicial: 2, Final: 12, Passo: 3. Saída: 2, 5, 8, 11.

num = int(input("Digite o número inicial: "))
final= int(input("Digite o número final: "))
passos= int(input("Digite o número de passos: "))


for i in range (num, final +1 , passos) :
    print(f"{i}")
