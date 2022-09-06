from math import sqrt
n1 = float(input('Digite um número: '))
n2 = n1 * 2
n3 = n1 * 3
n4 = sqrt(n1)
print('Seu número escolhido foi {}, logo, o dobro deste número é de {}, o triplo de {} e a raíz quadrada deste é de {:.2f}!'.format(n1, n2, n3, n4))