from datetime import date
ano = int(input('Digite o ano a ser analisado (Caso queira analisar o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é um ano BISSEXTO'.format(ano))
else:
    print('O ano de {} não é um ano BISSEXTO'.format(ano))
