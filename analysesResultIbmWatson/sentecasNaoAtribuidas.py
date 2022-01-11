def sentecasNaoAtribuidas(ibm: dict) ->int:
    sentecasNaoAtribuidas = 0
    for sentence in ibm["sentences_tone"]:
        if (len(sentence["text"])>0  and len(sentence["tones"]) == 0):
            sentecasNaoAtribuidas += 1
    return sentecasNaoAtribuidas
