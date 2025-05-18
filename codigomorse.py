caracteres_morse = {
    'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',   'e': '.', 
    'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.---', 
    'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'o': '---', 
    'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',  't': '-', 
    'u': '..-',   'v': '...-', 'w': '.--',   'x': '-..-',  'y': '-.--', 
    'z': '--..',
    
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}
morse_para_texto = {valor:chave for chave,valor in caracteres_morse.items()}

def converter_Texto_pra_Morse(entrada):
    palavra = list(entrada)
    for i in palavra :
        if i in caracteres_morse :
            print(caracteres_morse[i],end=" ")
def converte_Morse_pra_Texto(morse):
    palavras = morse.split("   ")
    texto = []

    for palavra in palavras:
        letras = palavra.split()
        palavra_convertida = "".join(morse_para_texto[letra] for letra in letras if letra in morse_para_texto)
        texto.append(palavra_convertida)
    return "".join(texto)
print(''' 
    [ 1 ] Converter Texto para Codigo Morse
    [ 2 ] Converter Codigo Morse para Texto
    [ 3 ] Sair
''')
while True:
    opcao = int(input("\nEscolha uma opção: "))
    if opcao == 1:
        entrada = str(input("Digite a palavra/numero a ser convertida: ")).lower().strip()
        converter_Texto_pra_Morse(entrada)
    elif opcao == 2:
        entrada_morse = str(input("Digite o codigo a ser convertido: "))
        texto_convertido = converte_Morse_pra_Texto(entrada_morse)
        print("Texto convertido: ",texto_convertido)
    elif opcao == 3:
        print("Saindo")
        break
    else:
        print("Opção invalida, insira novamente")
        