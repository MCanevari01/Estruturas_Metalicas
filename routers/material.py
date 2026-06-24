from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from database import get_session
from models.material import Material, MaterialBase
from models.categoria import Categoria


router = APIRouter(prefix="/materiais", tags=["Materiais"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Material)

def criar_material(material_input: MaterialBase, session: Session = Depends(get_session)):

    categoria_existente = session.get(Categoria, material_input.id_categoria)
    if not categoria_existente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria não encontrada"
        )

    material_existente = session.exec(
        select(Material).where(Material.nome == material_input.nome)).first()
    
    if material_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe um material cadastrado com esse nome"
        )
    
    novo_material = Material.model_validate(material_input)
    session.add(novo_material)
    session.commit()
    session.refresh(novo_material)
    return novo_material