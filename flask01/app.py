# test/__init__.py 변경

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config
#flask db init
#flask db migrate
#flask db upgrade

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #
    db.init_app(app)
    migrate.init_app(app,db)
    
    from views import main_views, board_views
    app.register_blueprint(main_views.mbp)
    app.register_blueprint(board_views.mbp2)

    
    return app