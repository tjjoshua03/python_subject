def generateDictionary(n):
    dictionary = {}
    
    for i in range(n):
        word = input("단어 입력: ")
        mean = input("뜻 입력: ")
        dictionary[word] = mean
        
    return dictionary

n = int(input("단어 개수 입력: "))
result = generateDictionary(n)

print("생선된 딕셔너리: ")
for word, mean in result.items():
    print(f"{word} : {mean}")