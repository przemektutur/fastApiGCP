"""Main application module."""
from fastapi import (
    FastAPI,
    Request,
    HTTPException, 
    Depends
)
from sqlalchemy.orm import (
    Session,
    joinedload,
)
from database import SessionLocal, engine, Base
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from schemas import CVCreate, CVUpdate, CV as SchemaCV
import models
import crud
from models import CV as ModelCV


app = FastAPI()

# Utworzenie tabel jeśli nie istnieją
Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/cvs/", response_model=SchemaCV)
def create_cv(cv_create: CVCreate, db: Session = Depends(get_db)):
    cv_model = ModelCV(name=cv_create.name, email=cv_create.email)
    db.add(cv_model)
    db.commit()
    db.refresh(cv_model)

    for exp_data in cv_create.experience:
        exp_model = models.Experience(**exp_data.dict(), cv_id=cv_model.id)
        db.add(exp_model)

    for edu_data in cv_create.education:
        edu_model = models.Education(**edu_data.dict(), cv_id=cv_model.id)
        db.add(edu_model)

    for skill_data in cv_create.skills:
        skill_model = models.Skill(**skill_data.dict(), cv_id=cv_model.id)
        db.add(skill_model)

    db.commit()
    return cv_model

@app.get("/cvs/{cv_id}", response_model=SchemaCV)
def read_cv(cv_id: int, db: Session = Depends(get_db)):
    return db.query(models.CV).options(
        joinedload(models.CV.experiences), 
        joinedload(models.CV.educations)
    ).filter(models.CV.id == cv_id).first()

"""
@app.put("/cvs/{cv_id}", response_model=SchemaCV)
def update_cv_endpoint(
        cv_id: int,
        cv_update: CVUpdate, 
        db: Session = Depends(get_db)
    ):
    updated_cv = crud.update_cv(db=db, cv_id=cv_id, cv_update=cv_update)
    if updated_cv is None:
        raise HTTPException(status_code=404, detail="CV not found")
    return updated_cv
"""

@app.put("/cvs/{cv_id}", response_model=SchemaCV)
def update_cv(cv_id: int, cv_update: CVUpdate, db: Session = Depends(get_db)):
    db_cv = db.query(models.CV).filter(models.CV.id == cv_id).first()
    if db_cv is None:
        return None

    for var, value in vars(cv_update).items():
        if value is not None and hasattr(db_cv, var):
            setattr(db_cv, var, value)

    db.commit()
    db.refresh(db_cv)

    db_cv = db.query(models.CV).options(
        joinedload(models.CV.experiences),
        joinedload(models.CV.educations)
    ).filter(models.CV.id == cv_id).first()
    return db_cv

@app.delete("/cvs/{cv_id}", status_code=204)
async def delete_cv(cv_id: int, db: Session = Depends(get_db)):
    crud.delete_cv(db=db, cv_id=cv_id)
