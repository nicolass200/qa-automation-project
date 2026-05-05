# QA Automation Project

Projeto de automação de testes para API e Web com integração contínua (CI/CD).
Estou com limitação técnica no ambiente agora para gerar o arquivo. Mas o conteúdo completo está aqui — copia e cria o `README.md` na raiz do projeto:

```markdown
# qa-automation-project

Projeto de automação de testes cobrindo API REST e fluxo Web E2E, com execução automática via GitHub Actions.

![CI](https://github.com/nicolass200/qa-automation-project/actions/workflows/ci.yml/badge.svg)

---

## Tecnologias

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.10 |
| Testes | pytest |
| Automação Web | Selenium 4 |
| Gerenciamento de driver | webdriver-manager |
| Testes de API | requests |
| CI/CD | GitHub Actions |

---

## Estrutura do Projeto

```
qa-automation-project/
│
├── api_tests/
│   ├── services/
│   │   ├── base_service.py
│   │   ├── user_service.py
│   │   ├── pet_service.py
│   │   └── store_service.py
│   └── tests/
│       ├── test_user.py
│       ├── test_pet.py
│       └── test_store.py
│
├── web_tests/
│   ├── base/
│   │   ├── base_page.py
│   │   └── base_test.py
│   ├── pages/
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   └── tests/
│       └── test_e2e.py
│
├── config.py
├── requirements.txt
└── .github/workflows/ci.yml
```

---

## Instalação

**Pré-requisitos:** Python 3.10+ e Google Chrome instalados.

```bash
git clone https://github.com/nicolass200/qa-automation-project.git
cd qa-automation-project

python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

---

## Execução

```bash
# Todos os testes
PYTHONPATH=. pytest

# Apenas API
PYTHONPATH=. pytest api_tests -v

# Apenas Web
PYTHONPATH=. pytest web_tests -v
```

---

## Cobertura de Testes

### API — Swagger Petstore

Base URL: `https://petstore.swagger.io/v2`

| Módulo | Cenário | Tipo |
|---|---|---|
| User | Criar, buscar e deletar usuário | Positivo |
| User | Buscar usuário inexistente | Negativo |
| Pet | Criar, atualizar e buscar pet | Positivo |
| Pet | Buscar pet inexistente | Negativo |
| Store | Criar, buscar e deletar pedido | Positivo |
| Store | Buscar pedido inexistente | Negativo |

### Web — SauceDemo

URL: `https://www.saucedemo.com/`

```
Login → Adicionar produto → Carrinho → Checkout → Confirmação
```

---

## Arquitetura Web

Padrão **Page Object Model (POM)** — cada página encapsula seus elementos e ações.

```
BasePage          → lógica de espera e interação reutilizável
├── LoginPage     → autenticação
├── InventoryPage → seleção de produtos
├── CartPage      → revisão do carrinho
└── CheckoutPage  → preenchimento de dados e finalização
```

---

## CI/CD

Pipeline executa automaticamente a cada `push` ou `pull request`:

1. Setup do Python 3.10
2. Instalação das dependências
3. Execução dos testes de API
4. Execução dos testes Web (Chrome headless)
5. Upload do screenshot em caso de falha

## Prints
### Prints das telas
### Tela de login
![Login](docs/login.png)

### Tela de produtos após login
![Produtos](docs/produtos.png)

### Carrinho com produto adicionado
![Carrinho](docs/carrinho.png)
### Tela de checkout com preenchimento dos dados
![Checkout](docs/checkout.png)

### checkout da compra
![Checkout](docs/checkout.png)

### Confirmação de compra
![Confirmação](docs/confirmacao.png)