from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from database import get_session
from models.categoria import Categoria, CategoriaCreate


router = APIRouter(prefix="/categorias", tags=["Categorias"])


@router.post("/", status_code=status.HTTP_201_CREATED,  response_model=Categoria)

def criar_categoria(categoria_input: CategoriaCreate, session: Session = Depends(get_session)):
    categoria_existente = session.exec(
        select(Categoria).where(Categoria.nome == categoria_input.nome)).first()


    if categoria_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe uma categoria cadastrada com esse nome"
        )
    
    nova_categoria = Categoria.model_validate(categoria_input)    
    session.add(nova_categoria)
    session.commit()
    session.refresh(nova_categoria)    
    return nova_categoria