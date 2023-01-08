print('\033[1;31mPrática 01 / Aula 3: Após receber os dados do usuário, mostre os dados logo abaixo.\033[m ')  # enunciado
print('\033[32m=-\033[m' * 15, '\033[1;33mDADOS PESSOAIS\033[33m', '\033[32m=-\033[m' * 15)  # formatação 1
nome = input('Qual seu nome? ')  # entrada de variável 1 feita pelo usuário
idade = input('Qual é sua idade? ')  # entrada de variável 2 feita pelo usuário
peso = input('Qual seu peso? ')  # entrada de variável 3 feita pelo usuário
print('Olá', nome, '! Prazer em te conhecer !', 'Sua idade é', idade, 'anos de idade', 'e seu peso é', peso, 'kg')  # retorno para o usuário
print('\033[32m=-\033[m' * 15, '\033[1;33mFIM\033[m', '\033[32m=-\033[m' * 15)  # formatação 2

