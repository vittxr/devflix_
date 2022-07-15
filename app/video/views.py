#### -> TASKS: 
    # - fazer a modal do jonh cena!!!!!! pam !!!! param !!!!! pam !!!!!!!!!!!!!!!!e do vídeo      ndo dar upload, a message fica armazenada e sendo repitida no alert
    #Icio import
from  app.video import video
from .rotas_videos import *

# Luiz Roberto: Importes desnecessarios estão a ser feitos
#from flask import Flask, render_template, request, flash, redirect, url_for, make_response

# Correção dos importes 14/06/2022
from flask import render_template
# Termino import
#@
@video.route("/") # Rota catálogo de videos.
#@loguin_required
def catalogo():
    return catalogo_func()
        # Renderiza arquivo html pasta templates

@video.route("/studio", methods=['GET', 'POST']) # Rota de alteração/upload de vídeos.
#@loguin_required
#@criar_required (ou outra permissão de upload de arquivos)
def studio():
    return studio_func()

@video.route("/view")
#@loguin_required
def view():
    return view_func()

##-> upload de video:
@video.route('/upload', methods=['GET', 'POST']) #upload de video
#@loguin_required
#@criar_required (ou outra permissão de upload de arquivos)
def upload_file():
    return upload_func()


@video.route('/habilitar_video')
#@loguin_required
#@desbilitar_required (ou outra permissão de upload de arquivos/modificar o bnanco de ados)
def habilitar_video():
    return habilitar_func()

@video.route("/editar_video", methods=['GET', 'POST'])
#@loguin_required
#@criar_required (ou outra de upload de arquivos)
def editar_video():
    return editar_func()
