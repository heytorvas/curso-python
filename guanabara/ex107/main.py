import coin
num = int(input('digite um numero: '))
print('aumentar 10% = {}'.format(coin.coin(coin.increase(num))))
print('diminuir 10% = {}'.format(coin.coin(coin.decrease(num))))
print('metade = {}'.format(coin.coin(coin.half(num))))
print('dobro = {}'.format(coin.coin(coin.double(num))))