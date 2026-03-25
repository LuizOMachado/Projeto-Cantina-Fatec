import datetime
import pickle
import os
from faker import Faker

fake = Faker('pt_BR')

class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade = quantidade

class NoEstoque:
    def __init__(self, produto):
        self.produto = produto
        self.proximo = None

class ListaEstoque:
    def __init__(self):
        self.inicio = None
        self.fim = None

    
    def adicionar_lote(self, produto):
        novo_no = NoEstoque(produto)
        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

   
    def baixar_item_especifico(self, nome_produto):
        atual = self.inicio
        anterior = None

        while atual is not None:
            if atual.produto.nome.lower() == nome_produto.lower():
                prod_selecionado = atual.produto
                
                if prod_selecionado.quantidade > 1:
                    prod_selecionado.quantidade -= 1
                    return prod_selecionado
                else:
                   
                    if anterior is None:
                        self.inicio = atual.proximo
                        if self.inicio is None:
                            self.fim = None
                    else:
                        anterior.proximo = atual.proximo
                        if atual.proximo is None:
                            self.fim = anterior
                    
                    prod_selecionado.quantidade = 0
                    return prod_selecionado
            
            anterior = atual
            atual = atual.proximo
            
        return None

    def listar_disponiveis(self):
        atual = self.inicio
        if not atual:
            print("Estoque vazio!")
            return False
            
        
        produtos_vistos = [] 
        print("\n--- ITENS DISPONÍVEIS NA CANTINA ---")
        while atual:
            p = atual.produto
            if p.nome not in produtos_vistos:
                print(f"- {p.nome} (R$ {p.preco_venda:.2f})")
                produtos_vistos.append(p.nome)
            atual = atual.proximo
        return True

    def listar_todos_os_lotes(self):
        atual = self.inicio
        i = 1
        if not atual:
            print("Estoque vazio!")
            return False
        print("\n--- TODOS OS LOTES NO ESTOQUE ---")
        while atual:
            p = atual.produto
            print(f"{i}. Produto: {p.nome} | Vencimento: {p.data_vencimento} | Qtd: {p.quantidade}")
            atual = atual.proximo
            i += 1
        return True

    def editar_quantidade_lote(self, indice, nova_quantidade):
        atual = self.inicio
        i = 1
        while atual:
            if i == indice:
                atual.produto.quantidade = nova_quantidade
                return True
            atual = atual.proximo
            i += 1
        return False

class Pagamento:
    def __init__(self, nome, categoria, curso, valor):
        self.nome_pagador = nome
        self.categoria = categoria
        self.curso = curso
        self.valor = valor
        self.data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


class RegistroConsumo:
    def __init__(self, pagamento, produto):
        self.pagamento = pagamento
        self.nome_produto = produto.nome
        self.preco_compra = produto.preco_compra
        self.preco_venda = produto.preco_venda

class NoSimples:
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar(self, item):
        novo = NoSimples(item)
        if not self.inicio:
            self.inicio = self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

class SistemaCantina:
    def __init__(self):
        self.estoque = ListaEstoque()
        self.pagamentos = ListaEncadeada()
        self.consumo = ListaEncadeada()
        self.arquivo = "banco_cantina.pkl"

    def salvar(self):
        with open(self.arquivo, 'wb') as f:
            pickle.dump({'e': self.estoque, 'p': self.pagamentos, 'c': self.consumo}, f)

    def carregar(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'rb') as f:
                d = pickle.load(f)
                self.estoque, self.pagamentos, self.consumo = d['e'], d['p'], d['c']

    def popular_faker(self):
       
        produtos_fake = ["Coxinha", "Refrigerante", "Bolo", "Suco", "Pão de Queijo"]
        hoje = datetime.date.today().strftime("%d/%m/%Y")
        vencimento = fake.future_date(end_date="+30d").strftime("%d/%m/%Y")
        
        for nome_prod in produtos_fake:
            pc = round(fake.random.uniform(2.0, 5.0), 2)
            pv = round(pc * 1.5, 2)
            q = fake.random_int(min=5, max=15)
            self.estoque.adicionar_lote(Produto(nome_prod, pc, pv, hoje, vencimento, q))

        
        for _ in range(5):
            nome_cliente = fake.name()
            curso = fake.random_element(elements=("IA", "ESG"))
            cat = fake.random_element(elements=("Aluno", "Professor", "Servidor"))
            
            produto_aleatorio = fake.random_element(elements=produtos_fake)
            prod_baixado = self.estoque.baixar_item_especifico(produto_aleatorio)
            
            if prod_baixado:
                p = Pagamento(nome_cliente, cat, curso, prod_baixado.preco_venda)
                self.pagamentos.adicionar(p)
                reg_consumo = RegistroConsumo(p, prod_baixado)
                self.consumo.adicionar(reg_consumo)

