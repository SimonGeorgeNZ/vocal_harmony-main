import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'vocal_harmony'
app.config["MONGO_URI"] = os.getenv("MONGO_URI") 

mongo = PyMongo(app)

MONGO_URI = os.environ.get('MONGO_URI')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')


@app.route('/', methods=['GET', 'POST'])
def home():
    sel_key = ""
    key_Sig = list(mongo.db.keys.find())
    if request.method == 'POST':
        selected_key = request.form.get('keySig')
        sel_key = mongo.db.keys.find_one({'keySig': selected_key})
        print(sel_key)
    return render_template('index.html', ks=key_Sig, sk=sel_key)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

