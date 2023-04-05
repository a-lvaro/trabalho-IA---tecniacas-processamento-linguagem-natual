from sumario import Sumario

class Contribuicao():
    def __init__(self, pdfLido: object, sumario :Sumario) -> None:
        self.__sumario = sumario
        # self.__contribuicao = self.__extrairContribuicao(pdfLido)