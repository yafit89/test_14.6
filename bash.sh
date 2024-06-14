#!/bin/bash 

FLASK_URL="http://127.0.0.1:5000"

response=(curl -s FLASK_URL)


word_count=$(echo $response | wc -w)

echo "Number of words in the joke: $word_count"

cd /Users/yafit/Desktop/TEST\ 14.6/ 

python3 app.py