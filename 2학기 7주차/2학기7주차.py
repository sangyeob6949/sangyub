# 1번 퀴즈
import random
def lotto():
    result = []
    while len(result) < 6:
        number = random.randint(1,45)
        if number not in result:
            result.append(number)
    return result

result = lotto()
print(f"생선된 로또 번호는{result}입니다.")

# 2번 퀴즈
class gugudan:
    def __init__(self, num):
        self.num = num
    def output(self):
        print(f"---{self.num}단---")
        for dan in range(1, 10):
            print(f"{self.num} x {dan} = {self.num * dan}")

user_input = int(input("구구단을 입력하세요:"))
Gugudan = gugudan(user_input)
Gugudan.output()
