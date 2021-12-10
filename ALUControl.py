from myhdl import block, always_comb, concat, intbv


@block
def ALUcontrol(func3, func7, branchIn, controlOut):

    @always_comb
    def Control():
        if branchIn == 1:
            controlOut.next = concat(intbv(2, 0, 3, 2), func3)
        else:
            controlOut.next = concat(intbv(0, 0, 1, 1), func7, func3)

    return Control

# @block
# def SimulateALUcontrol():
#     func3 = Signal(intbv(6,0,2**3,3))
#     func7 = Signal(intbv(1,0,2,1))
#     branchIn = Signal(intbv(0,0,2,1))
#     controlOut = Signal(intbv(0,0,2**5,5))
#     ALUcnt = ALUcontrol(func3,func7,branchIn,controlOut)
#     ALUcnt.convert('Verilog')
#     @instance
#     def RUNAluCnt():
#         yield delay(10)
#         print("FUNC3 : ",bin(func3))
#         print("FUNC7 : ",bin(func7))
#         print("BranchIn : ",bin(branchIn))
#         print("controlOut : ",bin(controlOut))
#         print("------------------------")
#     return RUNAluCnt, ALUcnt

# alucntrl = SimulateALUcontrol()
# alucntrl.config_sim(trace=True)
# alucntrl.run_sim()

