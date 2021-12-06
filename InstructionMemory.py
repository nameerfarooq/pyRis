from math import comb
from myhdl import *
@block
def InstructionMemory(clk,adr,instructionOut,instructions):
    
    @always(clk)
    def read():
        instructionOut.next = instructions[int(adr)]
    return read

# @block
# def SimulateIM():
#     instructions = [0x00500193,
# 0x00500113,
# 0x00500213,
# 0xfa610193,
# 0x00510193,
# 0x00418663,
# 0x00000013,
# 0x00302423]
#     adr = Signal(intbv(0,0,len(instructions)))
#     instructionOut = Signal(intbv(0,0,2**DW,DW))

#     IM = InstructionMemory(adr, instructionOut, instructions )
#     # IM.convert('Verilog')
#     adrList = [0,1,2,3,4,5,6,7]
#     @instance
#     def simulatorIM():
#         for i in adrList:
#             adr.next = i
#             yield delay(10)
#             print("address", int(adr))
#             print("instruction out",instructionOut)

#     return simulatorIM, IM

# tb = SimulateIM()
# tb.config_sim(trace=True)
# tb.run_sim()
