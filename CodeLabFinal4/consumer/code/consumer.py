
from flask import Flask,render_template,jsonify
import requests
import json
import random
import os

app = Flask(__name__)

@app.route('/')
def get_reco():
    r =requests.get("http://api.:5000/")
    food_item = r.text
    return render_template('food.html',meal=food_item)
    
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
