"""Database setup."""
from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from database import Base


class Experience(Base):
    """
    Represents an employment or professional experience related to a CV.

    Attributes:
    -----------
    id (Integer): Unique identifier for the experience record.
    company (String): Name of the company or organization.
    position (String): Job title or position held.
    from_date (Date): Start date of the experience.
    to_date (Date): End date of the experience. Nullable if currently employed.
    description (String): Description of job responsibilities and achievements.
    cv_id (Integer): Foreign key linking to the associated CV.
    cv (relationship): SQLAlchemy relationship to the CV model.
    """
    __tablename__ = "experiences"
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, index=True)
    position = Column(String, index=True)
    from_date = Column(Date)
    to_date = Column(Date, nullable=True)
    description = Column(String, nullable=True)
    cv_id = Column(Integer, ForeignKey("cvs.id"))
    cv = relationship("CV", back_populates="experiences")


class Education(Base):
    """
    Represents an educational qualification related to a CV.

    Attributes:
    -----------
    id (Integer): Unique identifier for the education record.
    institution (String): Name of the educational institution.
    degree (String): Degree or certification obtained.
    from_date (Date): Start date of the educational program.
    to_date (Date): Graduation or completion date.
    cv_id (Integer): Foreign key linking to the associated CV.
    cv (relationship): SQLAlchemy relationship to the CV model.
    """
    __tablename__ = "educations"
    id = Column(Integer, primary_key=True, index=True)
    institution = Column(String, index=True)
    degree = Column(String, index=True)
    from_date = Column(Date)
    to_date = Column(Date, nullable=True)
    cv_id = Column(Integer, ForeignKey("cvs.id"))
    cv = relationship("CV", back_populates="educations")


class Skill(Base):
    """
    Skill or competency related to a CV.

    Attributes:
    -----------
    id (Integer): Unique identifier for the skill record.
    name (String): Name of the skill or competency.
    level (String): Proficiency level of the skill.
    cv_id (Integer): Foreign key linking to the associated CV.
    cv (relationship): SQLAlchemy relationship to the CV model.
    """
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(String, index=True)
    cv_id = Column(Integer, ForeignKey('cvs.id'))
    cv = relationship("CV", back_populates="skills")


class CV(Base):
    """
    Curriculum Vitae (CV) or resume.

    Attributes:
    -----------
    id (Integer): Unique identifier for the CV record.
    name (String): Full name of the CV owner.
    email (String): Contact email of the CV owner.
    experiences (relationship): SQLAlchemy relationship to Experience models.
    educations (relationship): SQLAlchemy relationship to Education models.
    skills (relationship): SQLAlchemy relationship to Skill models.
    """
    __tablename__ = "cvs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    experiences = relationship("Experience", back_populates="cv")
    educations = relationship("Education", back_populates="cv")
    skills = relationship("Skill", back_populates="cv")
