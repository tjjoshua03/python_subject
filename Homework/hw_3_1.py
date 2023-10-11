# 함수로 가장 큰 수와 두 번째로 큰 수를 출력
def quiz_5(num):
    num.sort()
    print(num[-1],num[-2])

# 실행문
num_list = []

while True:
    num = input("숫자를 입력하시오: ")
    if num == "":
        break
    num_list.append(int(num))

quiz_5(num_list)
