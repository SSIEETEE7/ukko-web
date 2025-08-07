from flask import Flask, render_template

app = Flask(__name__, static_folder='static', static_url_path='/static')

# Home
@app.route('/')
def home():
    return render_template('index.html')

# Categorías (los nombres de función DEBEN coincidir con url_for(...) del index)
@app.route('/sports')
def sports():
    return render_template('category.html',
                           title='UKKO SPORTS',
                           subtitle='Proteínas, Bebidas')

@app.route('/care')
def care():
    return render_template('category.html',
                           title='UKKO CARE',
                           subtitle='Cuidado de la piel, Shampoos')

@app.route('/real-food')
def real_food():
    return render_template('category.html',
                           title='UKKO REAL FOOD',
                           subtitle='Comida, Snacks, Agua')

@app.route('/casa')
def casa():
    return render_template('category.html',
                           title='UKKO CASA',
                           subtitle='Detergentes, Aromatizantes')

@app.route('/essence')
def essence():
    return render_template('category.html',
                           title='UKKO ESSENCE',
                           subtitle='Aromaterapia')
