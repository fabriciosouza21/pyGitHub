
def toString(dict):
    tonesNames = ""
    tonesScores = ""
    sentence = dict["text"]
    tones = []
    for tone in dict["tones"]:
        toneName = tone["tone_name"]
        toneScore = tone["score"]
        tones.append((toneName, toneScore))

    for tone in tones:
        tonesNames = f"{tonesNames} {tone[0]}"
        tonesScores = f"{tonesScores} {tone[1]}"

    return f'{tonesNames},{tonesScores}, "{sentence}"\n'
