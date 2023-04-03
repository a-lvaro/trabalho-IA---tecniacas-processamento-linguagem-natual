import re

class Sumario:
    def __init__(self, pdfLido) -> None:
        self.__sumario = self.__sumario(pdfLido)

    def getSumario(self) -> dict:
        return self.__sumario
    33
    def getPaginasTopico(self, topico :str) -> list:
        paginas = []
        for keys, values in self.__sumario.items():
            if topico in keys:
                paginas.append(values)
                if len(paginas) == 2:
                    return paginas

    def __encontrarSumario(self, pdfLido):
        for pagina in pdfLido.pages:
            if 'sumário' in pagina.extract_text().lower()[:30]:
                return pagina.extract_text()
    
    def __sumario(self, pdfLido):
        pagina = self.__encontrarSumario(pdfLido)
        dic = {}
        aux = None

        for i in pagina.split('\n')[1:]:
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