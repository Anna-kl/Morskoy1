from sqlalchemy import create_engine, MetaData
engine = create_engine('postgresql://postgres:2537300@localhost:5432/postgres')
meta = MetaData()

from .models_base import User, Room

meta.create_all(engine)