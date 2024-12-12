"""
  Copyright 2024 LazySundayMorning

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import os
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for API access from different domains

# Load environment variables from .env file
load_dotenv()

# Configure OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configure SQLite Database (SQLAlchemy)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat_history.db'  # Use SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
db = SQLAlchemy(app)

# Define a model to store chat history
class ChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)  # Add user_id to track different users
    user_message = db.Column(db.String(500), nullable=False)
    bot_response = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<ChatHistory {self.id}>"

# Create the database tables
with app.app_context():
    db.create_all()

def get_gpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Or any other model of your choice
            messages=[
                {"role": "system", "content": "Đây là app hỗ trợ bệnh nhân sau thiên tai, bạn đóng vai trò như một bác sĩ hỗ trợ mọi người, ngôn ngữ bạn phản hồi dựa vào ngôn ngữ mà người dùng trò chuyện."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return str(e)

# API endpoint to get chatbot response
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')  # User message
    user_id = request.json.get('user_id')  # User ID (added to identify each user)

    if not user_input or not user_id:
        return jsonify({'error': 'Message and user_id are required'}), 400

    # Fetch the chat history for the specific user
    history = ChatHistory.query.filter_by(user_id=user_id).all()  # Filter history by user_id
    context = "\n".join([f"User: {h.user_message}\nBot: {h.bot_response}" for h in history])
    prompt = f"{context}\nUser: {user_input}\nBot:"

    # Get response from GPT
    bot_response = get_gpt_response(prompt)

    # Store the Q&A in the database with the user_id
    new_qa = ChatHistory(user_id=user_id, user_message=user_input, bot_response=bot_response)
    db.session.add(new_qa)
    db.session.commit()

    # Optionally, limit the size of history for performance (e.g., keep last 10 exchanges)
    if len(history) > 10:
        # Delete the oldest records for this user
        old_records = ChatHistory.query.filter_by(user_id=user_id).order_by(ChatHistory.id).limit(len(history) - 10).all()
        for record in old_records:
            db.session.delete(record)
        db.session.commit()

    return jsonify({'response': bot_response})

# API endpoint to get chat history for a specific user
@app.route('/history', methods=['GET'])
def get_history():
    user_id = request.args.get('user_id')  # Get user_id from query params

    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400

    # Fetch the chat history for the specific user
    history = ChatHistory.query.filter_by(user_id=user_id).all()

    return jsonify([{"user": h.user_message, "bot": h.bot_response} for h in history])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
