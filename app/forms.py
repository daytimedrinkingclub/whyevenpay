from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, URLField, SubmitField
from wtforms.validators import DataRequired, URL, Length

class ToolSubmissionForm(FlaskForm):
    name = StringField('Tool Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=500)])
    website = URLField('Website', validators=[DataRequired(), URL()])
    category = StringField('Category', validators=[DataRequired(), Length(max=50)])
    free_features = TextAreaField('Free Features', validators=[DataRequired()])
    paid_features = TextAreaField('Paid Features')
    why_pay = TextAreaField('Why Pay')
    submit = SubmitField('Submit Tool')
