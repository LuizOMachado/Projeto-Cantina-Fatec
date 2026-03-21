class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.nome} (Qtd: {self.quantidade} | Vence em: {self.data_vencimento})"

class NoProduto:
    def __init__(self, produto):
        self.produto = produto
        self.proximo = None

class FilaEstoque:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileirar(self, produto):
        novo_no = NoProduto(produto)
        if self.fim is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def desenfileirar(self):
        if self.inicio is None:
            return None
        no_removido = self.inicio 
        self.inicio = self.inicio.proximo 
        if self.inicio is None: 
            self.fim = None
        return no_removido.produto

    def editar_quantidade(self, nome_produto, nova_quantidade):
        atual = self.inicio
        while atual is not None:
            if atual.produto.nome == nome_produto:
                atual.produto.quantidade = nova_quantidade
                return True
            atual = atual.proximo
        return False