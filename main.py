import os
import pickle
from faker import Faker
from Consumo import SistemaCantina
from ControleDeEstoque import Produto


def main():
    arquivo_dados = 'cantina.pkl'
    
   
    if os.path.exists(arquivo_dados):
        with open(arquivo_dados, 'rb') as f:
            cantina = pickle.load(f)
        print("Dados carregados do arquivo!")
        
    else:
        cantina = SistemaCantina()
        fake = Faker('pt_BR')
        
        print("Criando cantina nova e gerando dados falsos...")
        
        cantina.cadastrar_produto('Coxinha', Produto('Coxinha', 2.0, 4.0, "2026-03-10", "2026-03-20", 10))
        cantina.cadastrar_produto('Bolo', Produto('Bolo', 3.0, 6.0, "2026-03-10", "2026-03-15", 5))
        cantina.cadastrar_produto('Café', Produto('Café', 1.0, 2.0, "2026-03-19", "2026-03-25", 20))

        for _ in range(3):
            nome_falso = fake.name()
            cantina.realizar_venda(nome_falso, "aluno", "IA", "Coxinha")



    cantina.historico_pagamentos.exibir_historico()
    cantina.historico_consumo.exibir_relatorio_consumo() 


    with open(arquivo_dados, 'wb') as f:
        pickle.dump(cantina, f)
    print("Dados salvos no arquivo!")

if __name__ == "__main__":
    main()

