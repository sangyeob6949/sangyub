class Fish_bun:
    def __init__(self, name, price):
        self.contents = name
        self.price = price
        self.total = 0
    def sell(self):
        self.total += self.price
        print(self.contents,"을",self.price,"원에 판매 하였습니다.")
    def eat(self):
        print(self.contents +"을 먹는다")

cream_bun = Fish_bun("슈붕",1000)
cream_bun.sell()

result = Fish_bun("슈붕",1000)
result.sell()
result.sell()
result.sell()
result.sell()
print(result.total)

