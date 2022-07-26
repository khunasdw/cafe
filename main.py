from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from forms import CafeForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/add", methods=["POST", "GET"])
def add():
    cafe_form = CafeForm()
    if cafe_form.validate_on_submit():
        new_cafe = Cafe(name=cafe_form.name.data,
                        map_url=cafe_form.map_url.data,
                        img_url=cafe_form.img_url.data,
                        location=cafe_form.location.data,
                        has_sockets=cafe_form.has_sockets.data,
                        has_toilet=cafe_form.has_toilet.data,
                        has_wifi=cafe_form.has_wifi.data,
                        can_take_calls=cafe_form.can_take_calls.data,
                        seats=cafe_form.seats.data,
                        coffee_price=cafe_form.coffee_price.data)
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('add'))

    return render_template("add.html", form=cafe_form)


@app.route("/")
def home():
    all_cafe = Cafe.query.all()
    # print(all_cafe[0].name, all_cafe[0].location, all_cafe[0].coffee_price)
    return render_template("index.html", all_cafe=all_cafe)


@app.route("/detail/<int:cafe_id>", methods=["POST", "GET"])
def show_detail(cafe_id):
    requested_cafe = Cafe.query.get(cafe_id)
    return render_template("detail.html", cafe=requested_cafe)


if __name__ == "__main__":
    app.run(debug=True)
