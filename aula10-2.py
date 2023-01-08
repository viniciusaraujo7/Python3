n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua nota foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim. Estude mais.')
