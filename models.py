from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from base import Base

class Vacancy(Base):
    __tablename__ = "vacancies"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40), nullable=False)
    company: Mapped[str] = mapped_column(String(40))
    skills: Mapped[Optional[str]] = mapped_column(String)
    salary: Mapped[str] = mapped_column(String)
    link: Mapped[str] = mapped_column(String)
