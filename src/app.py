from flask import Flask, jsonify
from flask import request
app = Flask(__name__)
todos=[{"label": "My first task", "done": False}]
add_new_todo=[{"label":"My second task", "done": False}]

@app.route('/todos', methods=['GET'])
def task():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

import json
decoded_object = json.loads(request.data)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)