import os
from flask import *
tools = Flask(__name__)
from settings import *
from views import *
from functools import wraps

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    tools.run(debug=True,host='0.0.0.0',port=port)
