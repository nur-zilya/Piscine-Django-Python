def my_var():
    i = 42
    print("42 has a type ", type(i))
    s = '42'
    print("42 has a type ", type(s))
    quarante = 'quarante-deux'
    print("quarante-deux has a type ", type(quarante))
    b = 42.0
    print("42.0 has a type ", type(b))
    l = [42]
    print("[42] has a type ", type(l))
    d = {42: 42}
    print("{42: 42} has a type ", type(d))
    t = (42,)
    print("(42,) has a type ", type(t))
    ss = set()
    print("set() has a type ", type(ss))



if __name__ == '__main__':
 my_var()