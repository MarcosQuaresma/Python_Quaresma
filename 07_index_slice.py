filme1 = "O Mascara"
# string [ inicio:fim ] - o indice começa na posição 0 : indice final -1

# 1 - Buscar toda string a partir da primeira posição (indice 0)
print(filme1[0:]) #veja, aqui eu não defini qual era o indice final
#                 mas em Python, ele interpreta e lerá até o ultimo indice, o indice final

print(filme1[:-2]) # nesse exemplo, eu defini que irá ler só até antes do penultimo indice.
print(filme1[:-1]) # nesse exemplo, eu defini que irá ler só até antes do ultimo indice.

print(filme1[3:]) # nesse exemplo, eu defini que irá ler a partir da 3° posição até o ultimo indice.
print(filme1[1:-1])# nesse exemplo, eu defini que não irá ler nem a 1° nem a ultima posição.

# na String o Python ler da seguinte maneira:

# str [inicio:fim:passo] = [x:y:z]

# o indice denominado no exemplo como "x" começa por padrão na posição 0 (mas podemos definir como nos exemplos assim)

# o indice final denominado no exemplo como "y" determina como padrão -1 (mas podemos definir como nos exemplos assim)

# já o "passo" ele por padrão é 1, pois ele é a maneira padrão que se define a leitura de uma string, porém se alterarmos
#   para um número qualquer que seja, ele irá determinar a maneira na qual a string esta sendo interpretada.


#------------------------ EXEMPLO ------------------------
print(filme1[::])  # Leitura normal
print(filme1[::2]) # a cada 2 indices ele não irá irá ler
print(filme1[::3]) # a cada 3 indices ele não irá irá ler

print(filme1[::-1]) # -1 faz com que a String seja interpretada de trás pra frente, sem pular indices
print(filme1[::-2]) # -2 faz com que a String seja interpretada de trás pra frente, porém, a cada 3 indices ele não irá irá ler
