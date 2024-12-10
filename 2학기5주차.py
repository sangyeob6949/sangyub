# 1번 문제
def add(n1,n2,n3,n4):
    result = sum([n1,n2,n3,n4])
    return result
sum_result=add(1,2,3,4)
print(sum_result)

def multiply(n1,n2,n3,n4):
    result= n1*n2*n3*n4
    return result
multiply_result=multiply(1,2,3,4)
print(multiply_result)

# class number():
#     def __init__(self,num1,num2,num3,num4):
#         self.num1 = num1
#         self.num2 = num2
#         self.num3 = num3
#         self.num4 = num4
#
#     def add(self):
#         print(self.num1 + self.num2 + self.num3 + self.num4)
#
#     def multiply(self):
#         print(self.num1 * self.num2 * self.num3 *self.num4)

# 2번 문제
def a(number):
    if number % 2 == 0:
        return "짝수"
    else:
        return "홀수"

print(a(3))
# class check():
#     def __init__(self,num):
#         self.num = num
#
#     def user_check(self):
#         if num % 2 == 0:
#             print("짝수")
#         else:
#             print("홀수")
#
# num = int(input("숫자를 입력하세요>>>"))
#
# last_usercheck = check(num)
# last_usercheck.user_check()

# 3번 문제
def average(number):
    total = 0
    for i in number:
        total += i
    return total / len(number)

print(average([2,3,4,5]))

# 4번 문제
class champion:
     def __init__(self,id,gender,job):
         self.id = id
         self.gender = gender
         self.job = job
     def bark(self):
        print("공격!!!")

a = champion("이상엽","남자","마법")
print(a.id,a.gender,a.job)
a.bark()

# 5번 문제
class 부동산:
    def __init__(self,위치,평수,건물의종류,가격,준공년도):
        self.위치=위치
        self.평수=평수
        self.건물의종류=건물의종류
        self.가격=가격
        self.준공년도=준공년도
    def 정보(self):
        print(self.위치,",",self.평수,",",self.건물의종류,",",self.가격,",",self.준공년도)

my_부동산 = 부동산("충주","3000평","학교","1,000,000,000원","2002준공")
my_부동산.정보()