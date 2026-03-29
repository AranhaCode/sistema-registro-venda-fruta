from funcoes import menu , registrar_frutas , registrar_vendas ,visualizar_estoque , remover_item
from dados import fruta_estoque 
vendas_totais = 0
while True:
    menus = menu()
    match menus:
        case "1":
            print("Indo para registrar frutas")
            registrar_frutas(fruta_estoque)
        case "2":
            print("Indo para registrar vendas")
            valor_venda = registrar_vendas(fruta_estoque)
            vendas_totais += valor_venda
        case "3":
            print("Indo para visualizaçao de estoque")
            visualizar_estoque(fruta_estoque)
        case "4":
            print("Indo para visualizaçao de vendas")
            print(f"Total de vendas: {vendas_totais}")
        case "5":
            print("Indo para remoçao de itens")
            remover_item(fruta_estoque)
        case "6":
            print("Fechando caixa")
            break
