from typing import List
from myhdl import *



@block
def TypeDecode(opCode,
                R_type,
                I_type,
                B_type,
                L_type,
                S_type,
                U_type,
                UJ_type,
                Auipc_type,
                Jalr_type):
    @always_comb
    def typeDec():
        # R_type.next,I_type.next,B_type.next,L_type.next,S_type.next,U_type.next,UJ_type.next,Auipc_type.next,Jalr_type.next = [intbv(0)[0:]  for i in range(9)]
        R_type.next = bool(False)
        I_type.next= bool(False)
        B_type.next= bool(False)
        L_type.next= bool(False)
        S_type.next= bool(False)
        U_type.next= bool(False)
        UJ_type.next = bool(False)
        Auipc_type.next= bool(False)
        Jalr_type.next = bool(False)
        
        if opCode == 0x33:
            R_type.next = True
        elif opCode == 0x13:
            I_type.next = True
        elif opCode == 0x63:
            B_type.next = True
        elif opCode == 0x03:
            L_type.next = True
        elif opCode == 0x23:
            S_type.next = True
        elif opCode == 0x37:
            U_type.next = True
        elif opCode == 0x6F:
            UJ_type.next = True
        elif opCode == 0x17:
            Auipc_type.next = True
        elif opCode == 0x67:
            Jalr_type.next = True
    return typeDec
@block
def SimulateTypeDecode():
    opCode = Signal(intbv(0)[7:])
    R_type,I_type,B_type,L_type,S_type,U_type,UJ_type,Auipc_type,Jalr_type = [Signal(bool(False)) for i in range(9)]
    typeDecoded = TypeDecode(opCode, R_type,I_type,B_type,L_type,S_type,U_type,UJ_type,Auipc_type,Jalr_type)
    opcodeList = [0x33,0x13,0x63,0x03,0x23,0x37,0x6f,0x17,0x67]
    typeDecoded.convert('Verilog')
    @instance
    def Run():
        for _ in opcodeList:
            opCode.next = _
            yield delay(10)
            print("opcode ", opCode)
            print("R_type ", R_type)
            print("I_type ", I_type)
            print("B_type ", B_type)
            print("L_type ", L_type)
            print("S_type ", S_type)
            print("U_type ", U_type)
            print("UJ_type ", UJ_type)
            print("Auipc_type ", Auipc_type)
            print("Jalr_type ", Jalr_type)
            print("......................")
    return Run, typeDecoded

# typedecodeSimulate = SimulateTypeDecode()
# typedecodeSimulate.run_sim()