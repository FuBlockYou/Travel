#coding:utf-8

from flask import Flask
from  flask_sqlalchemy import SQLAlchemy
from  config import config

#创建数据库对象
db = SQLAlchemy()
def create_app(config_name):
    #加载配置文件
    app = Flask(__name__)
    app.config.from_object(config[config_name])    #模块下配置文件名
    config[config_name].init_app(app)
    db.init_app(app)

    #注册蓝图
    from app.home import home as home_blueprint
    # from app.admin import admin as admin_blueprint
    app.register_blueprint(home_blueprint)
    # app.register_blueprint(admin_blueprint, url_prefix="/admin")
    return app
