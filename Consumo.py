
from ControleDeEstoque import FilaEstoque, Produto
from ControleDePagamento import ListaPagamentos, Pagamento


class RegistroConsumo:
    def __init__(self, pagamento, produto):
        self.pagamento = pagamento
        self.produto = produto   
        self.proximo = None


class ListaConsumo:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def registrar_consumo(self, pagamento, produto):
        novo_no = RegistroConsumo(pagamento, produto)
        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def exibir_relatorio_consumo(self):
        atual = self.inicio
        print("\n--- RELATÓRIO DE CONSUMO ---")
        if atual is None:
            print("Nenhum consumo registrado.")
        else:
            while atual is not None:
                print(f"Cliente: {atual.pagamento.nome_pagador} | Consumiu: {atual.produto.nome} | Curso: {atual.pagamento.curso}")
                atual = atual.proximo
        print("----------------------------\n")


class SistemaCantina:
    def __init__(self):
        
        self.estoque_por_produto = {} 
        self.historico_pagamentos = ListaPagamentos()
        self.historico_consumo = ListaConsumo()

   
    def cadastrar_produto(self, categoria_produto, produto):
      
        if categoria_produto not in self.estoque_por_produto:
            self.estoque_por_produto[categoria_produto] = FilaEstoque()
        
        self.estoque_por_produto[categoria_produto].enfileirar(produto)

    
   
    def realizar_venda(self, nome_cliente, categoria_cliente, curso, nome_produto_desejado):
        
        if nome_produto_desejado not in self.estoque_por_produto:
            print(f"Erro: Não vendemos '{nome_produto_desejado}' na cantina.")
            return

        fila_do_produto = self.estoque_por_produto[nome_produto_desejado]
        

        if fila_do_produto.inicio is None:
            print(f"Aviso: O estoque de '{nome_produto_desejado}' está totalmente esgotado!")
            return


        produto_venda = fila_do_produto.inicio.produto
        
        
        produto_venda.quantidade -= 1

        novo_pagamento = Pagamento(nome_cliente, categoria_cliente, curso, produto_venda.preco_venda)
        self.historico_pagamentos.registrar_pagamento(novo_pagamento)
        self.historico_consumo.registrar_consumo(novo_pagamento, produto_venda)
        
        print(f"Sucesso: {nome_cliente} comprou {nome_produto_desejado}! (Restam {produto_venda.quantidade} neste lote)")

        if produto_venda.quantidade == 0:
            fila_do_produto.desenfileirar()