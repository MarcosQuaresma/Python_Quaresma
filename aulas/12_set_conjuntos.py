conjuntos_filmes = {"O Poderoso Chefão", "Vingadores - Ultimato", "A Origem",
                    "Batman O Cavaleiro Das Trevas", "Ela"}

# 1 Buscar o tamanho do set (conjunto)
print(len(conjuntos_filmes))

# 2 "True" e "1" são considerados o  mesmo valor
ex_set_conjunto = {"A Origem", True, 1, 10.0}

print(ex_set_conjunto)

# 3 Adicionar item de outro set (conjunto)
conjuntos_filmes.update(ex_set_conjunto)

print(conjuntos_filmes)

# 4 Remover um item no set (conjunto)
conjuntos_filmes.remove(True)
conjuntos_filmes.remove(10.0)

print(conjuntos_filmes)