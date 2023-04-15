from sumario import Sumario
from extrairTopico import ExtrairTopico

class Metodologia():
    def __init__(self, pdfLido: object, sumario :Sumario) -> None:
        self.__extrairTopico = ExtrairTopico(sumario, r'metodologia\b')
        self.__metodologia = self.__extrairMetodologia(pdfLido)

    def getMetodologia(self) -> list:
        return self.__metodologia
    
    def __extrairMetodologia(self, pdfLido: object) -> str:
        reComecoTopico = r'[0-9](\.|)\s*(m\s*e\s*t\s*o\s*d\s*o\s*l\s*o\s*g\s*i\s*a|m\s*é\s*t\s*o\s*d\s*o)'
        textoTopico = self.__extrairTopico._getTopico(pdfLido, reComecoTopico)

        return textoTopico