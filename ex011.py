print('==========PRINT COLOR - O PROGRAMA DO PINTOR=============')
print('Aqui iremos realizar o cálculo para saber quanto de tinta será necessário para pintar cada parede do seu cômodo !')
altura = float(input('Quantos metros tem a altura da parede?: '))
largura = float(input('Quantos metros tem a largura da parede?: '))
area = altura * largura
quantidade = area / 2
print('A quantidade de tinta necessária para pintar essa parede será {} litros'.format(quantidade))

