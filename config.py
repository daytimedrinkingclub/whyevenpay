import os
from dotenv import load_dotenv
from supabase import create_client
from urllib.parse import urlparse

# Load environment variables from .env file
load_dotenv()

class Config:
    # Supabase settings
    SUPABASE_URL = os.environ.get('SUPABASE_URL')
    SUPABASE_PUBLIC_KEY = os.environ.get('SUPABASE_PUBLIC_KEY')
    SUPABASE_PRIVATE_KEY = os.environ.get('SUPABASE_PRIVATE_KEY')
    
    # Extract the host from the PostgreSQL connection string
    if SUPABASE_URL and SUPABASE_URL.startswith('postgres://'):
        parsed_url = urlparse(SUPABASE_URL)
        SUPABASE_URL = f'https://{parsed_url.hostname}'
    
    # Check if SUPABASE_URL is a valid URL
    if SUPABASE_URL and not SUPABASE_URL.startswith(('http://', 'https://')):
        SUPABASE_URL = f'https://{SUPABASE_URL}'
    
    # Create Supabase client with public key for general use
    supabase = create_client(SUPABASE_URL, SUPABASE_PUBLIC_KEY)
    print("Supabase client created with public key", supabase)
    # Create Supabase client with private key for admin operations
    supabase_admin = create_client(SUPABASE_URL, SUPABASE_PRIVATE_KEY)
    print("Supabase client created with private key", supabase_admin)
    # Flask-WTF settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Add any other configuration settings here
