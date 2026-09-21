import pprint

filmes_didionario = {
     "O Mascara": { # <- uma chave dentro de outra chave = Dicionário Aninhado.
         "Ano_de_lançamento": 1994,
         "IMDB_Nota": 7.0,
         "Genero": ["Comédia", "Ficção", "Ação"]
     }, # <- uma chave dentro de outra chave = Dicionário Aninhado.
     "Matrix": { # <- uma chave dentro de outra chave = Dicionário Aninhado.
         "Ano_de_lançamento": 1999,
         "IMDB_Nota": 8.7,
         "Genero": ["Ação", "Ficção Científica"]
    }, # <- uma chave dentro de outra chave = Dicionário Aninhado.
     "O Poderoso Chefão": { # <- uma chave dentro de outra chave = Dicionário Aninhado.
         "Ano_de_lançamento": 1972,
         "IMDB_Nota": 9.2,
         "Genero": ["Crime", "Drama"]  
    } # <- uma chave dentro de outra chave = Dicionário Aninhado.

}

pp = pprint.PrettyPrinter(depth=4) 
pp.pprint(filmes_didionario)

# 1 Buscar uma informação dentro de um dicionário aninhado.
pp.pprint(filmes_didionario["O Poderoso Chefão"]["Genero"])

# 2 Adicionar novo item
filmes_didionario["Matrix"]["Diretor(as)"] = "Lana Wachowski e Lilly Wachowski"
pp.pprint(filmes_didionario)

# 3 Excluir um dicionário.
del filmes_didionario["O Poderoso Chefão"]
pp.pprint(filmes_didionario)