# *args = Ultilizamos quando não temos certeza de auntos argumentos queremos ter em uma função.
#       *args são passados em Tupulas "()"
# 
# **kwargs = Além dos valores, podemos passar também as respectivas chaves para cada arguemnto.
#           **kwargs são passados como dicionários "[]"  
#
#
#

# 1 - Soma de números
def soma(*num):
    totalSoma = 0
    for n in num: # o "n" é a quantidade de números que teremos na Tupula "()"
        totalSoma += n 
    print(f"Soma é: {totalSoma}")

soma(6)
soma(6,6)
soma(6,6,9)
soma(4, 5.6, 4.1, 10) # ele também soma com float's

# 2 Apresentação de Cursos
def apresentacao(**data):
    for key, value in data.items(): # <----- eu posso epgar tanto o valor da "key" quanto o valor de "value"
        print(f"{key} - {value}")
print("Lista de Cursos:")
apresentacao(nome = "Python", categoria = "Backend", nivel = "Iniciante")
apresentacao(nome = "Visão Computacional", categoria = "AI", nivel = "Avançado")
apresentacao(nome = "Dahsboards com Dash", categoria = "Data Science", nivel = "Intermediário")