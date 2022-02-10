import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv("DEBUG", "False") == "True"

try:
    if DEBUG:
        from .dev import *
    else:
        from .prod import *
except ImportError:
    pass
