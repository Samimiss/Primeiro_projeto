#Exercício 7: Analisador de Triângulos
#Enunciado: Para exercitar a lógica matemática, peça para o usuário digitar o comprimento de três retas (A, B e C).
#Primeiro, o programa deve verificar se essas retas podem formar um triângulo
#(Regra: a soma de dois lados deve ser sempre maior que o terceiro).
#Se formarem, o programa deve usar o elif para dizer que tipo de triângulo
#ele é: • Equilátero: todos os lados iguais. •
#Isósceles: dois lados iguais.
#• Escaleno: todos os lados diferentes.

ra=float(input("Digite o cumprimento A :"))
rb=float(input("Digite o cumprimento B :"))
rc=float(input("Digite o cumprimento C :"))

if ra + rb > rc and rb + ra > rc and rc + ra > rc :
    print("Forma um triângulo.")
    if ra == rb and rb == rc and rc == ra:
        print("Equilátero.")
