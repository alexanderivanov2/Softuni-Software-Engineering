class Email:
    def __init__(self, sender, receiver, content, is_set=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_set = is_set

    def send(self):
        self.is_set = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_set}"


emails = []
line = input()
while not line == "Stop":
    emails.append(line)
    line = input()

index = [int(ind) for ind in input().split(", ")]

for i in range(len(emails)):
    sender, receiver, content = emails[i].split()
    email_to_class = Email(sender, receiver, content)
    if i in index:
        email_to_class.send()
    print(email_to_class.get_info())
