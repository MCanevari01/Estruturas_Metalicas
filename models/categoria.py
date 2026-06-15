from sqlmodel import Field, SQLModel

class CategoriaCreate(SQLModel):
    nome: str


class Categoria(CategoriaCreate, table=True):
    id: int | None = Field(default=None, primary_key=True)