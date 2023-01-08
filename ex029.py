v = int(input('Digite a velocidade atual do carro: '))
print('Você está a {}Km por hora.'.format(v))
if v <= 80:
    print('Você está dentro da velocidade permitida.')
else:
    m = (v - 80) * 7
    print('Você está a {}Km por hora. Excedeu o limite de velocidade e deverá pagar R${},00 de multa.'.format(v, m))


