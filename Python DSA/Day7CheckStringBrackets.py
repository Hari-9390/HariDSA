def evaluate_expression(str):
    stack=[]
    for char in str:
        if char.isdigit():
            stack.append(int(char))
        else:
            a=stack.pop()
            b=stack.pop()

            if char=="+":
                stack.append(a+b)
            elif char=="-":
                stack.append(a-b)
            elif char=="*":
                stack.append(a*b)
            elif char=="/":
                stack.append(a//b)
    return stack[0]
print(evaluate_expression(str))




