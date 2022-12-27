import random
aluno1 = str(input('Digite o nome do aluno de número 1 a participar do sorteio: '))
aluno2 = str(input('Digite o nome do aluno de número 2 a participar do sorteio: '))
aluno3 = str(input('Digite o nome do aluno de número 3 a participar do sorteio: '))
aluno4 = str(input('Digite o nome do aluno de número 4 a participar do sorteio: '))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)
print('Os alunos a participar do sorteio são: \n 1 - {} \n 2 - {} \n 3 - {}\n 4 - {}'.format(aluno1, aluno2, aluno3, aluno4))
print('Agora faremos o sorteio de quem apagará o quadro! \nE o sorteado é: {} !'.format(sorteio))
