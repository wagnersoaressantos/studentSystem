from menuAplicacao import menu
from controladorAluno import *
def main():

    while True:
        opcaoMenur=menu()
        if opcaoMenur ==1:
            cadastrarAluno()
        elif opcaoMenur ==2:
            listaDeAlunos()
        elif opcaoMenur ==3:
            calcularMediaGeral()
        elif opcaoMenur ==4:
            listaDeAprovados()
        elif opcaoMenur ==5:
            listaDeReprovados()
        elif opcaoMenur ==6:
            editarOuRemoverMatricula()
        elif opcaoMenur ==7:
            print("Finalizando programa!!!")
            break
        else:
            print("Opção invalida!!!")
            print("Escolha de novo!!!")
            input()
main()
