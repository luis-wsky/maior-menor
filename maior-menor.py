# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite um valor:'))
n2 = float(input('Digite outro valor:'))
n3 = float(input('Digite  mais um valor:'))
if n1 <= n2 and n1 <= n3:
    menor = n1
    print(' O menor valor digitado foi {}:'. format(menor))
if n2 <= n1 and n2 <= n3:
    menor2 = n2
    print(' O menor valor digitado foi {}:'.format(menor2))
if n3 <= n1 and n3 <= n2:
    menor3 = n3
    print(' O menor valor digitado foi {}:'.format(menor3))
if n1 >= n2 and n1 >= n3:
    maior = n1
    print(' O maior valor digitado foi {}:'.format(maior))
if n2 >= n1 and n2 >= n3:
    maior2 = n2
    print(' O maior valor digitado foi {}:'.format(maior2))
if n3 >= n1 and n3 >= n2:
    maior3 = n3
    print(' O maior valor digitado foi {}:'.format(maior3))
