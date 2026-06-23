#Exercício 7: Analisador de Triângulos
#Enunciado: Para exercitar a lógica matemática, peça para o usuário digitar o comprimento de três retas (A, B e C).
#Primeiro, o programa deve verificar se essas retas podem formar um triângulo
#(Regra: a soma de dois lados deve ser sempre maior que o terceiro).
#Se formarem, o programa deve usar o elif para dizer que tipo de triângulo
#ele é: • Equilátero: todos os lados iguais. •
#Isósceles: dois lados iguais.
#• Escaleno: todos os lados diferentes.

a=float(input("Digite o cumprimento A :"))
b=float(input("Digite o cumprimento B :"))
c=float(input("Digite o cumprimento C :"))

if a + b > c and b + a > c and c + a > c :
    print("Forma um triângulo.")
    if a == b == c:
        print("Triângulo equilátero.")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles.")
    else:
        print("Triângulo escaleno.")
else:
    print("As retas não podem formar um triângulo.")

