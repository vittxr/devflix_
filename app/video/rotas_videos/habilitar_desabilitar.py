import os
import app
from app import db
from app.video import video
from app.models import Video
from flask import render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename

def habilitar_func():
    print("aeeeeeeeeeeeeeeeeee")
    ### -> tentar testar video ...
    videoid = request.args.get("videoid")
    if video: 
        video_db = Video.query.filter_by(id = videoid).first()
        print(video_db.habilitado)
        if video_db.habilitado == 1:
            video_db.habilitado = 0
            db.session.add(video_db)
            db.session.commit()
            return redirect(url_for("video.catalogo", message="video desabilitado com sucesso"))
        else:
            video_db.habilitado = 1
            db.session.add(video_db)
            db.session.commit()
            return redirect(url_for("video.catalogo", message="video habilitado com sucesso"))