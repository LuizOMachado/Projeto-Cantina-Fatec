import datetime

class Pagamento:
    def __init__(self, nome_pagador, categoria, curso, valor):
        self.nome_pagador = nome_pagador
        self.categoria = categoria 
        self.curso = curso         
        self.valor = valor
        self.data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def __str__(self):
        return f"[{self.data_hora}] {self.nome_pagador} ({self.categoria}/{self.curso}) pagou R${self.valor:.2f}"

class NoPagamento:
    def __init__(self, pagamento):
        self.pagamento = pagamento
        self.proximo = None

class ListaPagamentos:
    def __init__(self):
        self.inicio = None
        self.fim = None 

    def registrar_pagamento(self, pagamento):
        novo_no = NoPagamento(pagamento)
        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no
    def exibir_historico(self):
        atual = self.inicio
        print("\n--- HISTÓRICO DE PAGAMENTOS (PIX) ---")
        if atual is None:
            print("Nenhum pagamento registrado.")
        else:
            while atual is not None:
                print(atual.pagamento)
                atual = atual.proximo
        print("-------------------------------------\n")