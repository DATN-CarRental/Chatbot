from flask import Flask, jsonify, request
from chat import handle_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat/', methods=['POST'])
def chat():
    print(request.json.get('question'))
    response = {
        'code_status': 200,
        'response': handle_response(request.json.get('question'))
    }
    insert_into_file(request.json.get('question'))
    print(response)
    return jsonify(response), 200

def insert_into_file(question):
    file_path = "conservation.txt"

    with open(file_path, "a", encoding='utf-8') as file:
        file.write(question + "\n")

if __name__ == '__main__':
    app.run()
