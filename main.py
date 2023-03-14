from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  return render_template('home.html')


@app.route("/page1.html")
def gents():
  return render_template('page1.html')


@app.route("/page2.html")
def ladies():
  return render_template('page2.html')


@app.route("/page3.html")
def kids():
  return render_template('page3.html')


@app.route("/contact.html")
def contact():
  return render_template('contact.html')


app.run(host='0.0.0.0', debug=True)
