#programa que le 6 numero do teclado e faz a soma dos numeros pares e desconcidera os impares

s = 0
cont = 0
for c in range(1, 6+1):
    n = int(input('digite um numero: '))
    if (n%2 == 0 ):
        s = s + n
        cont = cont +1

print('a soma dos numeros pares digitados é {} vc informou {} numeros pares'.format(s, cont))