# Calculadora python

num1 = int(input("Digite o primeiro numero: "))

num2 = int(input("Digite o segundo numero: "))

soma= num1 + num2
print(f"A soma de {num1} e {num2} é igual a = {soma}")
subtracao = num1 - num2
print(f"{num1} - {num2} é igual a = {subtracao}")
multiplicacao = num1 * num2
print(f"{num1} vezes o {num2} é igual a = {multiplicacao}")
divisao = num1 / num2
print(f"{num1} dividido por {num2} é igual a = {divisao:.3f}")
divisao_inteira = num1 // num2
print(f"{num1} e {num2} = {divisao_inteira}")
resto_divisao = num1 % num2
print(f"{num1} e {num2} = {resto_divisao}")
potenciacao = num1  ** num2
print(f"{num1} e {num2} = {potenciacao}")

