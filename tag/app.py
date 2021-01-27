from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/etiqueta', methods=['GET', 'POST'])
def tag():
    if request.method == 'POST':
        result = {
                'Dnome': request.form['Dnome'],
                'Dcep': request.form['Dcep'],
                'Dendereco': request.form['Dendereco'],
                'Dnum': request.form['Dnum'],
                'Dcomplemento': request.form['Dcomplemento'],
                'Dbairro': request.form['Dbairro'],
                'Dcidade': request.form['Dcidade'],
                'Destado': request.form['Destado'],
                'Rnome': request.form['Rnome'],
                'Rcep': request.form['Rcep'],
                'Rendereco': request.form['Rendereco'],
                'Rnum': request.form['Rnum'],
                'Rcomplemento': request.form['Rcomplemento'],
                'Rbairro': request.form['Rbairro'],
                'Rcidade': request.form['Rcidade'],
                'Restado': request.form['Restado']
            }

    return render_template('tag.html', result=result)
    