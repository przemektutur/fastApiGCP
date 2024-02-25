from pydantic import BaseModel
from typing import List, Optional

class Experience(BaseModel):
    company: str
    position: str
    from_date: str
    to_date: Optional[str] = None
    description: Optional[str] = None

class Education(BaseModel):
    institution: str
    degree: str
    from_date: str
    to_date: Optional[str] = None

class Skill(BaseModel):
    name: str
    level: str # Może być 'podstawowy', 'średniozaawansowany', 'zaawansowany'

class CV(BaseModel):
    name: str
    email: str
    experience: List[Experience]
    education: List[Education]
    skills: List[Skill]
