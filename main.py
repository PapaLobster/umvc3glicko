import requests
import json
import os
import pysmashgg
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.venv/Startgg_token.env')
load_dotenv(dotenv_path=dotenv_path)

API_Key = os.getenv('Startgg_Token')

