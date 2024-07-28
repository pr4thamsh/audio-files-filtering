import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEEPGRAM_API_KEY = os.environ.get('DG_API_KEY')