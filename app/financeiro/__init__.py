from flask import Blueprint

financeiro = Blueprint("financeiro", __name__)

from app.financeiro import views