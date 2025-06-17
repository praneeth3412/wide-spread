# app.py
from flask import Flask, request, jsonify
import openai  # You could replace this with your own AI model

app = Flask(_name_)

# Configure your API key (in production, use environment variables)
openai.api_key = "your-openai-api-key"

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    try:
        # Call the AI model (using OpenAI API in this example)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        
        return jsonify({
            "response": response.choices[0].message['content'],
            "status": "success"
        })
    except Exception as e:
        return jsonify({
            "response": str(e),
            "status": "error"
        })

if _name_ == '_main_':
    app.run(debug=True)