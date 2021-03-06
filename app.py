from flask import Flask  # import flask
from flask_restful import Api
from resources.roomResource import *
from resources.containerResource import *
from resources.itemResource import *
from resources.loginResource import *
from flask_cors import CORS
from model.models import db, ma

def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object('config')
    # app.config.from_pyfile('config.py')
    db.init_app(app)
    ma.init_app(app)
    api = Api(app)
    with app.app_context():
        from model.models import Room,Item,Container
        db.create_all()

    CORS(app, resources={r"/*": {"origins": "*"}})

    api.add_resource(AllRoomResource, '/list_rooms')
    api.add_resource(RoomResource, '/room')
    api.add_resource(AllContainerResource, '/list_containers')
    api.add_resource(ContainerResource, '/container')
    api.add_resource(AllItemResource, '/list_items')
    api.add_resource(ItemResource, '/item')
    api.add_resource(NewUserResource, '/new_user')
    api.add_resource(TokenResource, '/token')

    return app


# if __name__ == "__main__":
#     app = create_app()
#     app.run()