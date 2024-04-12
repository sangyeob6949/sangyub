gugudan = int(input("몇 단까지 출력 할까요?:"))

for gugu in range(1,gugudan+1):
    print("------[",gugu,"단]------ 입니다")
    for dan in range(1,20):
        print(gugu,"x",dan,"=",gugu*dan)