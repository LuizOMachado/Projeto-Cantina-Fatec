# 🍔 Sistema de Gerenciamento - Cantina Fatec

> **Avaliação Integrada:** Estrutura de Dados & Linguagem de Programação II
> **Instituição:** FATEC Rio Claro
> **Desenvolvedor:** Luiz Machado

---

## 🎯 O Desafio Acadêmico (Regra de Ouro)

O grande diferencial e o maior nível de dificuldade deste projeto foi a **proibição estrita do uso de bibliotecas built-in para lidar com estruturas de dados** (como listas `[]`, pilhas ou filas nativas do Python). 

Para solucionar isso, o sistema baseia-se no gerenciamento direto de referências de memória. Os desafios superados e implementados incluem:

1. **Construção de Nós (Nodes):** Criação manual de classes para encadear objetos na memória.
2. **Gerenciamento de Perecíveis (Fila/Queue):** Implementação de uma Fila rigorosa (FIFO) para garantir que a prioridade de venda seja sempre dos produtos mais velhos no estoque.
3. **Múltiplas Estruturas Simultâneas:** Integração de uma Fila (Estoque) com Listas Encadeadas (Pagamentos e Consumo) em um único fluxo de venda.

---

## 📌 Funcionalidades e Estruturas Implementadas

O sistema atende a todos os requisitos propostos no documento oficial:

* 📦 **Controle de Estoque (`Fila`):** Armazena produtos contendo nome, preço de compra, preço da venda, data da compra, data de vencimento e quantidade em estoque. Possui funcionalidade para baixar o estoque automaticamente nas vendas e permitir a edição manual de quantidades.
* 💸 **Controle de Pagamento (`Lista Encadeada Simples`):** Estrutura customizada para guardar o histórico de pagamentos via PIX. Armazena o nome de quem pagou, categoria (aluno, servidor ou professor), curso (IA ou ESG), valor pago e a data/hora exata.
* 🍽️ **Controle de Consumo (`Lista Encadeada Simples`):** Estrutura que cruza os dados, permitindo controlar quem consumiu o que, baseado no valor de compra e na baixa do estoque, calculando o lucro final da Atlética.
* 📊 **Relatórios:** Geração automática de relatórios separados para **Vendas** e **Consumo**.

---

## 🛠️ Tecnologias e Bibliotecas

* **Python 3** (Linguagem base)
* **`datetime`:** Para registro automático da hora da venda e controle de validade.
* **`faker`:** Utilizada para implementar o mecanismo de geração de dados aleatórios a fim de popular o sistema para testes estruturais.
* **`pickle`:** Utilizada para armazenar os dados de maneira não volátil, possibilitando seu carregamento posterior e salvando o estado da memória no disco.

---

## 🚀 Como executar o projeto

**1. Clone este repositório:**
```bash
git clone [https://github.com/LuizOMachado/Projeto-Cantina-Fatec.git](https://github.com/LuizOMachado/Projeto-Cantina-Fatec.git)