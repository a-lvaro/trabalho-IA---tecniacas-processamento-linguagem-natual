import re
from sumario import Sumario
from manipularPDF import removerNumeroPagina, removerPontuacao

class Problema():
    def __init__(self, pdfLido: object, sumario: Sumario) -> None:
        self.__sumario = sumario
        self.__problema = self.__extrairProblema(pdfLido)

    def getProblema(self) -> str:
        return self.__problema
    
    def __getPagina(self, pdfLido: object) -> str:
        texto = ''

        paginas = self.__sumario.getPaginasTopico(r'introdução\b')
        for posicao in range(paginas[0], paginas[1] + 1, 1):
             if re.search(r'(\n)(\d.|)(\d.|)\d\s\w+', pdfLido.pages[posicao].extract_text()):
                fim = re.search(r'(\n)(\d.|)(\d.|)\d\s\w+', pdfLido.pages[posicao].extract_text()).start()
                texto += removerNumeroPagina(pdfLido.pages[posicao].extract_text()[:fim])
             else:
                 texto += removerNumeroPagina(pdfLido.pages[posicao].extract_text())

        return texto
    
    def __limparPagina(self, pagina :str) -> str:
        pagina = pagina.lower()
        pagina = removerNumeroPagina(pagina)
        pagina = removerPontuacao(pagina)
        return pagina


    def __extrairProblema(self, pdfLido: object) -> str:
        pagina = self.__getPagina(pdfLido)
        pagina = self.__limparPagina(pagina)

        rePadrao = r'resolver o problema\b'
        # pattern2 = r'\b\d+\s+\w+'

        if re.search(rePadrao, pagina):
            posicaoInicio = re.search(rePadrao, pagina).start()
            # posicaoFim = re.search(
            #     pattern2, pagina[posicaoInicio:]).start()

            pagina = pagina[posicaoInicio:]

        return pagina