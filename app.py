from flask import Flask,render_template,request
from database import database

# blueprint import
from apps.admin.views import admin
from apps.monitor.views import monitor
def create_app():
    app=Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    database.init_app(app)
    app.register_blueprint(admin)
    app.register_blueprint(monitor,url_prefix="/monitor")
    return app

if __name__ == "__main__":
    create_app().run()
