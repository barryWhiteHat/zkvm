from dummy_function import *

## So now our stack bulider proof builds the stack so the evm proof can verify it. Only after veritying both do we trust that block is correct.  

## This block containts a single transaction 
contract_address = 0 
parameters = []
sig = []
transactions = [contract_address, parameters, sig]

# init our stack
stack = []

# init eth_state 
eth_state = get_eth_state()

for transaction in transactions: 
    # Let get the code for `contract_address`
    code = prove_membership(contract_address, eth_state)
    # next we go through our state and execute all the loads and stores. 

    # we can't go through every opcode becuase we don't know if every 
    # opcode will be executed. Instead we have to go via our execution map
    # which shows us which opcode will be executed in which order. 
    # We defer verificaion of the execution map until we get to the evm.py proof

    execution_map = get_execution_map(transaction)

    for i in execution_map: 
        if code[i] == "sload":
            # code[i+1] is the key to load
            var = prove_membership(code[i], code[i+1], eth_state)
            # replace sload opcode with var
            code[i] = var
            # remove the key that was loaded from the stack 
            # NOTE: I am not sure if we can do this that removing items from
            # from the stakc could cause invalid jumps to happen. 
            # have to think about this more and maybe chat with some EVM friends
            code.pop(i+1)
        if code[i] == "mload":
            # Same as above but check memory index instead of key
            pass
        if code[i] == "sstore":
            # okay ew also want to execute our sstores now so we can avoid
            # that inside the execution part.
            eth_state = update_eth_state(code, code[i+1], code[i+2], eth_state)
            # remove opcode from stack
            code.pop(i)
            # remove the key from stack
            code.pop(i+1)
            # remove the value from stack
            code.pop(i+2)
        if code[i] == "mstore":
            # same as above
            pass
        if code[i] == "mstore8":
            # same as above
            pass
        # note ad logic for Address, Balance, Origin , Caller, CallValue, 
        # calldataload , call data size, call date_copy, code_size, code_copy
        # gas_rpice, extcodecopy, returndatasize, returndatacopy, extcodehash,
        # blockhash, coinbase, timestamp, blocknumber, difficulty, gaslimit
    stack.append(code)

## Test stack that says 2 + 2 = 4
## opcode 0 is plus it takes the next two variable off the stack and adds them. 
## opcode 3 is term 
## 1 == add
## 0 == halt
## 1 can also be interperated as a variable by the evm
stack = [1,2,2,0]
execution_map = [0,1]
