#     Exercícios de fixação sobre métodos

'''
Para os métodos que não forem definidos nomes no enunciado,
crie o nome que desejar.
'''


'''
Exercício 1: Crie um método que recebe dois valores val1 e val2 (assuma que serão inteiros). O
método deve retornar verdadeiro se val1 for divisível por val2 e falso caso contrário.
'''

def conferirDivisao(val1, val2):
    
    if val1 % val2 == 0:
        return True
    else:
        return False


#conferirDivisao()

'''
Exercício 2: Crie um método chamado maiorValor que recebe 3 valores por parâmetro (assuma
que serão inteiros) e retorna o maior dos três valores.
'''

def compararMaior():
  
  primeiroNumero = int(input("Digite o primeiro número: "))
  segundoNumero = int(input("Digite o segundo número: "))
  terceiroNumero = int(input("Digite o terceiro número: "))

  maiorNumero = primeiroNumero if primeiroNumero > segundoNumero  else segundoNumero
  maiorNumero = terceiroNumero if terceiroNumero > maiorNumero  else maiorNumero

  print(f"O maior número é {maiorNumero}") 

  
#compararMaior()


'''
Exercício 3: Crie um método que recebe um valor por parâmetro (assuma que será inteiro) e
retorna a soma de todos os valores entre 0 e o valor recebido. Caso o valor seja negativo, o
método deve retornar -1.
'''

def somarRange(numero):
    
    if numero < 0:
        return -1

    somatorio = 0

    for i in range(0, numero):
        somatorio = somatorio + i
        
    print(somatorio)

#somarRange(10)


'''
Exercício 4: Crie um método que recebe um valor por parâmetro (assuma que será uma string)
e retorna a quantidade de letras ou outros caracteres que não sejam espaço que existem neste
texto.
'''

def contarLetras(resposta):

    numeroCaracteres = len(resposta) - resposta.count(" ")
    print(numeroCaracteres)

#contarLetras("minha string")

'''
Exercício 5: Crie um método que recebe uma lista por parâmetro e imprime os elementos da
lista recebida.
'''

def printarLista(lista):

    for i in lista:
        print(i)

minhaLista = ["a","b","c","d","e"]
#printarLista(minhaLista)

'''
Exercício 6: Crie um método que recebe uma lista por parâmetro (assuma que será uma lista de
string) e retorna a menor string da lista (com menos caracteres).
'''
minhaLista = ["10", "12", "5", "123", "1234"]


                                    # MÉTODO A


def retornarTamanho(elemento):
  return len(elemento)


def devolverMenorString(lista):

    lista.sort(key = retornarTamanho)
    menorString = lista[0]
    return menorString


#menorString = devolverMenorString(minhaLista)
#print(menorString)



                                    # MÉTODO B


def devolverMenorString2(lista):
    tamanhoString = []

    for i in lista:
        tamanhoString.append(len(i))

    return lista[tamanhoString.index(min(tamanhoString))]


#menorString2 = devolverMenorString2(minhaLista)
#print(menorString2)


'''
Exercício 7: Crie um método que recebe dois parâmetros, que serão um inteiro N e uma string
S (nesta ordem). O método deve imprimir na tela N vezes a string S.
'''

def printarNString(numero, string):

    print(numero * (string + "\n"))

#printarNString(2, "teste")


'''
Exercício 8: Crie um método que recebe um inteiro X por parâmetro e imprime os valores de 1
até X (inclusive).
'''

def printarRange(numero):

    for i in range(1, numero + 1):
        print(i)

#printarRange(5)

'''
Exercício 9: Crie um método que recebe 3 notas por parâmetro e retorna o conceito atingido
pela média aritmética das notas. Os conceitos são:
- entre 0.0 e 4.0 (inclusive): conceito "D"
- entre 4.0 (não incluído) e 7.0 (inclusive): conceito "C"
- entre 7.0 (não incluído) e 9.0 (inclusive): conceito "B"
- entre 9.0 (não incluído) e 10.0 (inclusive): conceito "A"
Caso alguma das notas digitadas seja negativa, retorne o texto "ERRO".
'''


def conferirMedia(nota1, nota2, nota3):

    media = (nota1 + nota2 + nota3) / 3

    if nota1 < 0 or nota2 < 0 or nota3 < 0:
        return "ERRO"

    if media > 0 and media <= 4.0:
        return "Conceito D"

    elif media > 4.0 and media <= 7.0:
        return "Conceito C"
    
    elif media > 7.0 and media <= 9.0:
        return "Conceito B"

    else: 
        return "Conceito A"
    

#print(conferirMedia(10,9,10))

'''
Exercício 10: Crie um método que recebe um inteiro por parâmetro e retorna verdadeiro caso
seja um valor primo e falso caso contrário. Caso o parâmetro seja negativo o método deve
retornar falso.
'''

def definirPrimo(resposta):

  numeroDivisores = 0
  
  i = resposta 

  while i > 0:

    if resposta % i == 0:
      numeroDivisores += 1

    if numeroDivisores > 2:
      print(f"{resposta} não é número primo.")
      return False
    
    i -= 1

  print(f"{resposta} é número primo")

  return True

#print(definirPrimo(10))
#print(definirPrimo(5))
#print(definirPrimo(847447))