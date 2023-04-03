from flask import Flask, request, jsonify
import predict
import mails
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CORS(app, origins='*')

@app.route('/urls', methods=['POST'])
def urls():
    print("Hello")
    print(request)
    urls = request.json['urls']
    return predict.prediction(urls)

@app.route('/mailer', methods=['POST'])
def mailer():
    data = request.json
    links = data.get('links', [])
    websites = data.get('websites', [])
    result = mails.mailer(links, websites)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)