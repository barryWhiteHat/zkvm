# ZKVM 

## Intro 

We want to build a ZKP that validates an entire EVM block or as much of it as we can efficiently. Its okay to adjust the gas costs for every EVM opcode. Its also to exclude some opcodes for now if they are super expensive. Its okay to exclude precompiles. 

This repo creates a sketch of how this can work as a way to explain but also to get the idea clear in my mind. 


### Arch 

We have two proofs that we use to prove validity of the state transition 

#### Proof 1: Contruct the stack 

We construct a commitment to the stack that is being executed. 

So here we do loads *AND* stores happen as well as membership proofs. The comimmtent to the new state after this block is also stored. 

The commitment is the whole stack for that block. It includes the op codes AND the variables that are loaded from memory. 

>[barry] Signatures go here too ? 

#### Proof 2: Execution 

For each opcode in the stack we execute it and update the stack.

Each EVM opcode is a custom constraint. We select the custom constraint based upon the stack and execute that. 
