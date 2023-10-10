#임의의 문자열을 입력 받고, 영문 소문자 'a'가 처음 등장하는 곳 다음부터 'z'가 처음 등장하기 전까지의 문자열만 필터링하여 출력하라
#ex)input = "xyzabazcdeabz" / ASCIICODE / A<Z -> True A>Z-> False, A < a -> True, A > a -> False 

input_x = input("문자열을 입력하세요: ")

#영문 소문자 'a'가 처음 등장하는 곳 찾기
find_a = input_x.find('a')

#'a'가 처음 등장하는 곳 다음부터 'z'가 처음 등장하는곳 찾기
find_z = input_x[find_a:].find('z')

filtered = input_x[find_a + 1:find_a + find_z]

print("필터링 된 문자열: ", filtered)