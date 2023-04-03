import PyPDF2   
from string import punctuation

def removerNumeroPagina(pagina :str) -> str:
    if pagina[3:5].isdigit():
        pagina = pagina[5:]
        
    return pagina

def removerPontuacao(texto :str) -> str:
    return "".join(caractere for caractere in texto if caractere not in punctuation)


def lerPDF(arquivo :str) -> str:
    return PyPDF2.PdfReader(arquivo)

