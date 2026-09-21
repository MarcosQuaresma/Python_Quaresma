# no dicionário eu tenho o valor e apropiredade dentro de um conjunto {}
filme_O_Mascara = {
    "Titulo":"O Mascara",
    "Ano_de_lançamento": 1994,
    "IMDB_Nota": 7.0,
    "Genero": ["Comédia", "Ficção", "Ação"] #Possi ultilizar uma lista "[]" dentro do dicionário "{}"
    }

print(filme_O_Mascara) # todo o conteudo do dicionáro.
print(len(filme_O_Mascara)) # quantidade itens dentro do dicionário.
print(type(filme_O_Mascara)) # qual o tipo do elemento. (no caso, um dict = Dicionário "{}")

# 1 Recuperar um elemnto do Dicionário.
print(filme_O_Mascara["Genero"])
print(filme_O_Mascara["IMDB_Nota"]) #---------:> no método Dicionário, ultiliza-se os "[]" para invocar qual item quero resgatar.
print(filme_O_Mascara["Titulo"])
print(filme_O_Mascara["Ano_de_lançamento"])

# 2 Buscar apenas as Chaves do dicionário.-->  x : 
print(filme_O_Mascara.keys()) # "keys()" apenas para itens a Esquerda dos ":" que são as chaves.

# 3 Buscar apenas os Valores do dicionário.-->   : y
print(filme_O_Mascara.values()) # "values()" apenas para itens a Direita dos ":" que são os valores.

# 4 Buscar tanto itens com Chave e Valores.--> x : y
print(filme_O_Mascara.items()) # Busca tanto Chaves quanto Valores. é uma Tupula.

# 5 Adicionar itens no dicionário.
filme_O_Mascara["Diretor"] = "Cuck Russell" # Nesse caso eu Criei e Adicionei um item em "x : y" x = "Diretor" 
                                            #                                                    y = "Chuck Russell"
print(filme_O_Mascara)
# 6 Atualizar itens no dicionário.
filme_O_Mascara.update({"IMDB_Nota": 8.7}) # Essa é a maneira na qual se altera um item no Dicionário.

print(filme_O_Mascara)
# 7 Remover item no Dicionário.
filme_O_Mascara.pop("Diretor") 

print(filme_O_Mascara)
