filme1 = "O Mascara"
filme2 = "O mascara"

print(filme1 == filme2) #Case sensitive = o Python bate os valores, e identificam se são iguais retornando "True" ou "False"

descricao_do_filme = """
    O filme do Mascara marcou a infância de muitos que nasceram por volta dos anos:
-> 90's e 2000's
 ----- Lançado em 1994.
 ----- Nota no IMBD de 7.0
"""
print(descricao_do_filme) # ele preserva o conceito de String-Multilinhas, sem que seja preciso abrir 4 "print()" como no exemplo.

# multiplicação de Strings

linha = "-"
print(linha*30)

# procurar dados dentro de uma String
print("Mascara" in filme1)
print("Mascara" in filme2) # retornarrá "False" pois eu invoquei no filme 2, mesmo sendo o mesmo nome
#                            o valor é diferente pois o "M" esta minúsculo na variável "filme2"

