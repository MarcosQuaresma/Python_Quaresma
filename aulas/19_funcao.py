# 1 Função para imprimir uma mensagem "def"

def welcome():
    print("Bem vindo ao sistema de filmes!")

for i in range(2):
    welcome()

# 2 Função para calcular a média de notas
def cacularNota():
    numNotas = int(input("Quantas avaliações deseja fazer do filme: "))
    total = 0 # Observar sepre, para que tenha o ponto inicial, o ponto de aprtida.
    for n in range(numNotas):
        nota = float(input("Digite a nota para o filme: "))
        total += nota
    if numNotas > 0:
        media = total / numNotas 
    else:
        media = 0
    return media   #-----> o "return" significa que eu preciso chamar minha função "def x:" dentro de um "print()"

print(f"a Média do filme é: {cacularNota():.2f}")


# 3 Função para cadastrar um filme

def cadastarFilme():
    filmeCadastro = input("QUal o nome do filme: ")
    filmePreco = float(input("Quanto você pagou no filme: "))
    filmeLancamento = int(input("Qual o ano de lançamento: "))
    filmeNota = float(input("Qual a nota do filme: "))
    print(f"O filme {filmeCadastro}, foi lançado em {filmeLancamento} a sua nota é {filmeNota}, e foi um total de R$ {filmePreco:.2f}!")

cadastarFilme()
cadastarFilme()