from Stack import Stack

data = [1,2,3,4,5,6,7,8,9]

stack = Stack()
before = ''
after = ''

for num in data:
    before += str(num) + ','
    stack.push(num)

while not stack.is_empty():
    after += str(stack.pop()) + ','

print(before)
print(after)
