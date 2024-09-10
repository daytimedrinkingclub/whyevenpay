import os
from dotenv import load_dotenv
from supabase import create_client

# Load environment variables from .env file
load_dotenv()

class Config:
    # Supabase settings
    SUPABASE_URL = os.environ.get('SUPABASE_URL')
    SUPABASE_PUBLIC_KEY = os.environ.get('SUPABASE_PUBLIC_KEY')
    SUPABASE_PRIVATE_KEY = os.environ.get('SUPABASE_PRIVATE_KEY')
    
    # Check if SUPABASE_URL is a valid URL
    if SUPABASE_URL and not SUPABASE_URL.startswith(('http://', 'https://')):
        SUPABASE_URL = f'https://{SUPABASE_URL}'
    
    # Create Supabase client with public key for general use
    supabase = create_client(SUPABASE_URL, SUPABASE_PUBLIC_KEY)

    # Create Supabase client with private key for admin operations
    supabase_admin = create_client(SUPABASE_URL, SUPABASE_PRIVATE_KEY)

    # Flask-WTF settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Add any other configuration settings here
