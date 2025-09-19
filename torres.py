from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("torres.html")

@app.route("/about")
def about():
    return render_template("abouttorres.html")
    
@app.route("/myportfolio")
def myportfolio():
    return render_template("torresportfolio.html")

if __name__ == '__main__':
    app.run(debug=True)