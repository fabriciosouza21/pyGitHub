from analysesResultIbmWatson.emptySentence import emptySentence
from analysesResultIbmWatson.quantidadeSentecas import quantidadeSentecas
from analysesResultIbmWatson.sentecasAtribuidas import sentecasAtribuidas
from analysesResultIbmWatson.sentecasNaoAtribuidas import sentecasNaoAtribuidas

def analysisResultIbmWatson(sentencesTone: list) -> dict:
    result = {}
    result["quantidadeSentecas"] = quantidadeSentecas(sentencesTone)
    result["sentecasAtribuidas"] = sentecasAtribuidas(sentencesTone)
    result["sentecasNaoAtribuidas"] = sentecasNaoAtribuidas(sentencesTone)
    result["emptySentence"] = emptySentence(sentencesTone)
    return result
