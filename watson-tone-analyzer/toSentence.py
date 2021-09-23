
def toSentence(comment):
    sentences = comment.split(".")
    return [f'{sentence}.' for sentence in sentences if sentence!=""]

