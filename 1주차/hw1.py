#임의의 문자열을 입력 받고, 그 문자열의 크기(길이)를 출력하라. 입력받은 문자열 중 영어 소문자의 개수를 출력하라.
#ex) input = 'ABCdefG' => length = 7, lowercase = 3

#임의의 문자열을 입력 받기.
x = input("문자열을 입력하세요: ")

#그 문자열의 크기를 출력하라
print("length: ", len(x))

# 입력 받은 문자열 중 영어 소문자의 개수를 출력하라.
#islower() 함수는 문자의 소문자 여부를 판별
lowercase_count = 0

for char in x:                              #x안에서 문자열
    if char.islower():                      #문자열 안에 소문자가 있으면
        lowercase_count += 1                #1올리세요
        
print("lowercase : ", lowercase_count)

#lowercase_count = sum(1 for char in input_string if char.islower())