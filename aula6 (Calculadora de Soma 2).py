print('\033[1;31mPrática 1 / Aula 6: Faça a soma dos dois números informados pelo usuário e mostre o total logo depois.\033[m')  # enunciado
print('\033[32m:-\033[m' * 15, '\033[1;33mCALCULADORA DE SOMA 2\033[m', '\033[32m:-\033[m' * 15)  # formatação 1
n1 = int(input('Digite um número: '))  # entrada de variável 1 feita pelo usuário
n2 = int(input('Digite outro número: '))  # entrada de variável 2 feita pelo usuário
s = n1 + n2  # aplicação soma as variáveis informadas pelo usuário
# print('A soma de',n1,'e',n2,'é',s)  # alternativa 1 de retorno ao usuário
print('A soma entre {} e {} totaliza {}'.format(n1, n2, s))  # alternativa 2 de retorno ao usuário
print('\033[1;32m:-\033[m' * 15, '\033[1;33mFIM\033[m', '\033[1;32m:-\033[m' * 15)  # formatação 2

