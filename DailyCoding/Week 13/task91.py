'''
What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
'''
if __name__ == "__main__":
    functions = []
    for i in range(10):
        functions.append(lambda i: i)
    i = 0
    for f in functions:
        print(f(i))
        i += 1
