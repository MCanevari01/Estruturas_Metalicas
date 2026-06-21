# 📓 Diário de Bordo: Aprendizado e Evolução

Resolvi criar esta documentação para avaliar e anotar pequenos insights e ideias que tive ao criar este modelo de ERP. Minha ideia é aprender na prática sobre desenvolvimento de software com básico em cibersegurança, com o objetivo de transição de carreira, além de documentar pequenas utilidades que uso constantemente, como comandos Git.

---

## 🚀 Minha Jornada e Contexto
* **Objetivo:** Transição de carreira para a área de Tecnologia.
* **Idade:** 27 anos.
* **Desafio:** Conciliar trabalho no setor de estruturas metálicas com o pouco tempo disponível para o desenvolvimento e aprendizagem de conceitos relativamente novos para mim.
* **Estratégia do Projeto:** Construir um **miniERP** voltado para a área de engenharia/estruturas metálicas, aplicando conceitos de validação rígida de dados e proteção de rotas.

---

## 💡 Insights e Ideias

- **Ideia - Inicial:** Minha ideia inicial era criar um ERP para a empresa onde trabalho, porém, ao observar, percebi que eles não tinham interesse no projeto, por esse motivo, decidi desenvolve-lo como um projeto pessoal para a transição de carreira e ingressar na área de Tecnologia, colocando em prática o que tenho aprendido no curso de graduação.
- **Insight - GitHub:** Pensei sobre como equipes trabalham, como fazem uso da main e das branches, por esse motivo, mesmo trabalhando sozinho no projeto, planejo adotar o sistema de criar branches e pull requests.
- **Ideia da Documentação:** Como ainda não tinha o hábito de programar constantemente e utilizar do GitHub, muitas vezes me perdia nos comandos e ficava tendo que pesquisa-los, por esse motivo, surgiu a ideia desta documentação, onde, inicialmente era apenas para esse propósito, e seria feito em arquivos de texto, mas ao pesquisar sobre, vi que é comum esse tipo de documentação e adotei a ideia de desenvolver e fazer algumas anotações.

### 💭 Hipótese
- **Evitar arquivos temporários:** Não sei se é o correto, porém tive pensamento de evitar arquivos temporários, por exemplo evitar criar um script em python para injetar dados no banco, ao invés disso, criar um modelo onde eu adicionaria diretamente pela API Web.

- **Construir um FrontEnd:** Embora não seja muito meu foco e meu ponto forte, desejo construir algo visual... Odiei a interface do Swagger


---

## 💭 Problemas, Reflexões e Aprendizados

### 📆 15/06/2026
* Ao dar prosseguimento no projeto, lembrei de algo que havia escutado na faculdade e em palestras sobre os desenvolvedores e projetos, onde não era correto ou pouco indicado que alguem da equipe fizesse commits direto no arquivo principal. Tinha apenas escutado comentários, e nunca havia trabalhado com o mesmo, porém queria levar em conta esse fato e começar a trabalhar sobre o mesmo. Com isso a solução que encontrei ao pesquisar foi sobre as branches e pull request, onde decidi adotar o mesmo. Porém, com isso também apareceu outros pequenos problemas, como a utilização de mais códigos git, o que não estou familiarizado. Para o mesmo, decidi criar um arquivo que conteria esses códigos, mas tomou uma outra proporção, onde crio esse diário de bordo como solução

* Ao começar desenvolver meu primeiro CRUD (cadastro de categorias), percebi que estava colocando muitos dados e códigos em um único arquivo (main.py), e também ja havia escutado que isso não era uma prática muito boa, devido a poluição do código. Para isso, pesquisei sobre e descobri uma forma mais "limpa" de organizar o código, atrvés de rotas (routers), que seriam responsáveis pela ligação entre os modelos (models), banco de dados e a aplicação, sem estar tudo concentrado em um único lugar.

### 📆 16/06/2026 
* Não é bem um problema, mas algo que me atrapalhou um pouco no dia. Ao chegar em casa do trabalho, devido ao cansaço percebi que seria mais complicado a constância no projeto, e devido ao horário também me desanimou bastante. Mas em mais de uma ocasião eu já havia visto que é melhor manter uma pequena constância do que dedicar muito tempo em um único dia, por esse motivo, mesmo que sejam pequenas modificações ou pequenos desenvolvimentos, vou tentar manter uma constância diária.

