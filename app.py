# app.py

from fastapi import FastAPI, HTTPException
from typing import List
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models import CV
import crud


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/cvs/", response_model=CV)
async def create_cv(cv: CV):
    return crud.create_cv(cv)

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
