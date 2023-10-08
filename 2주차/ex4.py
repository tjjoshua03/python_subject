EtoF = {'bread' : 'pain', 'wine' : 'vin', 'with' : 'avec', 'I': 'Je',
        'eat' : 'mange', 'drink' : 'bois', 'John': 'Jean', 'friends' : 'aims',
        'and' : 'et', 'of' : 'du', 'red' : 'rouge'}
FtoE = {'pain' : "bread", "vin" : "wine", "avec" : "with", "Je": "I", 
        "mange" : "eat", "bois" : "drink", "jean" : "john", "aims" : "frinds",
        'et' : 'and', 'du' : 'of', "rouge" : "red"}
dicts = {'English to French' : EtoF, "French to English" : FtoE}

def translateWord(word, dictionary):
    if word in dictionary.keys():
        return dictionary[word]
    elif word != '':
        return '"'+ word + '"'
    return word

def translate(phrase, dicts, direction):
    UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LULetters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCLetters + UCLetters
    dictionary = dicts[direction]
    transition = " "
    word = " "
    
    for c in phrase:
        if c in phrase:
            word = word + c
        else:
            transition = translation +translateWord(word, dictionary) + c
            word = " "
    
    return transition + " " + translateWord(word, dictionary)

print(translate("I drink good red wine, and eat bread.", EtoF ,'Enlish to French'))