def main():
    sys = SistemaCantina()
    sys.carregar()

    while True:
        print("\n" + "="*40)
        print("  SISTEMA DE CONFIANÇA - CANTINA FATEC")
        print("="*40)
        print("1. COMPRAR ALGO (Identificar-se)")
        print("2. ABASTECER ESTOQUE (Atlética)")
        print("3. EDITAR QUANTIDADE NO ESTOQUE")
        print("4. VER RELATÓRIOS (Vendas/Consumo)")
        print("5. POPULAR COM DADOS FALSOS (Faker)")
        print("0. SAIR")
        
        op = input("\nEscolha uma opção: ")

        if op == "1":
            if sys.estoque.listar_disponiveis():
                produto_escolhido = input("\nDigite o nome do produto que deseja pegar: ")
                
                nome = input("Digite seu Nome: ")
                print("Categorias: 1. Aluno | 2. Professor | 3. Servidor")
                cat_op = input("Sua Categoria: ")
                cat = "Aluno" if cat_op == "1" else "Professor" if cat_op == "2" else "Servidor"
                
                print("Cursos: 1. IA | 2. ESG")
                curso_op = input("Seu Curso: ")
                curso = "IA" if curso_op == "1" else "ESG"

                confirmar = input(f"Você confirma que pegou '{produto_escolhido}' e pagou via PIX? (S/N): ")
                if confirmar.lower() == 's':
                    item_vendido = sys.estoque.baixar_item_especifico(produto_escolhido)
                    
                    if item_vendido:
                        p = Pagamento(nome, cat, curso, item_vendido.preco_venda)
                        sys.pagamentos.adicionar(p)
                        
                        reg_consumo = RegistroConsumo(p, item_vendido)
                        sys.consumo.adicionar(reg_consumo)
                        print(f"\n Obrigado, {nome}! Registro realizado com sucesso.")
                    else:
                        print(f"\n Produto '{produto_escolhido}' não encontrado no estoque ou indisponível.")
            
        elif op == "2":
            n = input("Nome do Produto: ")
            pc = float(input("Preço de Compra: "))
            pv = float(input("Preço de Venda: "))
            dv = input("Vencimento (dd/mm/aaaa): ")
            q = int(input("Quantidade: "))
            hoje = datetime.date.today().strftime("%d/%m/%Y")
            sys.estoque.adicionar_lote(Produto(n, pc, pv, hoje, dv, q))
            print(" Lote adicionado ao estoque.")

        elif op == "3":
            if sys.estoque.listar_todos_os_lotes():
                try:
                    indice = int(input("\nDigite o número do lote que deseja editar: "))
                    nova_qtd = int(input("Digite a nova quantidade: "))
                    if sys.estoque.editar_quantidade_lote(indice, nova_qtd):
                        print(" Quantidade atualizada com sucesso.")
                    else:
                        print(" Lote não encontrado.")
                except ValueError:
                    print("Por favor, digite valores numéricos válidos.")

        elif op == "4":
            print("\n--- RELATÓRIO DE VENDAS ---")
            atual = sys.pagamentos.inicio
            if not atual: print("Nenhuma venda registrada.")
            while atual:
                v = atual.conteudo
                print(f"[{v.data_hora}] {v.nome_pagador} ({v.curso}) - R$ {v.valor:.2f}")
                atual = atual.proximo
            
            print("\n--- RELATÓRIO DE CONSUMO E LUCRO ---")
            atual = sys.consumo.inicio
            if not atual: print("Nenhum consumo registrado.")
            while atual:
                c = atual.conteudo
                lucro = c.preco_venda - c.preco_compra
                print(f"Item: {c.nome_produto} | Cliente: {c.pagamento.nome_pagador} | Lucro: R$ {lucro:.2f}")
                atual = atual.proximo

        elif op == "5":
            sys.popular_faker()
            print("Sistema populado com estoque e 5 vendas aleatórias (Faker).")

        elif op == "0":
            sys.salvar()
            print("Dados salvos. Encerrando...")
            break

if __name__ == "__main__":
    main()