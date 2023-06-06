class Aluno:
    def __init__(self, matricula, nota1, nota2):
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2

    def getMatricula(self):
        return self.matricula

    def setNota1(self, nota):
        self.nota1 = nota

    def setNota2(self, nota):
        self.nota2 = nota

    def getMedia(self):
        return (self.nota1 + self.nota2) / 2

    def mostrarInfo(self):
        print("Matricula:", self.matricula)
        print("Nota 1:", self.nota1)
        print("Nota 2:", self.nota2)
        print("Média:", self.getMedia())
        print()


def menu():
    print("Escolha uma opção:")
    print("1. Cadastrar alunos")
    print("2. Adicionar um aluno")
    print("3. Remover um aluno")
    print("4. Atualizar notas de um aluno")
    print("5. Mostrar informações dos alunos")
    print("6. Calcular média da turma")
    print("7. Sair")
    opcao = int(input("Opção: "))
    return opcao


turma = []

while True:
    opcao = menu()
    if opcao == 1:
        while True:
            matricula = input("Digite a matricula: ")
            nota1 = float(input("Digite a nota 1: "))
            nota2 = float(input("Digite a nota 2: "))
            aluno = Aluno(matricula, nota1, nota2)
            turma.append(aluno)
            turma.sort(key=lambda x: x.matricula)
            flag = input("Continuar cadastrando? (sim/não): ")
            if flag.lower() != "sim":
                break

    elif opcao == 2:
        matricula = input("Digite a matricula: ")
        nota1 = float(input("Digite a nota 1: "))
        nota2 = float(input("Digite a nota 2: "))
        aluno = Aluno(matricula, nota1, nota2)
        turma.append(aluno)

    elif opcao == 3:
        matricula = input("Digite a matricula do aluno a ser removido: ")
        for aluno in turma:
            if aluno.getMatricula() == matricula:
                turma.remove(aluno)

    elif opcao == 4:
        matricula = input("Digite a matricula do aluno: ")
        for aluno in turma:
            if aluno.getMatricula() == matricula:
                flag22 = input("Mudar nota1, nota2 do aluno? (sim/não): ")
                if flag22.lower() == "sim":
                    flag33 = input("Digite 1 para nota1 e 2 para nota2: ")
                    if flag33 == "1":
                        nova_nota = float(input("Digite a nova nota1: "))
                        aluno.setNota1(nova_nota)
                    elif flag33 == "2":
                        nova_nota = float(input("Digite a nova nota2: "))
                        aluno.setNota2(nova_nota)

    elif opcao == 5:
        for i, aluno in enumerate(turma, 1):
            print("Índice:", i)
            aluno.mostrarInfo()

    elif opcao == 6:
        media_turma = sum(aluno.getMedia() for aluno in turma) / len(turma)
        print("Média da turma")