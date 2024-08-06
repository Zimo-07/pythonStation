import random

lists = []

digit1 = random.randint(1, 100)
digit2 = random.randint(1, 100)

while digit1 % digit2 != 0:
    digit2 = random.randint(1, 100)

while True:
    usd = input("請輸入運算符號(1)+ (2)- (3)* (4)/")
    if usd == "1":
        a = digit1 + digit2 
        break
    
    elif usd == "2":
        a = digit1 - digit2
        break
    
    elif usd == "3":
        a = digit1 * digit2
        break
    
    elif usd == "4":
        a = digit1 / digit2
        for i in range(1, 101):
            
            if digit1 % i == 0:
                lists.append(i)                     
        break
    
    else:
        print("輸入代號")
        break
        
print("第一個數值是:", digit1)
print("第二個數值是:", digit2)
print("計算結果為:", a)
print("可被整除的數有:", lists)




