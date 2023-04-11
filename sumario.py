import re
from manipularPDF import limparTexto


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
                

    def __extrairTextoSumario(self, pdfLido :object) -> str:
        textoFinal = ''
        reInicioTopico =  r'sum\s*á\s*rio'
        reFimTopico = r'referências\s*\ .*\b'
        achouTopico = False

        for pagina in pdfLido.pages:
            paginaLida = pagina.extract_text()
            textoLimpo = limparTexto(paginaLida)
            
            inicioTopico = re.search(reInicioTopico, textoLimpo[:30])
            fimTopico = re.search(reFimTopico, textoLimpo)


            if inicioTopico and fimTopico:
                inicio = inicioTopico.end()
                fim = fimTopico.end()
                textoFinal = textoLimpo[inicio:fim]
                return textoFinal

            elif inicioTopico:
                inicio = inicioTopico.end()
                textoFinal = textoLimpo[inicio:]
                achouTopico = True

            elif fimTopico and achouTopico:
                fim = fimTopico.end()
                textoFinal += textoLimpo[:fim]
                return textoFinal
            
            elif achouTopico:
                textoFinal += textoLimpo
        
        return None
    
    def __excluirNumeracaoSumario(self, texto :str) -> str:
        texto = re.sub(r'\d+\.\s*', '', texto)
        return texto
    
    # alguns tópicos estão em duas linhas, é preciso padronizálos 
    def __padronizarTexto(self, texto :str) -> list:
        listaTopicos = []
        naoPadronizado = False
        aux = ''

        for topico in texto.strip().split('\n'):
            topico = topico.strip()
            # exclui a numeração do sumário
            if not topico.isdigit():
                topico = re.sub(r'^\d+\s*', '', topico)

            if topico != '':
                if topico[-1].isdigit() and naoPadronizado == False:
                    listaTopicos.append(topico)

                elif naoPadronizado == False:
                    aux = topico
                    naoPadronizado = True

                elif naoPadronizado == True:
                    listaTopicos.append(aux + ' ' + topico)
                    naoPadronizado = False

        return listaTopicos
            
    def __transformarEmDicionario(self, texto :str) -> list:
        dicTopicosSumario = {}

        for topico in texto:
            listaDividida = topico.split()
            numeroPagina = int(listaDividida[-1])
            nomeTopico = ' '.join(listaDividida[:-1])
            dicTopicosSumario[nomeTopico] = numeroPagina

        return dicTopicosSumario
    
    def __atualizarNumeracaoPaginas(self, dicionarioSumario :dict, atualizacao :int) -> dict:
        for keys, values in dicionarioSumario.items():
            dicionarioSumario[keys] = values + atualizacao
        return dicionarioSumario
    
    def __testarNumeracaoPaginas(self, pdfLido :str, dicionarioSumario :dict) -> bool:
        reTopico = r'i\s*n\s*t\s*r\s*o\s*d\s*u\s*ç\s*ã\s*o'
        paginasTopico = self.getPaginasTopico(reTopico)

        if re.search(reTopico, pdfLido.pages[paginasTopico[0]].extract_text()[:30].lower()):
            dicionarioSumario = dicionarioSumario
        elif re.search(reTopico, pdfLido.pages[paginasTopico[0] + 1].extract_text()[:30].lower()):
            dicionarioSumario = self.__atualizarNumeracaoPaginas(dicionarioSumario, 1)
        elif re.search(reTopico, pdfLido.pages[paginasTopico[0] - 1].extract_text()[:30].lower()):
            dicionarioSumario = self.__atualizarNumeracaoPaginas(dicionarioSumario, -1)
        else:
            dicionarioSumario = None

        return dicionarioSumario

    def __extrairSumario(self, pdfLido :object) -> dict:
        texto = self.__extrairTextoSumario(pdfLido)
        listaTextoPadronizado = self.__padronizarTexto(texto)
        listaTextoPadronizado.append('ultima pagina         ' + str(len(pdfLido.pages)))
        self.__sumario = dicionarioTextoPadronizado = self.__transformarEmDicionario(listaTextoPadronizado)
        return self.__testarNumeracaoPaginas(pdfLido, dicionarioTextoPadronizado)

        