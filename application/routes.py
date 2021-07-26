from . import app, db
from application.forms import Abilityform, Pokéform
from application.models import Pokémon, Abilities, Natures
from flask import redirect, url_for, request, render_template





@app.route("/")
@app.route("/home")
def home():
    all_pokemon = Pokémon.query.all()
    all_abilities = Abilities.query.all()
    return render_template("home.html", all_pokemon=all_pokemon, all_abilities=all_abilities)
   



@app.route("/create_poke", methods =["GET", "POST"])
def create_poke():
    form = Pokéform()

    if request.method == "POST":
        new_pokemon = Pokémon(pkname=form.pkname.data, nickname=form.nickname.data)
        db.session.add(new_pokemon)
        db.session.commit()

        return redirect(url_for("home"))
    else:
        abilities=Abilities.query.all()
        for ability in abilities:
            form.ability.choices=[(ability.id), (ability.abilityname)]

        return render_template("create_poke.html", form = form)



@app.route("/create_ability", methods =["GET", "POST"])
def create_ability():
    form = Abilityform()

    if request.method == "POST":
        new_ability = Abilities(abilityname=form.abname.data)
        db.session.add(new_ability)
        db.session.commit()

        return redirect(url_for("home"))
    else:
        return render_template("create_ability.html", form = form)
    
    



@app.route("/update/<int:id>", methods = ("GET", "POST"))
def update(id):
    pokemon = Pokémon.query.get(id)
    form = Pokéform()

    if request.method == "POST":
        pokemon.pkname = form.pkname.data
        pokemon.nickname = form.nickname.data
        db.session.add(pokemon)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("create.html", form = form)



@app.route("/delete/<int:id>")
def delete(id):
    pokemon = Pokémon.query.get(id)
    db.session.delete(pokemon)
    db.session.commit()
    return redirect(url_for("home"))