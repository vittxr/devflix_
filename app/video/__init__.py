from flask import Blueprint # Import biblioteca

video = Blueprint('video', __name__) # Cria planta de interface 

from app.video import views  # Import views