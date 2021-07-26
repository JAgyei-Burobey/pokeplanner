from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class Pokéform(FlaskForm):
    pkname = StringField("Pokémon name:")
    nickname = StringField("Pokémon nickname:")
    nature = SelectField("Choose a nature:", choices=[("+Att-Att", "Hardy"), ("Def-Def", "Docile"), ("+SpA-SpA", "Serious"), ("+SpD-SpD", "Bashful"), ("+Spe-Spe", "Quirky")
    ])
    ability = SelectField("Choose an ability:", choices= [])
    submit = SubmitField("Save")

class Abilityform(FlaskForm):
    abname = StringField("Ability name:")
    submit = SubmitField("Save")