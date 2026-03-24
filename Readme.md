# 🍔 Sistema de Gerenciamento - Cantina Fatec

[cite_start]Este projeto foi desenvolvido como requisito de avaliação integrada para as disciplinas de **Estrutura de Dados** e **Linguagem de Programação II** da faculdade **FATEC Rio Claro**[cite: 4, 5]. 

[cite_start]O objetivo principal é simular o sistema de gerenciamento de vendas e estoque da cantina universitária gerida pela Atlética[cite: 7], aplicando conceitos avançados de programação orientada a objetos e estruturas de dados criadas do zero.

## 🎯 O Desafio Acadêmico (Regra de Ouro)

[cite_start]O grande diferencial e o maior nível de dificuldade deste projeto foi a **proibição estrita do uso de bibliotecas built-in para lidar com estruturas de dados (como listas, pilhas ou filas nativas do Python)**[cite: 27]. Para solucionar isso, o sistema baseia-se no gerenciamento direto de referências de memória.

Os desafios superados e implementados incluem:
1. **Construção de Nós (Nodes):** Criação manual de classes para encadear objetos na memória.
2. [cite_start]**Gerenciamento de Perecíveis (Fila/Queue):** Implementação de uma Fila rigorosa (FIFO) para garantir que a prioridade de venda seja sempre dos produtos mais velhos no estoque[cite: 9].
3. **Múltiplas Estruturas Simultâneas:** Integração de uma Fila (Estoque) com Listas Encadeadas (Pagamentos e Consumo) em um único fluxo de venda.

## 📌 Funcionalidades e Estruturas Implementadas

O sistema atende a todos os requisitos propostos:

* [cite_start]**📦 Controle de Estoque (`Fila`):** Armazena produtos contendo nome, preço de compra, preço da venda, data da compra, data de vencimento e quantidade em estoque[cite: 8]. [cite_start]Possui funcionalidade para baixar o estoque automaticamente nas vendas e permitir a edição manual de quantidades[cite: 10, 18].
* [cite_start]**💸 Controle de Pagamento (`Lista Encadeada Simples`):** Estrutura customizada para guardar o histórico de pagamentos via PIX[cite: 12]. [cite_start]Armazena o nome de quem pagou, categoria (aluno, servidor ou professor), curso (IA ou ESG), valor pago e a data/hora exata[cite: 14].
* [cite_start]**🍽️ Controle de Consumo (`Lista Encadeada Simples`):** Estrutura que cruza os dados, permitindo controlar quem consumiu o que, baseado no valor de compra e na baixa do estoque, calculando o lucro[cite: 18].
* [cite_start]**📊 Relatórios:** Geração automática de relatórios separados para vendas e consumo[cite: 24].

## 🛠️ Tecnologias e Bibliotecas

* **Python 3** (Linguagem base)
* **`datetime`**: Para registro automático da hora da venda e controle de validade.
* [cite_start]**`faker`**: Utilizada para implementar o mecanismo de geração de dados aleatórios a fim de popular o sistema para testes[cite: 21].
* [cite_start]**`pickle`**: Utilizada para armazenar os dados de maneira não volátil, possibilitando seu carregamento posterior e salvando o estado da memória no disco[cite: 22].

## 🚀 Como executar o projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca `faker` rodando o comando no terminal:
   ```bash
   python -m pip install faker