"""User model definition."""

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from nextgigai.database import Base

class User(Base):
    """User model."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    # Relationships will be added as we develop modules
    # resumes = relationship("Resume", back_populates="owner")
    # applications = relationship("JobApplication", back_populates="user")
