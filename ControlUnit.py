from myhdl import *
from ControlDecode import ControlDecode
from typeDecode import TypeDecode

@block
def ControlUnit(opcode,
                R_type,
                I_type,
                B_type,
                L_type,
                S_type,
                U_type,
                UJ_type,
                Auipc_type,
                Jalr_type,
                branchOut,
                RegWriteOut,
                ImmediateOut,
                LoadOut,
                StoreOut,
                UtypeOut,
                AuipcOut,
                JalOut,
                JalrOut):
    
    
    td = TypeDecode(opcode,
                R_type,
                I_type,
                B_type,
                L_type,
                S_type,
                U_type,
                UJ_type,
                Auipc_type,
                Jalr_type)
    cd = ControlDecode(R_type,
            I_type,
            B_type,
            L_type,
            S_type,
            U_type,
            UJ_type,
            Auipc_type,
            Jalr_type,
            branchOut,
            RegWriteOut,
            ImmediateOut,
            LoadOut,
            StoreOut,
            UtypeOut,
            AuipcOut,
            JalOut,
            JalrOut)
    return td, cd
    

@block
def SimulateControlUnit():
        R_type = Signal(bool(False))
        I_type= Signal(bool(False))
        B_type= Signal(bool(False))
        L_type= Signal(bool(False))
        S_type= Signal(bool(False))
        U_type= Signal(bool(False))
        UJ_type = Signal(bool(False))
        Auipc_type= Signal(bool(False))
        Jalr_type = Signal(bool(False))
        branchOut = Signal(bool(False))
        RegWriteOut = Signal(bool(False))
        ImmediateOut = Signal(bool(False))
        LoadOut = Signal(bool(False))
        StoreOut = Signal(bool(False))
        UtypeOut = Signal(bool(False))
        AuipcOut = Signal(bool(False))
        JalOut = Signal(bool(False))
        JalrOut = Signal(bool(False))
        opCode = Signal(intbv(0)[7:])
        opCodeList = [0x33]
        ControledUnit = ControlUnit(opCode,
                R_type,
                I_type,
                B_type,
                L_type,
                S_type,
                U_type,
                UJ_type,
                Auipc_type,
                Jalr_type,
                branchOut,
                RegWriteOut,
                ImmediateOut,
                LoadOut,
                StoreOut,
                UtypeOut,
                AuipcOut,
                JalOut,
                JalrOut)
        # ControledUnit.convert('Verilog')
        @instance
        def Run():
            for _ in opCodeList:
                opCode.next = _
            yield delay(10)
            print("R_type ", R_type,"branchOut ", branchOut)
            print("I_type ", I_type,"RegWriteOut ", RegWriteOut)
            print("B_type ", B_type,"ImmediateOut ", ImmediateOut)
            print("L_type ", L_type,"LoadOut ", LoadOut)
            print("S_type ", S_type,"StoreOut ", StoreOut)
            print("U_type ", U_type,"UtypeOut ", UtypeOut)
            print("UJ_type ", UJ_type,"Auipc_type ", AuipcOut)
            print("Auipc_type ", Auipc_type,"Jalr_type ", JalrOut)
            print("Jalr_type ", Jalr_type,"JalOut ", JalOut)
    
        return Run, ControledUnit

controlUnitSimulate = SimulateControlUnit()
controlUnitSimulate.run_sim()








    # controlDec = ControlDecode(R_type,
    #             I_type,
    #             B_type,
    #             L_type,
    #             S_type,
    #             U_type,
    #             UJ_type,
    #             Auipc_type,
    #             Jalr_type,
    #             branchOut,
    #             RegWriteOut,
    #             ImmediateOut,
    #             LoadOut,
    #             StoreOut,
    #             UtypeOut,
    #             AuipcOut,
    #             JalOut,
    #             JalrOut)

