
#atividade 1

tri1 = 50
tri2 = 60
tri3 = 70
resultado = tri1 + tri2 + tri3
i = "vinicius"

if  resultado >= 180:
    print("A pontuacao do aluno "+i+" foi de "+str(resultado)+" entao foi aprovado")
else:
    print("A pontuacao do aluno "+i+" foi de "+str(resultado)+" entao foi reprovado")

#/////////////////////////////////////////////////////////////

#atividade 2

digit = input("digite o nucleotídeo:")

if digit ==  "A":
    print("T")
    
elif digit == "T":
    print("A")
    
elif digit == "C":
    print("G")
    
elif digit == "G":
    print("C")
    
else:
    print("nucleotídeo invalido")
  
#//////////////////////////////////////////////////////////

#atividade 3

print("informe dois numeros da sua escolha")

num1 = int(input("informe o primeiro numero da sua escolha:"))
num2 = int(input("informe o segundo numero da sua escolha:"))

num = print("escolha uma das opções:")

print("1. Some de 2 números")          
print("2. Diferença entre os 2 números (maior pelo menor)")          
print("3. Produto entre 2 números.")          
print("4. Divisão entre 2 números (o denominador não pode ser zero)")    

escolha = input("DIGITE O NUMERO DA OPCAO ESCOLHIDA AQUI:")

if escolha == "1":
    resultado = num1 + num2
    print("O resultado foi", resultado)
    
elif escolha == "2":
    resultado = num1 > num2
    print("O resultado foi", resultado)
    
elif escolha == "3":
    resultado = num1 * num2
    print("O resultado foi", resultado)
    
elif escolha == "4":
    if num2 != 0:
     resultado = num1 / num2
     print("O resultado foi", resultado)
    else:
     print("não é possível dividir por zero!")

else:
    print("Opção inválida!")

