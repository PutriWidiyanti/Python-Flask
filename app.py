from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/visi-misi')
def vision_mission():
    return render_template('visi-misi.html')

@app.route('/card-title1')
def card_title1():
    return render_template('card-title1.html')

if __name__ == '__main__':
    app.run(debug=True)
