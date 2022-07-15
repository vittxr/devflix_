from app.video import video
from app.models import Video
from flask import render_template, request

#@administrador -> O usuário só poderá acessar essa rota se ele tiver a permissão de administrador, mas esse decorar não existe ainda (nao foi pedido na demanda)
def studio_func():
    message = request.args.get("message")
       #message é uma variável que recebe o status do upload/edit. Se ele foi um sucesso, exibe um alerta avisando isso. Caso contrário, o usuário é informado que não deu certo
    if message: 
       return render_template("video/studio.html", message=message)
    return render_template("video/studio.html")  # Renderiza arquivo html pasta templates