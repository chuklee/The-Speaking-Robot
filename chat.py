import openai
import json

def initialize_openai():
    # Initialize the OpenAI API witht the credentials.json file
    openai.api_key = json.load(open("credentials.json"))["openai_api_key"]

def generate_prompt(conversation, request):
    prompt = ""
    prompt += "Here is our previous conversation: "
    prompt += conversation
    prompt += "Now here is my response: "
    prompt += request
    prompt += "You:{}"
    return prompt

def response(conversation, request):
    """
    answer = openai.Completion.create(
                model="text-davinci-003",
                prompt=generate_prompt(conversation, request),
                temperature=0.6,
            )
            """
    answer = openai.Completion.create(
        model = "text-davinci-003", 
        prompt = generate_prompt(conversation, request),
        temperature= 0.7,
        max_tokens= 300,
        top_p= 1,
        frequency_penalty= 0,
        presence_penalty= 0,
        stop= ["{}"],
)
    return answer.choices[0].text