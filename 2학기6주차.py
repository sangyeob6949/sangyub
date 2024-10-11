class user:
    def __init__(self,name,age,phone):
        self.name = name
        self.age = age
        self.phone = phone

    def info(self):
        print(f'가입하신 계정의 이름은 {self.name}이며, 나이는{self.age}, 그리고 연락처는{self.phone}입니다')

name = input("이름을 입력하세요>>>")
age = input("나이를 입력하세요")
phone = input("전화번호를 입력하세요 ex)000-0000-0000>>>")

User = user(name,age,phone)
User.info()


a = input("메세지를 입력하세요>>>")
def check_length_of_message(message):
    Q=len(message)
    if Q <= 20:
        return 50
    else:
        return 100

print(check_length_of_message(a))



