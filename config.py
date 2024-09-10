import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SUPABASE_URL = os.environ.get('SUPABASE_URL')
    SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
    LOGO_DEV_PUBLIC_KEY = os.environ.get('LOGO_DEV_PUBLIC_KEY')
    LOGO_DEV_API_KEY = os.environ.get('LOGO_DEV_API_KEY')
