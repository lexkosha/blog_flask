from flask import Blueprint
from flask import render_template

#Экземпляр класса Блюпринт
post = Blueprint('posts', __name__, template_folder='templates')

@post.route('/')
def index():
    return render_template('posts/index.html')
