import re
from sumario import Sumario
from manipularPDF import removerNumeroPagina

class ExtrairTopico():
    def __init__(self, sumario :Sumario, reNomeTopico :re) -> None:
        self.__sumario = sumario
        self.__reNomeTopico = reNomeTopico

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
    
    def __getTextoTopico(self, texto :str, comecoTopico :re) -> str:
        fimTopico = r'\n(\d.+)\d\s\w+\b'

        inicioTopico = re.search(comecoTopico, texto)
        fimTopico = re.search(fimTopico, texto[inicioTopico.end():])

        if inicioTopico and fimTopico:
            posicaoInicio = inicioTopico.end()
            posicaoFim = fimTopico.start()

            texto = texto[posicaoInicio: posicaoInicio + posicaoFim]

        return texto

    
    def _getTopico(self, pdfLido: object, reComecoTopico :re) -> str:
        paginasTopico = self.__sumario.getPaginasTopico(self.__reNomeTopico)
        textoPaginas = self.__getTextoPaginas(pdfLido, paginasTopico)
        textoTopico = self.__getTextoTopico(textoPaginas, reComecoTopico)

        return textoTopico