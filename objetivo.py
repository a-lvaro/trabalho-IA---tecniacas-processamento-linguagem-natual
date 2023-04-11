import re
from sumario import Sumario
from manipularPDF import removerNumeroPagina

class Objetivo():
    def __init__(self, pdfLido: object, sumario :Sumario) -> None:
        self.__sumario = sumario
        self.__objetivo = self.__extrairObjetivo(pdfLido)

    def getObjetivo(self) -> str:
        return self.__objetivo

    def __getTextoPaginas(self, pdfLido: object, paginasTopico :list) -> str:
        textoTopico = ''
        for posicao in range(paginasTopico[0], paginasTopico[1] + 1):
            texto = pdfLido.pages[posicao].extract_text()
            texto = self.__limparPagina(texto)
            textoTopico += texto

        return textoTopico
    
    def __getTextoTopico(self, texto :str) -> str:
        comecoTopico = r'[0-9]\sobjetivo(|s)(?:\sgera(l|is))?\b'
        fimTopico = r'\d+\s+\w+'

        if re.search(comecoTopico, texto):
            posicaoInicio = re.search(comecoTopico, texto).end()
            posicaoFim = re.search(
                fimTopico, texto[posicaoInicio:]).start()

            texto = texto[posicaoInicio: posicaoInicio + posicaoFim]

        return texto

    
    def __limparPagina(self, pagina :str) -> str:
        pagina = pagina.lower()
        pagina = removerNumeroPagina(pagina)
        return pagina

    def __extrairObjetivo(self, pdfLido: object) -> str:
        reTopico = r'objetivo(|s)(?:\sgera(l|is))?\b'
        
        paginasTopico = self.__sumario.getPaginasTopico(reTopico)
        textoPaginas = self.__getTextoPaginas(pdfLido, paginasTopico)
        textoTopico = self.__getTextoTopico(textoPaginas)

        return textoTopico
