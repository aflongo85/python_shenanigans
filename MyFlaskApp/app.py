from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Flask!!!"

@app.route('/store', methods=['POST'])
def create_store():
    pass

@app.route('/store/<string:name>')
def get_store(name):
    return name

@app.route('/store/<string:name>/item', methods=['POST'])
def create_store(name):
    pass


app.run(port=5000)