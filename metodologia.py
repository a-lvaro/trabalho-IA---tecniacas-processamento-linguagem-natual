import re
from sumario import Sumario
from manipularPDF import removerNumeroPagina, limparTexto

class Metodologia():
    def __init__(self, pdfLido: object, sumario :Sumario) -> None:
        self.__sumario = sumario
        self.__metodologia = self.__extrairMetodologia(pdfLido)

    def getMetodologia(self) -> list:
        return self.__metodologia
    
    def __getTextoTopico(self, texto :str) -> str:
        comecoTopico = r'[0-9](\.|)\s*(m\s*e\s*t\s*o\s*d\s*o\s*l\s*o\s*g\s*i\s*a|m\s*é\s*t\s*o\s*d\s*o)'
        fimTopico = r'\n(\d.+)\d\s\w+\b'

        inicioTopico = re.search(comecoTopico, texto)
        fimTopico = re.search(fimTopico, texto[inicioTopico.end():])
        print(inicioTopico)
        print(fimTopico)


        if inicioTopico and fimTopico:
            posicaoInicio = inicioTopico.end()
            posicaoFim = fimTopico.start()

            texto = texto[posicaoInicio: posicaoInicio + posicaoFim]

        return texto
    
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

    
    def __extrairMetodologia(self, pdfLido: object) -> str:
        reTopico = r'metodologia\b'

        paginasTopico = self.__sumario.getPaginasTopico(reTopico)
        textoPaginas = self.__getTextoPaginas(pdfLido, paginasTopico)
        textoTopico = self.__getTextoTopico(textoPaginas)

        return textoTopico