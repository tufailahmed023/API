import pymongo

client = pymongo.MongoClient("mongodb+srv://tufail:shaikhahmed@cluster0.q6hm0vv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
from flask import Flask , request,jsonify
app = Flask(__name__)

database = client['taskdb']
collection= database['taskcollection']

@app.route("/insert/mongo" , methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name:number})
        return jsonify(str("succefully inserted "))

if __name__=='__main__':
    app.run()