from collections import deque

client = input()
clients = deque()

while not client == "End":
    if client != "Paid":
        clients.append(client)
    else:
        while clients:
            print(clients.popleft())
    client = input()

print(f"{len(clients)} people remaining.")