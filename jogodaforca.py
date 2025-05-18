import random
import os

tentativas = []

with open("palavras.txt", "r", encoding="utf-8") as arquivo:
    palavras = arquivo.read().splitlines()

palavraSecreta = list(random.choice(palavras).strip())  
palavra_visivel = ['_' for _ in palavraSecreta]
chances = 1

print("PARA SAIR DIGITE 'sair'")

while "_" in palavra_visivel:
    print("TENTATIVA:", chances)
    print(' '.join(palavra_visivel))
    
    letra = str(input("Digite um letra: ")).lower().strip()
    
    if letra in tentativas:
        print('Você já utilizou essa letra.')    
        continue

    tentativas.append(letra)

    for i in range(len(palavraSecreta)):
        if palavraSecreta[i] == letra:
            palavra_visivel[i] = letra

    if letra == 'sair':
        break

    chances += 1
    print("=-=" * 15)

print("\nParabéns você acertou!!")
print("A palavra era:", ''.join(palavraSecreta))
