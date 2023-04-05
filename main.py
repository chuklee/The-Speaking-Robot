from chat import *

if __name__ == '__main__':
    initialize_openai()
    conversation = "Me: Hello, how are you? You: Fine and you."
    request = "How old are you?"
    print(response(conversation, request))
