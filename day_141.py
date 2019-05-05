# Implement 3 stacks using a single list:

# class Stack:
#     def __init__(self):
#         self.list = []

#     def pop(self, stack_number):
#         pass

#     def push(self, item, stack_number):
#         pass

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        stack = None
        try:
            stack = self.list[stack_number]
        except:
            return None

        return stack.pop()

    def push(self, item, stack_number):
        try:
            self.list[stack_number].append(item)
        except:
            self.list.append([item])