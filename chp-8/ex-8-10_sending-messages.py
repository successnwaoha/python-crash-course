def send_messages(messages,sent_messages):
    """Sends messages from one list to another"""
    while messages:
        new_message = messages.pop()
        sent_messages.append(new_message)
def another(sent_messages):
    """Prints all values in new list"""
    for sent in sent_messages:
        print(sent)
messages = ['This is me!', 'Python is fun', 'Python is cool', 'I like java script']
sent_messages = []
send_messages(messages,sent_messages)
another(sent_messages)