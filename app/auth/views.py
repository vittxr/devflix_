# Inicio import
from app.auth import auth 

# Luiz Roberto: Importes desnecessarios estão a ser feitos
#from flask import Flask, render_template, request, flash, redirect, url_for, make_response

# Correção dos importes 14/06/2022
from flask import render_template, url_for, redirect
# Termino Import

@auth.route("/login") # Rota de login
def login():  
    return render_template("login.html") # Renderiza arquivo html pasta templates

# Luiz Roberto: Rota /registro deve estar definida com 'GET' e 'POST'
#@auth.route('/registro') # Rota de registro

# Correção da rota de registro 14/06/2022
@auth.route('/registro') 
def registro():
    return render_template("register.html")  # Renderiza arquivo html pasta templates


@auth.route("/logout") # Rota de logout
def logout():  

    # Luiz Roberto: deveria está sendo utilizado return redirect(url_for()) e não 
    #return render_template("login.html")  

    # Correção do return 14/06/2022
    return redirect(url_for('auth.login'))  # Renderiza arquivo html pasta templates

