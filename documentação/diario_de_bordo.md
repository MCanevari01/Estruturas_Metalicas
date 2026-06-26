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
- **Seguimento do MER:** Registrar o modelo que utilizei de base para dar início do projeto de deixá-lo documentado para servir de guia do caminho e próximos passos do Projeto. Ainda é um modelo-esboço que deve ser lapidado e aprimorado.

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

### 📆 23/06/2026
* Quando comecei a fazer faculdade, era em modelo presencial na FEMA(Fundação Educacional do Municipio de Assis), antes de mudar para EAD (Cruzeiro do SUl) , e hoje enquanto desenvolvia o projeto me lembrei de algo que meu professor, grande Almir Camolesi, puxou minha orelha por não ter utilizado na época e que acabei utilizando hoje 🙀​. Era sobre integridade dos dados, onde, ao desenvolver o modelo dos materiais eu acabei utilizando para vincular as categorias com os materiais, e sei que utilizarei muito durante o desenvolvimento.
* Outro ponto, é que eu não mencionei antes, mas antes mesmo de começar a desenvolver, eu trabalhei na elaboração de um Modelo Entidade Relacionamento (MER), que estou utilizando para seguir como um caminho guia de evolução do projeto. Procurarei uma forma de coloca-lo também aqui na documentação.
* Estou tendo bastante dificuldade também durante esse desenvolvimento com alguns detalhes que considero importante, por exemplo, por se tratar de um modelo que estou utilizando como base meu serviço, sou relativamente novo no trabalho e muita coisa ainda desconheço de lá, e isso tem me gerado algumas dúvidas, por exemplo, ao trabalhar com o models/material, duas áreas tive problema em escolher o tipo de dados. Um deles foi relativamente fácil, que era o valor_unitario, que escolhi utilizar decimal. Porem a quantidade em estoque, hávia várias opções, como int (que poderia ser o mais "recomendado"), o float, pois eu poderia separar materiais com valores flutuantes, por exemplo, materiais que seriam sepadados por pesos, e decimal, que foi o que acabei optando por utilizar. Com isso em mente, enquanto eu trabalhava e estudava sobre, embora de maneira superficial, surgiu também sobre cadastrar uma forma de unidade de medida, algo que não estava no meu planejamento primário mas acabei por incluir.
* Mais um ponto a ser observado, quando fazia testes na aplicação, percebi que ao deletar uma categoria o meu banco continuava progressivamente, por exemplo, tendo 3 categorias registradas (1,2,3), ao deletar a (1), o próximo cadastro seria no (4), e o espaço (1) ficaria um vazio. Preciso ver como preencher ou reorganizar o banco de dados.

### 📆 24/06/2026
* Durante o dia, eu pesquisei sobre o que eu pensava ser um erro na minha aplicação ou falta de tratar algum acontecimento. Enquanto via sobre, descobri ser o tratamento comum para bancos de dados Relacionais, e que isso é para evitar diversos poblemas, como um que me chamou a atenção, Integridade Relacional onde por exemplo, *você tem uma tabela Usuarios e uma tabela Pedidos. O usuário com ID 2 fez três pedidos. Se você deletar o usuário 2 e, por algum motivo, forçar o banco a reutilizar esse número para um novo usuário, os pedidos antigos agora pertencerão a uma pessoa completamente diferente! Reutilizar IDs destrói a confiabilidade do histórico do seu sistema.*
* Ao testar a aplicação na noite anterior, percebi que estava dando erro no POST de materiais, e devido ao cansaço optei por resolver no dia seguinte. Quando analisava, e pesquisava, observei que o erro estava em meu banco de dados, mais especificamente na tabela de materiais, pois quando eu iniciei o projeto eu utilizei nome_material e quando comecei realmente a trabalhar na classe material, eu adotei nome como atributo para aquela classe, e isso trouxe esse pequeno problema 😔​. Optei por deletar e iniciar novamente o banco (Caso tenha problemas novamente tentarei outros métodos para aprendizado, pois quando trabalhar com bancos que já possuirem dados salvos, essa não será uma opção. Ví que há formas, como o Alembic, Flyway, Liquibase, mas não quero abordar isso no momento. Quero finalizar o CRUD de materiais como prioridade agora) Salvo pelo gitHub que continha a informação de como cadastrei e pude comparar. Isso trouxe mais um ponto que é sempre bom ter tudo registrado ou até mesmo uma extensão para visualizar a forma como o banco esta cadastrado.
* Observei durante o teste que a quantidade de dígitos decimais não está configurada, esse é um ponto que deve ser trabalhado em breve
* Percebo que o gitHub é muito mais do que apenas guardar o código, por exemplo, essa parte de correção pode ser registrada a parte antes de prosseguir com o desenvolvimento, porém não foi uma nova adição de funcionalidade, então utilizar *feat* não faria sentido. Analisando, descobri que há mais formas de documentar, como nesse caso atual, o *fix* e até mesmo para documentação a parte *docs*. É mais complexo do que imaginava...
* Enquanto registrava as informações percebo que tem ficado muita informação acumulada em um único local. Com o passar do tempo pretendo começar a dividir em arquivos diferentes, mas isso é assunto para daqui alguns dias.

