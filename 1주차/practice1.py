x = float(input("입력 :"))
if x <= 0:
    while x <= 0:
        x = float(input("입력 :"))
        if (x>=1):
            break
    
O =(3.14 * x**2)

if (O>= 50):
    print("BIG")
elif (O >= 0) :
    print("NORMAL")
else :
    print("wrong")

    