from cgitb import reset
from random import randint
from re import template
from flask import Flask, jsonify
import jinja2

app = Flask(__name__)

playerdata = [{
    "commonName":"Christiano Ronaldo",
    "firstName":"C. Ronaldo",
    "lastName": "dos Santos Aveiro",
    "nation":{
        "abbrName":"PRG",
        "id":38,
        "name":"Portugal"
    },
    "club":{
        "abbrName":"Man Utd",
        "id": 243,
        "name":"Manchester United"
    },
    "position":"LW",
    "height":185,
    "weight":80,
    "birthdate":"1985-02-05",
    "age":34,
    "quality":"gold",
    "rating":99
}]

#First endpoint returns soccer player Christiano Ronaldo's personal information
@app.route("/")
def index():
    return jsonify(playerdata)

#Second endpoint returns a Chuck Norris' joke randomly from the list of jokes
@app.route("/chuck-norris-jokes")
def random_chuck_norris_jokes():
    jokes = ["Chuck Norris makes onions cry.",
    "Chuck Norris uses pepper spray to spice up his steaks.",
    "When Chuck Norris wants an egg, he cracks open a chicken.",
    "When Chuck Norris wants popcorn, he breathes on Nebraska",
    "Chuck Norris grinds his coffee with his teeth and boils the water with his own rage.",
    "Chuck Norris does not eat. Food understands that the only safe haven from Chuck Norris' fists is inside his own body."]

    return jokes[randint(0, len(jokes)-1)]

class User:
    def __init__(self, username, name, email, phone_num):
        self.username = username
        self.name = name
        self.email = email
        self.phone_num = phone_num

# Returning html containting user's information using jinja2 
@app.route("/user")
def get_user_info():
   my_user = User("nabindhakal", "Nabin Dhakal","ndhakall@hotmail.com", "234-234-2345")

   with open('user.html', 'r') as f:
    contents = f.read()
    
    template = jinja2.Template(contents)
    filled_template = template.render(user=my_user)

    return filled_template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
