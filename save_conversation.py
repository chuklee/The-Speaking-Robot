def add_new_response(response, who):
    with open("data/conversation.csv", "a") as f:
        f.write(f"{who},{response}\n")

def load_conversation():
    conversation = ""
    with open("data/conversation.csv", "r") as f:
        for line in f:
            who, response = line.strip().split(",")
            conversation += f"{who}: {response} "
    return conversation