### 📆 25/06/2026
* Acreditava que seria um dia mais tranquilo em relação ao desenvolvimento, pois pretendia finalizar os endpoints restantes da classe Material, e como eu já havia feito antes o de Categorias pensava que seria mais tranquilo. Como me enganei😓​... Foi a primeira vez que trabalhei com uma classe que continha vários atributos portanto meu primeiro grande passo e que me travou bastante de inicio foi saber que teria que atualizar todos os atributos no PUT. Outro ponto, foi saber mais sobre regras de negócios. Eu já sabia que usaria mas não ao ponto que enfrentei hoje. Ao cadastrar o material, eu o vinculei com as categorias. Porém ao atualizar eu queria bloquear para não cadastrar mais de um material com o mesmo nome em uma mesma categoria. Porém ví que para fazer as checagens foi algo que não conseguiria em um curto espaço de tempo, por esse motivo, optei por deixar para resolver essa regra de negócio em um momento seguinte, provavelmente amanhã ou até o final dessa semana. Não quero passar para um próximo tópico deixando algo que considero grande para depois. Adaptações e modificações eu considero tudo bem, ter que voltar em algum momento para adaptar algo, porém, nesse sentido quero resolver o quanto antes. Para deixar para depois utilizei o TODO, ví que era um termo que é comumente utilizado em casos assim.
* Outro ponto, ainda sobre modificação, eu alterei levemente meu modelo de material, onde ví que havia o ponto de id_categoria em dois lugares, sendo que não é necessário pois uma função já herdaria da anterior. Ao tentar remover isso, meu sistema começou a dar erro de execução, e percebi que as modificações devem ser feitas com mais cautelas para não afetar a integridade do sistema.
* O dia não foi de todo complicações, pois ao desenvolvi percebi diversos pontos, como por exemplo, está ficando de certa forma mais tranquilo, pois tenho trabalhado com conceitos que tenho visto diariamente, e isso tem se tornado cada vez mais um hábito, que facilita muito meu desempenho.
* Enquanto programava ví também que meu código, principalmente na parte de routers, tem se tornado muito repetitivo, em um mesmo arquivo. Em breve procurarei uma forma de tornar isso mais simplificado e mais limpo, para facilitar e para me organizar. Isso eu acredito que será um bom próximo passo no meu desenvolvimento.
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

### Versão 0.2.5 (📆21 jun. 2026)
- Criação do Delete de categorias (DELETE)
- Realização dos Testes no Swagger.
- commit da alteração
- pequena revisão do conteúdo até o momento.
- Preparação para abertura da Pull Request

### Versão 0.3.1 (📆23 jun. 2026)
- Começando a trabalhar com a classe material
- Criação/Modificação do model de material
- Adição do relacionamento com Categoria
- Criação do routers de material
- Criação do Endpoint POST(Create)
- Realização dos Testes no Swagger.
- Commit da alteração.

### Versão 0.3.1.1 (📆24 jun. 2026)
- Correção (fix) do sistema
- Registrado no Diário de bordo
- Criação de novo tópico na documentação (modelagem)
- Adição do modelo entidade-relacionamento feito antes do inicio do projeto

### Versão 0.3.5(📆25 jun. 2026)
- Criação do Endpoint GET de materiais
- Criação do Endpoint GET por ID de materiais
- Criação do Endpoint PUT de materiais
- Criação do Endpoint DELETE de materiais
- Testes simples no Swagger
- Commits a cada finalização no gitHub
- Atualização no diário de bordo


---

## 🎯 Metas e Próximos Passos

**Metas Cumpridas**
### CRUD de Categorias (Finalizado na primeira semana do projeto — 📆15/06 a 21/06)
- [x] CREATE
- [x] GET
- [x] GET por ID
- [x] UPDATE
- [x] DELETE
### Adicionamento do MER que já havia feito antes de iniciar o projeto (📆24/06)


### Curto Prazo (Meta da Semana)
- Criar primeiros endpoints CRUD.
*  Referente a materiais
*  [x] CREATE (📆23/06/2026)
*  [x] GET (📆24/06/2026)
*  [x] GET por ID (📆25/06/2026)
*  [x] UPDATE (📆25/06/2026)
*  [x] DELETE (📆25/06/2026)
* Tratamento de casas decimais

### Médio/Longo Prazo
- Revisão do modelo entidade-relacionamento
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
  git push -u origin "nome da branch" (fazer ao iniciar uma nova branch para criar a branch no repositório)
* **Inicialização do uvicorn**
  ```bash
  uvicorn main:app --reload
---

### ⚠️ Observações
  **Nomeclatura:**
  - feature -> muito utilizado para indicar uma nova funcionalidade
  - fix -> utilizado para correções
  - refactor -> reorganização de código sem alterar comportamento
  - docs -> alterações em documentação
  - test -> adição ou alteração de testes
  - chore -> tarefas de manutenção

  # TODO
  # Explicação
  -> Pequeno trexo que como o nome diz TODO -> pendência, ou seja, voltarei para fazer algo alí depois, o que pode ser colocado em conjunto explicando em sequência