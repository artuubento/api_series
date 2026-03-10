from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.serie import SerieModel
from app.schema.serie import SerieSchema

serie = APIRouter()

@serie.post("/")
async def criar_serie(dados: SerieSchema, db: Session = Depends(get_db)):
    nova_serie = SerieModel(**dados.model_dump())
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie

@serie.get("/")
async def listar_series(db: Session = Depends(get_db)):
    return db.query(SerieModel).all()

@serie.put("/{serie_id}")
async def atualizar_serie(serie_id: int, dados: SerieSchema, db: Session = Depends(get_db)):
   
    db_serie = db.query(SerieModel).filter(SerieModel.id == serie_id).first()

   
    if not db_serie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Série não encontrada"
        )

    
    for chave, valor in dados.model_dump().items():
        setattr(db_serie, chave, valor)

    db.commit()
    db.refresh(db_serie)
    return db_serie

@serie.delete("/{serie_id}", status_code=status.HTTP_204_NO_CONTENT)
async def excluir_serie(serie_id: int, db: Session = Depends(get_db)):
   
    db_serie = db.query(SerieModel).filter(SerieModel.id == serie_id).first()

   
    if not db_serie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Série não encontrada"
        )

    
    db.delete(db_serie)
    db.commit()
    
    
    return None