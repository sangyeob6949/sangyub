def validate_resident_number(number):
    number = number.replace("-", "")  # 하이픈 제거

    multiply = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

    total = 0
    for i in range(12):
        total += int(number[i]) * multiply[i]  # int(number[i])로 수정

    remainder = total % 11
    check_digit = 11 - remainder # 체크 디지털 계산 수정

    if check_digit == int(number[-1]):
        return "유효한 주민등록번호"
    else:
        return "유효하지 않은 주민등록번호"


resident_number = input("주민등록번호를 입력하세요>>> ")
print(validate_resident_number(resident_number))
