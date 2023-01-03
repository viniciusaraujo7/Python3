print('=' * 12, 'ANALISANDO SEU NOME', '=' * 12)
nome = str(input('Digite seu nome completo: ')).strip()
print(nome)
print('Segue seu nome com todas as letras MAIÚSCULAS: {}'.format(nome.upper()))
print('Segue seu nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Segue quantidade de caracteres do seu nome sem considerar os espaços: {}'.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#print('Seu primeiro nome possui: {} letras'.format(len(dividido[0])))










