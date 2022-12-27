import random
aluno1 = input('Digite o nome do aluno de número 1: ')
aluno2 = input('Digite o nome do aluno de número 2: ')
aluno3 = input('Digite o nome do aluno de número 3: ')
aluno4 = input('Digite o nome do aluno de número 4: ')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.shuffle(lista)
print('Os alunos que participarão do sorteio para ordem de apresentação do trabalho são: \n1 - {} \n2 - {} \n3 - {} \n4 - {} '.format(aluno1, aluno2, aluno3, aluno4))
print('Segue abaixo a ordem sorteada de quem apresentará o trabalho: \n{}'.format(lista))


