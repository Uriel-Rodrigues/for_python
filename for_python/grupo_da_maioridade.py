#progrma aque leia o ano de nascimento de sete pessoas e no final mostre quantas ainda não atingiram a maoridade
# quantas ja ção maiores

from datetime import date

anoatual = date.today().year

maior = 0
menor = 0

for c in range (1,8):
    anonascimento = int(input('digite o ano de nascimento da {}° pessoa: '.format(c)))
    idade = anoatual - anonascimento

    if (idade >= 18):
        maior = maior + 1
    else:
        menor = menor + 1

print('das idades digitadas {} pessoas ainda são de menores, e {} ja é de maior '.format(menor, maior))

