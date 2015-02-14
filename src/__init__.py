from flask import Flask

app = Flask(__name__)
app.config.from_object('src.config')
app.url_map.strict_slashes = False



from src.helper import *
from src.models import *

from src.pages import *

app.register_blueprint(simple_page)
app.register_blueprint(user_page)
app.register_blueprint(posts_page)


