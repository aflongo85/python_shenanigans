from flask import Flask
from flask import Flask, jsonify

app = Flask(__name__)

my_stores = [{
        'name': 'My Wonderful Store',
        'id': '0001'
    },
    {
        'name': 'My Super Market',
        'id': '0002'
    }
]

# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# a_new_person = Person("Andrea", 33)

@app.route('/')
def home():
    return "Hello Flask!!!"

@app.route('/store', methods=['POST'])
def create_store():
    pass

@app.route('/store/<string:name>')
def get_store(name):
    return name

@app.route('/store')
def get_stores():
    return jsonify({'stores': my_stores})
    #return jsonify({'persona': a_new_person})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_with_name(name):
    pass

#just test, not in the tutorial
@app.route('/store/<string:name>/<string:item>')
def create_store_with_name_and_item(name, item):
    return "{} - {}".format(name, item)

app.run(port=8080)