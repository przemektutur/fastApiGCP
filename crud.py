# crud.py

from typing import List
from models import CV, Experience, Education, Skill

# Przykładowa "baza danych"
fake_db = {
    "cvs": []
}

def create_cv(cv: CV) -> CV:
    fake_db["cvs"].append(cv)
    return cv

def get_cv(cv_id: int) -> CV:
    return fake_db["cvs"][cv_id]

def update_cv(cv_id: int, cv: CV) -> CV:
    fake_db["cvs"][cv_id] = cv
    return cv

def delete_cv(cv_id: int):
    del fake_db["cvs"][cv_id]

