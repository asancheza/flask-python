#!/usr/bin/python
from flask import Flask, render_template, json, request
from flask.ext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

#app.config['MYSQL_DATABASE_USER'] = 'root'
app.config["MYSQL_DATABASE_PASSWORD"] = ""
app.config["MYSQL_DATABASE_DB"] = "BucketList"
app.confifg["MYSQL_DATABASE_HOST"] = "localhost"
mysql.init_app(app)


@app.route("/")
def main(): 
  return render_template("index.html")

@app.route("/showSignup")
def showSignup():
  return render_template("signup.html")

@app.route("/signup", methods["POST"])
def signup():
  _name = request.form["name"]
  _email = request.form["email"]
  _pass = request.form["pass"]

  if _name and _email and _pass:
    return json.dumps({'html': "All fields are good"})
  else:
    return json.dumps({'html': "Fields are required"})

if __name__ == "__main__":
      app.run()
