class Aluno:
    def __init__(self, Nome, nota):
        self.Nome = Nome
        self.__nota = None
        self.set_nota(nota)

    #getter
    def get_nota(self):
        return self.__nota

    #setter
    def set_nota(self, nova_nota):
        if 0 <= nova_nota <= 10:
            self.__nota = nova_nota
        else:
            print("Nota inválida. A nota deve estar entre 0 e 10.")

    def situação(self):
        if self.__nota >=6:
            return "Aprovado"
        elif self.__nota >=4:
            return "recuperação"
        else:
            return "Reprovado"

    def exibir_info(self):
        print("-" * 30)
        print("aluno:", self.Nome)
        print("Nota:", self.get_nota())
        print("Situação:", self.situação())
        print("-"*30)


a1=Aluno("Carlos", 7.5)
a1.exibir_info()

a2=Aluno("joão", 8)
a2.exibir_info()
a2.set_nota(10)
a2.exibir_info()


a3=Aluno("murilo", 0.5)
a3.exibir_info()