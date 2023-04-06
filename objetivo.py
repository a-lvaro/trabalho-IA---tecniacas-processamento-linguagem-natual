import re
from sumario import Sumario
from manipularPDF import removerPontuacao, removerNumeroPagina

class Objetivo():
    def __init__(self, pdfLido: object, sumario :Sumario) -> None:
        self.__sumario = sumario
        self.__objetivo = self.__extrairObjetivo(pdfLido)

    def getObjetivo(self) -> str:
        return self.__objetivo

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

    def __extrairObjetivo(self, pdfLido: object) -> str:
        reTopico = r'objetivo(|s)(?:\sgera(l|is))?\b'
        
        texto = self.__getTextoTopico(pdfLido, reTopico)
        texto = self.__limparPagina(texto)

        pattern1 = r'[0-9]\sobjetivo(|s)(?:\sgera(l|is))?\b'
        pattern2 = r'\d+\s+\w+'

        # padraoComeca = r'objetivo(|s)(?:\sgera(l|is))?\b'
        # padraoTermina = r'\d+\s+\w+'

        if re.search(pattern1, texto):
            posicaoInicio = re.search(pattern1, texto).end()
            posicaoFim = re.search(
                pattern2, texto[posicaoInicio:]).start()

            texto = texto[posicaoInicio: posicaoInicio + posicaoFim]

        return texto


# TODO está coltando um número inesperado, provevelmente pegando o número do tópico seguinte
# objetivo = Objetivo('ArquivosPT/DAR20052019.pdf')
# print(objetivo.getObjetivo())
