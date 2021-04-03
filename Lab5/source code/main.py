from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    name=searchName()
    return render_template('boton.html',valor=name)

def searchName():
    print("Presiona el botón para generar un nombre aleatorio")
    names = []
    with open ("/home/jurodriguezf/mysite/names.txt") as f:
        names = f.readlines()
    rand = random.randint(0,len(names))
    return names[rand]