from sqlalchemy.orm import Session

import models
import schemas

def create_cv(db: Session, cv: schemas.CVCreate) -> models.CV:
    db_cv = models.CV(**cv.dict())
    db.add(db_cv)
    db.commit()
    db.refresh(db_cv)
    return db_cv

def get_cv(db: Session, cv_id: int) -> models.CV:
    return db.query(models.CV).filter(models.CV.id == cv_id).first()

def update_cv(db: Session, cv_id: int, cv_update: schemas.CVUpdate) -> models.CV:
    db_cv = db.query(models.CV).filter(models.CV.id == cv_id).first()
    if db_cv is None:
        return None
    
    update_data = cv_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_cv, key, value)

    db.commit()
    db.refresh(db_cv)
    return db_cv

def delete_cv(db: Session, cv_id: int):
    db_cv = db.query(models.CV).filter(models.CV.id == cv_id).first()
    if db_cv:
        db.delete(db_cv)
        db.commit()
    else:
        raise Exception(f"CV with id {cv_id} not found")

