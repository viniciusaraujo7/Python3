print('='*15, 'CÁLCULO HIPOTENUSA', '='*15)
from math import hypot
oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('A hipotenusa do triângulo retângulo é: {:.2f}'.format(hipotenusa))
#hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2)
#print('A hipotenusa do triângulo retângulo é: {:.2f}'.format(hipotenusa))

