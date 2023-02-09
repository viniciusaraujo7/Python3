valor = float(input('Digite o valor da casa: R$ '))
salario = float(input('Qual o salário mensal?: R$ '))
anos = int(input('Em quantos anos será pago?: '))
prestacao = (valor / anos) / 12
limite = (salario * 30) / 100
print(prestacao)
print(limite)
if prestacao < limite:
    print('EMPRÉSTIMO APROVADO')
else:
    print('EMPRÉSTIMO REPROVADO')

