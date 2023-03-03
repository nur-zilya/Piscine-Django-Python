import os
import sys
import settings


def check_args():
    if len(sys.argv) != 2:
        return sys.stderr.write('Wrong number of arguments\n')
    if os.path.splitext(sys.argv[1])[1] != '.template':
        return sys.stderr.write('Wrong extension\n')
    if not os.path.isfile(sys.argv[1]):
        return sys.stderr.write('File does not exist\n')
    return 0


def main():
    if check_args():
        sys.exit(1)
    file = open(sys.argv[1], 'r')
    tmp = "".join(file.readlines()).format(
        title=settings.title,
        style=settings.style,
        name=settings.name,
        surname=settings.surname,
        age=settings.age,
        profession=settings.profession)
    file.close()
    file = open('file.html', 'w')
    file.write(tmp)
    file.close()


if __name__ == '__main__':
    main()