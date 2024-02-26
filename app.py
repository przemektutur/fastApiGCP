"""Main application module."""
from typing import Iterator

from fastapi import (
    FastAPI,
    Request,
    HTTPException,
    Depends,
)
from sqlalchemy.orm import (
    Session,
    joinedload,
)
from database import (
    SessionLocal,
    engine,
    Base,
)
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from schemas import CVCreate, CVUpdate, CV as SchemaCV
import models
import crud
from models import CV as ModelCV


app = FastAPI()

# Table creation if doesn't exist
Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def get_db() -> Iterator[Session]:
    """
    Dependency that creates a new SQLAlchemy session for a request,
    yields it for use, and closes it once the request is finished.

    This function is a generator that first establishes a connection
    to the database, then waits for the endpoint function to complete,
    and finally closes the connection, ensuring resources are freed properly.

    Yields:
    -------
    Session : sqlalchemy.orm.Session
        A SQLAlchemy session connected to the database.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_root(request: Request):
    """
    Renders and returns the main page template.

    Parameters:
    -----------
    request (Request): The request object.

    Returns:
    --------
    TemplateResponse: The rendered "index.html" template.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/cvs/", response_model=SchemaCV)
def create_cv(cv_create: CVCreate, db: Session = Depends(get_db)) -> SchemaCV:
    """
    Creates a new CV entry in the database.

    Parameters:
    -----------
    cv_create (CVCreate): The CV creation object containing CV details.
    db (Session): The database session.

    Returns:
    --------
    SchemaCV: The created CV as a Pydantic model.
    """
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
def read_cv(cv_id: int, db: Session = Depends(get_db)) -> SchemaCV:
    """
    Retrieves a CV entry from the database by its ID.

    Parameters:
    -----------
    cv_id (int): The ID of the CV to retrieve.
    db (Session): The database session.

    Returns:
    --------
    SchemaCV: The requested CV as a Pydantic model.
    """
    return db.query(models.CV).options(
        joinedload(models.CV.experiences),
        joinedload(models.CV.educations)
    ).filter(models.CV.id == cv_id).first()

@app.put("/cvs/{cv_id}", response_model=SchemaCV)
def update_cv(
        cv_id: int,
        cv_update: CVUpdate,
        db: Session = Depends(get_db)
    ) -> SchemaCV:
    """
    Updates an existing CV entry in the database.

    Parameters:
    -----------
    cv_id (int): The ID of the CV to update.
    cv_update (CVUpdate): The CV update object containing updated CV details.
    db (Session): The database session.

    Returns:
    --------
    SchemaCV: The updated CV as a Pydantic model.
    """
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
async def delete_cv(cv_id: int, db: Session = Depends(get_db)) -> None:
    """
    Deletes a CV entry from the database by its ID.

    Parameters:
    -----------
    cv_id (int): The ID of the CV to delete.
    db (Session): The database session.

    Returns:
    --------
    None
    """
    crud.delete_cv(db=db, cv_id=cv_id)
