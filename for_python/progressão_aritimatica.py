#programa que le o primeiro termo e a rezão de uma PA e mostre os 10 primeiros numeros
pnumero = int(input('digite o primriro numero da sua PA: '))
razao = int(input('digite a razão da sua PA: '))
decimo = pnumero + (10 - 1) * razao #com essa formula nos calculamos o decimo termo de uma PA onde o numero '10' é onde
#fica o termo que nos queremos descobrir

for c in range (pnumero, decimo+razao, razao):
    m = c +razao
    print(m)

#for c in range (pnumero, 10+1, razao):
    #m = c +razao
    #print(m)
#se nos fizer mos da forma acima o exercicio nao dara certo pois o for conta ate 10 e nao 10 termos dessa forma
#em casos que o primeiro termo fosse maior que 10 o laço nao funcionaria