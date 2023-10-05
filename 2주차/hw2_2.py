def my_plus(x, y):
    result = x + y
    return result
    
def my_minus(x,y):
    result = x - y
    return result

def my_multiply(x,y):
    result = x * y
    return result

def my_division(x,y):
    result = x/y
    return result

def my_calculate(x,y,operator):
    if operator == "+":
        return my_plus(x,y)
    elif operator == "-":
        return my_minus(x,y)
    elif operator == "*":
        return my_multiply(x,y)
    elif operator == "/":
        return my_division(x,y)
    else:
        return "잘못된 연산 기호입니다."
    

while True:
    try:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        if num1 == "q":
            break
        operator = input("연산 기호를 입력 하세요. (+, -, *(곱하기), /(나누기)): ")
        if operator not in [["+", "-", "*", "/"]]:
            print("잘못된 연산 기호입니다.")
            continue
        num2 = float(input("두 번째 숫자를 입력하세요: "))

        result = my_calculate(num1,num2,operator)
        
        print("계산 결과 : " ,result)
        break


    except ValueError:
        print("숫자를 입력하세요")
    except ZeroDivisionError:
        print("0으로는 숫자를 나눌 수 없습니다.")
        
        
    """ (5, 3, '+', 8),  # 덧셈 테스트
        (10, 7, '-', 3),  # 뺄셈 테스트
        (2.5, 1.5, '*', 3.75),  # 곱셈 테스트
        (8, 2, '/', 4.0),  # 나눗셈 테스트
        (5, 0, '/', "0으로는 숫자를 나눌 수 없습니다."),  # 0으로 나누는 테스트
        (5, 3, '%', "잘못된 연산 기호입니다."),  # 잘못된 연산 기호 테스트
    """