from sumario import Sumario
from extrairTopico import ExtrairTopico

class Metodologia():
    def __init__(self, pdfLido: object, sumario :Sumario) -> None:
        self.__topico = ExtrairTopico(sumario, self.__getPadroes())
        self.__metodologia = self.__extrairMetodologia(pdfLido)

    def getMetodologia(self) -> str:
        return self.__metodologia
    
    def __getPadroes(self):
        dictPadroes = {'topico': r'metodologia\b',
                      'reComecoTopico': r'[0-9](\.|)\s*(m\s*e\s*t\s*o\s*d\s*o\s*l\s*o\s*g\s*i\s*a|m\s*é\s*t\s*o\s*d\s*o)',
                      'reFimTopico': r'\n(\d.+)\d(\.|)\s\w+\b'}
        
        return dictPadroes
    
    def __extrairMetodologia(self, pdfLido: object) -> str:
        textoTopico = self.__topico._getTopico(pdfLido)

        return textoTopico