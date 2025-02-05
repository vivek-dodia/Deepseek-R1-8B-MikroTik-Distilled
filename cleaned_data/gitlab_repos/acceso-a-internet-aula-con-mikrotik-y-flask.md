# Repository Information
Name: acceso-a-internet-aula-con-mikrotik-y-flask

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/jgimenez/acceso-a-internet-aula-con-mikrotik-y-flask.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: app.py
================================================
# coding:utf-8
"""
Poner y quitar acceso a Internet en un aula
Activando/desactivando las reglas de NAT de un router mikrotik
"""
from subprocess import check_output, call
from flask import Flask, render_template, request, url_for
app = Flask(__name__)
@app.route("/", methods=("GET", "POST"))
def index():
    dir_ip_mikrotik="192.168.100.40"
    # Comprobamos si los alumnos tienen acceso a Internet
    estado_binario = check_output('ssh admin@'+dir_ip_mikrotik+' ip firewall nat print count-only  where disabled', shell=True)
    estado=estado_binario.decode('ascii')[0]
    if estado == "0":
        acceso_internet="SI"
        poner_quitar="Quitar acceso a Internet"
    else:
        acceso_internet="NO"
        poner_quitar="Poner acceso a Internet"
    # La primera vez que se carga la página del formulario lo hace con GET
    if request.method == "GET":
        return render_template("index.html",
                               acceso_internet=acceso_internet,
                               poner_quitar=poner_quitar)
    # Cuando el usuario ya ha entrado en el formulario y lo ha enviado con
    # el botón "Submit" se hace con POST
    elif request.method == "POST":
        if estado == "0":
            call('ssh admin@'+dir_ip_mikrotik+' ip firewall nat disable numbers=0', shell=True)
            acceso_internet="NO"
            poner_quitar="Poner acceso a Internet"
        else:
            call('ssh admin@'+dir_ip_mikrotik+' ip firewall nat enable numbers=0', shell=True)
            acceso_internet="SI"
            poner_quitar="Quitar acceso a Internet"
        return render_template("index.html",
                               acceso_internet=acceso_internet,
                               poner_quitar=poner_quitar)
if __name__ == "__main__":
    app.run()
================================================

File: como_instalar_flask.txt
================================================
Crear directorio
mkdir flask
cd flask/
Instalar flask
sudo apt install python3-pip
pip3 install --upgrade pip
pip3 install Flask
Ejecutar el servidor:
    Cada vez desde terminal
            export FLASK_APP=app.py
            export FLASK_ENV=development
            python3 -m flask  run
            Si queremos que el servidor veb sea accesible desde la red, no solo desde 127.0.0.1
            flask run --host=0.0.0.0
    O bien, configurar .flaskenv
        Creamos el archivo .flaskenv
        Añadimos las líneas
            FLASK_APP=app.py
            FLASK_ENV=development
            python3 -m flask  run
            Si queremos que el servidor veb sea accesible desde la red, no solo desde 127.0.0.1
            flask run --host=0.0.0.0
Comprobar en el navegador: http://localhost:5000
Desde otro PC en la red: http://IP-LAN:5000    (EJ: http://192.168.1.35:5000)
================================================

File: site.css
================================================
.body-content {
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: black;
    background-color: rgb(226, 220, 220);
}
.footer-content {
    padding-left: 50px;
    padding-top: 1px;
    padding-bottom: 1px;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-style: italic;
    font-weight: bold;
    color: black;
    background-color: lightblue;
}
================================================

File: index.html
================================================
{% extends "layout.html" %}
{% block title %}
Control acceso a Internet
{% endblock %}
{% block content %}
<form method="post">
    <label for=acceso_internet_label">Acceso Internet: {{ acceso_internet }}</label>
    <br>
    <br>
    <br>
    <input type="submit" value="{{ poner_quitar }}">
    <hr>
</form>
{% endblock %}
================================================

File: layout.html
================================================
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>{% block title %}{% endblock %}</title>
        <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='site.css')}}" />
    </head>
    <body>
        <div class="body-content">
            {% block content %}
            {% endblock %}
            <footer class="footer-content">
                <p>&copy; Joni (TFM) 2021</p>
            </footer>
        </div>
    </body>
</html>
================================================

File: README.md
================================================
# Acceso a Internet aula con mikrotik y flask