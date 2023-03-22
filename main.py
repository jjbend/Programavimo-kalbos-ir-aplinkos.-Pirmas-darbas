from flask import Flask, render_template,request
import sqlite3
app = Flask(__name__,static_url_path='')
variable=0
array = []

@app.route("/")
def mano_funkcija():
    return ("Labas")

@app.route("/test")
def test_route():
    if (request.args.get("name")):
        plus_one()
    return render_template('./index.html', var=plus_one())

@app.route("/debug")
def plus_one():
    global variable
    variable = variable +1
    return str(variable)
    

@app.route("/notes",methods=["GET","POST"])
def notes():

    if(request.method == "POST"):
        global array
        args=request.form.get("note2")
        if (args):
            array.append(args)
            print(array)
        return render_template('./notes.html', note=array)
    else:
        
       return render_template('./notes.html',note=array)
def add_to_array():
    array = []


    def createDB():
        connection=sqlite3.connect("C:\\Users\\1538822\\Desctop\\NotesDatabase.db")
        cursor=connection.cursor()

        createTableString= """CREATE TABLE IF NOT EXISTS Sheets (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL
        )"""
        
        cursor.execute(createTableString)

if __name__ =="__main__":
    
    app.run(host='0.0.0.0', port=5000, debug="true")



