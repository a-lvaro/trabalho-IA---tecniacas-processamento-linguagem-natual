import re
from manipularPDF import removerPontuacao, removerNumeroPagina, removerBarraN


class Sumario:
    def __init__(self, pdfLido :object) -> None:
        self.__sumario = self.__extrairSumario(pdfLido)

    def getSumario(self) -> dict:
        return self.__sumario

    def getPaginasTopico(self, topicoRegex: re) -> list:
        posicaoPaginas = []
        for keys, values in self.__sumario.items():
            if re.match(topicoRegex, keys) and len(posicaoPaginas) == 0:
                posicaoPaginas.append(values)
            elif len(posicaoPaginas) == 1:
                posicaoPaginas.append(values)
                return posicaoPaginas
                

    def __encontrarPagina(self, pdfLido :object, reTopico :re) -> str:
        texto = ''
        reReferencia = r'referências\s*\ .*\b'
        achouTopico = False

        for pagina in pdfLido.pages:
            paginaLida = pagina.extract_text().lower()
            inicioTopico = re.search(reTopico, paginaLida[:30])
            fimTopico = re.search(reReferencia, paginaLida)

            if inicioTopico and fimTopico:
                inicio = inicioTopico.end()
                fim = fimTopico.end()
                texto = pagina.extract_text()[inicio:fim]
                return texto

            elif inicioTopico:
                inicio = inicioTopico.end()
                texto = pagina.extract_text()[inicio:]
                achoTopico = True
            elif fimTopico:
                fim = fimTopico.end()
                texto += pagina.extract_text()[:fim]
                return texto
            elif achouTopico:
                texto += pagina.extract_text()
        
        return None
            
    def __limparPagina(self, texto :str) -> str:
        texto = texto.lower()
        texto = removerNumeroPagina(texto)
        texto = removerPontuacao(texto)
        return texto
            
    def __transformarEmLista(self, texto :str) -> list:
        listaTopicoPagina = []
        for topico in texto.split('\n')[1:]:
            print(topico)
            topicoSemNumero = topico.split(' ', 1)[-1].strip()
            listaTopicoPagina.append(re.split(r'\s{2,}', topicoSemNumero))

        return listaTopicoPagina
    
    def __transformarEmDicionario(self,  pdfLido :object, texto :str) -> dict:
        dic = {}
        aux = None
        for topico in texto:
            print(topico)

            if 'referência' in  topico[0].lower():
                dic['referências'] = int(topico[-1].strip())
                dic['ultima pagina'] = len(pdfLido.pages)
                return dic
            
            elif topico != ['']:
                print('aqui')
                if topico[-1].strip().isdigit():
                    if aux != None:
                        dic[aux] = int(topico[-1].strip())
                        aux = None
                    else:
                        dic[topico[0]] = int(topico[-1].strip())

        return None

        # TODO da pra colocar esse sumário no pandas, talvez facilite a vida
        # for topico in texto.split('\n')[1:]:
        #     topicoPagina = self.__transformarEmLista(topico)
        #     print(topicoPagina)

        #     if 'referências' in topico.split(' ', 1)[0].lower():
        #         dic['referências'] = int(topicoPagina[-1].strip()) #- 1

        #         dic['ultima pagina'] = len(pdfLido.pages) #- 1

        #         return dic
            
        #     elif len(topicoPagina) > 1:
        #         if topicoPagina[-1].strip().isdigit():
        #             if aux != None:
        #                 dic[aux] = int(topicoPagina[-1].strip()) #- 1
        #                 aux = None
        #             else:
        #                 dic[topicoPagina[0]] = int(topicoPagina[-1].strip()) #- 1
        #         else:
        #             aux = topicoPagina[0].strip()


    def __extrairSumario(self, pdfLido :object):
        reTopico =  r'sum\s*á\s*rio'

        texto = self.__encontrarPagina(pdfLido, reTopico)
        texto = self.__limparPagina(texto)
        listaTopico = self.__transformarEmLista(texto)
        print(listaTopico)
        return self.__transformarEmDicionario(pdfLido, listaTopico)

        