from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

bootstrap = Bootstrap()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)

    # Initialize Supabase client
    supabase = config_class.supabase

    # Register blueprints here
    from app.routes import main
    app.register_blueprint(main)

    @app.context_processor
    def inject_supabase():
        return dict(supabase=supabase)

    return app