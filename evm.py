
## we get the stack with all memory reads and writes executed. The data has been verifiied but here we need to verify 

# 1. The execution map used was correct 
# 2. That each opcode is exectuted correctly. 

from transcript_gen import stack, execution_map
from opcodes import *

i = 0 # current insturction 
j = 0 # step count

while True:
    assert(i == execution_map[j])
    # add
    if stack[i] == 1:  
        stack,i  = add(stack,i)

    # halt
    if stack[i] == 0:
        stack.pop(i)
        break


    j+=1

print(stack)

