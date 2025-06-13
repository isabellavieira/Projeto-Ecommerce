# E-commerce IsaFabBia

**Projeto desenvolvido por:** Fabiano Amorim, Isabella Vieira e Beatriz Vieira

## Descrição

Plataforma de e-commerce com chatbot inteligente e backend robusto. Permite consulta de produtos, realização de compras e gerenciamento de pedidos através de interface conversacional.

## Arquitetura

- **Chatbot (Python/Bot Framework)**: Interface conversacional
- **Backend (Java/Spring Boot)**: API REST para processamento
- **Bancos**: Azure Cosmos DB (produtos/pedidos) + Azure SQL Database (usuários)

## Funcionalidades

### Chatbot
- Consulta de produtos e pedidos
- Processo de compra guiado
- Validação de dados em tempo real

### Backend
- Processamento de compras
- Validação de saldo de cartão
- API REST completa

## Tecnologias

- **Frontend**: Python, Microsoft Bot Framework, Azure Cosmos DB SDK
- **Backend**: Java 17, Spring Boot, Spring Data JPA, Maven
- **Infraestrutura**: Azure App Service, Azure Cosmos DB, Azure SQL Database

## Instalação

### Backend
```bash
cd api
mvn clean install
mvn spring-boot:run
```

### Chatbot
```bash
cd bot
python -m venv venv
source venv/bin/activate  # Linux/Mac ou venv\Scripts\activate # Windows
pip install -r requirements.txt
python app.py
```

## Configuração

Configure as variáveis de ambiente:

```bash
# Backend
SPRING_DATASOURCE_URL=jdbc:mysql://your-database-url
AZURE_COSMOS_ENDPOINT=your-cosmos-endpoint
AZURE_COSMOS_KEY=your-cosmos-key

# Bot
MicrosoftAppId=your-bot-app-id
MicrosoftAppPassword=your-bot-password
```

## Endpoints Principais

- `POST /api/compras` - Realizar compra
- `GET /api/pedidos/{id}` - Consultar pedido
- `GET /api/produtos` - Listar produtos

## Como Usar

1. **Iniciar**: O bot apresenta opções (Consultar Pedidos/Produtos)
2. **Consultar**: Digite o nome do produto ou ID do pedido
3. **Comprar**: Digite "Comprar [produto]" e siga o fluxo guiado
4. **Dados**: Informe cartão, dados pessoais e endereço

## Testes

```bash
# Backend
cd api && mvn test

# Chatbot
# Use Bot Framework Emulator em http://localhost:3978/api/messages
```

## Estrutura

```
Projeto-Ecommerce/
├── api/                    # Backend Java/Spring Boot
│   ├── src/main/java/cloud/ecommerceisafabbia/
│   │   ├── controladores/  # Controllers REST
│   │   ├── objetosmodelo/  # Entidades
│   │   ├── service/        # Lógica de negócio
│   │   └── request/        # DTOs
│   └── pom.xml
├── bot/                    # Chatbot Python
│   ├── dialogs/           # Diálogos
│   ├── api/               # Cliente da API
│   ├── app.py             # Aplicação principal
│   └── config.py          # Configurações
└── README.md
```

## Deploy

Deploy automático via GitHub Actions no Azure App Service.
