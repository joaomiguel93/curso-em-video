"""Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""
from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    for c in range(i, f, p):
        print(f'{c} ', end=' ', flush=True)
        sleep(0.5)
    print('>>> FIM DO PROGRAMA <<<')


# Programa principal
contador(1, 11, 1)
contador(10, 0, -2)

print('=' * 30)
print('Agora é sua vez: ')
inicio = int(input('Digite o valor inicial: '))
fim = int(input('Digite o valor final: '))
passo = int(input('Digite o passo: '))
print('=' * 30)

contador(inicio, fim, passo)
print( )
