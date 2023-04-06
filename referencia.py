import re
from sumario import Sumario
from manipularPDF import removerNumeroPagina


class Referencia():
    def __init__(self, pdfLido: object, sumario :Sumario) -> None:
        self.__sumario = sumario
        self.__referencia = self.__extrairReferencia(pdfLido)

    def getReferencia(self) -> list:
        return self.__referencia

    def __getTextoPaginas(self, pdfLido: object, paginasTopico :list) -> str:
        textoTopico = ''

        for posicao in range(paginasTopico[0], paginasTopico[1]):
            texto = pdfLido.pages[posicao].extract_text()
            texto = self.__limparPagina(texto)
            textoTopico += texto

        return textoTopico
    
    def __getTextoTopico(self, texto :str) -> str:
        reComecoTopico = r'referências\b'
        reFimTopico = r'\s*(apêndice|anexo)'

        if re.search(reComecoTopico, texto):
            posicaoInicioTopico = re.search(reComecoTopico, texto).end()
            posicaoFimTopico = re.search(reFimTopico, texto[posicaoInicioTopico:]).start() if re.search(reFimTopico, texto[posicaoInicioTopico:]) else None

            if posicaoFimTopico:
                textoTopico = texto[posicaoInicioTopico: posicaoInicioTopico + posicaoFimTopico]
            else:
                textoTopico = texto[posicaoInicioTopico:]

        return textoTopico
    
    def __limparPagina(self, pagina :str) -> str:
        pagina = pagina.lower()
        pagina = removerNumeroPagina(pagina)
        return pagina

    def __extrairReferencia(self, pdfLido: object) -> str:
        reTopico = r'referências\b'

        paginasTopico = self.__sumario.getPaginasTopico(reTopico)
        textoPaginas = self.__getTextoPaginas(pdfLido, paginasTopico)
        textoTopico = self.__getTextoTopico(textoPaginas)

        textoTopico = textoTopico.split('.  \n')        

        return textoTopico