### 📆 17 à 20/06/2026
* Por se tratar de um primeiro projeto e de uma primeria experiência, não sei o que devo relatar que seria de proveito para mim ou alguem que ler, mas com o passar dos dias, devido a uma sobrecarga de trabalho, não consegui manter o desenvolvimento como queria e acabei ficando os últimos 3 dias sem fazer nenhuma alteração, algo que eu gostaria que não viesse a acontecer nem a se repetir, mas isso se deve a uma sobrecarga de trabalho. Por medida de metas próprias, desejo tentar finalizar e trabalhar com metas semanais, por exemplo, algo que não havia pensado antes porém tive a idéia, na semana desenvolver X passos do meu projeto, como essa semana agora, desenvolver todo o CRUD de categoria, e trabalhar com esse tipo e parâmetros e tentando sempre bater essas pequenas metas


---

## 🛠️ Ferramentas Utilizadas

### Backend

#### FastAPI
- Função: Construção da API do sistema.
- Motivo da escolha: Framework moderno, simples para iniciantes e breve conhecimento anterior em Python.

#### Uvicorn
- Função: Servidor ASGI para executar a aplicação.
- Motivo da escolha: Leve e recomendado pela documentação do FastAPI.

---

### Banco de Dados

#### SQLite
- Função: Armazenamento dos dados do sistema.
- Motivo da escolha: Escolha inicial para desenvolvimento pela facilidade.

---

### Controle de Versão

#### Git
- Função: Controle de versões do código.
- Motivo da escolha: Padrão da indústria para gerenciamento de código-fonte.

#### GitHub
- Função: Hospedagem do repositório e colaboração.
- Motivo da escolha: Plataforma amplamente utilizada e integrada ao Git.

---

### Desenvolvimento

#### Visual Studio Code
- Função: Editor de código principal.
- Motivo da escolha: Leve, gratuito e com grande quantidade de extensões.

---

## 📈 Evolução do Projeto

### Versão 0.1 (📆14 jun. 2026)
- Estrutura inicial do Projeto
- Instalação de extensões
- Configuração do GitHub

### Versão 0.2.1 (📆15 jun. 2026)
- Criação do diário de bordo
- Criação do primeiro Cadastro de Categorias e tratamento básico de nomes duplicados
- Realização de primeiro teste via swagger.

### Versão 0.2.2 (📆16 jun. 2026)
- Criação da Listagem geral de Categorias (GET)
- Realização do teste 

### Versão 0.2.3 (📆21 jun. 2026)
- Criação da Listagem de Categorias por ID (GET)
- Realização dos Testes no Swagger.
- commit da alteração

### Versão 0.2.4 (📆21 jun. 2026)
- Criação da Atualização de Categorias (PUT)
- Realização dos Testes no Swagger.
- commit da alteração
---

## 🎯 Próximos Passos
### Curto Prazo
- Criar primeiros endpoints CRUD.
*  Referente a categorias
*  [x] CREATE (15/06/2026)
*  [x] GET (16/06/2026)
*  [x] GET por ID (21/06/2026)
*  [x] UPDATE (21/06/2026)
*  [ ] DELETE

### Médio/Longo Prazo
- Implementar autenticação JWT.
- Controle de permissões.
- Migração para PostgreSQL.
- Construir FrontEnd

---

### 🌿 Git & GitHub

* **Configuração Inicial**
  ```bash 
  git init
  git branch -M main
  git remote add origin https://github.com/MCanevari01/Estruturas_Metalicas.git
  git push -u origin main

🔀 Fluxo de Trabalho Diário (Branches e Commits)

* **Salvar alterações localmente:**
  ```bash
  git add .
  git commit -m "tipo: descrição clara do que foi feito"
  git push 
  
* **Verificações:**
  ```bash
  git status
  git branch (confirma a branch atual)

* **Checando atualizações na main:**
  ```bash
  git checkout main (Muda para a branch main.)
  git pull origin main (Atualiza a branch main local com as alterações do repositório remoto.)

* **Iniciar uma tarefa isolada (Feature Branch):**
  ```bash
  git checkout -b feature/nome-da-tarefa (O comando -b diz ao Git para "criar" a branch, e o checkout te joga para dentro dela de forma isolada) 
  
* **Inicialização do uvicorn**
  ```bash
  uvicorn main:app --reload
---

### ⚠️ Observações
  **Nomeclatura:**
  - feature -> muito utilizado para indicar uma nova funcionalidade
  - fix -> utilizado para correções
