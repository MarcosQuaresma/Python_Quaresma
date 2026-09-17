num1 = float(input( "Digite o primeiro número: " ))
num2 = float(input( "Digite o segundo número: " ))

# aritiméticos

var1 = num1 + num2  # soma
var2 = num1 - num2  # subitração
var3 = num1 / num2  # divisão (retorna float)
var4 = num1 * num2  # multiplicação
var5 = num1 ** num2 # potenciação
var6 = num1 // num2 # divisão inteira (retorna int)
var7 = num1 % num2  # módulo (é o resto da divisão)

print(f"A soma entre {num1} e {num2} é {var1:.2f}")
print(f"A subitração entre {num1} e {num2} é {var2:.2f}")
print(f"A divisão entre {num1} e {num2} é {var3:.2f}")
print(f"A multiplicação entre {num1} e {num2} é {var4:.2f}")
print(f"A potenciação entre {num1} e {num2} é {var5:.2f}")
print(f"A divisão INTEIRA entre {num1} e {num2} é {var6:.2f}")
print(f"O módulo (o resto da divisão) entre {num1} e {num2} é {var7}\n")

# comparação
maior = num1 > num2 #boleanos, boelans
menor = num1 < num2 #boleanos, boelans
igual = num1 == num2 #boleanos, boelans
maior_ou_igual = num1 >= num2 #boleanos, boelans
menor_ou_igual = num1 <= num2 #boleanos, boelans
diferente = num1 != num2

print(f"O {num1} é maior que o {num2}? {maior}!")
print(f"O {num1} é menor que o {num2}? {menor}!")
print(f"O {num1} é igual que o {num2}? {igual}!")
print(f"O {num1} é mairou ou igual que o {num2}? {maior_ou_igual}!")
print(f"O {num1} é menor ou igual que o {num2}? {menor_ou_igual}!")
print(f"O {num1} é diferente que o {num2}? {diferente}!")

# atribuição
num1 += num2  # soma
num1 -= num2  # subtraçaõ
num1 /= num2  # divisão (retorna float)
num1 *= num2  # multiplicação 
num1 **= num2 # potenciação
num1 //= num2 # divisão inteira (retorna um int)
num1 %= num2  # mídulo (o resto da divissão)