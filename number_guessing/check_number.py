def check_number(numeroEscolhido, numeroAleatorio):

    if numeroEscolhido == numeroAleatorio:
        print("Parabéns, você acertou!")
        return True
    
    elif numeroEscolhido < numeroAleatorio:
        print("Número errado, escolha um número maior!")
    else:
        print("Numéro errado, escolha um número menor!")
