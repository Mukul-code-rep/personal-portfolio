from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Top-Secret-Key'
Bootstrap(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/experience')
def experience():
    return render_template("experience.html")


@app.route('/project')
def project():
    return render_template("projects.html")


@app.route('/research')
def research():
    return render_template("research.html")


@app.route('/resume')
def resume():
    return send_from_directory('static/', 'Periwal_Resume.pdf')


if __name__ == "__main__":
    app.run(debug=True, port=5004)
