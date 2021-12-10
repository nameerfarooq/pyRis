# from typing import List
# from myhdl import *

# @block
# def TypeDecode(clk,opCode,
#                 R_type,
#                 I_type,
#                 B_type,
#                 L_type,
#                 S_type,
#                 U_type,
#                 UJ_type,
#                 Auipc_type,
#                 Jalr_type):
#     @always(clk.posedge)
#     def typeDec():
#         # R_type.next,I_type.next,B_type.next,L_type.next,S_type.next,U_type.next,UJ_type.next,Auipc_type.next,Jalr_type.next = [intbv(0)[0:]  for i in range(9)]
#         R_type.next = intbv(0)[1:]
#         I_type.next= intbv(0)[1:]
#         B_type.next= intbv(0)[1:]
#         L_type.next= intbv(0)[1:]
#         S_type.next= intbv(0)[1:]
#         U_type.next= intbv(0)[1:]
#         UJ_type.next = intbv(0)[1:]
#         Auipc_type.next= intbv(0)[1:]
#         Jalr_type.next = intbv(0)[1:]

#         if opCode == 51:
#             R_type.next = intbv(1)[1:]
#         elif opCode == 19:
#             I_type.next = intbv(1)[1:]
#         elif opCode == 99:
#             B_type.next = intbv(1)[1:]
#         elif opCode == 3:
#             L_type.next = intbv(1)[1:]
#         elif opCode == 35:
#             S_type.next = intbv(1)[1:]
#         elif opCode == 55:
#             U_type.next = intbv(1)[1:]
#         elif opCode == 111:
#             UJ_type.next = intbv(1)[1:]
#         elif opCode == 23:
#             Auipc_type.next = intbv(1)[1:]
#         elif opCode == 103:
#             Jalr_type.next = intbv(1)[1:]
#     return typeDec
# @block
# def SimulateTypeDecode():
#     opCode = Signal(intbv(0)[7:])
#     R_type,I_type,B_type,L_type,S_type,U_type,UJ_type,Auipc_type,Jalr_type = [Signal(intbv(0)[1:]) for i in range(9)]
#     typeDecoded = TypeDecode(opCode, R_type,I_type,B_type,L_type,S_type,U_type,UJ_type,Auipc_type,Jalr_type)
#     opcodeList = [0x33,0x13,0x63,0x03,0x23,0x37,0x6f,0x17,0x67]
#     typeDecoded.convert('Verilog')
#     @instance
#     def Run():
#         for _ in opcodeList:
#             opCode.next = _
#             yield delay(10)
#             print("opcode ", opCode)
#             print("R_type ", R_type)
#             print("I_type ", I_type)
#             print("B_type ", B_type)
#             print("L_type ", L_type)
#             print("S_type ", S_type)
#             print("U_type ", U_type)
#             print("UJ_type ", UJ_type)
#             print("Auipc_type ", Auipc_type)
#             print("Jalr_type ", Jalr_type)
#             print("......................")
#     return Run, typeDecoded

# # typedecodeSimulate = SimulateTypeDecode()
# # typedecodeSimulate.run_sim()

from myhdl import block, always, intbv


@block
def TypeDecode(clk, opCode,
                R_type,
                I_type,
                B_type,
                L_type,
                S_type,
                U_type,
                UJ_type,
                Auipc_type,
                Jalr_type):

    @always(clk.posedge)
    def typeDec():
        # R_type.next,I_type.next,B_type.next,L_type.next,S_type.next,U_type.next,UJ_type.next,Auipc_type.next,Jalr_type.next = [intbv(0)[0:]  for i in range(9)]
        R_type.next = intbv(0)[1:]
        I_type.next = intbv(0)[1:]
        B_type.next = intbv(0)[1:]
        L_type.next = intbv(0)[1:]
        S_type.next = intbv(0)[1:]
        U_type.next = intbv(0)[1:]
        UJ_type.next = intbv(0)[1:]
        Auipc_type.next = intbv(0)[1:]
        Jalr_type.next = intbv(0)[1:]

        if opCode == 51:
            R_type.next = intbv(1)[1:]
        elif opCode == 19:
            I_type.next = intbv(1)[1:]
        elif opCode == 99:
            B_type.next = intbv(1)[1:]
        elif opCode == 3:
            L_type.next = intbv(1)[1:]
        elif opCode == 35:
            S_type.next = intbv(1)[1:]
        elif opCode == 55:
            U_type.next = intbv(1)[1:]
        elif opCode == 111:
            UJ_type.next = intbv(1)[1:]
        elif opCode == 23:
            Auipc_type.next = intbv(1)[1:]
        elif opCode == 103:
            Jalr_type.next = intbv(1)[1:]

    return typeDec
# @block
# def SimulateTypeDecode():
#     opCode = Signal(intbv(0)[7:])
#     R_type,I_type,B_type,L_type,S_type,U_type,UJ_type,Auipc_type,Jalr_type = [Signal(intbv(0)[1:]) for i in range(9)]
#     typeDecoded = TypeDecode(opCode, R_type,I_type,B_type,L_type,S_type,U_type,UJ_type,Auipc_type,Jalr_type)
#     opcodeList = [0x33,0x13,0x63,0x03,0x23,0x37,0x6f,0x17,0x67]
#     typeDecoded.convert('Verilog')
#     @instance
#     def Run():
#         for _ in opcodeList:
#             opCode.next = _
#             yield delay(10)
#             print("opcode ", opCode)
#             print("R_type ", R_type)
#             print("I_type ", I_type)
#             print("B_type ", B_type)
#             print("L_type ", L_type)
#             print("S_type ", S_type)
#             print("U_type ", U_type)
#             print("UJ_type ", UJ_type)
#             print("Auipc_type ", Auipc_type)
#             print("Jalr_type ", Jalr_type)
#             print("......................")
#     return Run, typeDecoded
