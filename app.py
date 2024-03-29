from flask import Flask

app = Flask(__name__)

from flask import render_template, redirect

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/status')
def status():
    return render_template('status.html')

@app.route("/secret")
def secret():
    return redirect("https://balls.org")



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=2510)