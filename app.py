# app.py

from fastapi import FastAPI, Request, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from typing import List
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from schemas import CVCreate, CV 
from database import SessionLocal, engine
import crud
import models


app = FastAPI()

# Utworzenie tabel jeśli nie istnieją
Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

'''
@app.post("/cvs/", response_model=CV)
def create_cv(cv: CVCreate, db: Session = Depends(get_db)):
    db_cv = CV(**cv.dict())
    db.add(db_cv)
    db.commit()
    db.refresh(db_cv)
    return db_cv
'''
@app.post("/cvs/", response_model=schemas.CV)
def create_cv(cv_create: schemas.CVCreate, db: Session = Depends(get_db)):
    # Tworzenie głównego obiektu CV
    cv_model = models.CV(name=cv_create.name, email=cv_create.email)
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


@app.get("/cvs/{cv_id}", response_model=CV)
async def read_cv(cv_id: int):
    try:
        return crud.get_cv(cv_id)
    except IndexError:
        raise HTTPException(status_code=404, detail="CV not found")

@app.put("/cvs/{cv_id}", response_model=CV)
async def update_cv(cv_id: int, cv: CV):
    try:
        return crud.update_cv(cv_id, cv)
    except IndexError:
        raise HTTPException(status_code=404, detail="CV not found")

@app.delete("/cvs/{cv_id}", status_code=204)
async def delete_cv(cv_id: int):
    try:
        crud.delete_cv(cv_id)
    except IndexError:
        raise HTTPException(status_code=404, detail="CV not found")
