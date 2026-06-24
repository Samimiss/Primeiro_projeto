#Exercício 4: Verificador de Maioridade da Turma (Intermediário)
#Enunciado: Desenvolva um programa que leia o ano de nascimento de 7 pessoas. Utilizando o for, o programa deve calcular
# a idade de cada uma com base no ano atual (2026) e, no final, exibir quantas pessoas já atingiram a maioridade
# (18 anos ou mais) e quantas ainda são menores.
m_i = 0
mn_i = 0

for i in range(1, 8):
    ano_nasc = int(input('qual o seu ano de nascimento: '))
    if ano_nasc > 2008:
        print('menor de idade')
        mn_i = mn_i +1
    else:
        print('maior de idade')
        m_i = m_i + 1

print(f"{m_i} maiores de idade , {mn_i} menores de idade")

