from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('tutorial.db', check_same_thread=False)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/names/<name>', methods=["GET","POST"])
def names(name):
    if(request.method == "POST"):
        c = conn.cursor()
        name = request.form["name"]
        c.execute(f"SELECT * FROM tutorial WHERE name='{name}'")
        names = c.fetchall()
        print(names)
        c.close()
        return render_template("names.html", names=names)
        
    if(request.method == "GET"):
        c = conn.cursor()
        c.execute(f"SELECT * FROM tutorial WHERE name='{name}'")
        names = c.fetchall()
        print(names)
        c.close()
        return render_template("names.html", names=names)
 
if __name__ == "__main__":
    app.run(port='5000', debug=True)

