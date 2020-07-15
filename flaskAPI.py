from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests 
from mangaReader import scape
# init app
app = Flask(__name__)

@app.route('/api/', methods = ['GET'])

def API():
    return jsonify(scape())
    


#Run Server
if __name__ == '__main__':
    app.run(debug=True)


