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
    
    def __getPadroes(self) -> dict:
        dictPadroes = {'topico': r'i\s*n\s*t\s*r\s*o\s*d\s*u\s*ç\s*ã\s*o',
                      'reComecoTopico': r'i\s*n\s*t\s*r\s*o\s*d\s*u\s*ç\s*ã\s*o',
                      'reFimTopico':  r'\n(\d.+)\d(\.|)\s\w+\b'}
        
        return dictPadroes
    
    def __procurarProblema(self, texto :str) -> str:
        reProblemaInicio = r'((resolver|solucioner) o problema|estudos estão sendo realizados|pretende-se gerar|pesquisa investigou|acreditamos que um estudo|projetar um\s*algoritmo|nesse contexto|a fim de aumentar|é muito comum|no brasil, o diagnóstico de sintomas|mas a partir dos anos 2000|até o presente momento não foi desenvolvida)\b'
        reProblemaFim = r'^(?:[^.]*\.){1}[^.]*\.'


        inicio = re.search(reProblemaInicio, texto)
        fim = re.search(reProblemaFim, texto[inicio.end():])
        
        texto = texto[inicio.start():inicio.end() + fim.end()]
        return texto

    def __extrairProblema(self, pdfLido: object) -> str:
        textoTopico = self.__topico._getTopico(pdfLido)
        problema = self.__procurarProblema(textoTopico)
        return problema