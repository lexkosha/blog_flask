from flask import Flask
from config import Configuration

from posts.blueprint import post


app = Flask(__name__)

#Передаем настройки из обьекта config
app.config.from_object(Configuration)

#регистрируем экземпляр класса Blueprint
app.register_blueprint(post, url_prefix='/blog')
