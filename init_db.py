from database import engine, Base
from models import Courier,Order


Base.metadata.create_all(bind=engine)
