
def emptySentence(ibm:dict)->int:
    sum = 0

    for sentence in ibm["sentences_tone"]:
        if  isEmpty(sentence):
            sum+=1
    return sum
    
def isEmpty(sentence):
    if not sentence["text"]:
        return True
    return False


