from myhdl import *

@block
def ImmediateGen(inst,pc,s_imm,sb_imm,uj_imm,u_imm,i_imm):
    @always_comb
    def generate():
        # i type immediate
        i_imm.next = concat(intbv(inst[31])[20:],inst[32:20])
        # s_imm immediate
        s_imm.next = concat(intbv(inst[31])[20:], inst[32:25], inst[12:7])
        #u type immediate
        u_imm.next = concat(inst[32:12], intbv(0)[11:])
        # sb type immediate
        sb_imm.next = concat(intbv(inst[31])[19:], inst[31], inst[7], inst[31:25], inst[12:8], intbv(0)[1:]) + pc
        # uj type immediate
        uj_imm.next = concat(intbv(inst[31])[12:], inst[20:12], inst[20], inst[31:21], intbv(0)[1:]) + pc
    return generate

DW = 2**31
# @block
# def simulate():
#     pc = Signal(intbv(0, 0, DW)[32:])
#     inst = Signal(intbv(0, 0, DW)[32:])
#     s_imm = Signal(intbv(0)[32:])
#     sb_imm= Signal(intbv(0)[32:])
#     uj_imm  = Signal(intbv(0)[32:])
#     u_imm = Signal(intbv(0)[32:])
#     i_imm = Signal(intbv(0)[32:])
#     imm = ImmediateGen(inst,pc,s_imm , sb_imm , uj_imm , u_imm, i_imm)
    
# #    test
#     instructionsList = [70353171]
#     imm.convert('Verilog')
#     @instance
#     def run():
#         for _ in instructionsList:
#             inst.next = _
#             pc.next = intbv(0)[32:]
#             yield delay(10)
#             print("inst : ",inst)
#             print("pc",pc)
#             print("i_imm : ",i_imm)
#             print("s_imm : ",s_imm)
#             print("sb_imm : ",sb_imm)
#             print("uj_imm : ",uj_imm)
#             print("u_imm : ",u_imm)
#             print("...........")
#     return run, imm

# tb = simulate()
# tb.run_sim()