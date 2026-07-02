class Turma:

    def __init__(self, NomeTurma):
        self.NomeTurma = NomeTurma
        self.Alunos = []


    def matricular(self):
        nome = input("Digite o nome do aluno: ")
        if nome in self.Alunos:
            print(f"Aluno {nome} já está matriculado.")
        else:
            self.Alunos.append(nome)
            print(f"Aluno {nome} matriculado com sucesso!")
    def remover(self):
        nome = input("Digite o nome do aluno: ")
        if nome in self.Alunos:
            self.Alunos.remove(nome)
            print(f"Aluno {nome} removido com sucesso!")
    def matriculado(self):
        nome = input("Digite o nome do aluno: ")
        if nome in self.Alunos:
            print(f"Aluno {nome} está matriculado.")
        else:
            print(f"Aluno {nome} não está matriculado.")
    def chamada(self):
        for i, nome in enumerate(self.Alunos, start=1):
            print(f"aluno: {nome}, posição na chamda {i}")

Turma1 = Turma("Ds")
Turma1.matricular()

Turma1.matricular()
Turma1.matricular()
Turma1.matricular()
Turma1.chamada()

Turma1.remover()
Turma1.chamada()

Turma1.matriculado()
Turma1.matriculado()
