import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, make_response
from werkzeug.utils import secure_filename

####-> Upload de video:
ALLOWED_EXTENSIONS = {'jpeg', 'png', 'jpg'}
ALLOWED_EXTENSIONSV = {'mp4'}


def allowed_fileV(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONSV

def allowed_fileI(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


