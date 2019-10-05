from flask import Flask, jsonify
import json    

app = Flask(__name__)

with open("C:\\Users\\hp\\Desktop\\pythonProject\\web_scraping\\personal.json") as json_file:
        json_data = json.load(json_file)
        print(json_data)

tasks = [
    {
        'id': 1,
        'Name': json_data['x']['name'],
        'Market_cap': json_data['y']['market_cap'], 
        'Price': json_data['z']['price'],
        'Valume':json_data['w']['valume'],
        'Circulating_supply': json_data['t']['circulating_supply']

    }
]

@app.route('/flask/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/flask/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'name' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['name'],
        'Market_cap': request.json.get('market_cap'),
        'Price': request.json['price'],
        'Valume': request.json['valume'],
        'Circulating_supply': request.json['circulating_supply']
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(debug=True)