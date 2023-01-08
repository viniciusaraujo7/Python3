import random
import time
nr = random.randint(0, 5)
nu = int(input('Digite um número entre 0 e 5: '))
print('PROCESSANDO...')
time.sleep(3)
if nr == nu:
    print('PARABÉNS! VOCÊ ACERTOU E GANHOU O PRÊMIO!')
else:
    print('Infelizmente você errou :( ')

