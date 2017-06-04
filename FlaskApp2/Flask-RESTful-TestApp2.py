from flask import Flask,request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'neil'
api = Api(app)

jwt=JWT(app, authenticate, identity) #/auth

items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        #for item in items:
        #    if item['name']==name:
        #        return(item)
        #This next line does all of the next 3
        item = next(filter(lambda x: x['name']==name,items), None)
        #filter function returns a filter object with all things matching the lambda
        #you can use list()to turn a filter object into a list
        #or next()to return the first item and then keep calling next for the next one
        #next()can also break it; that why put , None if nothing exists
        return({'item': item}), 200 if item else 404 #404 is not found

    def post(self, name):
        if next(filter(lambda x: x['name']==name,items), None) is not None:
            return({'message': "An item with name '{}' already exists.".format(name)}, 400)
        data = request.get_json()
        #force=True will force the content to be read as json even if not set
        #silent=True will not throw an error; it will just return null if error
        item = {'name':name, 'price': data['price']}
        items.append(item)
        return item, 201 #201 is an ok, its made

    def delete(self,name):
        global items
        items = list(filter(lambda x: x['name'] != name,items))
        return({'message': 'Item deleted'})

    def put(self,name):
        parser= reqparse.RequestParser()
        parser.add_arguement('price',type=float,required=True,help="This Field cannot be left blank")
        data = parser.parse_args()
        item = next(filter(lambda x: x['name'] == name,items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item



class ItemList(Resource):
    def get(self):
        return({'items': items})


api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
app.run(port=5000, debug= True)
