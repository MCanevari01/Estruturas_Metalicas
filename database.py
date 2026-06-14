from sqlmodel import SQLModel, create_engine
from models.categoria import Categoria
from models.material import Material


DATABASE_URL = "sqlite:///estruturas_metalicas.db"

engine = create_engine(DATABASE_URL, echo=True)


def inicializar_banco_de_dados():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    inicializar_banco_de_dados()