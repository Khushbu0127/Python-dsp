class Stack:
    def __init__(self): self.items = []
    def push(self, x): self.items.append(x)
    def pop(self): return self.items.pop() if self.items else None
    def is_empty(self): return len(self.items)==0

def infix_to_postfix(exp):
    prec = {'+':1, '-':1, '*':2, '/':2, '^':3}
    s = Stack()
    output = ""
    for ch in exp:
        if ch.isalnum(): output += ch
        elif ch == '(': s.push(ch)
        elif ch == ')':
            while not s.is_empty() and s.items[-1]!= '(':
                output += s.pop()
            s.pop()
        else:
            while not s.is_empty() and prec.get(ch,0) <= prec.get(s.items[-1],0):
                output += s.pop()
            s.push(ch)
    while not s.is_empty(): output += s.pop()
    return output

print(infix_to_postfix("a+b*(c^d-e)")) # abcde-^ *+
