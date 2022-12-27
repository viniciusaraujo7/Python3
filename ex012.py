print('==============CALCULADORA DE DESCONTO==================')
valor = float(input('Qual o valor do produto?: R$ '))
desconto = valor * 0.05
novovalor = valor - desconto
print('O valor do produto com desconto de 5% é R${} '.format(novovalor))
