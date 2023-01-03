frase = str(input('Digite uma frase: ').strip())
frase = frase.lower()
print('Quantas vezes aparece a letra A ? : {} vezes'.format(frase.count('a')))
print('Em qual posição a letra A aparece a na primeira vez?: Aparece na posição {}'.format(frase.find('a')+1))#Ajustando a contagem ao Python
print('Em qual posição a letra A aparece a última vez?: Aparece na posição {}'.format(frase.rfind('a')+1))#Ajustando a contagem ao Python
