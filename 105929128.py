import random

digit1 = random.randint(1, 100)
digit2 = random.randint(1, 100)
a = True

while digit1 % digit2 != 0:
    digit2 = random.randint(1, 100)
    
print("第一個數值是:", digit1)
print("第二個數值是:", digit2)

while a:
    user = input("請輸入想運算符號(1)+ (2)- (3)* (4)/")
    if user == "1":
        sum = digit1 + digit2 
        print("計算結果為:", sum)
        a = False
        
    elif user == "2":
        sum = digit1 - digit2
        print("計算結果為:", sum)
        a = False
        
    elif user == "3":
        sum = digit1 * digit2
        print("計算結果為:", sum)
        a = False
        
    elif user == "4":
        sum = digit1 / digit2
        print("計算結果為:", sum) 
        a = False
            
    else:
        print("請從1~4之間選擇")



