prod = float(input('Qual o valor deste produto? '))
desc = prod * 0.05
total = prod - desc
print('Este produto tem um desconto de 5%, portanto passou de {} para {}! Aproveite!'.format(prod, total))