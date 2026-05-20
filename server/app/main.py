from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
import random

app = FastAPI(
    title="API de Consumo e Vendas",
    description="Uma API para fornecer uma grande listagem de produtos e permitir compras simuladas.",
    version="1.2.0"
)


NOMES_PRODUTOS = ["Notebook", "Smartphone", "Tablet", "Monitor", "Teclado", "Mouse", "Cadeira Gamer", "Fone de Ouvido", "Mochila", "Smartwatch", "Câmera", "Microfone", "Placa de Vídeo", "SSD", "Memória RAM", "Processador", "Placa Mãe", "Gabinete", "Webcam", "Caixa de Som"]
ADJETIVOS_MARCAS = ["Pro", "Gamer", "Ultra", "Max", "Lite", "Plus", "X", "One", "Prime", "Elite", "Advanced", "Smart", "Mini", "Super"]

random.seed(42) 

BASE_DE_DADOS = [
    {
        "id": i,
        "nome": f"{random.choice(NOMES_PRODUTOS)} {random.choice(ADJETIVOS_MARCAS)} {random.randint(100, 9000)}",
        "preco": round(10.50 * i, 2),
        "em_estoque": i % 3 != 0
    }
    for i in range(1, 101)
]


HISTORICO_COMPRAS = []


class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_estoque: bool

class PedidoCompra(BaseModel):
    produto_id: int
    quantidade: int


@app.get("/", tags=["Home"])
def pagina_inicial():
    return {
        "mensagem": "Bem-vindo à API de Dados e Vendas!",
        "total_produtos_cadastrados": len(BASE_DE_DADOS),
        "documentacao": "/docs"
    }

@app.get("/produtos", response_model=List[Produto], tags=["Produtos"])
def obter_todos_os_produtos(em_estoque: Optional[bool] = None):
    
    if em_estoque is not None:
        return [p for p in BASE_DE_DADOS if p["em_estoque"] == em_estoque]
    return BASE_DE_DADOS

@app.get("/produtos/{produto_id}", response_model=Produto, tags=["Produtos"])
def obter_produto_por_id(produto_id: int):
    
    produto = next((p for p in BASE_DE_DADOS if p["id"] == produto_id), None)
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Produto com ID {produto_id} não encontrado."
        )
    return produto


@app.post("/comprar", status_code=status.HTTP_201_CREATED, tags=["Vendas"])
def realizar_compra(pedido: PedidoCompra):
    
    produto = next((p for p in BASE_DE_DADOS if p["id"] == pedido.produto_id), None)
    
    
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Produto com ID {pedido.produto_id} não encontrado."
        )
    
    
    if not produto["em_estoque"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"O produto '{produto['nome']}' está sem estoque no momento."
        )
    
    
    if pedido.quantidade <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A quantidade do pedido deve ser pelo menos 1."
        )
    
    
    valor_total = round(produto["preco"] * pedido.quantidade, 2)
    
    
    novo_pedido = {
        "pedido_id": len(HISTORICO_COMPRAS) + 1,
        "produto_id": produto["id"],
        "produto_nome": produto["nome"],
        "quantidade": pedido.quantidade,
        "valor_total": valor_total,
        "status": "Aprovado"
    }
    
    
    HISTORICO_COMPRAS.append(novo_pedido)
    
    return {
        "mensagem": "Compra realizada com sucesso!",
        "detalhes_do_pedido": novo_pedido
    }


@app.get("/compras", tags=["Vendas"])
def obter_historico_de_compras():
    
    return HISTORICO_COMPRAS