continuar= "s"


while continuar.lower() == "s":
    print("Demais cara ")
    num= float(input("Digite um número: "))
    print(num%2)
    if num % 2 == 0:
        print("Par")
    else:
        print("Impar")

        continuar=input("Deseja continuar?")