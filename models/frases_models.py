from core.configs import settings
from sqlalchemy import Column, Integer, String

class FrasesModel(settings.DBBaseModel):
    __tablename__ = 'frases'

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    quote: str = Column(String(500))
   