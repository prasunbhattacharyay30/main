from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/work")
def work():
    return render_template('work.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/canva")
def canva():
    return render_template('canva.html')

if __name__ == '__main__':
    app.run(debug=True)


