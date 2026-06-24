from sqlmodel import Field, SQLModel
from decimal import Decimal


class MaterialBase(SQLModel):
    nome: str
    preco_unitario: Decimal
    quantidade_estoque: Decimal
    unidade_medida: str
    id_categoria: int


class Material(MaterialBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    id_categoria: int = Field(foreign_key="categoria.id")