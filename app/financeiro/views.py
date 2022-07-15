from app.financeiro import financeiro
from flask import request, render_template

@financeiro.route("/", methods=['GET', 'POST' ])
def planos():
    return render_template("financeiro/planos.html")

@financeiro.route("/pagamento", methods=['GET', 'POST' ])
def dados_cartao():
    nome = request.form.get("nome")
    n_cartao = request.form.get("n_cartao")
    validade = request.form.get("validade")
    cvc = request.form.get("cvc")
    return render_template("financeiro/dados_cartao.html")

@financeiro.route("/agradecimento")
def agradecimento():
    return render_template("financeiro/agradecimento.html")