from datetime import date, datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length
from wtforms.widgets import PasswordInput



# WTF form as in the documentation https://python-adv-web-apps.readthedocs.io/en/latest/flask_forms.html
class BookingForm(FlaskForm):
    
    name = StringField('Your name', validators=[DataRequired(), Length(2, 12)])
    email = StringField('Your email', validators=[DataRequired(), Email()])
    booking_date = StringField('Which day?', validators=[DataRequired()])
    #opening time choice 
    opening_time = [('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00')]
    time = SelectField('What time?', choices=opening_time, validators=[DataRequired()])
    # Table selection, four tables
    tables = [(1, '1'), (2, '2'), (3, '3'), (4, '4')]
    table_num = SelectField('Choose a table', choices=tables, validators=[DataRequired()])
    submit = SubmitField('Book now')
    
    
class AdminLogin(FlaskForm):
    user = StringField('User name', validators=[DataRequired(), Length(2, 12)])
    password = StringField('Password', widget=PasswordInput(hide_value=False))
    submit = SubmitField('Edit bookings')

