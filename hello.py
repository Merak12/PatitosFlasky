from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class ArbolinForm(FlaskForm):
    value = StringField('Cambia tu variable a tres pesos', validators=[DataRequired()])
    submit = SubmitField('Submit')

class IBMForm(FlaskForm):
    gender = RadioField('¿Cuál es tu género?', choices=[('m','Masculino'), ('f','Femenino'),('o', 'Otro')])
    height = IntegerField('¿Cuánto mides en centímetros?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

@app.route('/IBMCalculator', methods=['GET', 'POST'])
def IBMFunct():
    form = IBMForm()
    ibm = None
    if form.validate_on_submit():
        gender = form.gender.data
        height = form.height.data
        form.gender.data = ''
        form.height.data = 0
        if gender == 'm':
            ibm = 50 + 0.91 * (height - 152.4)
        elif gender == 'f':
            ibm = 45.5 + 0.91 * (height - 152.4)
        else:
            ibm = "No tengo una fórmula en tu caso"
    return render_template('IBMCalculator.html', form=form, ibm=ibm)

@app.route('/anaBanana', methods=['GET', 'POST'])
def AnaFuncc():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('anaBanana.html', form=form, name=name)    

@app.route('/arbolin/<variable>', methods=['GET', 'POST'])
def AlvaroFunct(variable):
    form = ArbolinForm()
    if form.validate_on_submit():
        new_variable = form.value.data
        return redirect(url_for('AlvaroFunct', variable=new_variable))
    return render_template('alvaro.html', variable=variable, form=form)

@app.route('/anaBanana', methods=['GET', 'POST'])
def AnaFunct():
    return render_template('anaBanana.html')