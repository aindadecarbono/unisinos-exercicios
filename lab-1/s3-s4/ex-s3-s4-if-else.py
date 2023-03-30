                    #Exercícios de fixação sobre if/else



'''
Exercício 1. Crie um programa que recebe um inteiro pelo teclado e imprime se ele é
par ou ímpar.
'''
def descobrirPar(num):
  if num % 2 == 0:
    print("Número {} é par.".format(num))

  else:
    print("Número {} é ímpar.".format(num))

#descobrirPar(int(input("Digite um número para saber se ele é par: ")))


'''
Exercício 2. Crie um programa que recebe dois valores inteiros pelo teclado e imprime
qual dos dois é maior.
'''
def compararMaior():
  num1 = int(input("Digite o primeiro número: "))
  num2 = int(input("Digite o segundo número: "))
  if num1 > num2:
    print(f"O número {num1} é maior que {num2}.")

  elif num2 > num1:
    print(f"O número {num2} é maior que {num1}.")

  else:
    print(f"O número {num1} é igual a {num2}.")

#compararMaior()

'''
Exercício 3. Crie um programa que recebe dois valores inteiros A e B pelo teclado e
imprime o valor de A dividido por B. Entretanto, se o valor de B for 0, imprima uma
mensagem de erro e não faça a divisão.
'''

def dividir():
  primeiroNumero = int(input("Digite o primeiro número: "))
  segundoNumero = int(input("Digite o segundo número: "))

  if segundoNumero == 0:
    print("Você digitou 0, um número inválido para o denominador.")
    return None

  resultado = primeiroNumero / segundoNumero

  print(f"O resultado da divisão de {primeiroNumero} por {segundoNumero} é {resultado}")

#dividir()


'''
Exercício 4. Crie um programa que recebe três valores inteiros pelo teclado e imprime
qual dos três é menor.
'''

def compararMenor():
  
  primeiroNumero = int(input("Digite o primeiro número: "))
  segundoNumero = int(input("Digite o segundo número: "))
  terceiroNumero = int(input("Digite o terceiro número: "))

  menorNumero = primeiroNumero if primeiroNumero < segundoNumero  else segundoNumero
  menorNumero = terceiroNumero if terceiroNumero < menorNumero  else menorNumero

  print(f"O menor número é {menorNumero}") 

  
#compararMenor()





'''
Exercício 5. Crie um programa que recebe o preço de um produto pelo teclado e
imprime na tela a mensagem adequada, de acordo com o preço:
• “Preço inválido”, se o preço for negativo ou zero
• “Preço baixo”, se o preço for entre 0 e 30 (inclusive)
• “Preço médio”, se o preço for entre 30 e 50 (inclusive)
• “Preço alto”, se o preço for maior do que 50
'''

def compararPreco():

  preco = float(input("Digite o preço: "))

  if preco <= 0:
    print(f"O preço {preco} é inválido.")
    return
  
  elif preco <= 30:
    print(f"O preço {preco} é baixo.")
    return
  
  elif preco <= 50:
    print(f"O preço {preco} é médio.")
    return
  
  else:
    print(f"O preço {preco} é alto.")
    return

#compararPreco()



'''
Exercício 6. Crie um programa que aplica uma taxa de juros em um determinado preço
digitado pelo teclado. A taxa aplicada deve ser:
• Aumento de 10% caso o valor seja menor do que 100
• Aumento de 20% caso o valor esteja entre 100 (inclusive) e 300
• Aumento de 50% caso o valor esteja entre 300 (inclusive) e 1000
• Imprima uma mensagem de erro se o valor for negativo
• Ao final, seu programa deve imprimir o novo valor, já com a taxa aplicada.
'''

