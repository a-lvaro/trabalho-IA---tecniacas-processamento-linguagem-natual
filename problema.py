import re
from sumario import Sumario
from manipularPDF import removerNumeroPagina, removerPontuacao

class Problema():
    def __init__(self, pdfLido: object, sumario: Sumario) -> None:
        self.__sumario = sumario
        self.__problema = self.__extrairProblema(pdfLido)

    def getProblema(self) -> str:
        return self.__problema
    
    def __getTextoTopico(self, pdfLido: object, reTopico :re) -> str:
        texto = ''

        paginasPosicao = self.__sumario.getPaginasTopico(reTopico)
        for posicao in range(paginasPosicao[0], paginasPosicao[1] + 1):
             texto += pdfLido.pages[posicao].extract_text()

        return texto
    
    def __limparPagina(self, pagina :str) -> str:
        pagina = pagina.lower()
        pagina = removerNumeroPagina(pagina)
        pagina = removerPontuacao(pagina)
        return pagina


    def __extrairProblema(self, pdfLido: object) -> str:
        reTopico = r'introdução\b'

        pagina = self.__getTextoTopico(pdfLido, reTopico)
        # TODO talvez não esteja limpando a numeração das páginas
        pagina = self.__limparPagina(pagina)

        rePadrao = r'(resolver|solucioner) o problema\b'
        # pattern2 = r'\b\d+\s+\w+'

        match = re.search(rePadrao, pagina)
        if match:
            posicaoInicio = match.start()
            # posicaoFim = re.search(
            #     pattern2, pagina[posicaoInicio:]).start()

            pagina = pagina[posicaoInicio:]

        pagina = pagina.replace('\n', '')

        return pagina