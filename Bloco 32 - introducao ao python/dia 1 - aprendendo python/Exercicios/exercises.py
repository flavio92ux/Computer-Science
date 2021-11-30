""" Exercício 1: Crie uma função que receba dois números e retorne o maior deles. """
def greater (num1, num2):
    if (num1 > num2):
        return num1
    else:
        return num2

print(greater(10, 5))

""" Exercício 2: Calcule a média aritmética dos valores contidos em uma lista. """
list = [2, 3, 10, 40, 50, 20]
sum = 0

for item in list:
    sum += item

print(sum / len(list))

""" Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1,
imprima na tela um quadrado feito de asteriscos de lado de tamanho n . """

def printast (n):
    i = 0
    while i < n:
        print(n * '*')
        i += 1

printast(5)

""" Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome
com a maior quantidade de caracteres.
Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"] , o retorno deve ser "Fernanda" . """
def more_caracthers (list):
    aux = ''
    for item in list:
        if len(item) > len(aux):
            aux = item
    return aux

mylist = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]

print(more_caracthers(mylist))

""" Exercício 5: Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo a
quantidade de latas de tinta a serem compradas e o preço total a partir do tamanho de uma parede(em m²). """
import math

def amount_ink (wall_size):
    total_liters = wall_size / 3
    amount_lata = math.ceil(total_liters / 18)
    total_price = amount_lata * 80
    return (amount_lata, total_price)

print(amount_ink(200))