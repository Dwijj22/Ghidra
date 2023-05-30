from __main__ import *
import ghidra_basics as gh

# To get the current program
program = gh.current_program("/home/cs/development/c++/a.out")

# To get the listing
listing = program.getListing()

# Loop through all functions in the listing
functions = listing.getFunctions(True)
for function in functions:
    # Get the basic blocks for the function
    basicBlocks = function.getBody().getBasicBlocks()
    
    # Printing the basic blocks addresses
    print("Basic blocks for function " + function.getName() + ":")
    for block in basicBlocks:
        print(hex(block.getFirstStartAddress().getOffset()))

  
