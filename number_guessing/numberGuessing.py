import random
from check_number import *

numeroAleatorio = random.randint(1, 20)

print("Bem-vindo ao jogo de adivinhação de números!")

tentativas = 0

while tentativas < 3:
    try:
        numeroEscolhido = int(input("Escolha um número entre 1 e 20: "))

        if numeroEscolhido < 1 or numeroEscolhido > 20:
            print("Valor inválido! O número deve estar entre 1 e 20.")
            continue  

        acertou = check_number(numeroEscolhido, numeroAleatorio)

        if acertou:
            break

        tentativas += 1

    except ValueError:
        print("Por favor, digite um número inteiro válido.")

else:
    print("Suas tentativas acabaram!")
    print(f"O número era: {numeroAleatorio}")
