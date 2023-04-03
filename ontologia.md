Entidades: ArtigoCientífico, Título, Autor, Resumo, Introdução, Metodologia, Resultados, Discussão

Atributos:
- ArtigoCientífico: título (Título), autores (lista de Autor), resumo (Resumo), introdução (Introdução), metodologia (Metodologia), resultados (Resultados), discussão (Discussão)
- Autor: nome (string), afiliação (string)

Relações:
- ArtigoCientífico --tem--> Título
- ArtigoCientífico --tem--> Autor
- ArtigoCientífico --tem--> Resumo
- ArtigoCientífico --tem--> Introdução
- ArtigoCientífico --tem--> Metodologia
- ArtigoCientífico --tem--> Resultados
- ArtigoCientífico --tem--> Discussão

Restrições:
- Um ArtigoCientífico deve ter pelo menos um autor.
- Um ArtigoCientífico deve ter exatamente um título, resumo, introdução, metodologia, resultados e discussão.


# Próximo
Identificando os principais elementos:
Título
Resumo
Introdução
Métodos
Resultados
Discussão
Conclusão
Referências Bibliográficas
Definindo as propriedades de cada elemento:
Título: tem a propriedade "texto" que descreve o conteúdo do título.
Resumo: tem a propriedade "texto" que descreve o conteúdo do resumo.
Introdução: tem a propriedade "texto" que descreve o conteúdo da introdução.
Métodos: tem a propriedade "texto" que descreve o conteúdo dos métodos.
Resultados: tem a propriedade "texto" que descreve o conteúdo dos resultados.
Discussão: tem a propriedade "texto" que descreve o conteúdo da discussão.
Conclusão: tem a propriedade "texto" que descreve o conteúdo da conclusão.
Referências Bibliográficas: tem a propriedade "texto" que descreve as referências bibliográficas do artigo.
Identificando as relações entre os elementos:
A Introdução está relacionada aos Métodos e Resultados.
A Discussão está relacionada aos Métodos e Resultados.
A Conclusão está relacionada à Introdução, Métodos, Resultados e Discussão.
O artigo tem um único Título, Resumo e Referências Bibliográficas, mas pode ter várias seções de Introdução, Métodos, Resultados, Discussão e Conclusão.
Definindo as classes para cada elemento:
Artigo Científico: Classe que engloba todos os elementos.
Título: Classe específica para o título.
Resumo: Classe específica para o resumo.
Introdução: Classe específica para a introdução.
Métodos: Classe específica para os métodos.
Resultados: Classe específica para os resultados.
Discussão: Classe específica para a discussão.
Conclusão: Classe específica para a conclusão.
Referências Bibliográficas: Classe específica para as referências bibliográficas.
Criando hierarquias de classes:
Artigo Científico: superclasse que engloba todos os elementos.
Elemento do Artigo: subclasse que engloba os elementos específicos.
Título: subclasse específica para o título.
Resumo: subclasse específica para o resumo.
Introdução: subclasse específica para a introdução.
Métodos: subclasse específica para os métodos.
Resultados: subclasse específica para os resultados.
Discussão: subclasse específica para a discussão.
Conclusão: subclasse específica para a conclusão.
Referências Bibliográficas: subclasse específica para as referências bibliográficas.
Identificando as restrições e restrições de cardinalidade:
A propriedade "texto" da classe "Título", "Resumo", "Introdução", "Métodos", "Resultados", "Discussão" e "Conclusão" deve ter apenas um valor.
A propriedade "texto" da classe "Referências Bibliográficas