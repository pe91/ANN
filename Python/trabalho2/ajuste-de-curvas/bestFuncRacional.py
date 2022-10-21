from methods import *
import matplotlib.pyplot as plt
from math import *


x = [1.1387, 1.5597, 2.0507, 2.4161, 2.8776, 3.546, 4.14, 4.2913, 4.8954, 5.1525, 5.5576, 6.4178, 6.7262, 7.0844, 7.4988, 8.0848, 8.54, 8.779, 9.1937, 9.7884, 10.1284, 10.7972, 11.1378, 11.8284, 12.3078, 12.4113, 12.8915, 13.6138, 14.0468, 14.1954, 14.7286, 15.1025, 15.8553, 16.0428, 16.5834, 16.9172, 17.3496, 17.8422, 18.2835, 19.0322, 19.3531, 19.9285]
y = [1.8395, 2.1125, 2.3818, 2.5209, 2.6835, 2.8166, 2.9351, 2.9559, 3.0446, 3.0789, 3.1197, 3.1665, 3.2173, 3.2178, 3.2433, 3.2825, 3.3004, 3.3273, 3.3387, 3.3607, 3.3691, 3.3775, 3.397, 3.4209, 3.434, 3.4161, 3.4618, 3.4645, 3.4496, 3.4886, 3.4791, 3.4749, 3.5206, 3.499, 3.5371, 3.5226, 3.5251, 3.5241, 3.5589, 3.5561, 3.5577, 3.5657]
values = [6.7221, 10.746, 12.1853, 16.6088, 18.3345]

#linearização, transformando y em 1/y e x em 1/x
for i in range(0, len(y)):
    y[i] = 1/y[i]

for i in range(0, len(x)):
    x[i] = 1/x[i]

    

z, w = best_poly(x,y, 1) 

a = 1/z # a função te retorna um valor z = ln(a), então isola a e obtém a = exp(z)
b = a * w
print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return a * (x/(x+b))

print()
print('Values:\n')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")