from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    name = StringField("cafe name", validators=[DataRequired()])
    map_url = StringField("map_url", validators=[DataRequired()])
    img_url = StringField("img_url", validators=[DataRequired()])
    location = StringField("location", validators=[DataRequired()])
    seats = StringField("seats")
    coffee_price = StringField("coffee_price", validators=[DataRequired()])
    has_sockets = BooleanField("has_sockets", validators=[DataRequired()])
    has_toilet = BooleanField("has_toilet", validators=[DataRequired()])
    has_wifi = BooleanField("has_wifi", validators=[DataRequired()])
    can_take_calls = BooleanField("can_take_calls", validators=[DataRequired()])

    submit = SubmitField("Add Cafe")
