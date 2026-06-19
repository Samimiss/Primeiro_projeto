#Exercício 5: Análise de Crédito Bancário Simplificada
#Enunciado: Um banco precisa automatizar a aprovação de empréstimos.
#Crie um script que receba o salário bruto de um cliente e o valor da parcela do empréstimo que ele deseja pagar.
#O empréstimo só pode ser aprovado se o valor da parcela não ultrapassar 30% do salário bruto do cliente.
#Use if/else para exibir o resultado ("Crédito Aprovado" ou "Crédito Recusado").

salario=float(input("digite seu salário: "))
parcela=float(input("Digite a parcela: "))

limite= 0.3 * salario
if parcela <= limite :
    print("Aprovado!!")
else:
    print("Crédito recusado!")