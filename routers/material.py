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
        select(Material).where(
            Material.nome == material_input.nome,
            Material.id_categoria == material_input.id_categoria
            )
        ).first()
    
    if material_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe um material cadastrado com esse nome nessa categoria"
        )
    
    novo_material = Material.model_validate(material_input)
    session.add(novo_material)
    session.commit()
    session.refresh(novo_material)
    return novo_material


@router.get("/", response_model=list[Material])

def listar_materiais(session: Session = Depends(get_session)):
    materiais = session.exec(select(Material)).all()
    return materiais


@router.get("/{material_id}", response_model=Material)

def material_por_id(material_id: int, session: Session = Depends(get_session)):
    material = session.get(Material, material_id)

    if material is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material não encontrado"
        )
    return material


@router.put("/{material_id}", response_model=Material)

def atualizar_material(material_id: int, material_input: MaterialBase, session: Session = Depends(get_session)):
    material = session.get(Material, material_id)

    if material is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material não encontrado"
        )
    
    categoria_existente = session.get(Categoria, material_input.id_categoria)
    if not categoria_existente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria não encontrada"
        )
    
    material_existente = session.exec(
        select(Material).where(
            Material.nome == material_input.nome,
            Material.id_categoria == material_input.id_categoria,
            Material.id != material_id
        )
    ).first()
    
    if material_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe um material cadastrado com esse nome nessa categoria"
        )

    material.nome = material_input.nome
    material.preco_unitario = material_input.preco_unitario
    material.quantidade_estoque = material_input.quantidade_estoque
    material.unidade_medida = material_input.unidade_medida
    material.id_categoria = material_input.id_categoria

    session.commit()
    session.refresh(material)
    return material


@router.delete("/{material_id}")

def deletar_material(material_id: int, session: Session = Depends(get_session)):
    material = session.get(Material, material_id)

    if material is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material não encontrado"
        )
    
    session.delete(material)
    session.commit()
    return{
        "status": "Sucesso",
        "mensagem": f"Material '{material.nome}' deletado com sucesso!"
    }