

def add(stack, i): 
    opcode = stack.pop(i) 
    a = stack.pop(0)
    b = stack.pop(0)
    c = a + b % (2**256)
    stack.insert(0,c)
    i += 1
    return(stack,i)





