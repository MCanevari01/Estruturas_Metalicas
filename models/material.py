from typing import Optional
from sqlmodel import Field, SQLModel


class Material(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome_material: str = Field(nullable=False)
    preco_unitario: float = Field(nullable=False)
    quantidade_estoque: float = Field(nullable=False)
    id_categoria: int = Field(foreign_key="categoria.id")
    