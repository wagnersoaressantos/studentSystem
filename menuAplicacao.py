"""
criar função menu
"""
def menu():
    print("\n")
    print("[1]-CADASTRAR ALUNO")
    print("[2]-LISTA DE ALUNOS")
    print("[3]-CALCULAR MÉDIA GERAL")
    print("[4]-LISTA DE APROVADOS")
    print("[5]-LISTA DE REPROVADOS")
    print("[6]-EDITAR OU REMOVER MATRÍCULA")
    print("[7]-SAIR")
    opcao=int(input("digite uma opção:"))
    return opcao