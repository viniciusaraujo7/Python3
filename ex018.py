import math
angulo = float(input('Digite um ângulo para cálculo de suas medidas: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O seno deste ângulo é {:.2f} \nO cosseno deste ângulo é {:.2f} \nA tangente deste ângulo é {:.2f}'.format(seno, cos, tan))

