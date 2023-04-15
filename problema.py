import re
from sumario import Sumario
from manipularPDF import removerNumeroPagina
from extrairTopico import ExtrairTopico

class Problema():
    def __init__(self, pdfLido: object, sumario: Sumario) -> None:
        self.__topico = ExtrairTopico(sumario, self.__getPadroes())
        self.__problema = self.__extrairProblema(pdfLido)

    def getProblema(self) -> str:
        return self.__problema
    
    def __getPadroes(self):
        dictPadroes = {'topico': r'i\s*n\s*t\s*r\s*o\s*d\s*u\s*ç\s*ã\s*o',
                      'reComecoTopico': r'i\s*n\s*t\s*r\s*o\s*d\s*u\s*ç\s*ã\s*o',
                      'reFimTopico':  r'[1-9]{1,2}\s+\w{5,}'}
        
        return dictPadroes
    
    def __procurarProblema(self, texto :str) -> str:
        reProblemaInicio = r'((resolver|solucioner) o problema|estudos estão sendo realizados|pretende-se gerar|pesquisa investigou|acreditamos que um estudo|projetar um\s*algoritmo)\b'
        reProblemaFim = r'\.'

        match = re.search(reProblemaInicio, texto)
        if match:
            texto = texto[match.start():]

            for posicao, char in enumerate(texto):
                if char == '.':
                    return texto[:posicao + 1]

        return texto

    def __extrairProblema(self, pdfLido: object) -> str:
        textoTopico = self.__topico._getTopico(pdfLido)
        problema = self.__procurarProblema(textoTopico)
        return problema