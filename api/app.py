from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/canva")
def canva():
    return render_template('canva.html')

@app.route("/privacy")
def privacy():
    return render_template('privacy.html')

if __name__ == '__main__':
    app.run(debug=True) 


