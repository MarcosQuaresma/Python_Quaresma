# Função recursiva 
"""
EX:
Fatorial de um número:

1 -> 1 * 1      = 1
2 -> 2 * 1      = 2
3 -> 3 * 2 * 1  = 6
"""

# 1 Fatorial de um número:

def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return (num * fatorial(num - 1))

numero = int(input("Digite um número para um fatorial: "))

print(f"O fatorial de {numero} é {fatorial(numero)}") 

# 2 Soma total de um número
def somaTotal(num):
    if num == 1:
        return 1
    else:
        return (num + somaTotal(num - 1))

numero = int(input("Digite um número para soma: "))

print(f"A soma total {numero} é {somaTotal(numero)}")