from sumario import Sumario
from extrairTopico import ExtrairTopico

class Objetivo():
    def __init__(self, pdfLido: object, sumario :Sumario) -> None:
        self.__extrairTopico = ExtrairTopico(sumario, r'objetivo(|s)(?:\sgera(l|is))?\b')
        self.__objetivo = self.__extrairObjetivo(pdfLido)

    def getObjetivo(self) -> str:
        return self.__objetivo

    def __extrairObjetivo(self, pdfLido: object) -> str:
        reComecoTopico = r'[0-9](\.|)\sobjetivo(|s)(?:\sgera(l|is))?\b'

        textoTopico = self.__extrairTopico._getTopico(pdfLido, reComecoTopico)

        return textoTopico
