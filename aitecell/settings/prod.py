import os
import dj_database_url
from dotenv import load_dotenv
from pathlib import Path

from .base import *

load_dotenv()

DEBUG = False
print("DEBUG", DEBUG)

ALLOWED_HOSTS = ["*", "127.0.0.1", "localhost", "aitecell.herokuapp.com"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {"default": dj_database_url.config(default=os.getenv("DATABASE_URL"))}

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    "http://localhost:3000",
    "https://aitecell.netlify.app",
)
