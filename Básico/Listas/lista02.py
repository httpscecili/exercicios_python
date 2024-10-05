#Desenvolva um programa que armazene quatro notas em uma lista e que apresente a média final. Caso a média seja igual ou superior a 7, apresentar a mensagem "APROVADO", caso contrário, armazenar a nota da prova final e recalcular a média. Caso a nova média seja igual superior a 5, apresentar a mensagem "APROVADO", caso contrário, apresentar a mensagem "REPROVADO"

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota: "))

lista_media_final.insert = [ nota1 , nota2 , nota3 , nota4 ]

media_notas = sum(lista_media_final) / len(lista_media_final)

  if media_notas >= 7 :
    print("APROVADO")
    
  else :
    nota_final = float(input("Insira a nota da prova final: "))
    nova_media = (media_notas + nota_final) / 2
    if nova_media >= 5:
    print("APROVADO")
    else:
    print("REPROVADO")
