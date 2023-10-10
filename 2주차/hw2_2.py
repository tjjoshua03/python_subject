def generateDictionary(x):
    Dictionary = {}
    for i in range(x):
        word = str(input("Input word: "))
        description = str(input("Input description: "))
        Dictionary[word] = description
    return Dictionary

num = int(input("Input the number of words: "))
KorDic = generateDictionary(num)
print(KorDic)

def translateDictionary(dic):
    EngDic = {}
    for key in dic.keys():
        print("Description: ",dic[key])
        EngWord = input("Input new word: ")
        EngDic[EngWord] = dic[key]
    return EngDic

EngDic = translateDictionary(KorDic)
print(EngDic)

def searchEngine(dic):
    search = input("Input description for seearch: ")
    for findword in dic.keys():
        if search in dic[findword]:
            return(findword)
        
while(1):
    search = searchEngine(EngDic)
    print(search)