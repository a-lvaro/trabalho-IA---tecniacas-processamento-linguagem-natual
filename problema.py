import re
from sumario import Sumario
from manipularPDF import removerNumeroPagina, removerPontuacao, removerBarraN

class Problema():
    def __init__(self, pdfLido: object, sumario: Sumario) -> None:
        self.__sumario = sumario
        self.__problema = self.__extrairProblema(pdfLido)

    def getProblema(self) -> str:
        return self.__problema
    
    def __getTextoTopico(self, pdfLido: object, reTopico :re) -> str:
        textoTopico = ''
        # r'( \n)+\d+\.\d+\.\s+\w+' TESTAR ESSA FUNÇÃO
        reFimTopico = r'\d.\d\s*objetivos?\b'

        paginasPosicao = self.__sumario.getPaginasTopico(reTopico)
        
        for posicao in range(paginasPosicao[0], paginasPosicao[1] + 1):
            texto = pdfLido.pages[posicao].extract_text()
            texto = self.__limparPagina(texto)

            inicioTopico = re.search(reTopico, texto)
            fimTopico = re.search(reFimTopico[inicioTopico.end():], texto) if inicioTopico else None

            if inicioTopico and fimTopico:
                textoTopico += texto[inicioTopico.end():fimTopico.start()]
            elif inicioTopico:
                textoTopico += texto[inicioTopico.end():]
            elif fimTopico:
                textoTopico += texto[:fimTopico.start()]
        
        return textoTopico
    
    def __limparPagina(self, texto :str) -> str:
        texto = texto.lower()
        texto = removerNumeroPagina(texto)
        texto = removerBarraN(texto)
        return texto


    def __extrairProblema(self, pdfLido: object) -> str:
        reTopico = r'introdução'

        texto = self.__getTextoTopico(pdfLido, reTopico)

        reProblemaInicio = r'((resolver|solucioner) o problema|estudos estão sendo realizados)\b'
        # pattern2 = r'\b\d+\s+\w+'

        match = re.search(reProblemaInicio, texto)
        if match:
            texto = texto[match.start():]

            countPonto = 0
            for posicao, char in enumerate(texto):
                if char == '.':
                    countPonto += 1
                if countPonto == 2:
                    texto = texto[:posicao]

        return texto