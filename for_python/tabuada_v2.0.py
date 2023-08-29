#programa que le um numero do usuario e diz a tabuada usando FOR

numero = int(input('digite o numero da tabuada: '))

for c in range (1, 10+1):
    m = c * numero
    print('veja sua tabuada abaixo \n')
    print('{} x {} = {}'.format(c, numero,m))