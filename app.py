#biblioteca
import os

#lista
nomes = []
#loop
while true:
    #menu
    print("1- cadastrar novo nome.")
     print("2- exibir lista.")
     print("3- ordenar lista.")
     print("4-  alterar o nome da lista.")
     print("5-excluir nome da lista .")
     print("6- ir do programa.")
    
    #usuario imformar a opcao escolhida
    ]opcao = input("opcao desejada:")

#lista console
os.system("cls")

#programa verifica a opcao escolhida pelo usuario
match opcao:
   case "1":
      novo_nome = input("informe o nome  a ser cadastrado:")
      nomess.append(novo_nome)
      print(f"{novo_nome} cadastrado com sucesso.")
      continue
   case "2":
      print("LISTA:\n")
      for i in range(len(nomes)):
         print("\n")
         continue
      case "3":
      nomes.sort()
      print("lista ordenada com sucesso.")
      case "4"}:
try:
   indice = int(input("informe o indice do nome  aseralterado:"))
   confirmar =input(f"deseja alterar o nome{nomes[indice]}? digite 'sim' para confirmar:")
                    
    if confirmar == "sim":
         nomes[indice = input("informe o novo nome:")
        print("nome cadastrado com sucesso!")
        else:
        print("nome nao foi alterado.")
        except exception as e :
        print(f"nao foi possivel alterar.{e}.")
        finally:
        continuecase "5":
        indice = int(input("informe o indice do nome que deseja excluir:"))
        confirmar = input(f"deseja excluir o nome{nomes[indice]} da lista?digite 'sim' para confirmar:")
 case "5":
 try:
 indice = int("(informe o indice do nome que deseja excluir:"))
   confirmar = input
 
    