from flask import Flask, render_template
import requests
import random

app=Flask(__name__)


@app.route("/")
def chucknorris():
	response=requests.get('https://api.chucknorris.io/jokes/random')
	json_response=response.json()
	joke=json_response['value']
	return render_template("index.html",joke=joke,name="John",gender="Male")

@app.route("/pokemon")
def pokemon():
	response=requests.get('https://pokeapi.co/api/v2/pokemon-species/')
	json_response=response.json()
	pokemon_names=[]
	num=random.randint(0,17)
	for i in range(num):
		pokemon_names.append((json_response["results"][i]["name"],i+1))
	return render_template("pokemon.html",pokemon_names=pokemon_names)
	

if __name__=='__main__':
	app.run(debug=True)
	
	
	
	
#Models for all type
#
