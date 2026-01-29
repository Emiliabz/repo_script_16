#Valor a pagar pelo aluguel de carro

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar Ã© de R${}'.format(pago))

import math
num = int(input('Diga um numero inteiro qualquer: '))
raiz = math.sqrt(num)
print('A raiz de um {} Ã© igual a outro {}'.format(num,raiz))
