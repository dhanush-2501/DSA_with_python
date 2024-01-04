class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i], end='')
        print()

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()



def is_balanced_parentheses(input_str):
    stk = Stack()
    opening_parentheses = {'(', '[', '{'}
    closing_parentheses = {')': '(', ']': '[', '}': '{'}

    for char in input_str:
        if char in opening_parentheses:
            stk.push(char)
        elif char in closing_parentheses:
            if stk.is_empty() or stk.pop() != closing_parentheses[char]:
                return False

    return stk.is_empty()

def reverse_string(string):
    stack = Stack()
    for s in string:
        stack.push(s)
    reversed_string = ''
    for _ in range(stack.size()):
        reversed_string += stack.pop()

# print(is_balanced_parentheses("(((())))"))
reverse_string("dhanu")