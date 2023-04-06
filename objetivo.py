import re
from manipularPDF import removerPontuacao, removerNumeroPagina
from sumario import Sumario


class Objetivo():
    def __init__(self, pdfLido: object, sumario :Sumario) -> None:
        self.__sumario = sumario
        self.__objetivo = self.__extrairObjetivo(pdfLido)

    def getObjetivo(self) -> str:
        return self.__objetivo

    def __getPagina(self, pdfLido: object) -> str:
        texto = ''

        paginas = self.__sumario.getPaginasTopico(r'objetivo(|s)(?:\sgera(l|is))?\b')
        for posicao in range(paginas[0], paginas[1] - 1, -1):
             texto += pdfLido.pages[posicao].extract_text()

        return texto
    
    def __limparPagina(self, pagina :str) -> str:
        pagina = pagina.lower()
        pagina = removerNumeroPagina(pagina)
        pagina = removerPontuacao(pagina)
        return pagina

    def __extrairObjetivo(self, pdfLido: object) -> str:
        pagina = self.__getPagina(pdfLido)
        pagina = self.__limparPagina(pagina)

        pattern1 = r'[0-9]\sobjetivo(|s)(?:\sgera(l|is))?\b'
        pattern2 = r'\d+\s+\w+'

        # padraoComeca = r'objetivo(|s)(?:\sgera(l|is))?\b'
        # padraoTermina = r'\d+\s+\w+'

        if re.search(pattern1, pagina):
            posicaoInicio = re.search(pattern1, pagina).end()
            posicaoFim = re.search(
                pattern2, pagina[posicaoInicio:]).start()

            pagina = pagina[posicaoInicio: posicaoInicio + posicaoFim]

        return pagina


# TODO está coltando um número inesperado, provevelmente pegando o número do tópico seguinte
# objetivo = Objetivo('ArquivosPT/DAR20052019.pdf')
# print(objetivo.getObjetivo())
