'''Author: Aaditya Bhatia
Version: 1.0
Published Date: 7-01-2018
Functionality: This is a rest module consuming CNN and Twitter modules
'''

#   Importing the required libraries and modules
from flask import Flask, jsonify
from flask_cors import CORS
from cnn_crawler import loadDriver, findKeyword     # CNN module
from twitter_raw import getTweets                   # Twitter module

app = Flask(__name__)
CORS(app)

#   Default for checking the status of rest connectivity
@app.route('/')
def index():
    return "Status Connected!"

#   For fetching CNN Data
@app.route('/CNNData')
def cnnData():
    baseUrl = "http://edition.cnn.com"
    html_driver = loadDriver(baseUrl)
    label_url_dict = findKeyword(html_driver, baseUrl)
    list = []

    for key, val in label_url_dict.items():

        temp_dict = {}
        temp_dict['title'] = key
        temp_dict['link'] = val
        list.append(temp_dict)
    return (jsonify(list))

#   For fetching Twitter Data
@app.route('/twitterData')
def twitterData():
    public_account = "realDonaldTrump"
    tweets = getTweets(public_account)
    return jsonify(tweets)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True, threaded=True)