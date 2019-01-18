from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from web.app import mongo




class TeamForm(FlaskForm):
    # team_name = SelectField('Nombre del equipo', choices=[(country['name']) for country in countries], validators=[DataRequired()])
    flag_image = StringField('Bandera del equipo', validators=[DataRequired()])
    team_emblema = StringField('Escudo del equipo', validators=[DataRequired()])