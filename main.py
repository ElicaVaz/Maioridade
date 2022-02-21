I1 = int(input('Qual a primeira idade?'))
I2 = int(input('Qual a segunda idade?'))
I3 = int(input('Qual a terceira idade?'))
I4 = int(input('Qual a quarta idade?'))
I5 = int(input('Qual a quinta idade?'))

maior = 0
for i in [I1, I2, I3, I4, I5]:
    if (i >= 18):
        maior = maior + 1

print('Existem {} pessoas maior de 18 anos'.format(maior))
