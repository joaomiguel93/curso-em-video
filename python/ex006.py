# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n **(1/2)
print('Analisando o número {}, o dobro é {} e o triplo é {} \n e a raiz quadrada é {:.2f}'.format(n, d, t, r))
