def get_grades():
    list_x = []
    while True:
        my_input = input(" Enter a number :")
        if my_input != "done":
            list_x.append(int(my_input))
        else :
            break
    return list_x
    
final_list = get_grades()
    
for i in final_list:
    print(i)
    if i >= 70:
        print(i, "면허증 발급 결정")
    else :
        print(i,"면허증 발급 취소")