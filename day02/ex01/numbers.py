def print_numbers():
    with open('numbers.txt') as f:
        file = f.read()
        separated = file.split(',')
        for n in separated:
            print(n)

if __name__ == '__main__':
 print_numbers()