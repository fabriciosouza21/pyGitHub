
def emptySentence(sentences:list)->int:
    sum = 0

    for sentence in sentences:
        if  isEmpty(sentence):
            sum+=1
    return sum
    
def isEmpty(sentence):
    if not sentence["text"]:
        return True
    return False


