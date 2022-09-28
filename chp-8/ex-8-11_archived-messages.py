def send_messages(messages,sent_messages):
    while messages:
        new_message = messages.pop()
        print(f"printing model: {new_message}")
        sent_messages.append(new_message)
def another(sent_messages):
    for sent in sent_messages:
        print(sent)
messages = ['This is me!', 'Python is fun', 'Python is cool', 'I like java script']
sent_messages = []
send_messages(messages,sent_messages)
another(sent_messages)
send_messages(sent_messages, messages)
another(messages)