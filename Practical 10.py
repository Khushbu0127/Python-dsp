from collections import deque

# Stack - LIFO (Undo tasks)
stack = []
stack.append("Task 1")
stack.append("Task 2")
print("Undo:", stack.pop()) # Last task removed

# Queue - FIFO (To-Do tasks)
queue = deque()
queue.append("Task A")
queue.append("Task B")
print("Do first:", queue.popleft()) # First task removed
