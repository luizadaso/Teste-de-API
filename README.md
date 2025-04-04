# Busca de Operadoras de Saúde – ANS

Este projeto é uma aplicação web simples que permite buscar operadoras de planos de saúde ativas registradas na **Agência Nacional de Saúde Suplementar (ANS)**. Os dados são obtidos automaticamente do portal de dados abertos da ANS e disponibilizados por meio de uma API Flask, com uma interface web construída em Vue.js.

---

## Tecnologias Utilizadas

### Backend:
- [Python 3.13](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://docs.python-requests.org/)

### Frontend:
- [Vue.js 2](https://v2.vuejs.org/)
- [Axios](https://axios-http.com/)

---

## Estrutura do Projeto

```
Teste-de-API/
├── README.md
├── server.py
├── index.html
│
├── venv/
│   └── ... (ambiente virtual Python)
│
└── downloads/
    └── operadoras.csv
```

---

## Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install flask pandas requests
```

### 4. Inicie o servidor Flask

```bash
python server.py
```

O servidor estará disponível em `http://localhost:5000`.

### 5. Abra a interface web

Abra o arquivo `index.html` no navegador (basta dar um duplo clique ou arrastar para o navegador).

---

## Como Funciona

- O `server.py` faz o download do CSV de operadoras ativas da ANS caso o arquivo ainda não exista.
- Ele carrega os dados usando `pandas` e expõe um endpoint `/search` para realizar buscas em todos os campos do CSV.
- O frontend em Vue.js consome esse endpoint, enviando uma busca com o termo digitado pelo usuário e listando os resultados na tela.

---

## Exemplo de Busca

1. Digite no campo, por exemplo: `unimed`
2. Clique em **Buscar**
3. O sistema retorna todas as operadoras cujo nome ou qualquer outro campo contenha o termo `unimed`.

---

## Observações

- O campo exibido no frontend (`operadora.nome`) deve ser ajustado conforme o nome real da coluna no CSV. Ex: `RAZAO_SOCIAL`.
- A busca é feita em todos os campos e é **case-insensitive**.
- O CSV original é obtido da [ANS - Dados Abertos](https://dadosabertos.ans.gov.br/)

---

## Autora

Para mais informações, sinta-se à vontade para entrar em contato:

<div align="left">
  <img src="https://github.com/user-attachments/assets/57cac2a3-49b1-4a0a-aef3-e968523971eb" width="15%" alt="autora" />
</div>

- [Github](https://github.com/luizadaso)
- [Linkedin](https://www.linkedin.com/in/luizadaso)
