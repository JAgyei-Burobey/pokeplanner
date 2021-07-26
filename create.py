from application import db
from application.models import Pokémon


db.drop_all()
db.create_all()

