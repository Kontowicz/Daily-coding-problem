# What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

# Code below is correct
functions = []
for i in range(10):
    functions.append(lambda i=i: i)

for f in functions:
    print(f())