filmeLista = ["O Máscara", "Os Vingadores", "Homem de Ferro", "Titanic"]
numerosLista = [14, 45, 7.5, 9, 6, 51 , 8, "numero aleatório", 15, 60, 7.1]

# 1 Interando valores de uma lsita de filmes/números usando "while"

index = 0 # o index é como uma caixa vazia, ele permite adiniconar quantidade de itens que existe em uma lista
          # é como se fosse a linha de paretida, onde o primeior passo é o "0+1" o "1" é o primeiro item da lista

while index < len(filmeLista): # eu ultilizo o "len()" para descobir a quantidade de itens que existem nessa lsita
                               # é como se eu tivesse definido o "range()" descocobrindo atravez do "len()"

    print(filmeLista[index]) # no "filmeLista" eu tenho que definir o "[index]" para que ele não ultapasse a condição de "index < len()"
    index += 1  # esse é o contador que vai definir até a onde o "index" deve ir, sem ele é um looping infinito, pois sem o "index += 1"
                # ele nunca sairá do indisse 0

## 2° exemplo.    
index = 0 

while index < len(numerosLista):
    print(numerosLista[index])
    index += 1


# 2 Quando a condição for atendida, o loop será encerrado (break)

index = 0 

while index < len(filmeLista):
    if filmeLista[index] == "Homem de Ferro":
        break # nesse caso ele parou a lista no item "Homem de Ferro"

    print(filmeLista[index])
    index += 1

# 3 Quando a condição for atendida o loop vai para a próxima interação

index = 0 

while index < len(filmeLista):
    if filmeLista[index] == "Os Vingadores":
        index += 1
        continue # nesse caso ele pulou o item da lista "Os Vingadores" 

    print(filmeLista[index])
    index += 1

# 4 Avaliação do filme com "while"

nomeFilme = input("Digite o nome do filme: ")
notaPessoal = int(input("Digite quantas avaliações deseja fazer: "))
total = 0 
conta = 0 

while conta < notaPessoal:
    nota = float(input("Digite a nota que você daria para o filme: "))
    total += nota
    conta += 1 
    
if notaPessoal > 0:
    media = total / notaPessoal
else: 
    media = 0 
print(f"Média de avaliação do filme {nomeFilme} é de: {media:.1f}")