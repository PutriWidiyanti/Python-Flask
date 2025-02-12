from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/konsep-basis-data')
def about():
    return render_template('konsep-basis-data.html')

@app.route('/erd-layanan-kesehatan-digital')
def contact():
    return render_template('erd-layanan-kesehatan-digital.html')

@app.route('/flask')
def profile():
    return render_template('flask.html')

@app.route('/jinja')
def vision_mission():
    return render_template('jinja.html')

if __name__ == '__main__':
    app.run(debug=True)
