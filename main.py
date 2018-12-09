# coding: utf-8
# author: lucas Gyan Coloda
# podemos descobrir a próxima raiz se somarmos o número impar sequencial

w = 0
x = 2
y = 0
z = 0
print("Numero | raiz | impar sequencial")
while w <= 100:
    y = x * x
    w = w + 1
    z = 2 * x + 1
    print(y, x, z)
    x = x + 1
