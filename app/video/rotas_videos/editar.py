from app import db
from app.video import video
from app.models import Video
from flask import render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename
import os

def editar_func():
    if request.form: 
       titulo_antigo = request.form.get("titulo_antigo")
       idvideo = request.form.get("idvideo")

       novo_titulo = request.form.get("titulo") 
       nova_descricao = request.form.get("descricao")
   
       video_db = Video.query.filter_by(id = idvideo).first()
       video_db.titulo = novo_titulo
       video_db.descricao = nova_descricao
           #muda valor do registro no db

       db.session.add(video_db)
       db.session.commit()
       
       formatos = request.form.get("formatos").split("/")

       old_video = os.path.join("app/static/assets/videos", titulo_antigo + "." + formatos[0])
       new_video = os.path.join("app/static/assets/videos", novo_titulo + "." + idvideo + "." + formatos[0])
       os.rename(old_video, new_video)
            
       old_thumbnail = os.path.join("app/static/assets/img", titulo_antigo + "." + formatos[1])
       new_thumbnail = os.path.join("app/static/assets/img", novo_titulo + "." + idvideo + "." + formatos[1]) 
       os.rename(old_thumbnail, new_thumbnail)
           #muda nome do vídeo e da thumbnail no diretório especificado
            
       
       return redirect(url_for("video.catalogo", message="video editado com sucesso"))
    return redirect(url_for("video.catalogo", message="deu erro :)"))