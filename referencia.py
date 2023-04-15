from sumario import Sumario
from extrairTopico import ExtrairTopico

class Referencia():
    def __init__(self, pdfLido: object, sumario :Sumario) -> None:
        self.__topico = ExtrairTopico(sumario, self.__getPadroes())
        self.__referencia = self.__extrairReferencia(pdfLido)

    def getReferencia(self) -> list:
        return self.__referencia
    
    def __getPadroes(self):
        dictPadroes = {'topico': r'referências\b',
                       'reComecoTopico': r'referências\b',
                       'reFimTopico': r'\s*(apêndice|anexo)\b'}
        
        return dictPadroes

    def __extrairReferencia(self, pdfLido: object) -> str:
        textoTopico = self.__topico._getTopico(pdfLido)
        textoTopico = textoTopico.split('.  \n')        

        return textoTopico
