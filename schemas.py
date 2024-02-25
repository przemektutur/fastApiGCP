from pydantic import BaseModel
from typing import (
    List, 
    Optional,
)
from datetime import date


class ExperienceBase(BaseModel):
    """
    A database model representing an experience entry related to a CV.

    Attributes:
    -----------
    id (Integer): The unique identifier of the experience entry.
    company (String): The name of the company.
    position (String): The position held at the company.
    from_date (Date): The start date of the position.
    to_date (Date): The end date of the position (optional).
    description (String): A description of the position (optional).
    cv_id (Integer): The ID of the related CV.
    """
    company: str
    position: str
    from_date: date
    to_date: Optional[date] = None
    description: Optional[str] = None


class ExperienceCreate(BaseModel):
    """
    A Pydantic model for creating a new experience entry.

    Attributes:
    -----------
    company (str): Name of the company.
    position (str): Position at the company.
    from_date (date): Start date of the position.
    to_date (Optional[date]): The end date of the position.
    description (Optional[str]): A description of the position, optional.
    """
    company: str
    position: str
    from_date: date
    to_date: Optional[date] = None
    description: Optional[str] = None


class Experience(ExperienceBase):
    """
    A Pydantic model for representing an experience entry, extending 
    ExperienceBase with database ID and CV ID.

    Attributes:
    -----------
    id (int): Unique identifier of the experience entry.
    cv_id (int): ID of the related CV.
    """
    id: int
    cv_id: int

    class Config:
        orm_mode = True


class EducationBase(BaseModel):
    """
    Model (base) for education entries related to a CV.

    Attributes:
    -----------
    institution (str): Name of the educational institution.
    degree (str): Degree or certification obtained.
    from_date (date): Start date of the education.
    to_date (Optional[date]): End date of the education, optional.
    """
    institution: str
    degree: str
    from_date: date
    to_date: Optional[date] = None


class EducationCreate(EducationBase):
    """
    Model for creating a new education entry, based on EducationBase.
    """
    institution: str
    degree: str
    from_date: date
    to_date: Optional[date] = None


class Education(EducationBase):
    """
    A Pydantic model for representing an education entry, extending 
    EducationBase with database ID and CV ID.

    Attributes:
    -----------
    id (int): Unique identifier of the education entry.
    cv_id (int): ID of the related CV.
    """
    id: int
    cv_id: int

    class Config:
        orm_mode = True


class SkillBase(BaseModel):
    """
    A base Pydantic model for skills related to a CV.

    Attributes:
    -----------
    name (str): Name of the skill.
    level (str): Proficiency level of the skill.
    """
    name: str
    level: str  # Examp: 'podstawowy', 'średniozaawansowany', 'zaawansowany'


class SkillCreate(SkillBase):
    """
    A Pydantic model for creating a new skill entry, based on SkillBase.
    name (str): Skill name for CV
    level (str): Level of skill in the CV
    """
    name: str
    level: str


class Skill(SkillBase):
    """
    A Pydantic model for representing a skill entry, extending 
    SkillBase with database ID and CV ID.

    Attributes:
    -----------
    id (int): The unique identifier of the skill entry.
    cv_id (int): The ID of the related CV.
    """
    id: int
    cv_id: int

    class Config:
        orm_mode = True


class CVBase(BaseModel):
    """
    Base Pydantic model for CV entries.

    Attributes:
    -----------
    name (str): Name of the CV owner.
    email (str): Email address of the CV owner.
    """
    name: str
    email: str
    experiences: List[Experience] = []
    educations: List[Education] = []


class CVCreate(CVBase):
    """
    Pydantic model for creating a new CV, including lists of 
    experiences, educations, and skills to be associated with the CV.
    """
    experience: List[ExperienceCreate] = []
    education: List[EducationCreate] = []
    skills: List[SkillCreate] = []


class CVUpdate(BaseModel):
    """
    Pydantic model for updating an existing CV. 
    Fields are optional and only provided fields will be updated.

    Attributes:
    -----------
    name (Optional[str]): New name of the CV owner, if updating.
    email (Optional[str]): New email address of the CV owner, if updating.
    """
    name: Optional[str] = None
    email: Optional[str] = None

    class Config:
        orm_mode = True


class CV(CVBase):
    """
    A comprehensive Pydantic model for representing a CV, 
    including its associated experiences, educations, and skills.

    Attributes:
    -----------
    id (int): The unique identifier of the CV.
    experience (List[Experience]): List of experience entries related to CV.
    education (List[Education]): List of education entries related to CV.
    skills (List[Skill]): A list of skill entries related to the CV.
    """
    id: int
    experience: List[Experience] = []
    education: List[Education] = []
    skills: List[Skill] = []

    class Config:
        orm_mode = True
