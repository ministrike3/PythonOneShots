#The class is Flask
from flask import Flask,jsonify,request

#__name__ tells Flask its a new page, dw about it rn
app = Flask(__name__)
stores = [
    {
        'name': 'MyAmazingStore',
        'items': [
            {
            'name': 'MyItem',
            'price': 15.99
            }
        ]
    }
]

# / is the home page of the page
#Remember the @ sign is a decorator
#POST - use to receive some data
#GET - send some data

#POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return(jsonify(new_store))

#GET /store/<string:name>
@app.route('/store/<string:name>',)
def get_store(name):
    for store in stores:
        if store['name']==name:
            return(jsonify(store))
    return(jsonify({'message': 'store not found'}))

#GET /store
@app.route('/store')
def get_stores():
    return(jsonify({'stores':stores}))

#POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name']==name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return(jsonify(new_item))
        return(jsonify({'message': 'store not found'}))
#GET /store/<string:name>/item
@app.route('/store/<string:name>/item',)
def get_item_in_store(name):
    for store in stores:
        if store['name']==name:
            return(jsonify(store['items']))
    return(jsonify({'message': 'store not found'}))


#define a port, for now 5000
app.run(port=5000)
# you can access this at http://127.0.0.1:5000/
