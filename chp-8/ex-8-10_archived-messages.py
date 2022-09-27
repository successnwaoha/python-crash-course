messages = ['This is me!', 'Python is fun', 'Python is cool', 'I like java script']
sent_messsages = []
def send_messages(message):
    while message:
        new = messages.pop()
        sent_messsages.append(new)    

print(send_messages(messages))
print(send_messages(sent_messsages))