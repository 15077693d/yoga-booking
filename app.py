from flask import Flask, render_template
from model.pureDriver import PureDriver
import os
app = Flask(__name__)
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__),"templates")
STATIC_DIR = os.path.join(os.path.dirname(__file__),'static')
config_path = os.path.join(os.path.dirname(__file__),'resources/config.json')
log_path = os.path.join(os.path.dirname(__file__),'resources/log')
tool = PureDriver(config_path, log_path)
@app.route('/')
def home():
    return render_template('table.html')


if __name__ == '__main__':
    app.run()
