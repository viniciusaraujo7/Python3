s = float(input('Digite o salário a ser nivelado: '))
if s > 1250:
    nv = s + (s * 10 / 100)
else:
    nv = s + (s * 15 / 100)
print('O novo salário do colaborador é R${:.2f}'.format(nv))
