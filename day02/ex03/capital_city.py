import sys


def find_by_key(argv):
    if len(argv) != 2:
        return 1
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    k = argv[1]
    if k in states:
        val = states[k]
        print(capital_cities[val])
    else:
        print("Unknown state")



if __name__ == '__main__':
    find_by_key(sys.argv)