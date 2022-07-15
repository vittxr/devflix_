from app.video import video
from app.models import Video
from flask import render_template

def catalogo_func():
    videos = Video.query.all() #Caminhos para o vídeos
    return render_template("video/catalogo.html", videos=videos)
     
        # Renderiza arquivo html pasta templates