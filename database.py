from sqlmodel import SQLModel, create_engine, Session
from models.categoria import Categoria
from models.material import Material


nome_do_banco= "estruturas_metalicas.db"
DATABASE_URL = f"sqlite:///{nome_do_banco}"

connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)


def inicializar_banco_de_dados():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


if __name__ == "__main__":
    inicializar_banco_de_dados()