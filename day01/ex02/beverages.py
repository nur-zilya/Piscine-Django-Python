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

def main():
    print(HotBeverage(), '\n')
    # print(Coffee(), '\n')
    # print(Tea(), '\n')
    # print(Chocolate(), '\n')
    # print(Cappuccino())

if __name__ == '__main__':
    main()
