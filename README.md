# DevEx GPT app

Two apps make up this project:

- devex-gpt-api
- devex-gpt-app

## devex-gpt-api

This is a simple Python Flask app that serves as the backend for the devex-gpt-app. It is a REST API that uses the [OpenAI GPTAPI](https://learn.microsoft.com/en-us/azure/ai-services/openai/use-your-data-quickstart?tabs=command-line%2Cpython&pivots=programming-language-python) to generate text based on a prompt.

Please note that you will need to have an Azure OpenAI API key to use this app. You will also need to specify the custom model you are using.

When succesfully registed, please create a .env file in the root of the project with the following variables:

    ```bash
        # OpenAI values
        AOAIEndpoint = ""
        AOAIKey = ''
        AOAIDeploymentId = ''
        
        
        # Cognitive Search values
        COGNITIVE_SEARCH_ENDPOINT = ''
        COGNITIVE_SEARCH_KEY = ''
        COGNITIVE_INDEX_NAME = ''
    ```

Next, you will need to install the required Python packages. You can do this by running the following command:

    ```bash
        pip install -r requirements.txt
    ```

Finally, you can run the app by running the following command:

    ```bash
        python ./devex-gpt-api/ai-API.py
    ```

Without using the SPA to consume the API, you can test the API by using Postman using the following:

    ```bash
        POST http://localhost:5000/api/ai
        Content-Type: application/json
        {
            "prompt": "This is a test prompt",
        }
    ```

## devex-gpt-app

This is a NextJS APP used as a UI to communicate with the API. It is a simple form that allows you to enter a prompt and generate text based on the prompt. It is responsive and can be used to continue the conversation.

To install the required packages, run the following command:

    ```bash
        npm install
    ```

To run the app, run the following command:

    ```bash
        npm run dev
    ```

The app will be available at `http://localhost:3000`.

:::image type="content" source="{media\devex-gpt-chat.png}" alt-text="{image of chat bot}":::
