from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk
from nltk.stem import RSLPStemmer
from nltk.corpus import wordnet

from manipularPDF import removerPontuacao

from sumario import Sumario

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('floresta')   # conjunto de textos em português anotados com etiquetas morfossintáticas
nltk.download('stopwords')
nltk.download('rslp')


class TermosMaisCitados:
    def __init__(self, pdfLido: object, sumario :Sumario) -> None:
        self.__contagemTermos = self.__extrairPaginas(pdfLido, sumario)

    def __lamatizarPalavra(self, palavra :str) -> str:
        stemmer = RSLPStemmer()     # Removedor de Sufixos da Língua Portuguesa
        lemma = stemmer.stem(palavra)
        if lemma == palavra:
            synsets = wordnet.synsets(palavra, lang='por')
            if synsets:
                lemma = synsets[0].lemmas()[0].name()
        return lemma

    def __contagemTermos(self, texto :str) -> dict:
        texto = removerPontuacao(texto)
        palavras = texto.split()
        stopwordsPT = stopwords.words('portuguese')
        textoLematizado = [self.__lamatizarPalavra(palavra.lower()) for palavra in palavras if palavra.lower() not in stopwordsPT]

        return Counter(textoLematizado)
    
    def getContaTermos(self) -> dict:
        return self.__contagemTermos
    

    def nuvemPalavras(self, texto :str, quantidadePalavras: int) -> None:
        contagemPalavras = self.contagemTermos(texto)

        palavras = dict(contagemPalavras.most_common(quantidadePalavras))

        nuvem_palavras = WordCloud()
        nuvem_palavras.generate_from_frequencies(palavras)

        plt.imshow(nuvem_palavras, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    def __extrairPaginas(self, pdfLido: object, sumario :Sumario) -> list:
        textoArtigo = ''
        
        for posicao in range(0, sumario.getSumario()['referências']):
            texto = pdfLido.pages[posicao].extract_text()
            textoArtigo += texto

        

        contagemTermos = self.__contagemTermos(textoArtigo)
        return contagemTermos