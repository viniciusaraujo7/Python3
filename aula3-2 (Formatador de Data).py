print('\033[1;31mPrática 2 / Aula 3: Mostre para o usuário o dia de nascimento devidamente formatado.\033[m')   # enunciado
print('\033[32m=-\033[m' * 15, '\033[1;33mFORMATADOR DE DIA DE NASCIMENTO\033[m', '\033[32m=-\033[m' * 15)   # formatação 1
dia = input('Qual o dia de seu nascimento? ')  # entrada de variável 1 feita pelo usuário
mes = input('Qual o mês de seu nascimento? ')  # entrada de variável 2 feita pelo usuário
ano = input('Qual o ano de seu nascimento? ')  # entrada de variável 3 feita pelo usuário
print('Você nasceu na data', dia, '/', mes, '/', ano)  # retorno para o usuário
print('\033[1;32m=-\033[m' * 15, '\033[1;33mFIM\033[m', '\033[32m=-\033[m' * 15)  # formatação 2

      
