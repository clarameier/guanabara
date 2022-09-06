larg = float(input('Qual a largura da sua parede, em metros? '))
alt = float(input('Qual a altura da sua parede, em metros? '))
area = larg * alt
tinta = area / 2
print('Você precisará pintar {} m², logo será preciso de {} litros de tinta, pois um litro pinta uma área de 2m²!'.format(area, tinta))
