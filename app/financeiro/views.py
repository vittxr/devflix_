from app.financeiro import financeiro
from app.models import Cartao, User
from flask import request, render_template
from flask_login import current_user

@financeiro.route("/", methods=['GET', 'POST' ])
def planos():
    return render_template("financeiro/planos.html")

@financeiro.route("/pagamento", methods=['GET', 'POST' ])
def dados_cartao():
    novo_cartao = Cartao()
    novo_cartao.nome = request.form.get("nome")
    novo_cartao.numero = request.form.get("n_cartao")
    novo_cartao.validade = request.form.get("validade")
    novo_cartao.user_id = current_user.id

    # cartao_existe = requests.get("https//:cartaoexiste/cartao?nome={novo_cartao.nome}, cc{novo_cartao.numero}") 
      #será preciso verificar se o cartão existe na api que o professor gerou, a qual contém os cartões existentes.

    return redi
    #return render_template("financeiro/dados_cartao.html")

@financeiro.route("/agradecimento")
def agradecimento():
    return render_template("financeiro/agradecimento.html")

#class User(db.Model, UserMixin):
#    __tablename__ = "Users"
#    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
#    contas = db.relationship('Conta', backref="titular")
#    cartoes = db.relationship('Cartao', backref="titular")
#
#    def _init_(self):
#        self.criado_em = datetime.now()
#    def senha(self, valor):
#    def verify_password(self, senha):
#        return check_password_hash(self.senha_hash, senha)
#
#
#class Role(db.Model):
#    __tablename__ = "roles"
#    id = db.Column(db.Integer, primary_key=True)
#    def depositar(self, valor):
#        db.session.commit()
#
#        return {"status": "success", "message": "Depósito efetuado"}
#        return {"status": "error", "message": "Valor inválido"} 
#        return {"status": "error", "message": "Valor inválido"}
#
#    def to_dict(self):
#        return {
#            "id": self.id,
#            "saldo": self.saldo,
#            "titular": self.titular.nome
#        }
#
#
# #main