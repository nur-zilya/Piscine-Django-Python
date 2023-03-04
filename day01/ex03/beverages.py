class HotBeverage():
    def __init__(self, price=0.30, name="hot beverage"):
        self.price = price
        self.name = name

    def description(self) -> str:
        return "Just some hot water in a cup."

    def __str__(self):
        return "name : " + self.name + \
               "\nprice : " + "{0:.2f}".format(self.price) + \
                    "\ndescription : " + self.description()

class Coffee(HotBeverage):
    def __init__(self):
        self.name = "coffee"
        self.price = 0.40

    def description(self) -> str:
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self):
        self.name = "tea"
        self.price = 0.30

    def description(self) -> str:
        return "Just some hot water in a cup."

class Chocolate(HotBeverage):
    def __init__(self):
        self.name = "chocolate"
        self.price = 0.50

    def description(self) -> str:
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self):
        self.name = "cappucino"
        self.price = 0.45

    def description(self) -> str:
        return "Un po’ di Italia nella sua tazza!"


def main():
    print(HotBeverage(), '\n')
    print(Coffee(), '\n')
    print(Tea(), '\n')
    print(Chocolate(), '\n')
    print(Cappuccino())

if __name__ == '__main__':
    main()
