# crud.py
from sqlalchemy.orm import Session
from typing import List

from schemas import CVUpdate
from models import CV, Experience, Education, Skill


fake_db = {
    "cvs": []
}

def create_cv(cv: CV) -> CV:
    fake_db["cvs"].append(cv)
    return cv

def get_cv(cv_id: int) -> CV:
    return fake_db["cvs"][cv_id]

def update_cv(db: Session, cv_id: int, cv_update: CVUpdate):
    db_cv = db.query(CV).filter(CV.id == cv_id).first()
    if db_cv is None:
        return None

    for var, value in vars(cv_update).items():
        if hasattr(db_cv, var) and value is not None:
            setattr(db_cv, var, value)

    db.commit()
    return db_cv

def delete_cv(db: Session, cv_id: int):
    db_cv = db.query(CV).filter(CV.id == cv_id).first()
    if db_cv:
        db.delete(db_cv)
        db.commit()
    else:
        raise Exception(f"CV with id {cv_id} not found")
