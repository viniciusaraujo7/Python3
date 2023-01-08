print('\033[1;31mPrática 1 / Aula 8: Receba um número informado pelo usuário e calcule sua raiz quadrada.\033[m')  # enunciado
print('\033[32m*-\033[m' * 15, '\033[1;33mCALCULADORA DE RAIZ QUADRADA\033[m', '\033[32m*-\033[m' * 15)  # formatação 1
#import math  # importando o módulo math completo
from math import sqrt  # importando o item sqrt (cálculo de raiz quadrada) do módulo math
n = int(input('Digite um número para calcular sua raiz quadrada: '))  # entrada de variável 1 feita pelo usuário
r = sqrt(n)  # aplicação calcula a raiz quadrada da variável
print('A raiz quadrada de {} é {:.2f}'.format(n, r))  # retorno para o usuário
print('\033[1;32m*-\033[m' * 15, '\033[1;33mFIM\033[m', '\033[1;32m*-\033[m' * 15)  # formatação 2
