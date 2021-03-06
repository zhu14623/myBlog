# coding=utf-8
import os
from flask import Flask
from flask_login import current_user
# from flask_sqlalchemy import SQLAlchemy
from flask import redirect,url_for
from flask_cors import CORS

from app.common.db import db
from app.common.extensions import bcrypt
from app.common.extensions import openid
from app.common.extensions import login_manager
# from app.common.extensions import principals
# from app.common.extensions import Bootstrap
# from app.common.extensions import flask_celery
from app.common.extensions import mail
from app.common.extensions import cache
# from app.common.extensions import assets_env
# from app.common.extensions import main_js
# from app.common.extensions import main_css
from app.common.extensions import restful_api
#from app.common import MyResponse

from flask_principal import identity_loaded, UserNeed, RoleNeed
from config import config


# db = SQLAlchemy()


def create_app(config_name):
    """Create the app instance via `Factory Method`"""

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    db.init_app(app)
    #db.app = app

    #Access-Control-Allow-Origin
    CORS(app, supports_credentials=True)

    # Init the Flask-Bcrypt via app object
    bcrypt.init_app(app)

    # Init the Flask-OpenID via app object
    openid.init_app(app)

    # Init the Flask-Login via app object
    login_manager.init_app(app)

    # Init the Flask-mail via app object
    mail.init_app(app)

    # from app.api.apis import CommentApi
    # restful_api.add_resource(
    #     CommentApi,
    #     '/v1/comments',
    #     '/v1/comments/<string:id>')
    # restful_api.init_app(app)
    # Init the Flask-Cache via app object
    cache.init_app(app)

    # Will be callback on_reminder_save when insert recond into table `reminder`.
    #event.listen(Reminder, 'after_insert', on_reminder_save)
    # 注册蓝本
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint,url_prefix='/main')

    from app.post import post as post_blueprint
    app.register_blueprint(post_blueprint, url_prefix='/post')

    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    from app.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    # @identity_loaded.connect_via(app)
    # def on_identity_loaded(sender, identity):
    #     """Change the role via add the Need object into Role.
    #
    #        Need the access the app object.
    #     """
    #
    #     # Set the identity user object
    #     identity.user = current_user
    #
    #     # Add the UserNeed to the identity user object
    #     if hasattr(current_user, 'id'):
    #         identity.provides.add(UserNeed(current_user.id))
    #
    #     # Add each role to the identity user object
    #     if hasattr(current_user, 'roles'):
    #         for role in current_user.roles:
    #             identity.provides.add(RoleNeed(role.name))

    # 附加路由和自定义的错误页面
    @app.route('/')
    def root():
        return redirect(url_for('main.index'))


    return app

