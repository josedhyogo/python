# gerador de senha
import string, random
tamanho = int(input('Digite o tamanho da senha: '))
i = 0

def letrasAleatorias():
    letras = string.ascii_lowercase + string.ascii_uppercase
    return letras
def numerosAleatorios():
    numeros_str = [str(random.randint(1,100)) for _ in range(10)]
    random.shuffle(numeros_str)
    return ''.join(numeros_str)
sequencia = list(letrasAleatorias() + numerosAleatorios())
random.shuffle(sequencia)
senha = ''.join(sequencia[:tamanho])
print(senha)

