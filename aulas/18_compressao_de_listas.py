# 1 Listando valores de 0 a 10 que sejam menores do que 4
 
# Ultilizando "for in"
for num in range(10):
    if num < 4:
        print(num)

# Ultilizando Compressão de Lista, METODO DAHORA PRA KRL.
 
listaNum = [num for num in range(10) if num < 4]
print(listaNum)

# 2 Filmes que possuam a letra "M" no título

filmeLista = ["O Máscara", "Os Vingadores", "Homem de Ferro", "Titanic"]

filmesComM = [filmes for filmes in filmeLista if "m" in filmes.lower()]
print(filmesComM)

# Filmes que eu assisti (o exemplo consiste em que dos 4 filmes, o único que eu não assisti seja: "Os Vingadores")
filmesAssistido = [filmes for filmes in filmeLista if filmes != "Os Vingadores"]
print(filmesAssistido)

# Encontrando um filme pelo nome com "while True:" consiste em futuramente ultilizar um "break" para interromper a execução do loop
while True:
    procurarNome = input("Qual o nome do filme para buscar na lista: (para sair digite X) \n")
    if procurarNome.upper() == "X":
        print("---Programa Encerrado!!---")
        break

    achouFilme = [filme for filme in filmeLista if procurarNome.upper() in filme.upper()]
    if achouFilme:
        print(f"Filme(s) encontrado(s) com o nome: {procurarNome}")
        for achouFilme in achouFilme:
            print(achouFilme)
    else:
        print(f"Nenhum filme foi encontrado com o nome de {procurarNome}. Tente novamente!")