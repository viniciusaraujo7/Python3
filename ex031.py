d = int(input('Qual a distância em KM que será percorrida na viagem?: '))
p = d * 0.50 if d <= 200 else d * 0.45 #if simplificado
print('O valor da passagem custará R${:.2f}'.format(p))
'''if d <= 200:
    p = d * 0.50
    print('O valor da passagem custará R${:.2f}'.format(p))
else:
    p = d * 0.45
    print('O valor da passagem custará R${:.2f}'.format(p))'''
