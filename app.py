from flask import Flask, send_from_directory, request, jsonify
from dotenv import load_dotenv
import os
from webex import WebexAPI

# Load the environment variables from the .env file
load_dotenv()

access_token = os.getenv('WEBEX_ACCESS_TOKEN')
if not access_token:
    raise ValueError("Access token is not set. Please set the WEBEX_ACCESS_TOKEN environment variable.")
    

app = Flask(__name__, static_folder='static')

webex_api = WebexAPI(access_token)

@app.route('/')
def serve_static():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api')
def api():
    # Your API logic here
    return 'Hello, API!'

@app.route('/api/create-meeting', methods=['POST'])
def create_meeting():
    # Retrieve the request data
    data = request.get_json()
    title = data.get('title')
    start = data.get('start')
    end = data.get('end')

    # Your code to create the meeting goes here
    try:
        meeting = webex_api.create_meeting(title, start, end)
        return jsonify(meeting)
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/api/generate-join-link', methods=['POST'])
def generate_join_link():
    # Retrieve the request data
    data = request.get_json()
    meeting_id = data.get('meetingId')
    password = data.get('password')
    email = data.get('email')
    display_name = data.get('displayName')

    # Your code to generate the join link goes here
    join_link = webex_api.join_meeting(meeting_id, password, email, display_name)

    return jsonify(join_link)