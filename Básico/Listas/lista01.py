#Desenvolva um programa que armazene quatro notas em uma lista e que apresente: a média final, a maior nota e a menor nota

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota: "))

lista_notas.insert = [ nota1 , nota2 , nota3 , nota4]

media_notas = sum(lista_notas) / len(lista_notas)

print("A menor das notas é: ", min(lista_notas))
print("A maior das notas é: ", max(lista_notas))
print("A média das notas é: ", media_notas)
