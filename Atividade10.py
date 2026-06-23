#Exercício 10: O Cálculo do IMC com Diagnóstico Completo
#Enunciado: Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
#O script deve pedir o peso (em kg) e a altura (em metros). O cálculo é feito pela
#fórmula: IMC = peso / (altura * altura) . Após calcular o valor do IMC, utilize uma estrutura encadeada de
#if/elif/else para exibir o diagnóstico exato: • Abaixo de 18.5: Abaixo do peso• Entre 18.5 e 24.9: Peso ideal (parabéns)
#• Entre 25.0 e 29.9: Levemente acima do peso• Entre 30.0 e 34.9: Obesidade Grau I• Acima de 35.0: Obesidade Severa/Mórbida

peso=float(input("Digite seu peso: "))
alt=float(input("Digite sua altura: "))

imc= (peso / alt * alt)

if imc < 18.5:
    print("Abaixo do peso...Vai sair voando!")
elif imc > 18.5 and imc >= 24.9:
    print("Peso ideal...Parabéns!!!")
elif imc > 25.0 and imc >= 29.9:
    print("Levemente acima do peso...")
elif imc > 30.0 and imc >= 34.9 :
    print("Obesidade grau I")
else:
    print("Obesidade severa/ mórbida...")
