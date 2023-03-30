#Exercícios de fixação WHILE (lista 1)

'''
Exercício 1. Crie um programa que pede para o usuário digitar o nome de 13 pessoas
pelo teclado.
'''
def coletarNomes():
  i = 0
  nomes = []
  while i < 13:
    nomes.append(input("Digite um nome: "))
    i += 1
  print(nomes)

#coletarNomes()
  
'''
Exercício 2. Crie um programa que imprime os números de 0 a 1000.
'''

def imprimirNumeros1000():
  i = 0
  while i <= 1000:
    print(i)
    i += 1 

#imprimirNumeros1000()

'''
Exercício 3. Crie um programa que imprime os números pares de 0 a 2000.
'''
def imprimirPares2000():
  i = 0
  while i <= 2000:
    if i % 2 == 0:
      print(i)
    i += 1 

#imprimirPares2000()

'''
Exercício 4. Crie um programa que imprime os números de 0 a 1000 em ordem
decrescente (ou seja, de 1000 a 0).
'''

def imprimirNumeros1000Decrescente():
  i = 1000
  while i >= 0:
    print(i)
    i -= 1 

#imprimirNumeros1000Decrescente()


'''
Exercício 5. Crie um programa que solicita o time de 10 usuários pelo teclado. Ao final,
imprima quantos torcedores torcem para o Grêmio.
'''
def contarTorcedores():
  
  torcedoresGremio = 0
  i = 0
  
  while i < 10:
    
    if input("Digite seu time: ").lower() == "grêmio":
      torcedoresGremio += 1
    
    i += 1
  
  print(f"O número de torcedores do Grêmio é {torcedoresGremio}.")

#contarTorcedores()


'''
Exercício 6. Crie um programa que pede para o usuário digitar 20 números com ponto
flutuante pelo teclado. Ao final, seu programa deve imprimir todos os números
digitados. Dica: armazene-os em uma string e concatene os valores digitados. No final,
imprima a string.
'''

def digitarFlutuantes():

  numeros = 0.0
  i = 1

  while i <= 20:

    numeros = numeros + float(input(f"Digite o {i}º número flutuante: "))
    
    i += 1

  print(f"O resultado da soma é {numeros}.")

#digitarFlutuantes()




'''
Exercício 7. Crie um programa que solicita para o usuário que ele digite 10 valores
inteiros. Ao final, imprima a soma de todos os valores digitados.
'''

def digitarInteiros():

  numeros = 0
  i = 1

  while i <= 10:

    numeros = numeros + int(input(f"Digite o {i}º número inteiro: "))
    
    i += 1

  print(f"O resultado da soma é {numeros}.")

#digitarInteiros()



'''
Exercício 8. Crie um programa que pergunta para o usuário (via Teclado) quantos
números ele irá digitar e armazena em uma variável chamada quant. Logo após, faça
com que o usuário digite quant números inteiros, e para cada número digitado imprima
na tela se o número é negativo, positivo ou zero.
'''

def criarQuantidadeNumeros():

  i = 0

  quantidade = int(input("Digite a quantidade de números a serem armazenados: "))

  while i < quantidade:

    numeroTeste = int(input("Digite um número a ser testado: "))

    if numeroTeste == 0:
      print("O número é zero.")
      
    
    elif numeroTeste > 0:
      print(f"{numeroTeste} é positivo.")
    
    else:
      print(f"{numeroTeste} é negativo.")

    i += 1



#criarQuantidadeNumeros()
    



'''
Exercício 9. Crie um programa que pede para o usuário digitar 2 valores inteiros via
Teclado (val1 e val2). Se nenhum dos valores for negativo, escreva os números pares
entre o menor e o maior valor.
'''

def numerarParesRange():

  val1 = abs(int(input("Digite o primeiro valor: ")))
  val2 = abs(int(input("Digite o segundo valor: ")))

  maiorNumero = val1 if val1 > val2 else val2
  menorNumero = val1 if val1 < val2 else val2
   
  while menorNumero < maiorNumero:
    if menorNumero % 2 == 0:
      print(menorNumero)
    menorNumero += 1

#numerarParesRange()


'''
Exercício 10. Crie um programa que faça a soma dos valores de 0 até 198.
'''

def somar198():

  somatorio = 0

  i = 0

  while i < 198:

    somatorio = somatorio + i
    
    i += 1

  print(somatorio)


#somar198()

'''
Exercício 11. Crie um programa que imprima a soma dos valores pares e a soma dos
valores ímpares entre dois números quaisquer digitados pelo usuário.
'''

def somaParImparRange():
  
  val1 = abs(int(input("Digite o primeiro valor: ")))
  val2 = abs(int(input("Digite o segundo valor: ")))

  maiorNumero = val1 if val1 > val2 else val2
  menorNumero = val1 if val1 < val2 else val2

  somatorioPares = 0
  somatorioImpares = 0
   
  while menorNumero < maiorNumero:
    if menorNumero % 2 == 0:
      somatorioPares = somatorioPares + menorNumero

    else:
      somatorioImpares = somatorioImpares + menorNumero
    
    menorNumero += 1

  print(f"Somatório dos números pares: {somatorioPares}")
  print(f"Somatório dos números ímpares: {somatorioImpares}")

#somaParImparRange()


'''
Exercício 12. Crie um programa que pede para o usuário digitar números positivos via
Teclado. Quando o usuário digitar um número negativo, informe a média de todos os
números que ele informou.
'''

def somarPositivos():

  numeroDigitado = 1
  denominador = 0
  somatorio = 0

  while numeroDigitado:

    resposta = int(input("Digite um número a ser somado: "))

    if resposta < 0:

      numeroDigitado = 0

      print(f"A média do somatório é {somatorio/denominador}.")

    denominador += 1

    somatorio += resposta

#somarPositivos()


'''
Exercício 13. Crie um programa que calcule o fatorial de um número informado pelo
usuário (não permita números negativos).
'''

def calcularFatorial():

  i = 0

  fatorial = abs(int(input("Digite um número para calcular o fatorial: ")))
  
  i = fatorial

  while i > 1:
    
    fatorial = fatorial * (i - 1)

    i -= 1

  print(f"O resultado do cálculo fatorial é: {fatorial}")

#calcularFatorial()

'''
Exercício 14. Crie um programa que diga se o número informado pelo usuário é primo
ou não.
'''

def definirPrimo():

  resposta = abs(int(input("Digite um número para saber se ele é primo: ")))
  
  numeroDivisores = 0
  
  i = resposta 

  while i > 0:

    if resposta % i == 0:
      numeroDivisores += 1

    if numeroDivisores > 2:
      print(f"{resposta} não é número primo.")
      return
    
    i -= 1

  print(f"{resposta} é número primo")

#definirPrimo()


'''
Exercício 15. Crie um programa que imprime os números primos entre 0 e 200,
imprimindo ao final a soma destes números.
'''

def somarPrimos200():
  
  displayNumeros = []

  somatorioPrimos = 0

  numeroDivisores = 0

  numero = 200
  
  i = numero 

  while numero > 0:

    numeroDivisores = 0

    i = numero

    while i > 0:
      
      if numero % i == 0:
        numeroDivisores += 1

      i -= 1 

    if numeroDivisores == 2:
      somatorioPrimos += numero
      displayNumeros.append(numero)
      
    numero -= 1

  
  print(f"\nLista de números primos:\n\n{displayNumeros}")
  print(f"\nSomatório de números primos: {somatorioPrimos}")


#somarPrimos200()

