import datetime
def menu():
        print("="*40)
        print(" MENU ")
        print("="*40)
        opcao = input("Oque voce deseja fazer:\n 1.Registrar frutas \n 2.Registrar venda \n 3.Visualizar estoque .\n 4.Visualizar vendas \n 5.Remover item do estoque \n 6.Sair")
        return opcao
def registrar_frutas(fruta_estoque):
    while True:
        data_entrada = datetime.datetime.now().strftime("%d/%m/%Y |%H:%M")
        nome = input("Insira o nome da fruta:").lower().capitalize()
        kilos = float(input("Insira quantos quilos essas frutas tem:"))
        custo = float(input("Insira o preço por quilo dessa fruta:"))
        lista_frutas = { "Nome": nome, 
                        "Quilos": kilos ,
                        "Preço por quilo": custo ,
                        "Data de entrada": data_entrada  }
        fruta_estoque.append(lista_frutas)
        mais = input("Deseja adicionar mais frutas?: \n 1.Sim \n 2.Nao")
        if mais == "2":
            print("Voltando para o menu")
            return
def registrar_vendas(fruta_estoque):
     total_sessao = 0
     if len(fruta_estoque) == 0:
          print("Nao a nenhuma fruta no estoque para ser vendida")
          return 0
     while True:
        nome_fruta = input("Insira o nome da fruta vendida:")
        nome_quilos = float(input("Insira a quantidade de quilos que foram vendidos"))
        achou = False
        for fruta in fruta_estoque:
            if fruta['Nome'].lower() == nome_fruta.lower():
                    achou = True
                    if fruta['Quilos'] >= nome_quilos:
                            valor = nome_quilos * fruta["Preço por quilo"]
                            fruta['Quilos'] -= nome_quilos
                            total_sessao += valor
                            print(f"O valor foi de {valor:.2f}")
                            if fruta['Quilos'] < 5:
                                print("Comprar mais frutas!!")
                    else:
                          print("Nao possui fruta no estoque")
        if achou == False:
             print("Essa fruta nao esta cadastrada no estoque")                   
        maiss = input("Deseja registrar mais vendas. \n 1.Sim \n 2.Nao")                
        if maiss == "2":
             return total_sessao
def visualizar_estoque(fruta_estoque):
     if len(fruta_estoque) == 0:
          print("Nao a frutas no estoque")
          return  
     for Visufruta in fruta_estoque:
          print(f"Nome: {Visufruta['Nome']} | Quilos: {Visufruta['Quilos']} | Preço por quilo: {Visufruta['Preço por quilo']} | Data de entrada: {Visufruta['Data de entrada']}")            
def remover_item(fruta_estoque):   
     if len(fruta_estoque) == 0:
          print("Nao a nada no estoque para ser removido")
          return
     tudo_um = input("Oque voce deseja fazer: \n 1.Remover um item \n 2.limpar a lista inteira")
     match tudo_um:
          case "1":
               while True:
                    item = input("Qual fruta voce deseja remover da lista?:").lower()
                    achado = False
                    for frutinha in fruta_estoque:
                         if frutinha['Nome'].lower() == item.lower():
                              achado = True
                              fruta_estoque.remove(frutinha)
                              print(f"A fruta {item} foi removida da lista")
                              maisss = input("Voce deseja remover mais um item?: \n 1.Sim \n 2.Nao")
                              if maisss == "2":
                                   print("Voltando para o menu")
                                   return
                    if achado == False:
                         print("Fruta nao encontrada")
          case "2":
               certeza = input("Voce tem certeza que deseja limpar a lista inteira?: \n 1.Sim \n 2.Nao")
               if certeza == "1":
                    fruta_estoque.clear()
                    print("Todos os item da lista foram removidos")
                    return
