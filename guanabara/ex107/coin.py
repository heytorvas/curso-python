def increase(n):
    return n + (n * 0.1)

def decrease(n):
    return n - (n * 0.1)

def double(n):
    return n * 2

def half(n):
    return n / 2

def coin(n, coin='R$'):
    return '{}{}'.format(coin, n)