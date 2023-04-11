from sumario import Sumario
from objetivo import Objetivo
from referencia import Referencia
from problema import Problema
from metodologia import Metodologia
from manipularPDF import lerPDF


class Artigo():
    def __init__(self, path: str) -> None:
        self.__pdfLido = lerPDF(path)
        self.__sumario = Sumario(self.__pdfLido)

        self.__objetivo = Objetivo(self.__pdfLido, self.__sumario)
        # self.__referencia = Referencia(self.__pdfLido, self.__sumario)
        # self.__problema = Problema(self.__pdfLido, self.__sumario)
        # self.__metodologia = Metodologia(self.__pdfLido, self.__sumario)
        self.__contribuicao = None

    def getSumario(self) -> dict:
        return self.__sumario.getSumario()
    
    def getObjetivo(self) -> str:
        return self.__objetivo.getObjetivo()
    
    # def getReferencia(self) -> list:
    #     for referencia in self.__referencia.getReferencia():
    #         print(referencia)
    
    # def getProblema(self) -> str:
    #     return self.__problema.getProblema()
    
    # def getMetodologia(self) -> str:
    #     return self.__metodologia.getMetodologia()


artigo = Artigo('ArquivosTeste/TCC FINAL_Sandy.pdf')
print(artigo.getSumario())
print('\n\n OBJETIVO')
print(artigo.getObjetivo())
# print('\n\n REFERÊNCIAS')
# artigo.getReferencia()
# print('\n\n PROBLEMA')
# print(artigo.getProblema())
# print('\n\n METODOLOGIA')
# print(artigo.getMetodologia())
