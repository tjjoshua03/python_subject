import random

# 무작위 숫자 선택
computer_number = random.randint(1, 100)

# 시도 횟수 초기화
attempts = 0

print("1에서 100 사이의 숫자를 맞춰보세요.")

while True:
    # 사용자로부터 숫자 입력 받기
    user_guess = int(input("숫자를 입력하세요: "))
    
    # 시도 횟수 증가
    attempts += 1
    
    # 입력한 숫자와 컴퓨터의 숫자 비교
    if user_guess < computer_number:
        print("더 큰 숫자를 입력하세요.")
    elif user_guess > computer_number:
        print("더 작은 숫자를 입력하세요.")
    else:
        print(f"축하합니다! {computer_number}를 맞췄습니다.")
        print(f"{attempts}번 만에 맞췄습니다.")
        break
