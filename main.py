from chat import *
from save_conversation import *
if __name__ == '__main__':
    initialize_openai()
    conversation = load_conversation()
    request = "What is my name?"
    answer = response(conversation, request)
    add_new_response(answer, "bot")