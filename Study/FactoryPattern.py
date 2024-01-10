from enum import Enum

class CoffeeType(Enum):
    Latte = 1
    Espresso = 2

class Coffee:
    def __init__(self, price, name):
        self.price = price
        self.name = name
    
    def get_coffee(self):
        print(f"{self.name}의 가격은 {self.price}원입니다.")

class Latte(Coffee):
    def __init__(self, price):
        super().__init__(price, "라떼")
    
    def iam_latee(self):
        pass

class Espresso(Coffee):
    def __init__(self, price):
        super().__init__(price, "에스프레소")
    
    def iam_espresso(self):
        pass

class CoffeeFactory:

    @staticmethod
    def create_coffee(coffee: CoffeeType, price) -> Coffee:
        if coffee is CoffeeType.Latte:
            return Latte(price)
        elif coffee is CoffeeType.Espresso:
            return Espresso(price)
        else:
            return Coffee(1000, "커피")
        

coffee1 = CoffeeFactory.create_coffee(CoffeeType.Latte, 1500)
coffee2 = CoffeeFactory.create_coffee(CoffeeType.Espresso, 2000)

coffee1.get_coffee()
coffee2.get_coffee()