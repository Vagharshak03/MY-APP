from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/ima')
def ima():
    return render_template('ima.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8485', debug=True)
