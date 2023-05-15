from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    from .models import db
    from .models.todo import Todo
    db.init_app(app)

    with app.app_context():
        db.create_all()
        db.session.commit()

    from .views.routes import api
    app.register_blueprint(api)

    return app
