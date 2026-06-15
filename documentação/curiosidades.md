Nesse Documento, anotarei algumas curiosidades que obtive enquanto estudava

Uso do yield session
    def get_session():
    with Session(engine) as session:
        yield session
        (Usado na crriação do banco de dados)
        -Ao final de funções, é comum usar o return, mas nesse caso, a utilização do yield garante a abertura e fechamento do mesmo, ou seja, ao ser requisitado é aberto a seção e ao concluir o bloco, a seção e automaticamente encerrada.(Considerado forma mais segura e limpa de fornecer dados ao banco de dados)