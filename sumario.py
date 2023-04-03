import re
from manipularPDF import removerPontuacao, lerPDF, removerNumeroPagina


class Sumario:
    def __init__(self, path) -> None:
        pdfLido = lerPDF(path)
        self.__sumario = self.__extrairSumario(pdfLido)

    def getSumario(self) -> dict:
        return self.__sumario

    def getPaginasTopico(self, topico: str) -> list:
        posicaoPaginas = []
        for keys, values in self.__sumario.items():
            if topico == keys:
                posicaoPaginas.append(values)
            elif len(posicaoPaginas) == 1:
                posicaoPaginas.append(values)
                return posicaoPaginas

    def __encontrarPaginaSumario(self, pdfLido):
        for pagina in pdfLido.pages:
            if 'sumário' in pagina.extract_text().lower()[:30]:
                return pagina.extract_text()

    def __extrairSumario(self, pdfLido):
        paginaSumario = self.__encontrarPaginaSumario(pdfLido)
        paginaSumario = removerNumeroPagina(paginaSumario)
        paginaSumario = removerPontuacao(paginaSumario)
        paginaSumario = paginaSumario.lower()

        dic = {}
        aux = None

        for i in paginaSumario.split('\n')[1:]:
            p = i.split(' ', 1)[-1].strip()
            x = re.split(r'\s{2,}', p)

            if 'referências' in i.split(' ', 1)[0].lower():
                dic['referências'] = x[-1].strip()

                return dic

            if x[-1].strip().isdigit():
                if aux != None:
                    dic[aux] = x[-1].strip()
                    aux = None
                else:
                    dic[x[0]] = x[-1].strip()
            else:
                aux = x[0].strip()

        return dic


# x = Sumario('ArquivosPT/DAR20052019.pdf')
# print(x.getPaginasTopico('introdução'))
# print('\n\n')
# print(x.getSumario())
