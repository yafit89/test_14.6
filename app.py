from flask import Flask 
import pyjokes 
import sys
import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")
if response.status_code == 200:
    joke = response.json()
    print(joke['setup'])
    print(joke['punchline'])
else:
    print("Failed to fetch joke")


app=Flask(__name__) 


@app.route("/") 
def home(): 
	joke=pyjokes.get_joke() #It only returns one joke. We get random joke each time. 
	return f'<h2>{joke}</h2>'

@app.route("/MultipleJokes") 
def jokes(): 
	jokes=pyjokes.get_jokes() #Here, we get a list of jokes. 
	return f'<h2>{jokes}</h2>'

if __name__ == "__main__": 
	app.run(debug=True)

