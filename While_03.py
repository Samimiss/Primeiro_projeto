# Exercício 3: Menu Interativo de Sistema (Simulando do while)
# Enunciado: Crie um menu interativo de calculadora utilizando while True. O programa deve exibir na tela:
# Somar
# Subtrair
# Multiplicar
# Dividir
# Sair
# O programa deve executar a ação escolhida e mostrar o menu novamente. Ele só deve encerrar de verdade quando o usuário digitar a opção 3.

while True:
    print('''
digite dois numeros e selecione as operações
(+,-,*,/)
    ''')
    n1 = int(input('digite um numero: '))
    n2 = int(input('digite um numero: '))
    op = input('selecione a operação: ')
    if op == '+':
        print(n1+n2)
    elif op == '-':
        print(n1-n2)
    elif op == '*':
        print(n1*n2)
    elif op == '/':
        print(n1/n2)
    s = input('deseja sair (s/n): ')
    if s == 's':
        break
