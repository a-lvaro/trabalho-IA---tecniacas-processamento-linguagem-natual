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
            if re.match(topicoRegex, keys) and len(posicaoPaginas) == 0:
                posicaoPaginas.append(values)
            elif len(posicaoPaginas) == 1:
                posicaoPaginas.append(values)
                return posicaoPaginas
                

    def __extrairTextoSumario(self, pdfLido :object) -> str:
        texto = ''
        reInicioTopico =  r'sum\s*á\s*rio'
        reFimTopico = r'referências\s*\ .*\b'
        achouTopico = False

        for pagina in pdfLido.pages:
            paginaLida = pagina.extract_text().lower()
            
            inicioTopico = re.search(reInicioTopico, paginaLida[:30])
            fimTopico = re.search(reFimTopico, paginaLida)

            if inicioTopico and fimTopico:
                inicio = inicioTopico.end()
                fim = fimTopico.end()
                texto = pagina.extract_text()[inicio:fim]
                return texto

            elif inicioTopico:
                inicio = inicioTopico.end()
                texto = pagina.extract_text()[inicio:]
                achouTopico = True

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
    
    def __excluirNumeracaoSumario(self, texto :str) -> str:
        texto = re.sub(r'\d+\.\s*', '', texto)
        return texto
    
    # alguns tópicos estão em duas linhas, é preciso padronizálos 
    def __padronizarTexto(self, texto :str) -> list:
        listaTopicos = []
        naoPadronizado = False
        aux = ''

        for topico in texto.strip().split('\n'):
            # exclui a numeração do sumário
            topico = re.sub(r'^\d+\s*', '', topico.strip())

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

    def __extrairSumario(self, pdfLido :object) -> dict:
        texto = self.__extrairTextoSumario(pdfLido)
        texto = self.__limparPagina(texto)
        listaTextoPadronizado = self.__padronizarTexto(texto)
        listaTextoPadronizado.append('ultima pagina         ' + str(len(pdfLido.pages)))
        return self.__transformarEmDicionario(listaTextoPadronizado)

        