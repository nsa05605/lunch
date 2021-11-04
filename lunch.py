import random

print("오늘 점심 뭐 먹지?")
menu = ["짜장면", "짬뽕", "라면", "김밥", "돈까스"]

for i in menu :
    print(i)
    print("이 중에서 엄청난 알로리즘으로 당신의 머릿속을 분석하여 추천하는 메뉴")
    print("두구 두구 두구 두구~~~~")
a = random.randint(0, 4)
print("{} 입니다".format(menu[a]))