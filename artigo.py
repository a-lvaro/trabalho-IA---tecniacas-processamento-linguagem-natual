from sumario import Sumario
from objetivo import Objetivo
from referencia import Referencia
from problema import Problema
from metodologia import Metodologia
from contribuicao import Contribuicao
from manipularPDF import lerPDF


class Artigo():
    def __init__(self, path: str) -> None:
        self.__pdfLido = lerPDF(path)
        self.__sumario = Sumario(self.__pdfLido)

        self.__objetivo = Objetivo(self.__pdfLido, self.__sumario)
        self.__metodologia = Metodologia(self.__pdfLido, self.__sumario)
        self.__problema = Problema(self.__pdfLido, self.__sumario)
        self.__contribuicao = Contribuicao(self.__pdfLido, self.__sumario)
        self.__referencia = Referencia(self.__pdfLido, self.__sumario)

    def getSumario(self) -> dict:
        return self.__sumario.getSumario()
    
    def getObjetivo(self) -> str:
        return self.__objetivo.getObjetivo()
    
    def getMetodologia(self) -> str:
        return self.__metodologia.getMetodologia()
    
    def getProblema(self) -> str:
        return self.__problema.getProblema()

    def getContribuicao(self) -> str:
        return self.__contribuicao.getContribuicao()

    def getReferencia(self) -> list:
        return self.__referencia.getReferencia()

    def salvarArtigo(self) -> None:
        texto = '|++|'

        texto += self.getObjetivo()
        texto += ';;' + self.getProblema()
        texto += ';;' + self.getMetodologia()
        texto += ';;' + self.getContribuicao()
        texto += ';;' + '||'.join(self.getReferencia())

        with open('dadosExtraidos.txt', 'a') as arquivo:
            arquivo.write(texto)


# artigo = Artigo('artigos/DetecçãoCâncerMama.pdf')
# print(artigo.getSumario())
# print('\n\n OBJETIVO') 
# print(artigo.getObjetivo())
# print('\n\n METODOLOGIA')
# print(artigo.getMetodologia())
# print('\n\n PROBLEMA')
# print(artigo.getProblema())
# print('\n\n CONTRIBUIÇÃO')
# print(artigo.getContribuicao())
# print('\n\n REFERÊNCIAS')
# for i in artigo.getReferencia():
#     print(i)

# artigo.salvarArtigo()
