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


@router.get("/", response_model=list[Categoria])

def listar_categorias(session: Session = Depends(get_session)):
    categorias = session.exec(select(Categoria)).all()
    return categorias


@router.get("/{categoria_id}", response_model=Categoria)

def categoria_por_id(categoria_id: int, session: Session = Depends(get_session)):
    categoria = session.get(Categoria, categoria_id)

    if categoria is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria não encontrada"
        )
    return categoria