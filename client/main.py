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


