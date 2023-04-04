import re
from manipularPDF import removerPontuacao, removerNumeroPagina, lerPDF


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
            

    def __limparSumario(self, sumario :str) -> str:
        sumario = sumario.lower()
        sumario = removerNumeroPagina(sumario)
        sumario = removerPontuacao(sumario)
        return sumario
            
    def __transformarEmLista(self, topico :str) -> list:
        topicoSemNumero = topico.split(' ', 1)[-1].strip()
        listaTopicoPagina = re.split(r'\s{2,}', topicoSemNumero)
        return listaTopicoPagina

    def __extrairSumario(self, pdfLido :object):
        paginaSumario = self.__encontrarPaginaSumario(pdfLido)
        paginaSumario = self.__limparSumario(paginaSumario)

        dic = {}
        aux = None

        # TODO da pra colocar esse sumário no pandas, talvez facilite a vida
        for topico in paginaSumario.split('\n')[1:]:
            topicoPagina = self.__transformarEmLista(topico)

            if 'referências' in topico.split(' ', 1)[0].lower():
                dic['referências'] = int(topicoPagina[-1].strip()) - 1
                dic['ultima pagina'] = len(pdfLido.pages) - 1

                return dic

            if topicoPagina[-1].strip().isdigit():
                if aux != None:
                    dic[aux] = int(topicoPagina[-1].strip()) - 1
                    aux = None
                else:
                    dic[topicoPagina[0]] = int(topicoPagina[-1].strip()) - 1
            else:
                aux = topicoPagina[0].strip()


lerpdf = lerPDF('ArquivosPT/DAR20052019.pdf')
referencia = Sumario(lerpdf)
print(referencia.getSumario())