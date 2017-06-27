class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def parchecker(parstr):
    s = Stack()
    index = 0
    balance = True
    while index < len(parstr) and balance:
        if parstr[index] == "(":
            s.push(parstr[index])
        else:
            if s.isEmpty():
                balance = False
            else:
                s.pop()
        index += 1
    if balance and s.isEmpty():
        return True
    else:
        return False

print parchecker('   ')
print parchecker('((()))')
print parchecker('(((())')
print parchecker('(())')