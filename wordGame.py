import random

def true_or_false(guess,count):
    while guess != secret and count != 2:
        count += 1
        if guess > secret:
            print("""
猜錯啦，就說你不夠格當本姑娘的駙馬:)
不要說我對逆不好，再給逆猜一次:)
給你點提示:)
逆現在大了~~~大了~~~，回去點!!!
            """)    
        elif guess < secret:
            print("""
猜錯啦，就說你不夠格當本姑娘的駙馬:)
不要說我對逆不好，再給逆猜一次:)
給你點提示:)
逆現在小了~~~小了~~~，靠近點!!!
            """)
        guess = int(input(""))
    if guess == secret:
        print("""
我草，你是人家心中的蛔蟲嗎?!")

呼，我還是不依，撞牆去吧，你!!!!!
        """)
    else:
        print("""
哎呀!!!!這樣都猜不中，爛透了，小小孩~~~
        """)

secret = random.randint(0,9)

print("--------------------你是好人------------------")

count = 0

try:
    guess = int(input("不妨猜一下人家現在想的數字，我就跟你交往:)\n"))
    true_or_false(guess,count)
except:
    try:
        guess = int(input("""
死屁孩，輸入錯誤了，
給我重新輸入，輸入0~9之間的整數
再錯就去死:)
"""))
        true_or_false(guess,count)
    except:
        print("去死吧!!!!!")
    
print("遊戲結束，再見不聯絡:)，哈哈哈~~~~~~")
