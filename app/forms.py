from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Optional
from app.data_service import get_categories

class AdminLoginForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ToolSubmissionForm(FlaskForm):
    name = StringField('Tool Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    website = StringField('Website URL', validators=[DataRequired(), URL()])
    category = SelectField('Category', validators=[DataRequired()], coerce=int)
    free_features = TextAreaField('Free Features', validators=[DataRequired()])
    paid_features = TextAreaField('Paid Features', validators=[Optional()])
    why_pay = TextAreaField('Why Pay?', validators=[Optional()])
    why_not_pay = TextAreaField('Why Not Pay?', validators=[Optional()])
    when_to_pay = TextAreaField('When to Pay?', validators=[Optional()])
    submitted_by = StringField('Your Email', validators=[DataRequired(), Email()])
    logo_public_url = StringField('Logo URL', validators=[Optional(), URL()])
    submit = SubmitField('Submit Tool for Review 🚀')

    def __init__(self, *args, **kwargs):
        super(ToolSubmissionForm, self).__init__(*args, **kwargs)
        self.category.choices = [(cat['id'], cat['name']) for cat in get_categories()]
