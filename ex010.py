print('==================CONVERSOR REAL/DÓLAR==================')
carteira = float(input('Qual valor você tem na carteira? R$ '))
dolar = carteira / 3.27
print('Com o que você tem na carteira seria possível comprar ${:.2f}'.format(dolar))
