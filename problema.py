import re
from sumario import Sumario
from manipularPDF import removerNumeroPagina, removerPontuacao, removerBarraN

class Problema():
    def __init__(self, pdfLido: object, sumario: Sumario) -> None:
        self.__sumario = sumario
        self.__problema = self.__extrairProblema(pdfLido)

    def getProblema(self) -> str:
        return self.__problema
    
    def __getTextoPaginas(self, pdfLido: object, paginasTopico :list) -> str:
        textoTopico = ''
        for posicao in range(paginasTopico[0], paginasTopico[1] + 1):
            texto = pdfLido.pages[posicao].extract_text()
            texto = self.__limparPagina(texto)
            textoTopico += texto

        return textoTopico
    
    def __getTextoTopico(self, texto :str) -> str:
        comecoTopico = r'i\s*n\s*t\s*r\s*o\s*d\s*u\s*ç\s*ã\s*o'
        fimTopico = r'[1-9]+\s+\w{4,}'

        inicioTopico = re.search(comecoTopico, texto)
        fimTopico = re.search(fimTopico, texto[inicioTopico.end():])
        
        if inicioTopico and fimTopico:
            posicaoInicio = inicioTopico.end()
            posicaoFim = fimTopico.start()

            texto = texto[posicaoInicio: posicaoFim]

        return texto
    
    def __limparPagina(self, texto :str) -> str:
        texto = texto.lower()
        texto = removerNumeroPagina(texto)
        texto = removerBarraN(texto)
        return texto
    
    def __procurarProblema(self, texto :str) -> str:
        reProblemaInicio = r'((resolver|solucioner) o problema|estudos estão sendo realizados|pretende-se gerar)\b'
        # reProblemaFim = r'\b\d+\s+\w+'

        match = re.search(reProblemaInicio, texto)
        if match:
            texto = texto[match.start():]

            countPonto = 0
            for posicao, char in enumerate(texto):
                if char == '.':
                    countPonto += 1
                if countPonto == 2:
                    texto = texto[:posicao]

        return texto

    def __extrairProblema(self, pdfLido: object) -> str:
        reTopico = r'i\s*n\s*t\s*r\s*o\s*d\s*u\s*ç\s*ã\s*o'

        paginasTopico = self.__sumario.getPaginasTopico(reTopico)
        textoPaginas = self.__getTextoPaginas(pdfLido, paginasTopico)
        textoTopico = self.__getTextoTopico(textoPaginas)
        # print('\n\n\n ----------------- Problema -----------------')
        # print(textoTopico)
        # print('---------------------------------- \n\n\n ')
        problema = self.__procurarProblema(textoTopico)
        return problema