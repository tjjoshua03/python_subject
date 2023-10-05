while True:
    def my_plus(x, y):
        result = x + y
        return result

    try:
        num1 = float(input("첫 번째 숫자를 입력하세요 : "))
        num2 = float(input("두 번째 숫자를 입력하세요 : "))

        result = my_plus(num1, num2)
        print("Sum is ",result)
        break
    except ValueError:
        print("숫자를 입력하세요")
        
        
        """1. 양수 + 양수
                x = 12
                y = 10
                result = Sum is 22
            2. 음수 + 음수 
                x = -20
                y = -10
                result = Sum is -30
            3. 양수 + 음수
                x = 40
                y = - 20
                result = Sum is 20
            4. 소수점 + 소수점 
                x = 20.2
                y = 0.8
                result = Sum is 21.0
            
        """