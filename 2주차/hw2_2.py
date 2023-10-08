def generateDictionary(n):
    dictionary = {}  
    for i in range(n):
        word = input("단어 입력: ") 
        meaning = input("뜻 입력: ") 
        dictionary[word] = meaning  

    return dictionary

n = int(input("단어 개수 입력: ")) 
result = generateDictionary(n)  


print("생성된 딕셔너리:")
for key in result:
    print(result[key])
