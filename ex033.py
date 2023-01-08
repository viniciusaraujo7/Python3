n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))
n3 = int(input('Digite o número 3: '))
maior = n1
if n2 > n1:
    maior = n2
if n3 > maior:
    maior = n3
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('O número maior é: {} e o menor é: {}'.format(maior, menor))
