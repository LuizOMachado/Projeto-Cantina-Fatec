# 🍔 Sistema de Gerenciamento - Cantina Fatec

Este projeto está sendo desenvolvido como requisito de avaliação integrada para as disciplinas de **Estrutura de Dados** e **Linguagem de Programação II** da faculdade **FATEC**. 

O objetivo principal é simular o sistema de gerenciamento de vendas e estoque de uma cantina universitária, aplicando conceitos de programação orientada a objetos e estruturas de dados criadas do zero.

## 🎯 O Desafio Acadêmico (Em desenvolvimento)

O grande desafio deste projeto é a **proibição do uso de listas nativas do Python** (como `[]` ou métodos embutidos como `.append()`). Para solucionar isso, o sistema baseia-se no gerenciamento direto de referências de memória.

Até o momento, os desafios superados incluem:
1. **Construção de Nós (Nodes):** Criação manual de classes para encadear objetos na memória.
2. **Gerenciamento de Perecíveis (Fila/Queue):** Implementação de uma Fila rigorosa (FIFO) para garantir que os lotes de produtos mais antigos sejam vendidos primeiro.
3. **Histórico Linear:** Implementação de listas encadeadas simples para registro contínuo de dados.

## 📌 Estruturas Implementadas até agora

* **📦 Controle de Estoque (`Fila`):** Separa os lotes de produtos em formato FIFO. (Arquivo: `ControleDeEstoque.py`)
* **💸 Controle de Pagamento (`Lista Encadeada Simples`):** Estrutura customizada para guardar o histórico de pagamentos via PIX, armazenando dados do cliente e a data/hora exata da transação. (Arquivo: `ControleDePagamento.py`)

*(Projeto em andamento. Próximas etapas incluirão o relatório integrado de consumo e a persistência de dados em disco).*
