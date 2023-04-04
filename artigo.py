from sumario import Sumario
from objetivo import Objetivo
from referencia import Referencia
from manipularPDF import lerPDF


class Artigo():
    def __init__(self, path: str) -> None:
        self.__pdfLido = lerPDF(path)
        self.__sumario = Sumario(self.__pdfLido)

        self.__objetivo = Objetivo(self.__pdfLido, self.__sumario)
        self.__referencia = Referencia(self.__pdfLido, self.__sumario)
        self.__metodologia = None
        self.__problema = None
        self.__contribuicao = None

    def getSumario(self) -> dict:
        return self.__sumario.getSumario()
    
    def getObjetivo(self) -> str:
        return self.__objetivo.getObjetivo()
    
    def getReferencia(self) -> list:
        return self.__referencia.getReferencia()


artigo = Artigo('ArquivosPT/DAR20052019.pdf')
# print(artigo.getSumario())
print(artigo.getObjetivo())
# print(artigo.getReferencia())
