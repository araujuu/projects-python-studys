import random

palavras_ptbr = [
    "casa", "água", "livro", "tempo", "feliz", "sol", "computador",
    "programação", "dados", "jogo", "musica", "brasil", "python"
]

palavra_aleatoria = random.choice(palavras_ptbr)
letras_descobertas = ['_'] * len(palavra_aleatoria)
max_tentativas = 6
tentativas = 0
letras_erradas = []

def adivinhar_letra():
    global tentativas, letras_erradas, letras_descobertas 
    
    while tentativas < max_tentativas and '_' in letras_descobertas:
        letra = input("\nDigite uma letra: ").lower()

        while len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas UMA letra válida!")
            letra = input("\nDigite uma letra: ").lower()
        
        if letra in letras_descobertas or letra in letras_erradas:
            print(f"Você já tentou a letra '{letra}'. Tente outra!")
            continue

        if letra in palavra_aleatoria:
            print("Parabéns, você acertou uma letra!")
            
            for i in range(len(palavra_aleatoria)):
                if palavra_aleatoria[i] == letra:
                    letras_descobertas[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas += 1
            print(f"Errado! Tentativas restantes: {max_tentativas - tentativas}")
            print(f"Letras erradas: {', '.join(letras_erradas)}")

        print(' '.join(letras_descobertas))

    if '_' not in letras_descobertas:
        print("\nParabéns! Você ganhou!")
    else:
        print(f"\nGame over! A palavra era: {palavra_aleatoria}")