import tkinter as tk
import random

# Função para desenhar o boneco da forca
def desenhar_forca(erros):
    partes = [
        '''
          -----
          |   |
              |
              |
              |
              |
              |
        -----------
        ''',
        '''
          -----
          |   |
          O   |
              |
              |
              |
              |
        -----------
        ''',
        '''
          -----
          |   |
          O   |
          |   |
              |
              |
              |
        -----------
        ''',
        '''
          -----
          |   |
          O   |
         /|   |
              |
              |
              |
        -----------
        ''',
        '''
          -----
          |   |
          O   |
         /|\\  |
              |
              |
              |
        -----------
        ''',
        '''
          -----
          |   |
          O   |
         /|\\  |
         /    |
              |
              |
        -----------
        ''',
        '''
          -----
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        -----------
        '''
    ]
    return partes[erros]

# Função para o jogo da forca com interface gráfica
class JogoDaForca(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Jogo da Forca")
        self.geometry("600x500")
        
        self.tentativas = []
        self.erros = 0
        self.max_erros = 6  # Número máximo de erros (seis partes do boneco)

        # Carregar palavras do arquivo
        with open("palavras.txt", "r", encoding="utf-8") as arquivo:
            self.palavras = arquivo.read().splitlines()
        
        # Escolher uma palavra secreta
        self.palavraSecreta = list(random.choice(self.palavras).strip())
        self.palavra_visivel = ['_' for _ in self.palavraSecreta]
        
        # Criar widgets
        self.label_forca = tk.Label(self, text=desenhar_forca(self.erros), font=("Courier", 14), justify="left")
        self.label_forca.pack()

        self.label_palavra = tk.Label(self, text=" ".join(self.palavra_visivel), font=("Courier", 18))
        self.label_palavra.pack()

        self.entry_letra = tk.Entry(self, font=("Courier", 18))
        self.entry_letra.pack(pady=20)

        self.botao_tentar = tk.Button(self, text="Tentar", command=self.tentar, font=("Courier", 14))
        self.botao_tentar.pack()

        self.label_mensagem = tk.Label(self, text="Digite uma letra para começar!", font=("Courier", 14))
        self.label_mensagem.pack(pady=20)

        self.atualizar_jogo()

    def tentar(self):
        letra = self.entry_letra.get().lower().strip()
        self.entry_letra.delete(0, tk.END)

        if letra == 'sair':
            self.quit()
            return

        if letra in self.tentativas:
            self.label_mensagem.config(text="Você já utilizou essa letra.")
            return

        self.tentativas.append(letra)

        if letra in self.palavraSecreta:
            for i in range(len(self.palavraSecreta)):
                if self.palavraSecreta[i] == letra:
                    self.palavra_visivel[i] = letra
        else:
            self.erros += 1
        
        self.atualizar_jogo()

    def atualizar_jogo(self):
        self.label_forca.config(text=desenhar_forca(self.erros))
        self.label_palavra.config(text=" ".join(self.palavra_visivel))

        if "_" not in self.palavra_visivel:
            self.label_mensagem.config(text="Parabéns! Você acertou a palavra.")
        elif self.erros >= self.max_erros:
            self.label_mensagem.config(text=f"Você perdeu! A palavra era: {''.join(self.palavraSecreta)}")
        else:
            self.label_mensagem.config(text="Digite uma letra para continuar.")

# Iniciar o jogo
if __name__ == "__main__":
    app = JogoDaForca()
    app.mainloop()
