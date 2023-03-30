                    #Exercícios de fixação WHILE 


# EX 1

i = 0


# while i < 10:
    
#     resposta = int(input("Digite um número aleatório: "))
    
#     if resposta < 0:
#       print("Número negativo")
    
#     elif resposta == 0:
#        print("O número digitado é zero.")

#     elif resposta > 0:
#        print("Número positivo")

#     i += 1
       

'''
Exercício 2. Faça um programa que escreva na
tela todos os números inteiros entre 0
(inclusive) e 1000 (inclusive).
'''

i = 0

for i in range(0, 1001):
   print(i)



'''
Exercício 3. Faça um programa que escreva na
tela todos os valores inteiros que estão entre dois
valores digitados pelo usuário (num1e num2).
Caso num1seja maior do que num2, imprima uma
mensagem de erro e não imprima.
'''

i = 0

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
   print("Erro")

for i in range(num1, num2):
   print(i)



'''   
Exercício 4. Faça um programa que escreva na
tela todos os valores inteiros entre dois valores
digitados pelo usuário (num1e num2). Caso
num1 seja maior do que num2, seu programa
deve imprimir os valores entre num1 e num2da
mesma forma.
'''

i = 0

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
   for i in range(num2, num1):
      print(i)

else:
  for i in range(num1, num2):
    print(i)


'''   
Exercício 5. Faça um programa que
imprima na tela a soma de todos os
valores entre 1 e 1000.
'''

somatorio = 0

i = 1

while i < 1000:

    somatorio = somatorio + i
    
    i += 1

print(somatorio)



'''
Exercício 6. Faça um programa que solicita ao
usuário que ele digite números que sejam
positivos e pares. Quando o usuário digitar um
número que não seja o solicitado, imprima na
tela a soma dos valores positivos e pares
digitados.
'''
somatorio = 0

resposta = int(input("Digite um número: "))

while resposta > 0 and resposta % 2 == 0:
   somatorio += resposta

   resposta = int(input("Digite um número: "))

print(f"Soma dos números: {somatorio}")

'''
Exercício 7. O usuário e a senha de um cliente
são, respectivamente, USER10 e
PASSWORD1234. Sabendo disso, faça um
programa que solicita ao usuário que ele digite
seu usuário e senha. O programa só termina
quando ele acertar o usuário e a senha. Quando
ele acertar, você deve informar a mensagem:
LOGIN EFETUADO COM SUCESSO.
'''

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

while usuario.lower() != "user10" or senha.lower() != "password1234":
  print("Login inválido. Usuário e/ou senha incorreta/s.")
  usuario = input("Digite seu usuário: ")
  senha = input("Digite sua senha: ")

print("LOGIN EFETUADO COM SUCESSO")




'''
Exercício 8. O usuário e a senha de um cliente são,
respectivamente, USER10 e PASSWORD1234 . Sabendo
disso, faça um programa que solicita ao usuário que ele
digite seu usuário e senha. O programa termina quando ele
acertar o usuário e a senha ou quando ele exceder o máximo
de 3 tentativas. Quando ele acertar, o programa deve
informar a mensagem: LOGIN EFETUADO COM
SUCESSO . Caso ele exceda a quantidade de tentativas, o
programa deve informar a mensagem: NÚMERO MÁXIMO
DE TENTATIVAS EXCEDIDO !
'''

def logar():

  usuario = input("Digite seu usuário: ")
  senha = input("Digite sua senha: ")
  tentativasLogin = 0

  while usuario.lower() != "user10" or senha.lower() != "password1234":
    print("Login inválido. Usuário e/ou senha incorreta/s.")
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    
    tentativasLogin += 1

    if tentativasLogin == 3:
      print("NÚMERO MÁXIMO DE TENTATIVAS EXCEDIDO")
      return
    
  print("LOGIN EFETUADO COM SUCESSO")

logar()