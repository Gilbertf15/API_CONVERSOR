# ⚡ API Conversor de unidades - FastAPI

> API criada em FastApi para a conversão de algumas unidades de temperatura, peso e distância, com métodos GET para acessar os valores convertidos de 0 a 100, e métodos POST para converter um valor específico.

![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Licença](https://img.shields.io/badge/licença-MIT-blue)

---

## 📑 Sumário

- [📘 Sobre o Projeto](#-sobre-o-projeto)
- [🚀 Tecnologias Utilizadas (Padrão)](#-tecnologias-utilizadas-padrão)
- [📁 Estrutura de Pastas (Modelo Base)](#-estrutura-de-pastas-modelo-base)
- [⚙ Instalação](#-instalação)
- [▶ Como Usar](#-como-usar)
- [🧪 Testes](#-testes)
- [🛠 Contribuindo](#-contribuindo)
- [📄 Licença](#-licença)
- [📫 Contato](#-contato)

---

## 📘 Sobre o Projeto

Projeto desenvolvido com FastAPI, api para conversão de unidades( temperatura, peso, distãncia)

Funcionalidades principais:

- 🚀 Conversão de fahrenheit para celsius (GET, POST)
- 🚀 Conversão de celsius para kelvin (GET, POST)
- 🚀 Conversão de quilogramas para libras (GET, POST)
- 🚀 Conversão quilometros para milhas
- 🛢 Integração com banco de dados relacional (SQLite)

---

## 🚀 Tecnologias Utilizadas (Padrão)

Este projeto usa a seguinte stack padrão:

- _Python 3.11+_

- _FastAPI 0.110+_

- _SQLite_

- _pytest_ ou _unittest_

---

## 📁 Estrutura de Pastas (Modelo Base)

```bash
📦 nome-do-projeto
├── 📁 app/                    # Código principal
│   ├── 📁main/               #  contém a classe de criação do objeto FastApi
│       ├── __init__.py
│   ├── 📁 controller/ # pasta de controllers de aplicação
│        ├── __init__.py
│   ├── 📁 interface/ # contém a classe abstrata que é inplementada nos controllers
│        ├── __init__.py
│   ├── 📁 models/ # criação das tabelas e da classe de conexão do banco
│        ├── __init__.py
│   ├── 📁 rotas/ # rotas da aplicação
│        ├── __init__.py
│
│   📁 img_readme/ # imagens da documentação
│
├── 📁 tests/                 # Testes automatizados
├── .env                     # Variáveis de ambiente
├── .gitignore
├── LICENSE                   # Licensa da aplicação
├── requirements.txt
├── .readem_doc.dm             # documentação
├── README.md
└── main.py                   # Script para rodar a aplicação
```

## ⚙️ Instalação

# 1. Clone o repositório

git clone https://github.com/Gilbertf15/API_CONVERSOR.git

# 2. Crie e ative o ambiente virtual

python -m venv venv

source venv/bin/activate # Linux/macOS

venv\Scripts\activate # Windows

# 3. Instale as dependências

pip install -r requirements.txt

## ▶️ Como usar

## Execute o seguinte comando:

uvicorn main:app -reload

## 📫 Contato

    Gmail: gilbertcorreia18@gmail.com

## 🧪 Testes

│ Esse projeto conta com alguns testes unitarios, testando os métodos das classes individualmente.

### execute o seguinte comando:

#### no windows: python test/teste_main.py
