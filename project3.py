# Modules opened in order
stack = []

# Student opens modules
stack.append("Module 1")
stack.append("Module 2")
stack.append("Module 3")

# Simulate Back button (2 times)
stack.pop()  # Goes back from Module 3
stack.pop()  # Goes back from Module 2

# What's currently visible?
current_module = stack[-1] if stack else "No module open"
print("Current visible module:", current_module)
# Stack of transactions
transactions = []

# Push transactions
transactions.append("School Fees")
transactions.append("Airtime")
transactions.append("Electricity Bill")

# Undo actions (pop)
undo1 = transactions.pop()
undo2 = transactions.pop()
undo3 = transactions.pop()

print("Undo order:")
print(undo1)
print(undo2)
print(undo3)
sentence = "It always looks green on the other side"
words = sentence.split()

stack = []

# Step 1 & 2: Push words into stack
for word in words:
    stack.append(word)

# Step 3: Pop to reverse
reversed_words = []
while stack:
    reversed_words.append(stack.pop())

# Join reversed words
reversed_sentence = " ".join(reversed_words)
print(reversed_sentence)
from collections import deque

queue = deque()

# 3 people arrive
queue.append("Person A")
queue.append("Person B")
queue.append("Person C")

# 1 person served
served = queue.popleft()

print("Served:", served)
print("Queue state:", list(queue))
from collections import deque

sim_requests = deque()

# 4 requests
sim_requests.append("Client 1")
sim_requests.append("Client 2")
sim_requests.append("Client 3")
sim_requests.append("Client 4")

# Serve first
first_served = sim_requests.popleft()
print("First served:", first_served)
from collections import deque

ticket_queue = deque()

# Fans arrive
ticket_queue.append("Fan 1")
ticket_queue.append("Fan 2")
ticket_queue.append("Fan 3")

# Gate allows entry
entered = ticket_queue.popleft()

print("Entered stadium:", entered)
print("Remaining queue:", list(ticket_queue))
