from ghidra.program.model.block import BasicBlockModel
from ghidra.program.model.listing import CodeUnit
from ghidra.util.task import TaskMonitor

def print_disassembly(block):
    listing = currentProgram.getListing()
    ins_iter = listing.getInstructions(block, True)

    while ins_iter.hasNext():
        ins = ins_iter.next()
        address = ins.getAddressString(False, True)
        mnemonic = ins.getMnemonicString()
        operands = ', '.join([str(op) for op in ins.getOpObjects(ins.getNumOperands())]) # there is smtg wrong with this line
        comment = ins.getComment(CodeUnit.EOL_COMMENT)
        print("{}\t{}\t{}\t{}".format(address, mnemonic, operands, comment))

bbm = BasicBlockModel(currentProgram)
blocks = bbm.getCodeBlocks(TaskMonitor.DUMMY)
block = blocks.next()

while block:
    print("Block Start address {}".format(block.getMinAddress()))
    print("Block End address {}".format(block.getMaxAddress()))
    print("========================================")
    print_disassembly(block)
    print("")
    block = blocks.next()
