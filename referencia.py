import re
from sumario import Sumario
from manipularPDF import removerNumeroPagina, removerBarraN


class Referencia():
    def __init__(self, pdfLido: object, sumario :Sumario) -> None:
        self.__sumario = sumario
        self.__referencia = self.__extrairReferencia(pdfLido)

    def getReferencia(self) -> list:
        return self.__referencia

    def __getPagina(self, pdfLido: object) -> str:
        texto = ''

        paginas = self.__sumario.getPaginasTopico(r'referências\b')
        for posicao in range(paginas[0], paginas[1] + 1, 1):
            pagina = pdfLido.pages[posicao].extract_text()
            pagina = self.__limparPagina(pagina)

            if re.match(r'\s*(apêndice|anexo)', pagina[:30]):
                return texto
            else:
                texto += pagina

        return texto
    
    def __limparPagina(self, pagina :str) -> str:
        pagina = pagina.lower()
        pagina = removerNumeroPagina(pagina)
        return pagina

    def __extrairReferencia(self, pdfLido: object) -> str:
        pagina = self.__getPagina(pdfLido)

        pagina = pagina.split('.  \n')        

        return pagina


# referencia = Referencia('ArquivosPT/DAR20052019.pdf')
# referencia.getReferencia()
