import os
from supabase import create_client, Client
from supabase.client import ClientOptions
# Establish a connection to Supabase
# Load environment variables
from dotenv import load_dotenv
load_dotenv()
# Load the Supabase URL and Key from environment variables
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(
    url, 
    key,
    options=ClientOptions(
        postgrest_client_timeout=10,
        storage_client_timeout=10,
        schema="public",
    )
)