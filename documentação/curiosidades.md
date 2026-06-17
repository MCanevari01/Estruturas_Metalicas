# 📚 Anotações de Estudo

Neste documento registro conceitos, curiosidades e aprendizados obtidos durante o desenvolvimento do projeto ERP Estruturas Metálicas.

---

## 🔄 Uso do `yield` em `get_session()`

```python
def get_session():
    with Session(engine) as session:
        yield session
```

### O que é?

Normalmente utilizamos `return` para devolver um valor ao final de uma função. Entretanto, no FastAPI, é comum utilizar `yield` para gerenciar recursos que precisam ser abertos e fechados automaticamente, como conexões com banco de dados.

### Como funciona?

1. A sessão é criada através de:

```python
with Session(engine) as session:
```

2. O `yield` disponibiliza a sessão para a rota que a solicitou.

3. Quando a execução da rota termina, o FastAPI retorna para a função.

4. O bloco `with` é encerrado e a sessão é fechada automaticamente.

### Vantagens

* Evita conexões abertas desnecessariamente.
* Garante o fechamento correto da sessão.
* Reduz risco de vazamento de recursos.
* É o padrão recomendado pelo FastAPI para gerenciamento de sessões.

---

## 🌐 Endpoints e CRUD

### O que é CRUD?

CRUD representa as quatro operações básicas realizadas em um banco de dados:

| Operação | Significado   |
| -------- | ------------- |
| Create   | Criar         |
| Read     | Ler/Consultar |
| Update   | Atualizar     |
| Delete   | Excluir       |

---

### Relação entre CRUD e Endpoints HTTP

Em APIs REST, cada operação do CRUD normalmente é representada por um método HTTP:

| CRUD   | Método HTTP  |
| ------ | ------------ |
| Create | POST         |
| Read   | GET          |
| Update | PUT ou PATCH |
| Delete | DELETE       |

---

### Por que geralmente existem 5 endpoints?

Embora o CRUD possua apenas 4 operações, é comum uma entidade possuir 5 endpoints principais:

```http
POST   /categorias
GET    /categorias
GET    /categorias/{id}
PUT    /categorias/{id}
DELETE /categorias/{id}
```

Isso ocorre porque a operação **Read** normalmente é dividida em duas consultas:

* Listar todos os registros (`GET /categorias`)
* Buscar um registro específico (`GET /categorias/{id}`)

Assim, uma entidade costuma possuir 5 endpoints, apesar de continuar representando as 4 operações do CRUD.
