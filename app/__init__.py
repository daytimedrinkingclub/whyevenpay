from flask import Flask
from flask_bootstrap import Bootstrap
from supabase import create_client, Client
from config import Config

bootstrap = Bootstrap()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    bootstrap.init_app(app)

    # Initialize Supabase client
    app.supabase: Client = create_client(app.config['SUPABASE_URL'], app.config['SUPABASE_KEY'])

    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app