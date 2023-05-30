from ghidra.program.model.block import BasicBlockModel
from ghidra.util.task import TaskMonitor

bbm = BasicBlockModel(currentProgram)
blocks = bbm.getCodeBlocks(TaskMonitor.DUMMY)
block = blocks.next()

while block:
    print("Label: {}".format(block.name))
    print("Min Address: {}".format(block.minAddress))
    print("Max address: {}".format(block.maxAddress))
    print("Length: {}".format(block.maxAddress.offset - block.minAddress.offset))
    print
    block = blocks.next()
