from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Length,ValidationError

class RequirementForm(FlaskForm):
    k_skills = StringField('',
                           validators=[DataRequired(), Length(min=2, max=100)])
    t_skills = StringField('',
                           validators=[DataRequired(), Length(min=2, max=100)])
    experience = RadioField('Experience', choices=[('1-3 years','1-3 years'),('3-5 years','3-5 years'),
                                                    ('5+ years','5+ years'),('None','None')],validators=[DataRequired()])
    education = RadioField('', choices=[('SSC','SSC'),('HSC','HSC'),('Graduate','Graduate'),
                                                    ('Post Graduate','Post Graduate'),('PHD','PHD')])  
    refrences = BooleanField('Refrences')
    projects = BooleanField('Projects')
    e_history = BooleanField('Emolyment History')
    carrier_obj = BooleanField('Carrier Objective')
    submit = SubmitField('Next')

class UploadForm(FlaskForm):
        submit = SubmitField('Upload')


    