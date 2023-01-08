print('\033[1;31mPrática 3 / Aula : Faça a soma dos dois números informados pelo usuário.\033[m')  # enunciado
print('\033[32m:-\033[m' * 15, '\033[1;33mCALCULADORA DE SOMA\033[m', '\033[32m:-\033[m' * 15)  # formatação 1
numero1 = int(input('Qual o primeiro número? '))  # entrada de variável 1 feita pelo usuário
numero2 = int(input('Qual o segundo número? '))  # entrada de variável 2 feita pelo usuário
soma = numero1 + numero2  # aplicação soma as variáveis informadas pelo usuário
print('A soma dos números é: {}'.format(soma))  # retorno para o usuário
print('\033[1;32m:-\033[m' * 15, '\033[1;33mFIM\033[m', '\033[1;32m:-\033[m' * 15)  # formatação 2
