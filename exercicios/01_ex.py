# 1° Escreva um programa que lê dois nomes e retorne uma string formatada no formato "ÚltimoNome, PrimeiroNome"
# 2° Inverta a ordem das palavras em uma string fornecida.
# 3° Verifique se uma string fornecida é um palindromo.

# 1° 
nome1 = str(input("Qual é o seu primeiro nome:\n"))
nome2 = str(input("Qual é o seu último nome:\n"))

print(f"{nome2}, {nome1}")

# 2° 
guy = nome1 + nome2

print(f"Seu nome invertido ficará {guy[::-1]}!")

# 3°

text = str(input("Digite um palindromo: \n"))

palindromo = text[::-1]

print(palindromo==text)