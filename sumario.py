import re
from manipularPDF import removerPontuacao, removerNumeroPagina


class Sumario:
    def __init__(self, pdfLido :object) -> None:
        self.__sumario = self.__extrairSumario(pdfLido)

    def getSumario(self) -> dict:
        return self.__sumario

    def getPaginasTopico(self, topicoRegex: re) -> list:
        posicaoPaginas = []
        for keys, values in self.__sumario.items():
            if re.match(topicoRegex, keys):
                posicaoPaginas.append(values)
            elif len(posicaoPaginas) == 1:
                posicaoPaginas.append(values)
                return posicaoPaginas
                

    def __encontrarPaginaSumario(self, pdfLido :object) -> str:
        for pagina in pdfLido.pages:
            if 'sumário' in pagina.extract_text().lower()[:30]:
                return pagina.extract_text()

    def __extrairSumario(self, pdfLido :object):
        paginaSumario = self.__encontrarPaginaSumario(pdfLido)
        paginaSumario = removerNumeroPagina(paginaSumario)
        paginaSumario = removerPontuacao(paginaSumario)
        paginaSumario = paginaSumario.lower()

        dic = {}
        aux = None

        # TODO da pra colocar esse sumário no pandas, talvez facilite a vida
        for i in paginaSumario.split('\n')[1:]:
            p = i.split(' ', 1)[-1].strip()
            x = re.split(r'\s{2,}', p)

            if 'referências' in i.split(' ', 1)[0].lower():
                dic['referências'] = int(x[-1].strip()) - 1

                dic['ultima pagina'] = len(pdfLido.pages) - 1

                return dic

            if x[-1].strip().isdigit():
                if aux != None:
                    dic[aux] = int(x[-1].strip()) - 1
                    aux = None
                else:
                    dic[x[0]] = int(x[-1].strip()) - 1
            else:
                aux = x[0].strip()


# x = Sumario('ArquivosPT/DAR20052019.pdf')
# # print(x.getPaginasTopico('introdução'))
# print('\n\n')
# print(x.getSumario())


# lerpdf = lerPDF('ArquivosPT/DAR20052019.pdf')
# referencia = Sumario(lerpdf)
# print(referencia.getSumario())