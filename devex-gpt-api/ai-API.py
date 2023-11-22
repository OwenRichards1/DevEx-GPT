from flask import Flask, request, jsonify
import os
import openai
import dotenv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load environment variables from a .env file if you're using one
dotenv.load_dotenv()

# Get Azure OpenAI Configuration
endpoint = os.environ.get("AOAIEndpoint")
api_key= os.environ.get("AOAIKey")
deployment = os.environ.get("AOAIDeploymentId")

# Configure the OpenAI client NEW
client = openai.AzureOpenAI(
    base_url=f"{endpoint}/openai/deployments/{deployment}/extensions",
    api_key=api_key,
    api_version="2023-08-01-preview",
)

# Azure Cognitive Search setup
search_endpoint = os.getenv("COGNITIVE_SEARCH_ENDPOINT")
search_key = os.getenv("COGNITIVE_SEARCH_KEY"); # Add your Azure Cognitive Search admin key here
search_index_name = os.getenv("COGNITIVE_INDEX_NAME"); # Add your Azure Cognitive Search index name here

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('user_message')

    try:
        message_text = [{"role": "user", "content": user_message}]
        response = client.chat.completions.create(
            model=deployment,
            messages=message_text,
            extra_body={
                "dataSources": [
                    {
                        "type": "AzureCognitiveSearch",
                        "parameters": {
                            "endpoint": search_endpoint,
                            "key": search_key,
                            "indexName": search_index_name
                        }
                    }
                ]
            }
        )

        # Extract the 'content' field of the 'message' object
        bot_response = response.choices[0].message.content
        return jsonify({'bot_response': bot_response})
    except Exception as e:
        # Handle API request errors and return an appropriate JSON response
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
