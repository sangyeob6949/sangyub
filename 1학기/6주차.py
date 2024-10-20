rank = {"철수":{"중간고사":50,"기말고사":80},"영희":{"중간고사":60,"기말고사":70},"민수":{"중간고사":50,"기말고사":40}}

num1 = (rank["철수"]["중간고사"]) + (rank["철수"]["기말고사"])
num2 = (rank["영희"]["중간고사"]) + (rank["영희"]["기말고사"])
num3 = (rank["민수"]["중간고사"]) + (rank["민수"]["기말고사"])

if num1 > num2 and num1 > num3:
    print("국어 1등은 철수 입니다")
elif num2 > num1 and num2 > num3:
    print("국어 1등은 영희 입니다")
elif num3 > num1 and num3 > num2:
    print("국어 1등은 민수 입니다")
else:
    print("국어 공동 1등이 나왔습니다")
