#programa que leia o nome, idade e sexo de 4 pessoas no final do programa, mostre : a media de idade do grupo,
#qual o nome do homem mais velho e quantas mulheres tem menos de 20 anos

somaidade = 0
maior = 0
nomemaior = ''
nomemenor = ''
menor = 0
feminino = 0
for p in range (1, 5):
    print('------ {}° PESSOA ------'.format(p))
    nome = str(input('digite o nome da {}° pessoa: '.format(p))).strip()
    idade = int(input('digite a idade da {}° pessoa: '. format(p)))
    sexo = str(input('digite o sexo da {}° pessoa: '.format(p))).lower().strip()

    somaidade = somaidade + idade

    if (p == 4):
        media = somaidade/4

    if (sexo == 'masculino'):
        if (p == 1):
            maior = idade
            nomemaior = nome
            menor = idade
            nomemenor = nome
        else:
            if (idade > maior):
                maior = idade
                nomemaior = nome
            if (idade < menor):
                menor = idade
                nomemenor = nome

    if (sexo == 'feminino' and idade < 20):
        feminino = feminino + 1

print('----- RESULTADO -----\n')

print('a media de idade dos homem é de {} anos'.format(media))
print('dos homem o de maior idade tem {} anos de idade e o seu nome é {}'.format(maior, nomemaior))
print('dos homem o de menor idade tem {} anos de idade e o seu nome é {}'.format(menor, nomemenor))
print('das mulheres digitadas {} tem menos de 20 anos'.format(feminino))