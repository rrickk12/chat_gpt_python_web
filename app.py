# app.py
from flask import Flask, request, jsonify, render_template
from api.chatGPT import run_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/run-api', methods=['POST'])
def handle_run_api():
    # Execute the function
    text = request.json.get('text')
    result = run_api(text)
    print(result['choices'][0]['message']['content'])
    return result['choices'][0]['message']['content']

# @app.route('/process', methods=['POST'])
# def process_message():
#     data = request.json
#     message = data.get('message', '')
#     processed_message = message[::-1]
#     return jsonify({'message': processed_message})

if __name__ == '__main__':
    app.run(debug=True)
