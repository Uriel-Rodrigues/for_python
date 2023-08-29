#programa que le um numero inteiro e diz se é ou nao primo
#divisivel por um ou por ele mesmo
num = int(input('digite um numero para ver se ele é primo: '))
total = 0
for c in range (1, num+1):
    if (num % c == 0):
        print('\033[33m', end=' ')
        total = total + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c),end='')
print('\n\033[m0 numero {} foi divisivel {} vezes'.format(num,total))
if (total == 2):
    print('o seu numero é primo')
else:
    print('seu numero nao é orimo')
