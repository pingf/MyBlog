from wtforms import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from wtforms.csrf.session import SessionCSRF


class LoginForm(Form):
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


