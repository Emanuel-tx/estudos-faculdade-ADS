total_reposicoes:int = 0
total_vendas:int = 0
estoque:int = 100
def acao_venda():
    global: estoque, total_vendas
    if(estoque < 1):
        print("ERRO: Não foi possivel fazer a venda. O estoque está vazio")
    else:
        estoque -= 1
        total_vendas += 1
        print("Vendido 1 produto")
        return estoque and total_vendas
def acao_reposicao():
    estoque += 1
    print("Adicionado 1 produto ao estoque")
    return estoque
def listar_estat():
    print("Total de vendas: ",total_vendas)
    print("Total de reposições: ",total_reposicoes)
    print("Estoque atual: ",estoque)
print("1: Fazer reposição")
print("2: Fazer uma venda")
print("3: Listar estatísticas")
print("4: Sair")
opcao:int = input("Digite o número da ação que deseja fazer: ")
if (opcao == 1):
    acao_reposicao()
elif(opcao == 2):
    acao_venda()
