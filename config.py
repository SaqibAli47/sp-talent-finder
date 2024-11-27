import os

from dotenv import load_dotenv

load_dotenv()

AZURE_AI_SEARCH_KEY = os.getenv("AZURE_AI_SEARCH_KEY", "")
AZURE_AI_SEARCH_INDEX = os.getenv("AZURE_AI_SEARCH_INDEX", "")
AZURE_AI_SEARCH_ENDPOINT = os.getenv("AZURE_AI_SEARCH_ENDPOINT", "")
OPENAI_API_TYPE = os.getenv("OPENAI_API_TYPE", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "")
OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION", "")
OPENAI_API_MODEL = os.getenv("OPENAI_API_MODEL", "gpt-4o")
OPENAI_API_MAX_TOKENS = int(os.getenv("OPENAI_API_MAX_TOKENS", 1000))
OPENAI_API_TEMPERATURE = float(os.getenv("OPENAI_API_TEMPERATURE", 0.1))
OPENAI_API_TOP_P = float(os.getenv("OPENAI_API_TOP_P", 0.9))
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "")
NO_OF_CONTEXT=int(os.getenv("NO_OF_CONTEXT", 11))
DEFAULT_USER = os.getenv("DEFAULT_USER", "admin")
USER_PASSWORD = os.getenv("USER_PASSWORD", "admin")

CLIENT_ID=os.getenv("CLIENT_ID", "")
CLIENT_SECRET=os.getenv("CLIENT_SECRET", "")

SQL_SERVER = os.getenv("SQL_SERVER", "")
SQL_DATABASE = os.getenv("SQL_DATABASE", "")
SQL_UID = os.getenv("SQL_UID", "")
SQL_PWD = os.getenv("SQL_PWD", "")
OPENAI_INSTRUCTIONS_IN_GERMAN=os.getenv("OPENAI_INSTRUCTIONS_IN_GERMAN", "")
NO_OF_SEARCH_RESULTS=int(os.getenv("NO_OF_SEARCH_RESULTS", 7))
LOGOUT_REDIRECT_URL=os.getenv("LOGOUT_REDIRECT_URL", "https://sp-talent-finder-app-dev.azurewebsites.net/")
REDIRECT_URI=os.getenv("REDIRECT_URI", "https://sp-talent-finder-app-dev.azurewebsites.net/microsoft/auth-callback")