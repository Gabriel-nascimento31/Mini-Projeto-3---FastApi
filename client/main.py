import requests

#URL = "http://127.0.0.1:8000/produtos"

URL_PRODUTOS = "http://127.0.0.1:8000/produtos"
URL_COMPRAR = "http://127.0.0.1:8000/comprar"

print("--Produtos Disponíveis--")
resposta_produtos = requests.get(URL_PRODUTOS)

if resposta_produtos.status_code == 200:
    dados_produtos = resposta_produtos.json()
    for produto in dados_produtos:
        status_estoque = "Em estoque" if produto["em_estoque"] else "Sem estoque"
        print(f"ID: {produto['id']} | {produto["nome"]} - R$ {['preco']}({status_estoque})")
else:
    print("Erro ao listar os produtos da API.")
    exit()
print("\n" + "="*50 + "\n")


while True:
    print("--- ÁREA DE COMPRA ---")
    
    try:
        # Capturando os dados digitados pelo usuário
        id_escolhido = int(input("Digite o ID do produto que deseja comprar: "))
        quantidade_escolhida = int(input("Digite a quantidade desejada: "))
        
        dados_da_compra = {
            "produto_id": id_escolhido,
            "quantidade": quantidade_escolhida
        }

        print(f"\nEnviando pedido de compra para a API...")
        resposta_compra = requests.post(URL_COMPRAR, json=dados_da_compra)

        # Se o status for 201 (Created), a compra deu certo
        if resposta_compra.status_code == 201:
            resultado = resposta_compra.json()
            detalhes = resultado["detalhes_do_pedido"]
            
            print("\n SUCESSO!")
            print(f"Mensagem: {resultado['mensagem']}")
            print(f"Pedido ID: #{detalhes['pedido_id']}")
            print(f"Produto: {detalhes['produto_nome']}")
            print(f"Quantidade: {detalhes['quantidade']}")
            print(f"Valor Total: R$ {detalhes['valor_total']}")
        
        # Se retornar erro (ex: produto sem estoque ou ID inexistente)
        else:
            erro = resposta_compra.json()
            print("\n FALHA NA COMPRA!")
            print(f"Motivo: {erro.get('detail', 'Erro desconhecido')}")

    except ValueError:
        print("\n ERRO DE DIGITAÇÃO!")
        print("Por favor, digite apenas números inteiros válidos para o ID e quantidade.")

    print("\n" + "-"*30)
    
    # Condição de saída do loop infinito
    opcao = input("Deseja fazer outra compra? (Pressione Enter para continuar ou 's' para sair): ").strip().lower()
    if opcao == 's':
        print("\n Obrigado por comprar conosco. Até logo!")
        break # Quebra o loop infinito e encerra o programa
        
    print("\n" + "="*50 + "\n")
