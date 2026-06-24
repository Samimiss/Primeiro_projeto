#Exercício 5: Validador de Senhas e Tentativas (Intermediário)
#Enunciado: Um sistema de segurança permite que o usuário tente digitar sua senha de acesso no máximo 3 vezes.
# Crie um loop for que execute 3 vezes pedindo a senha. Se o usuário digitar a senha correta (defina uma senha
# padrão no código), o programa deve exibir "Acesso Permitido" e interromper o laço imediatamente usando o break.
# Se as 3 tentativas falharem, exiba "Conta Bloqueada".


for i in range (3):
    s=int(input("Digite a senha: "))
    if 1234 == s:
        print("senha correta! ")
        break
    elif i == 2:
        print('conta bloqueada')
        break
    else:
        print('senha incorreta')
