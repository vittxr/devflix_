import os
import app
from app import db
from app.video import video
from app.models import Video
from flask import render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename

def view_func():
    videoid = request.args.get('videoid')
    if videoid:
        video_selecionado = Video.query.filter_by(id = videoid).first()
        return render_template("video/video.html", video=video_selecionado)
    return redirect(url_for("video.catalogo"))