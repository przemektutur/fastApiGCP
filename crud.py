from sqlalchemy.orm import Session

import models
import schemas

def create_cv(db: Session, cv: schemas.CVCreate) -> models.CV:
    """
    Create a new CV entry in the database.

    Parameters:
    -----------
    db: Session - Database session.
    cv: schemas.CVCreate - CV data for creation.

    Returns:
    --------
    models.CV - The created CV object.
    """
    db_cv = models.CV(**cv.dict())
    db.add(db_cv)
    db.commit()
    db.refresh(db_cv)
    return db_cv

def get_cv(db: Session, cv_id: int) -> models.CV:
    """
    Retrieve a CV entry from the database by its ID.

    Parameters:
    -----------
    db: Session - Database session.
    cv_id: int - ID of the CV to retrieve.

    Returns:
    --------
    models.CV - The retrieved CV object or None if not found.
    """
    return db.query(models.CV).filter(models.CV.id == cv_id).first()

def update_cv(db: Session, cv_id: int, cv_update: schemas.CVUpdate) -> models.CV:
    """
    Update an existing CV entry in the database.

    Parameters:
    -----------
    db: Session - Database session.
    cv_id: int - ID of the CV to update.
    cv_update: schemas.CVUpdate - Data to update the CV with.

    Returns:
    --------
    models.CV - The updated CV object or None if not found.
    """
    db_cv = db.query(models.CV).filter(models.CV.id == cv_id).first()
    if db_cv is None:
        return None
    
    update_data = cv_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_cv, key, value)

    db.commit()
    db.refresh(db_cv)
    return db_cv

def delete_cv(db: Session, cv_id: int) -> None:
    """
    Delete a CV entry from the database.

    Parameters:
    -----------
    db: Session - Database session.
    cv_id: int - ID of the CV to delete.

    Raises:
    -------
    Exception: If the CV with the specified ID does not exist.
    """
    db_cv = db.query(models.CV).filter(models.CV.id == cv_id).first()
    if db_cv:
        db.delete(db_cv)
        db.commit()
    else:
        raise Exception(f"CV with id {cv_id} not found")

