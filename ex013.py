print('===============CÁLCULO DA PROMOÇÃO==============')
salario = float(input('Qual o salário atual do colaborador?: R$ '))
novosalario = salario + (salario * 5 / 100)
print('O novo salário do colaborador após a promoção será de R$ {:.2f}'.format(novosalario))

