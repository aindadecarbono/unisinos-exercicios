#PROG 1
#EXERCÍCIOS SEMANA 3-4


'''
Exercício 1. Crie um programa que recebe um inteiro pelo teclado 
e imprime se ele é par ou ímpar.  
'''

def paridade(num):
  if num % 2 == 0:
    print("Número {} é par.".format(num))

  else:
    print("Número {} é ímpar.".format(num))

paridade(int(input("Digite um número para saber se ele é par: ")))




 
'''
Exercício 2: Crie um programa que recebe dois valores inteiros A e B 
pelo teclado e imprime o valor de A dividido por B. Entretanto, 
se o valor de B for 0, imprima uma mensagem de erro e não faça a divisão.
'''

def divisao():
  primeiroNumero = int(input("Digite o primeiro número: "))
  segundoNumero = int(input("Digite o segundo número: "))

  if segundoNumero == 0:
    print("Você digitou 0, um número inválido.")
    return None

  resultado = primeiroNumero / segundoNumero

  print("O resultado da divisão de {} por {} é {}".format(primeiroNumero, segundoNumero, resultado))

divisao()





'''
Exercício 3. Crie um programa que recebe um valor inteiro referente a 
um determinado ano. Imprima na tela se o ano informado é bissexto ou não 
(para simplificar, você pode utilizar apenas a informação de o ano é 
divisível por 4 ou não).
'''

def anoBissexto():
  ano = abs(int(input("Digite um ano: ")))
  if ano % 4 == 0:
    print("O ano {} é bissexto.".format(ano))
    
  else:
    print("O ano {} não é bissexto.".format(ano))

anoBissexto() 





'''
Exercício 4. Crie um programa que recebe a nota do Grau A e a nota do 
Grau B pelo teclado e imprime na tela se será necessário ou não realizar
o Grau C (considere o sistema de avaliação da Unisinos, sendo o GA 
valendo 30% e o GB valendo 70%). Caso algum valor informado seja negativo,
informe uma mensagem de erro e não realize o cálculo.
'''

def calcularNota():
  
  grauA = abs(float(input("Digite o grau A: ")))
  grauB = abs(float(input("Digite o grau B: ")))

  while (grauA > 10 or grauB > 10):
    print("Digite números até 10")
    grauA = abs(float(input("Digite o grau A: ")))
    grauB = abs(float(input("Digite o grau B: ")))
    
  notaFinal = (grauA * 0.3) + (grauB * 0.7)

  if notaFinal < 6.0:
    print("Sua nota final é {}. Você precisa realizar grau C.".format(notaFinal))
    return

  else:
    print("Você passou com a nota {}".format(notaFinal))

calcularNota()




 
'''
Exercício 5. Crie um programa que solicita que o usuário digite uma letra
e imprime na tela se a letra é uma vogal ou uma consoante.
'''

def definirVogalConsoante():
  letra = input("Digite uma letra: ")

  while len(letra) > 1:
    letra = input("Digite APENAS uma letra: ")

  letra = letra.lower()

  if (letra !="a") and (letra !="e") and (letra !="i") and (letra !="o") and (letra !="u"):
    print("Você digitou uma consoante.")
    return

  else:
    print("Você digitou uma vogal.")

definirVogalConsoante()




 
'''
Exercício 6. O que é um parâmetro de entrada de um método?
'''

# Variável local para ser manipulada na respectiva função.



 
'''
Exercício 7. O que é o retorno de um método?
'''

# O retorno é o resultado de um método, sendo que ele pode ser devolvido
# para fora da função ou não. 




'''
Exercício 8. Utilizando while, crie um programa que imprime os números de
0 a 1000. 
'''

i = 0
while i <= 1000:
  print(i)
  i += 1
 



'''
Exercício 9. Utilizando while, crie um programa que imprime os números 
pares de 0 a 2000.
'''

i = 0
while i <= 2000:
  if i % 2 == 0:
    print(i)
  
  i += 1



 
'''
Exercício 10. Utilizando while, crie um programa que imprime os números 
de 0 a 1000 em ordem decrescente (ou seja, de 1000 a 0).
'''

i = 1000
while i >= 0:
  print(i)
  
  i -= 1



 
'''
Exercício 11. Utilizando while, crie um programa que solicita para o 
usuário que ele digite 10 valores inteiros. Ao final, imprima a soma de 
todos os valores digitados. 
'''

somatorio = 0
i = 0

while i < 10:
  
  somatorio = somatorio + int(input("Digite um número> "))
  i += 1

print(somatorio)


 
'''
Exercício 12. Comparando os comandos de repetição for e while, em quais 
ocasiões é mais comum a utilização de um ou de outro?

'''

# O comando while geralmente é mais utilizado quando não sabemos a 
# quantidade de repetições que nosso código fará. Por exemplo, “enquanto o 
# usuário não acertar o usuário e a senha, peça novamente”. Já o comando 
# for é mais utilizado quando sabemos o número de iterações a realizar. 
# Por exemplo, “o usuário possui 5 tentativas para acertar o usuário e a 
# senha”.

 



'''
Exercício 13. Utilizando for, crie um programa imprime na tela os valores 
de 1 a 100 (incluindo o 1 e o 100).
'''

for x in range(1,101):
  print(x)



 
'''
Exercício 14. Utilizando for,crie um programa que imprime a tabuada de um 
número inteiro digitado pelo usuário.
'''
 
def tabuada():
  numero = int(input("Digite um número> "))

  for x in range (1, 11):
    print("{} X {} é igual a : ".format(x, numero), x * numero)

tabuada()





'''
Exercício 15. Crie um programa que permita que o usuário crie sua lista 
de compras. Primeiramente, solicite que ele informe quantos produtos 
serão adicionados na lista. Depois disto, peça para que o usuário digite 
os produtos que ele vai comprar, e armazene em uma lista. Ao final, 
imprima a lista de compras do usuário.
'''

def listar():
  quantidadeProdutos = int(input("Quantos produtos você quer pôr na lista? "))

  lista = []

  for x in range(quantidadeProdutos):
    produto = input("Digite o produto #{}: ".format(x+1))
    lista.append(produto)
  
  else: 
    print("\nSua lista de compras: ", lista)

listar()




