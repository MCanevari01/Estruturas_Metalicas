# ERP Estruturas Metálicas

Projeto de estudo em desenvolvimento para aprendizado de desenvolvimento backend utilizando FastAPI.
A proposta é construir um mini ERP voltado para o setor de estruturas metálicas, aplicando conceitos de modelagem de dados, regras de negócio, APIs REST, autenticação e controle de acesso.

## Tecnologias Utilizadas

- Python
- FastAPI
- SQLModel
- SQLite
- Uvicorn
- Git
- GitHub

## Funcionalidades

### Categorias
- Cadastro
- Listagem
- Consulta por ID
- Atualização
- Exclusão

### Materiais
- Cadastro
- Listagem
- Consulta por ID
- Atualização
- Exclusão
- Validação de nomes duplicados por categoria


## Executando o projeto

Criar ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

# 7. Próximos Passos

## Roadmap

- [x] CRUD de Categorias
- [x] CRUD de Materiais
- [ ] Controle de estoque
- [ ] Autenticação JWT
- [ ] Controle de permissões
- [ ] PostgreSQL
- [ ] Frontend

## Documentação

Consulte:
- 📓 [Diário de Bordo](docs/diario_de_bordo.md)
- 📐 [Modelo Entidade Relacionamento](docs/modelagem/mer.md)

## 🚧 Em desenvolvimento

Funcionalidades concluídas:
- CRUD de Categorias
- CRUD de Materiais

Próxima etapa:
- Controle de Estoque