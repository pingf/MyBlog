from flask import Flask

app = Flask(__name__)
app.config.from_object('src.config')

app.url_map.strict_slashes = False

from src.helper import *
from src.models import *

