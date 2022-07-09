"""
Criar lista e funções
"""
listaAluno=[]
def cadastrarAluno():
    print("*****CADASTRAR ALUNO****")
    while True:
        matricula=input("Digite Matrícula:")
        if checarAluno(matricula):
            print("Matrícula já cadastrada!!")
            input("Click em enter para retornar au menu!!!")
            break
        nome=input("Digite nome:")
        media=float(input("Digite média:"))
        aluno=[matricula,nome,media]
        listaAluno.append(aluno)
        opcao=int(input("Deseja fazer outro cadastro? [1] - Sim;[2] - Não:\n"))
        print("opção: ",opcao)
        if opcao != 1:
            break
def checarAluno(matricula):
    cadastrarAluno=False
    for i in range(0,len(listaAluno)):
        if matricula==listaAluno[i][0]:
            cadastrarAluno=True
    return cadastrarAluno

def listaDeAlunos():
    print("\n")
    print("*****LISTA DE ALUNOS*****")
    print("Matricula\tNome\t\tMédia")
    for i in range (0,len(listaAluno)):
        print("\t"+listaAluno[i][0]+"\t\t"+listaAluno[i][1]+"\t\t"+str(listaAluno[i][2]))
        """print("Matrícula: ",listaAluno[i][0])
        print("Nome: ", listaAluno[i][1])
        print("Média: ", listaAluno[i][2])"""
    input("Click em enter para voltar ao menu!!")

def calcularMediaGeral():
    print("\n")
    print("*****CALCULAR MÉDIA GERAL*****")
    somaMedias=0.0
    for i in range (0,len(listaAluno)):
        somaMedias+= listaAluno[i][2]
        media=somaMedias/len(listaAluno)
    print(media)
    input("Click em enter para voltar ao menu!!")
def listaDeAprovados():
    print("\n")
    print("*****LISTA DE APROVADOS*****")
    for i in range(0, len(listaAluno)):
        if listaAluno[i][2] >= 7:
            print("Matrícula: ", listaAluno[i][0])
            print("Nome: ", listaAluno[i][1])
            print("Média: ", listaAluno[i][2])
    input("Click em enter para voltar ao menu!!")

def listaDeReprovados():
    print("\n")
    print("*****LISTA DE REPROVADOS*****")
    for i in range(0, len(listaAluno)):
        if listaAluno[i][2] < 7:
            print("Matrícula: ", listaAluno[i][0])
            print("Nome: ", listaAluno[i][1])
            print("Média: ", listaAluno[i][2])
    input("Click em enter para voltar ao menu!!")

def editarOuRemoverMatricula():
    print("\n")
    print("*****EDITAR OU REMOVER MATRÍCULA*****")
    matricula=input("Informe a matrícular: ")
    for i in range(0, len(listaAluno)):
        if listaAluno[i][0]==matricula:
            print("Deseja Remover ou Editar o cadastros do Aluno:")
            print("Matrícula: ", listaAluno[i][0])
            print("Nome: ", listaAluno[i][1])
            print("Média: ", listaAluno[i][2])
            opcao = int(input("Digite:\n[1]- PARA EDITAR \nou\n[2]- PARA REMOVER\nOpção: "))
            if opcao == 1:
                print("*****EDITAR CADASTRO*****")
                print("Do(a) aluno(a): ", listaAluno[i][1])
                confirmacao = int(input("\nDeseja editar o cadastro:\n[1]-SIM\n[2]-NÃO\nQual opção?"))
                if confirmacao == 1:
                    editar=int(input("\nGosta de editar oque:\n[1]-Matrícula\n[2]-Nome\n[3]-Média\nqual opção?"))
                    if editar==1:
                        print("Editar matricula")
                        print("De", listaAluno[i][1])
                        novaMatricula=input("\nDigite a nova matricula: ")
                        print("Matrícula antiga: ",listaAluno[i][0])
                        listaAluno[i][0]=novaMatricula
                        print("Nova matrícula: ",listaAluno[i][0])
                    elif editar==2:
                        print("editar Nome")
                        novoNome = input("\nDigite a novo nome: ")
                        print("Nome antigo: ", listaAluno[i][1])
                        listaAluno[i][1] = novoNome
                        print("Nova nome: ", listaAluno[i][1])
                    elif editar==3:
                        print("Editar média")
                        novaMedia = input("\nDigite a nova media: ")
                        print("Média antiga: ", listaAluno[i][2])
                        listaAluno[i][1] = novaMedia
                        print("Nova média: ", listaAluno[i][2])
                    input("Clik enter para retorna ao menur!!")
            elif opcao==2:
                print("*****REMOVER CADASTRO*****")
                print("Do(a) aluno(a): ", listaAluno[i][1])
                confirmacao=int(input("\nconfimar a exclusão:\n[1]-SIM\n[2]-NÃO\nQual opção?"))
                if confirmacao==1:
                    listaAluno.pop(i)
                    print("Cadastro excluido!!")
                    input("Clik enter para retorna ao menur!!")
                return
            return
    print("Matrícula não encontrada!!!")
    input("click em entre para retorna ao menu!!!")