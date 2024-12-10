# 1번 퀴즈
a = input("인사를 먼저하세요<<<")

if a == "안녕하세요" :
    print("반갑습니다")
else:
    print("인사를 먼저하세요")

# 2번 퀴즈
a = int(input("값을 입력하세요<<<"))

c = 100 + a

if c >= 150:
    print(c)
else:
    print("값이 부족합니다")

# 3번 퀴즈
results = []

numbers = [100,200,300]

for a in numbers:
   b= a * 1.1
   results.append(b)
print(results)

# 4번 퀴즈
numbers = [3, 100, 23, 33, 72, 94]
result = []

for a in numbers:
    if a % 3 == 0:
        result.append(a)
print(result)

# 5번 퀴즈

# 6번 퀴즈
a = 1
sum = 0
while a <= 100:
    if a % 3 == 0:
        sum = +a
    a += 1
print(sum)
































