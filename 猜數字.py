import random

ans = random.randint(1, 100)
guess = 0
count = 1
minValue = 1
maxValue = 100

while ans != guess and count <= 5:
    guess = int(input("輸入"+str(minValue)+"~"+str(maxValue)+"整數"))
    
    if guess >= minValue and guess <= maxValue:
        count -= 1
        print("你還剩", count, "次") 
        if guess > ans:
            maxValue = guess
            print(minValue, "至", maxValue)
            
        elif guess < ans:
            minValue = guess
            print(minValue, "至", maxValue)
             
    else:
        print("瞎嗎,", minValue, "至", maxValue)
            
if ans == guess:
    print("猜對了")
    
else:
    print(ans)
    print("猜錯了, 次數已滿")
