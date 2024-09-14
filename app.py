from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.json.get('message')
    messages.append(message)
    return jsonify({'status': 'success'})

@app.route('/poll_messages')
def poll_messages():
    last_message_count = int(request.args.get('last_message_count', 0))
    while len(messages) <= last_message_count:
        time.sleep(1)
    return jsonify({'messages': messages[last_message_count:]})

if __name__ == '__main__':
    app.run(debug=True)
