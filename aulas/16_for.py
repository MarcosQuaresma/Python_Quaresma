# Lista de Filmes
filmeLista = ["O Máscara", "Os Vingadores", "Homem de Ferro", "Titanic"]
numerosLista = [14, 45, 7.5, 9, 6, 51 , 8, "numero aleatório", 15, 60, 7.1]

# 1 Interando valores de uam lista (apresentar-los fora de uma lista)
for filme in filmeLista:
    print(filme)

# 2 Quando a condiçõa for atendida o loop será encerrado
for numero in numerosLista:
    if numero == "numero aleatório":
      break
    print(numero)

# 3 quando a interação for atendida, o loop vai apra a próxima interação (ele pula o item indicado)
for numero in numerosLista:
    if numero == "numero aleatório":
        continue
    print(numero)

# 4 Avaliação do filme:
nomeFilme = input("Digite o nome do filme: ")
notaPessoal = int(input("Digite quantas avaliações deseja fazer: "))

total = 0

for valor in range(notaPessoal):
    nota = float(input("Digite uma nota para esse filme: "))
    total += nota

if notaPessoal > 0:
    media = total / notaPessoal
else: 
    media = 0 
print(f"Média de avaliação do filme {nomeFilme} é de: {media:.1f}")