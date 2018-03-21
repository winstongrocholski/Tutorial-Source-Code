from Stack import Stack

forward = "Never odd or even"
backward = ""

stack = Stack()

for char in forward:
    stack.push(char)

while not stack.is_empty():
    backward += str(stack.pop())

print(forward)
print(backward)
