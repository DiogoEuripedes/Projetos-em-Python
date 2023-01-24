import math
o = float(input('Digite um número: '))
a = float(input('Digite um número: '))
x = math.pow(o,2)
y = math.pow(a,2)
h = math.sqrt(x+y)

print('{:.3f}'.format(h))