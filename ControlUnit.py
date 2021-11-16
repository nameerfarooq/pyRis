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
        R_type = Signal(intbv(0)[1:])
        I_type= Signal(intbv(0)[1:])
        B_type= Signal(intbv(0)[1:])
        L_type= Signal(intbv(0)[1:])
        S_type= Signal(intbv(0)[1:])
        U_type= Signal(intbv(0)[1:])
        UJ_type = Signal(intbv(0)[1:])
        Auipc_type= Signal(intbv(0)[1:])
        Jalr_type = Signal(intbv(0)[1:])
        branchOut = Signal(intbv(0)[1:])
        RegWriteOut = Signal(intbv(0)[1:])
        ImmediateOut = Signal(intbv(0)[1:])
        LoadOut = Signal(intbv(0)[1:])
        StoreOut = Signal(intbv(0)[1:])
        UtypeOut = Signal(intbv(0)[1:])
        AuipcOut = Signal(intbv(0)[1:])
        JalOut = Signal(intbv(0)[1:])
        JalrOut = Signal(intbv(0)[1:])
        opCode = Signal(intbv(0)[7:])
        opCodeList = [intbv(51)[7:]]
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
        ControledUnit.convert('Verilog')
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

