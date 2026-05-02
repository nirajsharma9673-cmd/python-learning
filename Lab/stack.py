def stack_operations(*args):
    stack = []

    for value in args:
        stack.append(value)  

    print("Stack after push:", stack)

    if stack:
        popped = stack.pop()
        print("Popped element:", popped)

    print("Final Stack:", stack)


stack_operations(50, 60,70,80)