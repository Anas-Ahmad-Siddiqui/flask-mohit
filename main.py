from flask import Flask, request, jsonify
import predict
import mails
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CORS(app, origins='*')

@app.route('/urls', methods=['POST'])
def urls():
    urls = request.json['urls']
    score = predict.prediction(urls)
    if(score == -1):
        return jsonify({'error': 'Invalid URL'})
    else:
        print(score)
        data = {'Obscenity Confidence': score}
        response = jsonify(data)
        response.status_code = 200
        return response

@app.route('/mailer', methods=['POST'])
def mailer():
    data = request.json
    links = data.get('links', [])
    websites = data.get('websites', [])
    result = mails.mailer(links, websites)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)