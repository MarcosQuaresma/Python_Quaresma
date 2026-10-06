##  Informações sobre o filme
# nome_Filme = input("Digite o nome do filme: \n")
# ano_lancamento = int(input("Digite o ano de lançamento: \n"))
# notaIMDB = float(input("Digite a nota de acordo com o IMDB: \n"))

# if notaIMDB > 8.0 and ano_lancamento > 2015:
#     print(f"Filme {nome_Filme} reocmendo assistir-lo!!")
# else:
#     print(f"O Filme {nome_Filme} não apresenta uma exelente nota de recomendação! ") 

num1 = float(input("Digite o primeiro número: \n"))
num2 = float(input("Digite o segundo número: \n"))

operacao = input("Digite a operação realizada: (+ - * / ) \n")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisão por zero")
        resultado = 0
else:
    print("Operação inválida")
    resultado = 0

print(f"O resultado de {num1} {operacao} {num2} é igual a: {resultado:.2f}")