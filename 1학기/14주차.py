menu = ["냉면","볶음밥","피자","짜장면"]

while True:
    try:
        user_input = input("메뉴를 숫자로 입력하세요 (1:냉면, 2:볶음밥, 3:피자, 4:짜장면):")
        menu_number = int(user_input)
        food = menu[menu_number - 1]

        print(f"선택한 음식은 {food} 입니다.")
        break

    except ValueError:
        print("유효하지 않은 번호입니다. 다시 입력해주세요.")

    except IndexError:
        print("메뉴에 없는 번호입니다. 다시 입력해주세요.")

