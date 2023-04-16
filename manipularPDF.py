import re
import PyPDF2   
from string import punctuation

def removerNumeroPagina(pagina: str) -> str:
    padrao0 = r'\d+\b'
    padrao1 = r'(\w+\s|)\d+\d'
    padrao2 = r'\w+(í)\w+\s\d.\s\w+(çã)\w\s\d+'
    padrao3 = r'\w+(í)\w+\s*\d.\s*\w+\s*\w+\s*[a-zà-ú]+\s*\d+\n'
    
    busca0 = re.search(padrao0, pagina[:5])
    busca1 = re.search(padrao1, pagina[:10])
    busca2 = re.search(padrao2, pagina[:30])
    busca3 = re.search(padrao3, pagina[:50])
    
    if busca0:
        termina = busca0.end()
        pagina = pagina[termina:]
    elif busca1:
        termina = busca1.end()
        pagina = pagina[termina:]
    elif busca2:
        termina = busca2.end()
        pagina = pagina[termina:]
    elif busca3:
        termina = busca3.end()
        pagina = pagina[termina:]
        
    return pagina

def removerPontuacao(texto :str) -> str:
    return "".join(caractere for caractere in texto if caractere not in punctuation)

def limparTexto(texto :str) -> str:
    texto = texto.lower()
    texto = removerNumeroPagina(texto)
    texto = removerPontuacao(texto)
    return texto

# é usado na classe problema. Será que é necessário?
def removerBarraN(texto :str) -> str:
    return texto.replace('\n', ' ')

def lerPDF(arquivo :str) -> str:
    return PyPDF2.PdfReader(arquivo)

