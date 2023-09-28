from flask import Flask, jsonify, request 
from flask_restful import Api, Resource

app = Flask(__name__) 


# using flask jsonify object 

@app.route('/returnjson', methods = ['GET'])
def returnJSON():
    if request.method == 'GET':
        data = {
            "Modules":15,
            "Subject":"Data structures and algorithms",
        }
        return jsonify(data)
    

# using the flask_restful library with flask 
api = Api(app)

class returnjson2(Resource):
    def get(self):
        data = {
            "Modules": 16,
            "Subject":"Data structures and algorithms"
        }
        return data 

api.add_resource(returnjson2,'/returnjson2')

if __name__ == '__main__':
    app.run(debug = True)


