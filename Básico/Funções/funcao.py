#Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar

number = int(input("Insira qualquer número inteiro: "))

if number % 2 == 0:
    print("O número", number, "é par")
else:
    print("O número", number, "é ímpar")
