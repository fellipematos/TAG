from flask import Flask, render_template, request, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/etiqueta', methods=['GET', 'POST'])
def tag():

    if request.method == 'POST':
        dados = {
            'dnome': request.form['dnome'],
            'dcep': request.form['dcep'],
            'drua': request.form['drua'],
            'dnum': request.form['dnum'],
            'dcom': request.form['dcom'],
            'dbairro': request.form['dbairro'],
            'dcidade': request.form['dcidade'],
            'duf': request.form['duf'],
            'rnome': request.form['rnome'],
            'rcep': request.form['rcep'],
            'rrua': request.form['rrua'],
            'rnum': request.form['rnum'],
            'rcom': request.form['rcom'],
            'rbairro': request.form['rbairro'],
            'rcidade': request.form['rcidade'],
            'ruf': request.form['ruf']
        }
    return render_template('tag.html', result=dados)