import re
from sumario import Sumario
from manipularPDF import lerPDF, removerNumeroPagina, removerPontuacao


class Referencia():
    def __init__(self, path: str) -> None:
        pdfLido = lerPDF(path)
        self.__sumario = Sumario(path)
        self.__referencia = self.__extrairReferencia(pdfLido)

    def getReferencia(self) -> list:
        return self.__referencia

    def __getPaginaReferencia(self, pdfLido: object) -> str:
        texto = ''

        paginas = self.__sumario.getPaginasTopico(r'referências\b')
        print(paginas)
        for posicao in paginas:
            for pagina in pdfLido.pages[posicao].extract_text():
                texto += pagina

        return texto

    def __extrairReferencia(self, pdfLido: object) -> str:
        paginaReferencia = self.__getPaginaReferencia(pdfLido)
        print(paginaReferencia)
        paginaReferencia = removerNumeroPagina(paginaReferencia)

        paginaReferencia = paginaReferencia.lower().split(
            ' referências  \n')[1]
        paginaReferencia = paginaReferencia.split('.  \n')

        paginaReferencia = [referencia.replace(
            '\n', '') for referencia in paginaReferencia]

        return paginaReferencia


referencia = Referencia('ArquivosPT/DAR20052019.pdf')
referencia.getReferencia()
