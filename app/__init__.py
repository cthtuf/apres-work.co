from flask import Flask
from flask.ext.mobility import Mobility

app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')
Mobility(app)
from app import views

app.secret_key = 'fsd98UI@JHDSA^%!&*(DSOIAUHBCNXZ289eda78uih2ed*(SA'

if __name__ == "__main__":
    app.run(debug=True)
