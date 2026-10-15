# A função Lambda sempre recebe uam variável ou seja -> variavel =  lambda x: y

# 1 Função de potência de um número:
potenciaEm2 = lambda num: num ** 2 # <- essa variável é específica para o número 2, mas posso ter outras para vários outros números.

print(potenciaEm2(5)) # o que estiver dentro do "()" será potenciado a 2
print(potenciaEm2(4))

# 2 Função que verifica se o número é par

ePar = lambda num: num % 2 == 0

print(ePar(30)) # retorna com boleano, ou bolean = True ou False
print(ePar(37))
  
# 3 Função que divide um número por outro

divisaoNumero = lambda x, y: x/y

print(divisaoNumero(4,2))
print(divisaoNumero(20,5))

# 4 Função que inverte uma string "str"

inverterString = lambda string: string[::-1]

print(inverterString("Pyhton"))
print(inverterString("Marcos Pedrosa Quaresma"))

# 5 Funcionalidades relacionadas a filmes

conjuntos_filmes = ["O Poderoso Chefão", "Vingadores - Ultimato", "A Origem", "Batman O Cavaleiro Das Trevas", "Ela"]
notas = {
    "O Poderoso Chefão": [8.7, 9.8, 9.0],
    "Vingadores - Ultimato": [10.0, 9.8, 9.9],
    "A Origem": [8.7, 9.2, 9.5],
    "Batman O Cavaleiro Das Trevas": [9.0, 8.9, 9.3],
    "Ela": [8.6, 9.1, 9.5],
}
# ----> Função apra calcular a média de avalização dos filmes
mediaNotas = lambda nomeFilme: sum(notas[nomeFilme]) / len(notas[nomeFilme])

print(f"Média de avaliadão do filme Vingadores - Ultimato: {mediaNotas("Vingadores - Ultimato")}")

# ----> FUnção de verifica se um filme está na lsita
conferirFilme = lambda nomeFilme: nomeFilme in conjuntos_filmes

print(f"BOPE esta na lista? {conferirFilme("BOPE")}")

# ----> Função para recomendar um filme com base na avaliação média
recomendarFilme = lambda nomeFilme: f"Recomedno assistir '{nomeFilme}' com a média de {mediaNotas(nomeFilme):.2f}"

print(f"{recomendarFilme("Ela")}")
