r1 = int(input('Digite o comprimento da reta 1: '))
r2 = int(input('Digite o comprimento da reta 2: '))
r3 = int(input('Digite o comprimento da reta 3: '))
'''base = r1
if r2 > r1:
    base = r2
if r3 > base:
    base = r3
if r1 == base:
    s = r2 + r3
    if s > base:
        print('Com essas medidas é possível formar um triângulo')
    else:
        print('Com essas medidas não é possível formar um triângulo')
if r2 == base:
    s = r1 + r3
    if s > base:
        print('Com essas medidas é possível formar um triângulo')
    else:
        print('Com essas medidas não é possível formar um triângulo')
if r3 == base:
    s = r1 + r2
    if s > base:
        print('Com essas medidas é possível formar um triângulo')
    else:
        print('Com essas medidas não é possível formar um triângulo')'''
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Com essas medidas é possível formar um triângulo.')
else:
    print('Com essas medidas não é possível formar um triângulo')






