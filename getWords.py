from sklearn.feature_extraction.text import TfidfVectorizer

def getWords(texto):

    vetorizador = TfidfVectorizer()

    vetor = vetorizador.fit_transform([texto])
    palavras = vetorizador.get_feature_names_out()

    pontuacoes = vetor.toarray()[0]

    tfidf = {}
    for palavra, pontuacao in zip(palavras, pontuacoes):
        tfidf[palavra] = pontuacao

    palavras_relevantes = sorted(tfidf, key=tfidf.get, reverse=True)[:200]

    removes = ['da', 'de', 'di', 'do', 'a', 'o', 'e','como','não','sim', 'na', 'ou', 'e', 'problema', 'pergunta', 'ser', 'será',
               'ante', 'após', 'até', 'com', 'contra', 'de', 'desde', 'em', 'entre', 'para', 'per', 'perante', 'por', 'sem', 'sob', 'sobre', 'trás',
               'nem', 'não só', 'mas também', 'mas', 'porém', 'entretanto','entanto', 'contudo', 'todavia', 'obstante',
               'se', 'uma', 'um', 'fazer', 'perguntas', 'tentei', 'você', 'ajuda', 'alguem', 'algumas', 'apagar', 'as', 'aí', 'ao', 'seja', 'sempre', 'use','todos',
               'ajudado', 'ajude'
               ]

    for remuve in removes:
        if remuve in palavras_relevantes: palavras_relevantes.remove(remuve)

    hotTopcs = {}
    i=1
    for hotTopc in palavras_relevantes[:5]:
        hotTopcs[f'ht{i}'] = hotTopc
        i += 1

    print(hotTopcs)
    return hotTopcs