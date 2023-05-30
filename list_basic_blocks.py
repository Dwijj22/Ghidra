from ghidra.program.model.block import BasicBlockModel
from ghidra.util.task import TaskMonitor

def print_disassembly(block):
    listing = currentProgram.getListing()
    ins_iter = listing.getInstructions(block, True)

    while ins_iter.hasNext():
        ins = ins_iter.next()
        print "{} {}".format(ins.getAddressString(False, True), ins)

bbm = BasicBlockModel(currentProgram)
blocks = bbm.getCodeBlocks(TaskMonitor.DUMMY)
block = blocks.next()

while block:
    print_disassembly(block)
    block = blocks.next()
    print
