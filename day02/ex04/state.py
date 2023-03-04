import sys

def find_by_val(argv):
    if len(argv) != 2:
        return 1
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    state = ""
    v = argv[1]
    for key, val in capital_cities.items():
        if val == v:
            state = key
            break
    for key, val in states.items():
        if val == state:
            print(key)
            return 0
    print("Unknown capital city")


if __name__ == '__main__':
    find_by_val(sys.argv)