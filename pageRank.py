from artigo import Artigo
import PyPDF2
import os

def pageRank(nome_artigo):
    artigo = Artigo(nome_artigo)

    #Parte 1 da equação
    d = 0.85 #fator amortecimento
    n = contadorPaginas(nome_artigo)
    parte1 = (1-d)/n

    #Parte 2 da equação
    entrada = arquivosEntrada(nome_artigo)

    if entrada == False:
        print("Infelizmente, não é possível calcular o rank desse arquivo")
        return False

    parte2 = 0
    for nome_arquivo in entrada:
        artigoRef = Artigo(nome_arquivo)
        linksSaidaRef = contLinkSaida(artigoRef)
        rankRef = pageRank(nome_arquivo)
        parte2 += rankRef/linksSaidaRef
    
    parte2 *= d

    rank = parte1 + parte2
       
    return rank

def getTitulo(nome_artigo):
    article = open(nome_artigo, 'rb')
    pdf_reader = PyPDF2.PdfReader(article)
    titulo = pdf_reader.metadata.get('/Title')
    metadata = pdf_reader.metadata
    article.close()

    # Lendo todos os metadados dos arquivos
    for key, value in metadata.items():
        print(f'{key}: {value}')
    
    print('O título aqui:')
    print(titulo)
    return titulo


def contadorPaginas(nome_artigo):
    with open(nome_artigo, 'rb') as article:
        pdf_reader = PyPDF2.PdfReader(article)
        paginas = len(pdf_reader.pages)
    print("A quantidade de páginas")
    print(paginas)
    return paginas

def listagemArquivos(caminho_pasta):
    lista_arquivos = os.listdir(caminho_pasta)
    print("Os arquivos:")
    print(lista_arquivos)
    return lista_arquivos


def arquivosEntrada(nome_artigo):
    arquivos_que_referenciam = []
    artigo = Artigo(nome_artigo)
    pasta = localizar_pasta(nome_artigo)
    documentos = listagemArquivos(pasta)
    titulo = nome_artigo.split('/')[1]
    titulo = titulo[:-4].lower()
    print('aaaaaaaaaaaaaaaaaaaaa')
    print(titulo)
    for documento in documentos:
        referencia = artigo.getReferencia()
        for item in referencia:
            minusculo = item.lower()
            if titulo in minusculo:
                nome_artigo_novo = pasta + '/' + documento
                print('AQUI O NOVO ARTIGO Ó:', nome_artigo_novo)
                arquivos_que_referenciam.append(nome_artigo_novo)
            else:
                print('título não encontrado na referencia')
    return arquivos_que_referenciam



# Alguns artigos retornam apenas 1 lista com 1 string ;-;
# Um outro contou 101, sendo que são 115
def contLinkSaida(artigo):
    numRef = len(artigo.getReferencia())
    print("Referenciou")
    print(numRef)
    return numRef

def localizar_pasta(nome_artigo):
    caminho_pasta = nome_artigo.split('/')[0]
    print("Nome da pasta: ")
    print(caminho_pasta)
    return caminho_pasta

endereco = 'artigos'
pasta = listagemArquivos(endereco)
rank = dict()
for arquivo in pasta:
    nome_documento = endereco + '/' + arquivo
    print(nome_documento)
    pontuacao = pageRank(nome_documento)
    rank[arquivo] = pontuacao

rank_ordenado = sorted(rank.items(), key=lambda x: x[1], reverse=True)
for item in rank_ordenado:
    print('NOME: ', item[0], 'NOTA: ', item[1])




# pageRank(nome_artigo)


#O numero de referencias nao esta retornando o que deve (115) :(
# contLinkSaida(text)

# linkSaida(text)