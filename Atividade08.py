#Exercício 8: Calculadora de Desconto de Black Friday
#Enunciado: Uma loja de departamento está aplicando descontos progressivos baseados no valor total da compra do cliente.
#Escreva um script que leia o valor total das compras e aplique o desconto correto usando a estrutura condicional:
#• Compras até R$ 100,00: Sem desconto.
#• Compras de R$ 100,01 até R$ 300,00: 5% de desconto.
#• Compras de R$ 300,01 até R$ 500,00: 10% de desconto.
#• Compras acima de R$ 500,00: 15% de desconto.
#Ao final, exiba o valor original, o valor do desconto aplicado e o total a pagar com desconto.

valor_total=float(input("Digite o valor da compra: "))

if valor_total <= 100:
    print("Sem desconto.")

elif valor_total > 100 and valor_total <= 300:
    desconto = (valor_total * 0.05)
    desconto = (valor_total - desconto)
    print(f"Valor original: {valor_total:.2f}, valor com desconto: {desconto:.2f}")
elif valor_total > 300 and valor_total <= 500:
    desconto = (valor_total * 0.10)
    desconto = (valor_total - desconto)
    print(f"Valor original: {valor_total:.2f}, valor com desconto: {desconto:.2f}")
else:
    desconto = (valor_total * 0.15)
    desconto = (valor_total - desconto)
    print(f"Valor original: {valor_total:.2f}, valor com desconto: {desconto:.2f}")