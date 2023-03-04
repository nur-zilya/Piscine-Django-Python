from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
import random

class CoffeeMachine():
    def __init__(self):
        self.num_cups = 10

    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90

        def description(self) -> str:
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.num_cups = 10
        print("Machine repaired")

    def serve(self, beverage):
        if self.num_cups:
            self.num_cups -= 1
            if not random.randint(0, 5):
                return CoffeeMachine.EmptyCup
            return beverage()
        else:
            raise self.BrokenMachineException


def main():
    coffee_machine = CoffeeMachine()
    beverages = [Coffee, Tea, Chocolate, Cappuccino]
    for _ in range(25):
        try:
            print(coffee_machine.serve(random.choice(beverages)))
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            coffee_machine.repair()


if __name__ == '__main__':
    main()