def atribuirJuro():

  preco = float(input("Digite o preço: "))

  if preco < 0:
    print(f"O preço {preco} é inválido.")
    return
  
  
  elif preco < 100:
    preco = preco + preco * 0.1
    print(f"O novo preço é {preco}.")
    return


  elif preco < 300:
    preco = preco + preco * 0.2
    print(f"O novo preço é {preco}.")
    return


  elif preco < 1000:
    preco = preco + preco * 0.5
    print(f"O novo preço é {preco}.")
    return
  
  else:
    print(f"O preço {preco} não sofreu alteração.")
  
#atribuirJuro()

'''
Exercício 7. Crie um programa que recebe um valor inteiro referente a um
determinado ano. Imprima na tela se o ano informado é bissexto ou não.
'''

def encontrarAnoBissexto():
  ano = abs(int(input("Digite um ano: ")))
  if ano % 4 == 0:
    print("O ano {} é bissexto.".format(ano))
    
  else:
    print("O ano {} não é bissexto.".format(ano))


#encontrarAnoBissexto() 



'''
Exercício 8. Crie um programa que exibe um menu de calculadora na tela. O menu
exibido deve ser o seguinte:
• Digite 1 para somar dois valores
• Digite 2 para subtrair dois valores
• Digite 3 para multiplicar dois valores
• Digite 4 para dividir dois valores
• Digite 5 para realizar uma potência entre dois valores
• Digite 6 para realizar uma radiciação entre dois valores
• Digite qualquer outro número para sair
De acordo com a opção informada pelo usuário, solicite os valores necessários para o
usuário e imprima na tela o resultado da operação realizada.
'''


ligado = True

def calcular():


  def somar():
    print("SOMA")
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    return print("A soma é ", numero1 + numero2)

  def subtrair():
    print("SUBTRAÇÃO")
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    return print("A subtração é ", numero1 - numero2)

  def multiplicar():
    print("MULTIPLICAÇÃO")
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    return print("A multiplicação é ", numero1 * numero2)

  def dividir():
    print("DIVISÃO")
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    while numero2 == 0: 
      numero2 = float(input("Número inválido. Digite outro número: "))
    return print("A divisão é ", numero1 / numero2)

  def potenciar():
    print("POTENCIAÇÃO")
    numero1 = float(input("Digite a base: "))
    numero2 = float(input("Digite o expoente: "))
    return print("A potenciação é ", numero1 ** numero2)

  def radiciar():
    print("RADICIAÇÃO")
    numero1 = float(input("Digite o radicando: "))
    numero2 = float(input("Digite o índice: "))
    return print("A radiciação é ", numero1 ** (1/numero2))

  def switch(numero):
    if numero == "1":
        somar()
    elif numero == "2":
        subtrair()
    elif numero == "3":
        multiplicar()
    elif numero == "4":
        dividir()
    elif numero == "5":
        potenciar()
    elif numero == "6":
        radiciar()
    else:
      print("Fim do programa")
      global ligado 
      ligado = False
      
  def criarMenu():
    
    print('''     CALCULADORA
    \n
      • Digite 1 para somar dois valores\n
      • Digite 2 para subtrair dois valores\n
      • Digite 3 para multiplicar dois valores\n
      • Digite 4 para dividir dois valores\n
      • Digite 5 para realizar uma potência entre dois valores\n
      • Digite 6 para realizar uma radiciação entre dois valores\n
      • Digite qualquer outro número para sair\n
    '''
    )


  while ligado:
    

    criarMenu()
    
    resposta = input()

    switch(resposta)
    
    

#calcular()

'''
Exercício 9. Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo
teclado e imprime na tela se será necessário ou não realizar o Grau C (considere o
sistema de avaliação da Unisinos). Caso algum valor informado seja negativo, informe
uma mensagem de erro e não realize o cálculo.
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
    print(f"Sua nota final é {notaFinal}. Você precisa realizar grau C.")
    return

  else:
    print(f"Você passou com a nota {notaFinal}")

#calcularNota()




'''
Exercício 10. Crie um programa que solicita que o usuário digite uma letra e imprime
na tela se a letra é uma vogal ou uma consoante.
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

#definirVogalConsoante()

