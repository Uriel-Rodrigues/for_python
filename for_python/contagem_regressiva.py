#contagem regreciva de 0 ate 10 com pausa de 1 segundo
from time import sleep

for c in range (10, -1, -1):
    sleep(1)
    print(c)
sleep(1)
print('FELIZ ANO NOVO!')