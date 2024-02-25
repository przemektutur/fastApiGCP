from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base


class Experience(Base):
    __tablename__ = "experiences"
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, index=True)
    position = Column(String, index=True)
    from_date = Column(Date)
    to_date = Column(String, nullable=True)
    description = Column(String, nullable=True)
    cv_id = Column(Integer, ForeginKey("cvs.id"))


class Education(Base):
    __tablename__ = "education"
    id = Column(Integer, primary_key=True, index=True)
    institution = Column(String, index=True)
    degree = Column(String, index=True)
    from_date = Column(Date)
    to_date = Column(Date, nullable=True)
    cv_id = Column(Integer, ForeignKey("cvs.id"))


class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(String, index=True)
    cv_id = Column(Integer, ForeignKey('cvs.id'))


class CV(Base):
    __tablename__ = "cvs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    experiences = relationship("Experience", backref="cv")
    educations = relationship("Education", backref="cv")
    skills = relationship("Skill", backref="cv")
