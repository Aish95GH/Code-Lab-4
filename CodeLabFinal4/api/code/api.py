from random import random
from flask import Flask
import os
import random

app = Flask(__name__)

meals = [{'Name':'Margherita pizza','price':'$20'},
        {'Name':'Speghetti pasta','price':'$25'},
        {'Name':'Anti-pasta','price':'$12'},
        {'Name':'Bruscheta','price':'$12'},
        {'Name':'Caesar salad','price':'$15'},
        {'Name':'MUSHROOM RAVIOLI AL FORNO','price':'$29'},
        {'Name':'SHRIMP SCAMPI','price':'$28'},
        {'Name':'LOBSTER CREAM SAUCE','price':'$35'},
        {'Name':'CHICKEN MARSALA','price':'$30'},
        {'Name':'CHICKEN PARMESAN','price':'$30'},
        {'Name':'Risotto','price':'$28'},
        {'Name':'Gnocchi','price':'$28'},
        {'Name':'Pesto alla Genovese','price':'$29'},
        {'Name':'lasagne','price':'$30'},
        {'Name':'SPAGHETTI & MEATBALL','price':'$30'}]


@app.route('/')
def get_reco():
    random_choice = random.randint(0,14)
    return meals[random_choice]

if __name__ == "__main__":
     app.run('0.0.0.0', port=5000,debug=True)
 