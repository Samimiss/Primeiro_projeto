#Exercício 9: Sistema de Autenticação com Operadores Lógicos
#Enunciado: Crie um sistema de login que exija duas informações: o nome de usuário (string) e a chave de segurança token
#(número inteiro). O acesso só deve ser concedido se o usuário for exatamente "admin" E o token for igual a 9988.
#Se um dos dois dados (ou ambos) estiver incorreto, o programa deve exibir "Dados de acesso inválidos".
import token

nome_usuario=str(input("Digite seu usuário: "))
chave_segurança=int(input("Token de seugurança: "))

if nome_usuario != "admin" or chave_segurança != 9988:
    print("Dados de acesso inválidos.")
else:
    print("Logado.")
