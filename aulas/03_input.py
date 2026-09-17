filme = str(input("Por favor, digite o nome de um filme:\n "))
data_de_lancamento = int(input("Qual o ano de lançamento:\n "))
nota_do_filme = float(input("Que nota você daria para esse filme?\n "))

print(f"\nO filme '{filme}', você daria uma nota de {nota_do_filme} foi lançado em {data_de_lancamento}\n")
print(f"Os dados inseridos em cada linha foi:\n Nome do Filme: {type(filme)}\n Ano de Lançamento: {type(data_de_lancamento)}\n Nota do Filme: {type(nota_do_filme)}")