import json
import os

turmas = {}

def salvar_turmas():
    with open("turmas.json","w") as arquivo:
        json.dump(turmas,arquivo, indent=4)
def carregar_turmas():
    if os.path.exists("turmas.json"):
        with open("turmas.json", "r") as arquivo:
            return json.load(arquivo)
    else:
        return{}
def cadastrar_Turma():
    turma = str(input("Digite o nome da turma: ")).strip().upper()
    turmas[turma] = {}
    salvar_turmas()
    return turmas

def adicionar_Aluno_em_Turma():
    turma = str(input("Digite a turma que o aluno será cadastrado: ")).strip().upper()
    aluno = str(input("Digite o nome do aluno: ")).strip().upper()
    turmas[turma][aluno] = []
    salvar_turmas() 
    return turmas

def adiconar_Nota_aluno():
    turma = str(input("Digite a turma do aluno: ")).strip().upper()
    aluno = str(input("Nome do aluno: ")).strip().upper()
    nota = float(input("Nota: "))
    turmas[turma][aluno].append(nota)
    salvar_turmas()

def mostrar_Turmas():
    for turma in turmas:
        if turma in turmas:
            print(turma)
        for aluno,nota in turmas[turma].items():
            print(f"\nNome: {aluno} -- Nota: {nota}")
        print("_"*20)

def mostrar_Alunos_Turma():
    print("TURMAS CADASTRADAS")
    print("_"*20)
    for turma in turmas:
        print(turma)
        pass
    print()
    escolha = str(input("Escolha uma das turma: ")).strip().upper()
    if escolha in turmas:    
        for aluno,nota in turmas[escolha].items():
            print(f"\nNome: {aluno} -- Nota: {nota}")
    print("_"*20)

def consultar_Media_aluno():
    print("MEDIA-ALUNO")
    aluno_especifico = str(input("Digite o nome do aluno: ")).strip().upper()
    encontrado = False
    for turma, alunos in turmas.items():
        for nome_aluno, notas in alunos.items():
            if nome_aluno == aluno_especifico:
                media = sum(notas) / len(notas)
                print(f"Nome: {nome_aluno} -- Turma: {turma} -- Media: {media:.2f}")
                encontrado = True
    if not encontrado:
        print("Aluno não encontrado.")

def consultar_Media_turma():
    print("MÉDIA - TURMA")
    turma_especifica = str(input("Digite a turma: ")).strip().upper()
    encontrado = False

    for nome_turma, alunos in turmas.items():
        if nome_turma == turma_especifica:
            soma_total = 0
            quantidade_notas = 0
            for notas in alunos.values():
                soma_total += sum(notas)
                quantidade_notas += len(notas)
            if quantidade_notas > 0:
                media = soma_total / quantidade_notas
                print(f"Turma: {nome_turma} — Média: {media:.2f}")
            else:
                print("Essa turma não possui notas registradas.")
            encontrado = True
            break

    if not encontrado:
        print("Turma não encontrada.")


#Menu
turmas = carregar_turmas()
while True:
    try:
        print('''
        MENU - Gerenciador de Turmas e Alunos
        [1] Cadastrar nova turma
        [2] Adicionar aluno a uma turma
        [3] Adicionar nota para um aluno
        [4] Mostrar turmas cadastradas
        [5] Mostrar alunos de uma turma
        [6] Consultar média de um aluno
        [7] Mostrar média geral da turma
        [8] Sair
        ''')
        print("_"*20)
        opcao = int(input("Escolha uma opção: "))
        match opcao:
            case 1:
                cadastrar_Turma()
            case 2:
                adicionar_Aluno_em_Turma()
            case 3:
                adiconar_Nota_aluno()
            case 4:
                mostrar_Turmas()
            case 5:
                mostrar_Alunos_Turma()
            case 6:
                consultar_Media_aluno()
            case 7:
                consultar_Media_turma()
            case 8:
                break
            case _:
                print("Opção invalida , insira sua opção novamente.")
    except ValueError:
        print("Algo deu errado, tente novamente.")
        print()