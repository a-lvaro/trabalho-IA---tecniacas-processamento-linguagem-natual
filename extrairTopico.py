import re
from sumario import Sumario
from manipularPDF import removerNumeroPagina

class ExtrairTopico():
    def __init__(self, sumario :Sumario, rePadroes :dict) -> None:
        self.__sumario = sumario
        self.__rePadroes = rePadroes

    def __getTextoPaginas(self, pdfLido: object, paginasTopico :list) -> str:
        textoTopico = ''
        for posicao in range(paginasTopico[0], paginasTopico[1] + 1):
            texto = pdfLido.pages[posicao].extract_text()
            texto = self.__limparPagina(texto)
            textoTopico += texto

        return textoTopico

    def __limparPagina(self, pagina :str) -> str:
        pagina = pagina.lower()
        pagina = removerNumeroPagina(pagina)
        return pagina
    
    def __getTextoTopico(self, texto :str) -> str:
        inicioTopico = re.search(self.__rePadroes['reComecoTopico'], texto)
        fimTopico = re.search(self.__rePadroes['reFimTopico'], texto[inicioTopico.end():])

        if inicioTopico and fimTopico:
            posicaoInicio = inicioTopico.end()
            posicaoFim = fimTopico.start()

            texto = texto[posicaoInicio: posicaoInicio + posicaoFim]

        return texto

    
    def _getTopico(self, pdfLido: object) -> str:
        paginasTopico = self.__sumario.getPaginasTopico(self.__rePadroes['topico'])
        textoPaginas = self.__getTextoPaginas(pdfLido, paginasTopico)
        print('============================================')
        print(textoPaginas)
        print('============================================')
        textoTopico = self.__getTextoTopico(textoPaginas)

        return textoTopico