class Intern():
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.name = name

    def __str__(self)-> str:
        return self.name

    def work(self) -> str:
        raise Exception("I’m just an intern, I can’t do that...")

    class Coffee():
        def __str__(self) -> str:
            return "This is the worst coffee you ever tasted."

    def make_coffee(self) -> Coffee:
        return Intern.Coffee()


def main():
    noname = Intern()
    print(noname)
    mark = Intern(name="Mark")
    print(f"My name is {mark}")
    print(mark.make_coffee())
    try:
        intern.work()
    except Exception as exception:
        print(exception)
    print(noname.work())

if __name__ == '__main__':
    main()
