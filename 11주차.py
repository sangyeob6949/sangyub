def validate_resident_number(number):
    number = number.replace("-", "")

    multiply = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

    total = 0
    for i in range(12):
        total += int(number[i]) * multiply[i]

    remainder = total % 11
    check_digit = (11 - remainder) % 10

    if check_digit == int(number[-1]):
        return "유효한 주민등록번호입니다."
    else:
        return "잘못된 주민등록번호입니다."

resident_number = input("주민등록번호를 입력하세요: ")
print(validate_resident_number(resident_number))

