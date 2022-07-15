import os
import app
from app import db
from app.video import video
from app.models import Video
from flask import render_template, request, redirect, flash, url_for
from ..utils import allowed_fileV, allowed_fileI
from werkzeug.utils import secure_filename

def upload_func():
    if request.method == 'POST':
        print(request.files)

        video = request.files['video']
        thumbnail = request.files['thumbnail']
           #request.files é um dicionário com os arquivos selecionados no input.       

        """ if 'video' not in video or 'image' not in thumbnail:
            print("2")
            flash('No file part')
            return redirect(request.url) """
        #file = request.files['file']
        if video.filename == '' or thumbnail.filename == '':
            print("3")
            flash('No selected file')
            return redirect(request.url)
        if video and allowed_fileV(video.filename):
            if thumbnail and allowed_fileI(thumbnail.filename):
                titulo = request.form.get("titulo") 
                descricao = request.form.get("descricao")
                   #armazena-se os dados do formulário.

                video_filename_V1 = secure_filename(video.filename)
                #retorna uma versão segura do vídeo
                #..._V1 = versão 1; ..._V2 = versão 2; ...VF = versão final.
                video_filename_V2 = video_filename_V1.split(".") 
                video_filename_V2[0] = titulo 
                video_filename_VF = video_filename_V2[0] + "." + video_filename_V2[1] 
                    #o nome do arquivo (filename) é renomeado, para que tenha o mesmo nome que o titulo escolhido pelo usuário.

                thumbnail_filename_V1 = secure_filename(thumbnail.filename)
                thumbnail_filename_V2 = thumbnail_filename_V1.split(".") 
                thumbnail_filename_V2[0] = titulo 
                thumbnail_filename_VF = thumbnail_filename_V2[0] + "." + thumbnail_filename_V2[1] 

                    #salva o filename (video no caso) na pasta especificada. 

                #commit no banco de dados
                formatos = f"{video_filename_V2[1]}/{thumbnail_filename_V2[1]}"

                new_video = Video(titulo=titulo, formatos=formatos, descricao=descricao)
                db.session.add(new_video)
                db.session.commit()

                ultimo_video_colocado = Video.query.all()[-1]
                print(ultimo_video_colocado.titulo)

                video_filename_VF = video_filename_VF.split(".")[0] + "." + str(ultimo_video_colocado.id) + "." + video_filename_VF.split(".")[1] 

                thumbnail_filename_VF = thumbnail_filename_VF.split(".")[0] + "." + str(ultimo_video_colocado.id) + "." + thumbnail_filename_VF.split(".")[1]
                   #O nome do vídeo e da thumbnail serão o titulo + id, para ser um nome único.

                video.save(os.path.join('app/static/assets/videos', video_filename_VF))
                thumbnail.save(os.path.join('app/static/assets/img', thumbnail_filename_VF))                 
                   #...filename_V2[1] tem a extensão do arquivo. Para ser guardada no banco de dados, é criado uma string, contendo as extensões do mesmo arquivo. 
               
                return redirect(url_for("video.studio", message="Deu certo!"))
                #res = download_file(video_filename_VF, thumbnail_filename_VF)
            else:
                return redirect(url_for("video.studio", message="Formato da thumbnail esperado: jpg ou png"))
        else:
            return redirect(url_for("video.studio", message="Formato do vídeo esperado: mp4"))


    return redirect(url_for("video.studio", message="Erro no upload :/"))
       #caso o upload não dê certo