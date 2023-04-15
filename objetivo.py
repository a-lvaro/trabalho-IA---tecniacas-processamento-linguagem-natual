from sumario import Sumario
from extrairTopico import ExtrairTopico

class Objetivo():
    def __init__(self, pdfLido: object, sumario :Sumario) -> None:
        self.__topico = ExtrairTopico(sumario, self.__getPadroes())
        self.__objetivo = self.__extrairObjetivo(pdfLido)

    def getObjetivo(self) -> str:
        return self.__objetivo
    
    def __getPadroes(self):
        dictPadroes = {'topico': r'objetivo(|s)(?:\sgera(l|is))?\b',
                      'reComecoTopico': r'[0-9](\.|)\sobjetivo(|s)(?:\sgera(l|is))?\b',
                      'reFimTopico': r'\n(\d.+)\d(\.|)\s\w+\b'}
        
        return dictPadroes

    def __extrairObjetivo(self, pdfLido: object) -> str:
        textoTopico = self.__topico._getTopico(pdfLido)

        return textoTopico
