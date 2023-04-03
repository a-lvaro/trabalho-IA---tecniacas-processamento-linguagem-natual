import re

class Sumario:
    def __init__(self, pagina) -> None:
        self.__sumario = self.__sumario(pagina)

    def getSumario(self):
        return self.__sumario
    33
    def getPaginasTopico(self, topico):
        paginas = []
        for keys, values in self.__sumario.items():
            if topico in keys:
                paginas.append(values)
                if len(paginas) == 2:
                    return paginas

    
    def sumario(pagina):
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