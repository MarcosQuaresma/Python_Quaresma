filme1 = "O Mascara"

descricao_do_filme = """
    O filme do Mascara, marcou a infância de muitos que nasceram, por volta dos anos:
-> 90's e 2000's
 ----- Lançado em 1994.
 ----- Nota no IMDB de 7.0
"""

maiusculo = filme1.upper() # TUDO EM MAIUSCULO

minusculo = filme1.lower() # tudo em minusculo

primei_letra_maiuscula = filme1.capitalize() # Primeira etra em maiusculo

titulo = filme1.title() # Primeira Letra A Pos Um " " Espaço, Em Maiusculo

centralizado = filme1.center(20, "-") #---- retorna a string centralizada com caractere de preechiento]

maiusculo_descricao = descricao_do_filme.upper() # TUDO EM MAIUSCULO

encontrar = descricao_do_filme.find("a") # encontra a posição/indice que esse caractere aparece a primeira vez

contar = descricao_do_filme.count("a") # conta quantas vezes esse caractere aparece na String

alterar = filme1.replace("O", "O sem") # altera um elemento por outro seguindo a lógica (a , b), "a" será o elemento que irá ser trocado por "b"

quebrando_strings = descricao_do_filme.split(",") # irá quebrar o a string onde haver "," virgulas, como no exemplo

print(f"{maiusculo}\n{minusculo}\n{primei_letra_maiuscula}\n{titulo}\n{centralizado}\n{maiusculo_descricao}\n{encontrar}\n{contar}\n{alterar}")
print(f"{quebrando_strings}\n")