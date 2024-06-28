# -*- coding: utf-8 -*-
import os

import click
from flask import Flask, render_template
from flask_wtf.csrf import CSRFError

from pms.blueprints.admin import admin_bp
from pms.blueprints.ajax import ajax_bp
from pms.blueprints.auth import auth_bp
from pms.blueprints.main import main_bp
from pms.blueprints.user import user_bp
from pms.extensions import bootstrap, db, login_manager, mail, dropzone, moment, whooshee, avatars, csrf
from pms.models import Role, User, Photo, Tag, Collect, Permission
from pms.settings import config


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('pms')
    
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errorhandlers(app)
    register_shell_context(app)
    # register_template_context(app)

    return app


def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    dropzone.init_app(app)
    moment.init_app(app)
    whooshee.init_app(app)
    avatars.init_app(app)
    csrf.init_app(app)


def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(ajax_bp, url_prefix='/ajax')


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, User=User, Photo=Photo, Tag=Tag, Collect=Collect)


def register_errorhandlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(413)
    def request_entity_too_large(e):
        return render_template('errors/413.html'), 413

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        return render_template('errors/400.html', description=e.description), 500


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    def init():
        """Initialize PMS."""
        click.echo('初始化数据库...')
        db.create_all()

        Role.init_role()

        click.echo('创建管理员账户...')
        init_admin()

        click.echo('初始化完成！请执行flask run来运行PMS！')


def init_admin():
    admin = User.query.filter_by(name='Administrator').first()
    if admin is not None:
        return
    admin = User(name='Administrator',
                 username='admin',
                 email='pmsadmin2024@126.com',
                 website='https://github.com/Makapic/photo-management-system',
                 confirmed=True)
    admin.set_password('administrator')
    db.session.add(admin)
    db.session.commit()
