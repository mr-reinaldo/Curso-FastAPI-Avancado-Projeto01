# Curso: FastAPI Avançado 2023 | 2 Projetos | TDD | PostgreSQL

## Projeto [1]

O projeto consiste em uma API para conversão de moedas em tempo real. No curso, o professor utilizou a API da [Alphavantage](https://www.alphavantage.co/documentation/), porém, a API tinha um limite de requisições diárias. Por isso, decidi utilizar a API de cotações da [AwesomeAPI](https://docs.awesomeapi.com.br/), que é gratuita e não possui limite de requisições.

## Exemplo de requisições e respostas da API

A seguir, é fornecido um exemplo de como fazer uma requisição para a API. A requisição é um comando GET para o endpoint `/converter/BRL/sync` ou `/converter/BRL/async` na máquina local na porta 3000. O corpo da requisição contém um objeto JSON que especifica um preço em BRL e uma lista de códigos de moedas para as quais esse preço deve ser convertido.

### Conversão de moedas (sincrona)

```http
GET /converter/BRL/sync HTTP/1.1
Host: localhost:3000
Content-Type: application/json
User-Agent: insomnia/9.0.0
Accept: */*
Content-Length: 74

{
  "price": 100,
  "to_currencies": [
    "USD","CAD", "AED", "BOB"
  ]
}
```

### Resposta (sincrona)

```json
[
  {
    "from_currency": "BRL",
    "to_currency": "USD",
    "price": 100.0,
    "converted_price": 19.24
  },
  {
    "from_currency": "BRL",
    "to_currency": "CAD",
    "price": 100.0,
    "converted_price": 26.619999999999997
  },
  {
    "from_currency": "BRL",
    "to_currency": "AED",
    "price": 100.0,
    "converted_price": 70.7
  },
  {
    "from_currency": "BRL",
    "to_currency": "BOB",
    "price": 100.0,
    "converted_price": 130.31
  }
]
```

Fazendo uma requisição sincrona para a API, o tempo de resposta foi de 1.9 segundos.
![alt text](.printscreen/sync.png)

### Conversão de moedas (assincrona)

```http
GET /converter/BRL/async HTTP/1.1
Host: localhost:3000
Content-Type: application/json
User-Agent: insomnia/9.0.0
Accept: */*
Content-Length: 74

{
  "price": 200,
  "to_currencies": [
    "USD","CAD", "AED", "BOB"
  ]
}
```

### Resposta (assincrona)

```json
[
  {
    "from_currency": "BRL",
    "to_currency": "USD",
    "price": 200.0,
    "converted_price": 38.48
  },
  {
    "from_currency": "BRL",
    "to_currency": "CAD",
    "price": 200.0,
    "converted_price": 53.239999999999995
  },
  {
    "from_currency": "BRL",
    "to_currency": "AED",
    "price": 200.0,
    "converted_price": 141.42
  },
  {
    "from_currency": "BRL",
    "to_currency": "BOB",
    "price": 200.0,
    "converted_price": 260.62
  }
]
```

Fazendo uma requisição assincrona para a API, o tempo de resposta foi de 502 milissegundos bem mais rápido que a requisição sincrona.

![alt text](.printscreen/async.png)

## Tecnologias utilizadas

Foram utilizadas as seguintes tecnologias:

- FastAPI (Para criação da API)
- Pydantic (Para validação de dados)
- Requests (Para fazer requisições HTTP para a API de cotações da [AwesomeAPI](https://docs.awesomeapi.com.br/))
- Uvicorn (Para rodar o servidor)
- AIOHTTP (Para fazer requisições assincronas)

## Como rodar o projeto na sua máquina

Para rodar o projeto na sua máquina, siga os seguintes passos:

- Clone o repositório

```bash
git clone https://github.com/mr-reinaldo/Curso-FastAPI-Avancado-Projeto01.git
```

- Instale as dependências

```bash
pip install -r requirements.txt
```

- Rode o servidor

```bash
python main.py
```

- Faça uma requisição para a API

```bash
curl -X 'GET' \
  'http://localhost:3000/converter/BRL/sync' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "price": 100,
  "to_currencies": [
    "USD","CAD", "AED", "BOB"
  ]
}'
```
