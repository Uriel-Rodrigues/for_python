#crie um programa que leia uma frase e diga se ela é um palindromo desconciderando os espaços

frase = str(input('digite a sua frase ')).strip().upper()
quebra = frase.split()
juntando = ''.join(quebra)
inverso = ''
for letra in range (len(juntando)-1, -1, -1):  #com esse for nos fizemos uma caminhada pela string contando começando da ultima ate a primeira letra
    inverso = inverso + juntando[letra] #aqui inverso recebeu 0 e com juntando[letra] nos aplicamos as coisas que não feitas na variavel
    #juntando em letra
    #print(juntando[letra])
print(juntando, inverso)
if (juntando == inverso):
    print('sua palavra é um palindromo')
else:
    print('nao é um palindromo')