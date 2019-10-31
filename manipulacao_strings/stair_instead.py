scanner = str(input('DIGITE O NOME: '))
s = ''
for i in scanner:
    s += i
for i in range(len(scanner)):
    h = s[0:len(scanner)-i:]
    print(h)