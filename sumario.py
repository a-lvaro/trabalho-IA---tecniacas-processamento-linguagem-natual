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
                

    def __extrairTextoSumario(self, pdfLido :object) -> list:
        textoFinal = ''
        reInicioTopico =  r'sum\s*á\s*rio'
        reFimTopico = r'referências\s*\ .*\b'
        achouTopico = False
        posicaoSumario = None

        for posicao, pagina in enumerate(pdfLido.pages):
            paginaLida = pagina.extract_text()
            textoLimpo = limparTexto(paginaLida)
            
            inicioTopico = re.search(reInicioTopico, textoLimpo[:30])
            fimTopico = re.search(reFimTopico, textoLimpo)

            if inicioTopico and fimTopico:
                inicio = inicioTopico.end()
                fim = fimTopico.end()
                textoFinal = textoLimpo[inicio:fim]
                posicaoSumario = posicao
                return textoFinal, posicaoSumario

            elif inicioTopico:
                inicio = inicioTopico.end()
                textoFinal = textoLimpo[inicio:]
                achouTopico = True
                posicaoSumario = posicao

            elif fimTopico and achouTopico:
                fim = fimTopico.end()
                textoFinal += textoLimpo[:fim]
                return textoFinal, posicaoSumario
            
            elif achouTopico:
                textoFinal += textoLimpo
        
        return None, None
    
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
            if keys != 'ultima pagina':
                dicionarioSumario[keys] = values + atualizacao
        return dicionarioSumario
    
    def __testarNumeracaoPaginas(self, pdfLido :str, dicionarioSumario :dict) -> bool:
        reTopico = r'i\s*n\s*t\s*r\s*o\s*d\s*u\s*ç\s*ã\s*o'
        paginasTopico = self.getPaginasTopico(reTopico)

        if re.search(reTopico, pdfLido.pages[paginasTopico[0]].extract_text()[:30].lower()) and dicionarioSumario['sumario'] != paginasTopico[0]:
            dicionarioSumario = dicionarioSumario
        else:
            naoEcontrou = True
            posicaoContador = dicionarioSumario['sumario'] + 1
            # print('========================')
            # print(dicionarioSumario['sumario'])
            # print(posicaoContador)
            # print('========================')
            while naoEcontrou:
                pagina = pdfLido.pages[posicaoContador].extract_text()
                if re.search(reTopico, pagina[:30].lower()):
                    dicionarioSumario = self.__atualizarNumeracaoPaginas(dicionarioSumario, posicaoContador - paginasTopico[0])
                    naoEcontrou = False
                posicaoContador += 1

        return dicionarioSumario

    def __extrairSumario(self, pdfLido :object) -> dict:
        texto, posicaoSumario = self.__extrairTextoSumario(pdfLido)
        listaTextoPadronizado = self.__padronizarTexto(texto)
        listaTextoPadronizado.append('sumario         ' + str(posicaoSumario))
        listaTextoPadronizado.append('ultima pagina         ' + str(len(pdfLido.pages) - 1))
        self.__sumario = dicionarioTextoPadronizado = self.__transformarEmDicionario(listaTextoPadronizado)
        return self.__testarNumeracaoPaginas(pdfLido, dicionarioTextoPadronizado)

        