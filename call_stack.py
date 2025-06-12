def a():
    print('a() starts')
    b()
    d()
    print('a() returrns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starst')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()