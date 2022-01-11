def sentecasAtribuidas(ibm:dict)->int:
    sentecasAtribuidas = 0
    for sentence in ibm["sentences_tone"]:
        if (len(sentence["text"])>0  and len(sentence["tones"]) > 0):
            sentecasAtribuidas += 1
    return sentecasAtribuidas