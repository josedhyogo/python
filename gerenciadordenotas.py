notas = {}
def adicionarNota():
    aluno = str(input("Nome do aluno: ")).strip().upper()
    nota = float(input("Nota: "))
    notas[aluno] = nota
    return notas
def exibirNotas():
    for aluno,nota in notas.items():
        print(f"Nome: {aluno}\nNota: {nota}")
        print("_"*10)
        print()
def buscarAluno():
    aluno_especifico = str(input("Nome do Aluno: ")).strip().upper()
    print()
    if aluno_especifico in notas:
        print(f"Nome:{aluno_especifico}\nNota:{notas[aluno_especifico]}")
    else:
        print(f"\033[31mAluno '{aluno_especifico}' não encontrado.\033[0m")
def alterarNota():
    aluno = str(input("Digite o nome do aluno: ")).strip().upper()
    if aluno in notas:
        nota_alterada = float(input("Digite a nova nota: "))
        notas[aluno] = nota_alterada
    else:
        print(f"O aluno {aluno}, não está cadastrado.")

# Menu

while True:
    try:
        print("_"*15)
        print("\033[33m[ 1 ] Adicionar Nota\n[ 2 ] Mostrar todas as notas\n[ 3 ] Buscar Aluno Específico\n[ 4 ] Atualizar nota de um aluno\n[ 5 ] Sair\n\033[0m")
        print("_"*15)
        opcao = int(input("\nDigite sua opção: "))
        print()
        match opcao:
            case 1:
                adicionarNota()
            case 2:
                exibirNotas()
            case 3:
                buscarAluno()
            case 4:
                alterarNota()
            case 5:
                break
            case _:
                print("\033[31mOpção inválida. Tente novamente.\033[0m")
           
    except ValueError:
        print("\033[31mAlgo deu errado , tente novamente.\033[0m")