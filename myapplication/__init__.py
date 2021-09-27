import os.path
import os
from flask import Flask, app, render_template, make_response, jsonify
from flask_login import LoginManager, login_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_migrate import Migrate
from pathlib import Path
from flask_restful import Api, Resource


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
basedir = Path(__file__).parent.absolute()


def create_app():
    app = Flask(__name__)
    api = Api(app)
    #engine = create_engine('sqlite:///db.sqlite')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config.from_mapping(SECRET_KEY='dev')
    # app.permanent_session_lifetime = timedelta(minutes=20)
    #bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from myapplication.models import Recipes, Opinions, Users, BlackListToken

    create_database(app)

    login_manager.login_view = 'views.home'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    from myapplication.auth.api import RegisterApi
    api.add_resource(RegisterApi, '/api/register')

    from myapplication.auth.api import LoginApi
    api.add_resource(LoginApi, '/api/login')

    from myapplication.auth.api import UserAPI
    api.add_resource(UserAPI, '/api/status')

    from myapplication.recipes.api import RecipesApi
    api.add_resource(RecipesApi, '/api/recipes')

    from myapplication.recipes.api import RecipeApiByID
    api.add_resource(RecipeApiByID, '/api/recipesbyid')

    from myapplication.recipes.api import DeleteRecipeAPI
    api.add_resource(DeleteRecipeAPI, '/api/recipesdelete')

    from myapplication.auth.api import LogoutAPI
    api.add_resource(LogoutAPI, '/api/logout')

    from myapplication.opinions.api import OpinionsApi
    api.add_resource(OpinionsApi, '/api/opinions')

    from myapplication.opinions.api import OpinionsApiByID
    api.add_resource(OpinionsApiByID, '/api/opinionsbyid')

    from myapplication.views import home as bp_home
    app.register_blueprint(bp_home)

    from myapplication.users import users as bp_users
    app.register_blueprint(bp_users)

    return app


def create_database(app):
    db.create_all(app=app)
