[![wakatime](https://wakatime.com/badge/user/3bd24664-869f-460a-94e1-b98da8136504/project/018e8d4e-1d1d-4ab6-b83a-d34dc918f6f1.svg)](https://wakatime.com/badge/user/3bd24664-869f-460a-94e1-b98da8136504/project/018e8d4e-1d1d-4ab6-b83a-d34dc918f6f1)

<h2 align="center">API de Produtos</h2>

## Índice

- [Sobre](#-sobre)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Endpoints](#-endpoints)
- [Como usar o projeto](#-como-usar-o-projeto)
- [Documentação](#-documentação)
- [Autor](#️-autor)

## 📖 Sobre

Está API foi desenvolvida para o desafio técnico da empresa [Shoppub](https://shoppub.com.br/). O desafio consiste em
desenvolver uma API RESTful para gerenciar produtos. A API deve permitir a criação, listagem, atualização e remoção
lógica de produtos.

## 🚀 Tecnologias Utilizadas

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [PostgreSQL](https://www.postgresql.org/)

## 🎯 Endpoints

Consumir a API é muito simples, pode ser consumida através do Postman ou hospedada no Render, através do link:

[![Deployed on Render](https://img.shields.io/badge/Deployed%20on-Render-blue?style=for-the-badge&logo=render)](https://api-shoppub-drf.onrender.com/)

[![Run in Postman](https://run.pstmn.io/button.svg)](https://galactic-space-475622.postman.co/collection/26400668-cd2e8982-2591-4cc8-bef4-53419483bb3e?source=rip_markdown)

### Autenticação

Para consumir a API, necessário seguir o fluxo de autenticação. Sendo preciso criar um usuário no django admin com o
comando `python manage.py createsuperuser`, e acessar o endpoint do token `api-token-auth/`.

![image](https://imgur.com/0Jts69E.png)

```json
{
  "username": "admin",
  "password": "123456"
}
```

O token gerado deve ser passado no header `Authorization` para acessar os demais endpoints.

```json
{
  "Authorization": "Token <token>"
}
```

## Django Admin

Acessar o Django Admin através do link:

[![Django Admin](https://img.shields.io/badge/Django%20Admin-blue?style=for-the-badge&logo=django)](https://api-shoppub-drf.onrender.com/admin/login/?next=/admin/)

O Django Admin é uma ferramenta poderosa para gerenciar os dados do projeto. Para acessar o admin, é necessário criar um
super usuário com o comando:

```bash
$ python manage.py createsuperuser
```

### Produtos

- `GET /products/`: Lista todos os produtos ativos.
- `POST /products/create/`: Cria um novo produto.
- `GET /products_detail/<int:pk>/`: Retorna os detalhes de um produto específico.
- `PUT /products/update/<int:pk>/`: Atualiza um produto existente.
- `DELETE /products/delete/<int:pk>/`: Remove logicamente um produto existente.
- `GET /products/reactivate/<int:pk>/`: Reativa um produto inativo.

### Exemplos de uso

#### Criar um novo produto

- `POST /products/create/`

```json
{
  "name": "Produto 1",
  "description": "Descrição do produto 1",
  "price": 10.00,
  "quantity": 10,
  "is_active": true
}
```

## 📦 Como usar o projeto

```bash
    # Clonar o repositório
    $ git clone https://github.com/matheus-feu/api_shoppub_drf.git
```

```bash
    # Instalar as dependências
    $ pip install -r requirements.txt

    # Rodar as migrações
    $ python manage.py migrate

    # Rodar o projeto
    $ python manage.py runserver
```

## 📝 Documentação

Através do link abaixo, é possível acessar a documentação da API:

[![Postman](https://img.shields.io/badge/Postman-blue?style=for-the-badge&logo=postman)](https://documenter.getpostman.com/view/26400668/2sA35HVzdf)

## ♾️ Fontes

Links úteis para o desenvolvimento do projeto:

- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django](https://www.djangoproject.com/)
- [Authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- [Generic Views](https://www.django-rest-framework.org/api-guide/generic-views/)
- [Django Admin](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/)

## 🧙‍♂️️ Autor

[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/matheus-feu)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&labelColor=blue)](https://www.linkedin.com/in/matheus-feu-558558186/)
[![Gmail](https://img.shields.io/badge/Email-red?style=flat&logo=gmail&labelColor=red)](mailto:matheusfeu@gmail.com)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=flat&logo=Instagram&logoColor=white)](https://www.instagram.com/math_feu/)


