from . import app, db

class Pokémon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pkname = db.Column(db.String(30), nullable = False)
    nickname = db.Column(db.String(12), nullable = False, default = "----")
    type_1 = db.Column(db.String(12), nullable = False, default = "-")
    type_2 = db.Column(db.String(12), nullable = False, default = "-")
    ability_id = db.Column(db.Integer, db.ForeignKey('abilities.id'))
    nature_id = db.Column(db.Integer, db.ForeignKey('natures.id'))

    
class Abilities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    abilityname = db.Column(db.String(30), nullable = False)
    ability_info = db.Column(db.String(300), nullable = False, default = "")
    pokémon = db.relationship('Pokémon', backref='ability')


class Natures(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naturename = db.Column(db.String(30), nullable = False)
    nature_info = db.Column(db.String(300), nullable = False)
    pokémon = db.relationship('Pokémon', backref='nature')
