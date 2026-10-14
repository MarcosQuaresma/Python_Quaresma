# O que vem dentro dos "()" dentro de uma função "def nomedafunção()" é um argumento.

# 1 Função que imprime um nome completo

def nomeCompleto(primeiroNome, ultimoNome): # <----- essa é a definição de função com argumentos
    print(f"O nome é: {primeiroNome} {ultimoNome}") 

nomeCompleto("Marcos", "Quaresma") 
nomeCompleto("Gabriela","Rocha")

# 2 Função para somar dois números

def somaNum(a, b):
    return a + b 

print(f"A soma é: {somaNum(10, 12)}")

# Funções ultilizando aprametros default = eu defino diretamente no parametro da função

def endereco(pais="Brasil"):
    print(f"O endereço atual é: {pais}")

endereco() # ao invocar essa função eu tenho como definido dentro dela o meus pais como "Brasil"

endereco("Canadá") # posso alterar também ultilizando esse método escrevendo dentro da prórpia função, que subistitui as "str"

# 4 Funçõa pra avaliar filme
def notaFilme(numAvaliacoes, nomeFilme):
    total = 0
    for i in range(numAvaliacoes):
        nota = float(input("Digite a nota para o filme: \n"))
        total += nota 

    if numAvaliacoes > 0:
        media = total / numAvaliacoes
    else:
        media = 0
    
    print(f"Meédia de avaliação do filme {nomeFilme} é: {media:.2f}")

notaFilme(2, "Os Vingadores")