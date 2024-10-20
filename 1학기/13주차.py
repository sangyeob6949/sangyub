class Beverage:
    def __init__(self, name, price):
        self.order = {"커피": 3000, "녹차": 2500, "아이스티": 3000}
        self.name = name
        self.price = price

    def sell(self):
        if self.name == "커피" or self.name == "녹차" or self.name == "아이스티":
            print(f"음료의 총 가격은 {self.order[self.name] * self.price}입니다.")
        else:
            print("다시 주문해 주세요:")


name = input("주문할 음료를 선택하세요 (커피, 녹차, 아이스티): ")
price = int(input("수량을 선택하세요: "))

beverage = Beverage(name, price)
beverage.sell()




