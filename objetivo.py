import re
from manipularPDF import removerPontuacao, removerNumeroPagina
from sumario import Sumario


class Objetivo():
    def __init__(self, pdfLido: object, sumario :Sumario) -> None:
        self.__sumario = sumario
        self.__objetivo = self.__extrairObjetivo(pdfLido)

    def getObjetivo(self) -> str:
        return self.__objetivo

    def __getPaginaObjetivo(self, pdfLido: object) -> str:
        texto = ''

        paginas = self.__sumario.getPaginasTopico(r'objetivo(?:\sgeral)?\b')
        for posicao in paginas:
             texto += pdfLido.pages[posicao].extract_text()

        return texto

    def __extrairObjetivo(self, pdfLido: object) -> str:
        paginaObjetivo = self.__getPaginaObjetivo(pdfLido)
        paginaObjetivo = removerNumeroPagina(paginaObjetivo)
        paginaObjetivo = removerPontuacao(paginaObjetivo)
        paginaObjetivo = paginaObjetivo.lower()

        pattern1 = r'[0-9]\sobjetivo(?:\sgeral)?\b'
        pattern2 = r'\b\d+\s+\w+'

        if re.search(pattern1, paginaObjetivo):
            posicaoInicio = re.search(pattern1, paginaObjetivo).end()
            posicaoFim = re.search(
                pattern2, paginaObjetivo[posicaoInicio:]).start()

            paginaObjetivo = paginaObjetivo[posicaoInicio: posicaoInicio + posicaoFim]

        return paginaObjetivo


# TODO está coltando um número inesperado, provevelmente pegando o número do tópico seguinte
# objetivo = Objetivo('ArquivosPT/DAR20052019.pdf')
# print(objetivo.getObjetivo())
