from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class ExperienceBase(BaseModel):
    company: str
    position: str
    from_date: date
    to_date: Optional[date] = None
    description: Optional[str] = None


class ExperienceCreate(BaseModel):
    company: str
    position: str
    from_date: date
    to_date: Optional[date] = None
    description: Optional[str] = None


class Experience(ExperienceBase):
    id: int
    cv_id: int

    class Config:
        orm_mode = True


class EducationBase(BaseModel):
    institution: str
    degree: str
    from_date: date
    to_date: Optional[date] = None


class EducationCreate(EducationBase):
    institution: str
    degree: str
    from_date: date
    to_date: Optional[date] = None


class Education(EducationBase):
    id: int
    cv_id: int

    class Config:
        orm_mode = True


class SkillBase(BaseModel):
    name: str
    level: str  # Exampl: 'podstawowy', 'średniozaawansowany', 'zaawansowany'


class SkillCreate(SkillBase):
    name: str
    level: str


class Skill(SkillBase):
    id: int
    cv_id: int

    class Config:
        orm_mode = True


class CVBase(BaseModel):
    name: str
    email: str


class CVCreate(CVBase):
    experience: List[ExperienceCreate] = []
    education: List[EducationCreate] = []
    skills: List[SkillCreate] = []


class CVUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    # Dodaj inne pola zgodnie z potrzebami

    class Config:
        orm_mode = True


class CV(CVBase):
    id: int
    experience: List[Experience] = []
    education: List[Education] = []
    skills: List[Skill] = []

    class Config:
        orm_mode = True
