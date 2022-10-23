class Pessoa:
    def __init__(self, nome, matricula, nota):
        self.__nome = nome
        self.__matricula = matricula
        self.__nota = nota
    
    def get_nome(self):
        return self.__nome
    
    def get_matricula(self):
        return self.__matricula

    def get_nota(self):
        return self.__nota