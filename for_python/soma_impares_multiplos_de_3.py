#programa que calcula a soma de todos os numeros impares multiplos de 3 no inteervalo de 1 ate 500
s = 0
cont = 0
for c in range (1, 500+1,2):
    if (c%2 != 0 and c%3 == 0):
        cont = cont + 1 #ou cont+=1
        s = s+c #ou s+=c
print('o somatorio dos numero impares multiplos de 3 entre 1 e 500 é {} foram acumulados {} valores'.format(s, cont))