import sys

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

def find_state(city):
    for abb, capital in capital_cities.items():
        if city.lower() == capital.lower():
            for state, abbrev in states.items():
                if abb.lower() == abbrev.lower():
                    return [city, state]
    return None

def find_city(state):
    for state_name in states:
        if state_name.lower() == state.lower():
            if capital_cities.get(states[state_name]):
                return [capital_cities[states[state_name]], state_name]
    return None

def split_str(str):
    vals = str.split(",")

    for val in vals:
        strip_val = val.strip(" ")
        if strip_val:
            ret_state = find_state(strip_val)
            ret_city = find_city(strip_val)
            if ret_state:
                print(f"{ret_state[0]} is the capital of {ret_state[1]}")
            elif ret_city:
                print(f"{ret_city[0]} is the capital of {ret_city[1]}")
            else:
                print(f"{strip_val} is neither  neither a capital city nor a state")

if __name__ == '__main__' :
	if len(sys.argv) == 2:
	    split_str(sys.argv[1])



