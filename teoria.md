# N-grama
usado para prever a próxima letra ou caractere em uma sequência de texto
esse modelo é definido como uma cadeia de Markov de ondem n - 1

o texto é dividio em n-gramas, onde n é representa o número de caracteres em cada bloco.
exemplo: "Hello, how are you?" seria dividida em "Hel", "ell", "llo", "lo,", "o, ", ", h", " ho", "how", "ow ", "w a", " ar", "are", "re ", "e y", " yo", "you", "ou?". Neste caso, n = 3.

o modelo de caracteres n-grama calcula a frequência de cada n-grma e usa isso para prever a próxima letra ou caractere.Para fazer uma previsão, o modelo procura o N-grama mais semelhante à sequência atual e usa a frequência de ocorrência desse N-grama para prever a próxima letra ou caracteres.

O modelo de caracteres de N-grama pode ser usado em uma variedade de tarefas de processamento de linguagem natural, como a correção automática de erros ortográficos, a predição de palavras em um aplicativo de digitação e a geração de texto em um modelo de linguagem natural.

