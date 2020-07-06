from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index1():
    return render_template("index1.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run()