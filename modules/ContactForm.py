from flask_wtf import FlaskForm 
from wtforms import StringField, EmailField, TextAreaField
from wtforms.validators import InputRequired 
from werkzeug.security import generate_password_hash 

class ContactForm(FlaskForm):

	name_atributtes = {
		"type":"text",
		"class":"form-control", 
		"id":"name"
	}

	email_atributtes = {
		"type":"email", 
		"class":"form-control",
		"id":"email"
	}

	subject_atributtes = {
		"type":"text",
		"class":"form-control",
		"id":"subject"
	}

	message_atributtes = {
		"class":"form-control",
		"rows":"14"
	}

	name = StringField('Name', validators=[InputRequired()],
						render_kw = name_atributtes)
	email = EmailField('Email', validators=[InputRequired()],
						render_kw = email_atributtes)
	subject = StringField('Subject', validators=[InputRequired()],
					       render_kw = subject_atributtes)
	message = TextAreaField('Message', validators=[InputRequired()],
						 	render_kw = message_atributtes)