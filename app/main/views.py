# Inicio import
from app.main import main

# Luiz Roberto: Importes desnecessarios estão a ser feitos
#from flask import Flask, render_template, request, flash, redirect, url_for, make_response

# Correção dos importes 14/06/2022
from flask import render_template
# Termino import

@main.route("/", methods=['GET','POST']) # Rota index em desenvolvimento
def index():
    return render_template("base.html")  # Renderiza arquivo html pasta templates