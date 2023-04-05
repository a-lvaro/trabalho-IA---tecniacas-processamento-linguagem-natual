import re
from sumario import Sumario
from manipularPDF import removerNumeroPagina, removerPontuacao

class Metodologia():
    def __init__(self, pdfLido: object, sumario :Sumario) -> None:
        self.__sumario = sumario
        self.__metodologia = self.__extrairMetodologia(pdfLido)

    def getMetodologia(self) -> list:
        return self.__metodologia
    
    def __getPagina(self, pdfLido: object) -> str:
        texto = ''

        paginas = self.__sumario.getPaginasTopico(r'metodologia\b')
        for posicao in range(paginas[0], paginas[1] + 1, 1):
             if re.search(r'(\n)(\d.|)(\d.|)\d\s\w+', pdfLido.pages[posicao].extract_text()):
                fim = re.search(r'(\n)(\d.|)(\d.|)\d\s\w+', pdfLido.pages[posicao].extract_text()).start()
                texto += removerNumeroPagina(pdfLido.pages[posicao].extract_text()[:fim])
             else:
                 texto += removerNumeroPagina(pdfLido.pages[posicao].extract_text())

        return texto
    
    def __extrairMetodologia(self, pdfLido: object) -> str:
        pagina = self.__getPagina(pdfLido)
        pagina = removerPontuacao(pagina)

        pagina = pagina.lower().split(' metodologia  \n')[1]
        pagina = pagina.split('.  \n')

        pagina = [metodologia.replace(
            '\n', '') for metodologia in pagina]

        return pagina