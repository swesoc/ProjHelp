

from models import *

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.app_context().push()

db.init_app(app)
db.create_all()

