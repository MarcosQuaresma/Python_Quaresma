lista_filmes = ["O Poderoso Chefão", "Vingadores - Ultimato", "A Origem",
                 "Batman O Cavaleiro Das Trevas", "Ela"]
# 1 Tamanho da lista
print(len(lista_filmes)) # quantidade de itens na lsita

# 2 Recuperar um item da lsita pelo indice
print(lista_filmes.index("Ela")) # a posição na qual o iten se encontra na lista.

# 3 Add item ao final da lista
lista_filmes.append("BOPE")

print(lista_filmes)

# 4 Ordenar lista, por ordem ALFABETICA
lista_filmes.sort()

print(lista_filmes)

# 5 Copiar os itens de uma lista para outra
copia_filmes = lista_filmes.copy()
copia_filmes.remove("A Origem")

print(copia_filmes)

# 6 Remover todos os itens da lista
lista_filmes.clear()

print(lista_filmes)
