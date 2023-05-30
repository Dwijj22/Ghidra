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
        operands = ', '.join([str(op) for op in ins.getOpObjects(ins.getNumOperands())])
        comment = ins.getComment(CodeUnit.EOL_COMMENT)
        print("{}\t{}\t{}\t{}".format(address, mnemonic, operands, comment))

def jmp(ins, blocks):
    if ins.getMnemonicString() == "JMP":
        jmp_target = ins.getAddressString()[0]
        for block in blocks:
            if block.getMinAddress() <= jmp_target < block.getMaxAddress():
                ins_at_target = currentProgram.getListing().getInstructionAt(jmp_target)
                if ins_at_target.getMnemonicString() == "NOP":
                    return "NOP"
                else:
                    return block.getName()
    return None

bbm = BasicBlockModel(currentProgram)
blocks = list(bbm.getCodeBlocks(TaskMonitor.DUMMY))

for block in blocks:
    code_refs = block.getDestinations(TaskMonitor.DUMMY)
    next_blocks = []
    while code_refs.hasNext():
        code_ref = code_refs.next()
        next_blocks.append(code_ref.getDestinationBlock())
        print(block.getName())
    # print("Block Start address: {}".format(block.getMinAddress()))
    # print("Block End address: {}".format(block.getMaxAddress()))
    # next_blocks = block.getDestinations(TaskMonitor.DUMMY)
    print("Next blocks: {}".format(next_blocks))
    print("========================================")
    print_disassembly(block)
    print("")
