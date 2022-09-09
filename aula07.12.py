dias = int(input('Por quantos dias foi alugado o carro? '))
km = float(input('Quantos km foram rodados com este mesmo carro? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de {:.2f} reais.'.format(pago))
