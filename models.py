from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Experience(Base):
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
    __tablename__ = "educations"
    id = Column(Integer, primary_key=True, index=True)
    institution = Column(String, index=True)
    degree = Column(String, index=True)
    from_date = Column(Date)
    to_date = Column(Date, nullable=True)
    cv_id = Column(Integer, ForeignKey("cvs.id"))
    cv = relationship("CV", back_populates="educations")


class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(String, index=True)
    cv_id = Column(Integer, ForeignKey('cvs.id'))
    cv = relationship("CV", back_populates="skills")


class CV(Base):
    __tablename__ = "cvs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    experiences = relationship("Experience", back_populates="cv")
    educations = relationship("Education", back_populates="cv")
    skills = relationship("Skill", back_populates="cv")
