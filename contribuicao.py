import re
from sumario import Sumario
from extrairTopico import ExtrairTopico

class Contribuicao():
    def __init__(self, pdfLido: object, sumario :Sumario) -> None:
        self.__topico = ExtrairTopico(sumario, self.__getPadroes())
        self.__contribuicao = self.__extrairContribuicao(pdfLido)

    def getContribuicao(self) -> str:
        return self.__contribuicao

    def __getPadroes(self) -> dict:
        
        dictPadroes = {'topico': r'(conclus(ão|ões)|considerações finais)\b',
                       'reComecoTopico': r'(c\s*o\s*n\s*c\s*l\s*u\s*s\s*(ã\s*o|\s*õ\s*e\s*s)|considerações finais)\b',
                       'reFimTopico':  r'r\s*e\s*f\s*e\s*r\s*ê\s*n\s*c\s*i\s*a\s*s'}
        return dictPadroes
    
    def __procurarContribuicao(self, texto: str) -> str:
        # neste\s*trabalho
        reProblemaInicio = r'(criou\s*uma\s*base\s*de\s*dados|executou-se\s*dois\s*experimentos|estes resultados apresentados, comprovam|discutiu-se\s*a\s*variação|foi\s*proposto\s*um\s*modelo|neste trabalho, propusemos|neste  trabalho  foi utilizado  técnicas|mesmo sendo uma técnica promissora|neste trabalho foram  aplicadas técnicas|os resultados obtidos pela metodologia)\b'
        reProblemaFim = r'^(?:[^.]*\.){1}[^.]*\.' # identifica a segunda ocorrência de um ponto

        inicio = re.search(reProblemaInicio, texto)
        fim = re.search(reProblemaFim, texto[inicio.end():])

        texto = texto[inicio.start():inicio.end() + fim.end()]
        return texto
    
    def __extrairContribuicao(self, pdfLido: object) -> str:
        textoTopico = self.__topico._getTopico(pdfLido)
        # print('|||||||||||||||||')
        # print(textoTopico)
        # print('|||||||||||||||||')
        contribuicao = self.__procurarContribuicao(textoTopico)
        return contribuicao