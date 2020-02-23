from flask import Flask
from flask_dropzone import Dropzone

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_REDIRECT_VIEW'] = 'dashboard'
dropzone = Dropzone(app)


from cvs import routes