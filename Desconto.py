p = float(input('Preço do produto: '))
d = float(input('Quanto é o desconto: '))
de = (p*d)/100
pd = p-de
print('O produto com desconto fica: {}'.format(pd))
