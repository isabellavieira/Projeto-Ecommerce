# Projeto-Ecommerce

Fabiano Amorim, Isabella Vieira e Beatriz Vieira

---

## Objetivo do Projeto

O sistema tem como objetivo criar uma plataforma de vendas online que:
- Permite o cadastro de usuários com informações de cartão de crédito;
- Possibilita a adição de produtos ao carrinho e a realização de pedidos;
- Verifica, antes da finalização, se o saldo disponível no cartão de crédito é suficiente para a compra;
- Armazena os dados dos produtos, pedidos e usuários utilizando bancos de dados NoSQL e relacionais;
- Implementa um deploy automatizado via GitHub Actions e conta com testes de unidade para o backend.

---

## Arquitetura do Sistema

### 2.1 API Gateway
- **Endpoints principais:**
  - `POST /pedido` → Cria um pedido.
  - `GET /produtos` → Lista os produtos disponíveis.
  - `POST /produto` → Adiciona um novo produto.
  - `PUT /produto/{id}` → Atualiza as informações de um produto.
  - `DELETE /produto/{id}` → Remove um produto.
  - `POST /usuario` → Cadastra um usuário com cartão de crédito.
  - `PUT /usuario/{id}` → Atualiza os dados do usuário.
  - `GET /relatorio-vendas` → Gera o relatório de vendas.

### 2.2 Backend (Azure App Service)
  - Criar e armazenar pedidos no banco de dados.
  - Listar, criar, atualizar e remover produtos.
  - Criar e atualizar usuários (incluindo informações de cartão de crédito).
  - Verificar se o saldo no cartão de crédito é suficiente antes de confirmar o pedido.
  - Executar testes de unidade para validar as funcionalidades do sistema.

### 2.3 Banco de Dados
- **Banco NoSQL (Azure Cosmos DB):**
  - Armazena os produtos e os pedidos.
- **Banco Relacional (Azure SQL Database):**
  - Gerencia as informações dos usuários e seus dados de cartão de crédito.
 
### 2.4 Outras Tecnologias e Práticas
- **Deploy Automatizado:** Utilização de GitHub Actions para a automação do processo de implantação.
- **Testes de Unidade:** Implementação de testes automatizados no backend para garantir a qualidade do código.

---

## Funcionalidades e Status de Implementação

### Funcionalidades Implementadas
- **API Gateway:**
  - Roteamento de requisições para criação, listagem, atualização e remoção de produtos.
  - Cadastro e atualização de usuários com informações de cartão de crédito.
  - Endpoint para criação de pedidos.
  
- **Backend (Azure App Service):**
  - Lógica para criação, armazenamento e gerenciamento de pedidos.
  - Gerenciamento do catálogo de produtos.
  - Verificação do saldo do cartão de crédito antes da confirmação do pedido.
  - Realização de testes de unidade para as principais funcionalidades.

- **Bancos de Dados:**
  - Configuração do Banco NoSQL para o armazenamento de produtos e pedidos.
  - Configuração do Banco Relacional para a gestão dos dados dos usuários.

- **Deploy Automatizado:**
  - Configuração usando GitHub Actions para automatizar a implantação do sistema.

---

## Fluxo de Trabalho do Sistema

1. **Cadastro do Usuário:**
   - O usuário se cadastra no e-commerce, informando os dados pessoais e os detalhes do cartão de crédito, incluindo um saldo inicial.
   
2. **Realização do Pedido:**
   - O usuário adiciona produtos ao carrinho e finaliza a compra.
   - Antes de confirmar o pedido, o sistema verifica se o saldo do cartão é suficiente.
   
3. **Processamento do Pedido:**
   - Se o saldo for adequado, o pedido é confirmado, o valor é debitado e as informações são enviadas ao backend via API Gateway.
   - O backend armazena o pedido no Banco NoSQL e atualiza os dados do usuário no Banco Relacional.

4. **Relatórios de Vendas:**
   - Os administradores podem acessar o endpoint de relatório (`GET /relatorio-vendas`) para visualizar análises e relatórios gerados a partir dos dados processados.

---

## Tecnologias Utilizadas

- **API Gateway:** Azure API Management.
- **Backend:** Desenvolvido e hospedado no Azure App Service.
- **Bancos de Dados:**
  - **NoSQL:** Azure Cosmos DB para produtos e pedidos.
  - **Relacional:** Azure SQL Database para gestão dos usuários.
- **Deploy Automatizado:** GitHub Actions.
- **Testes Automatizados:** Testes de unidade implementados no backend.
