class Paciente:
    def __init__(self, NomePaciente, cpf, idade):
        self.Nome = NomePaciente
        self.__CPF = cpf
        self.__Idade = idade # quando colocamos __ antes do nome do atributo, ele se torna privado e não pode ser acessado diretamente fora da classe
        self.__historico = []

        #getters
    def get_CPF(self):
        cpf=self.__CPF
        return f"***.***.{cpf[8:11]}-{cpf[11:]}"

    def get_Idade(self):
        return self.__Idade

    def get_historico(self):
        return list(self.__historico)

    #setters

    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self.__Idade = nova_idade
        else:
            print("Idade invalida ")

    #métodos
    def adicionar_historico(self, diagnostico):
        self.__historico.append(diagnostico)
        print(f"diagnóstico registrado: {diagnostico}")

    def exibir_prontuario(self):
        print("="*30)
        print(f"Paciente: {self.Nome}")
        print(f"CPF: {self.get_CPF()}")
        print(f"Idade: {self.__Idade} anos")
        print("Histórico:")
        if self.__historico:
            for diagnostico in self.__historico:
                print(f"  - {diagnostico}")
        else:
            print("  Nenhum diagnóstico registrado.")
        print("="*30)

p1 = Paciente("João", "123.456.789-00", 30)
p1.adicionar_historico("gripe")
p1.adicionar_historico("Febre")

p1.set_idade(1)
p1.exibir_prontuario()