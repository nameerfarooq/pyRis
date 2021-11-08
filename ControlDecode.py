from myhdl import *
import random

@block
def ControlDecode(
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
    @always_comb
    def ControlDecoding():
        branchOut.next,RegWriteOut.next,ImmediateOut.next,LoadOut.next, StoreOut.next,UtypeOut.next,AuipcOut.next,JalOut.next,JalrOut.next = [False for i in range(9)]
        if B_type == True:
            branchOut.next = True
        if (UJ_type | U_type | R_type | I_type | L_type | Auipc_type) == True:
            RegWriteOut.next = True
        if ( I_type | S_type | L_type ) == True:
            ImmediateOut.next = True
        if S_type == True:
            StoreOut.next = True
        if L_type == True:
            LoadOut.next = True
        if U_type == True:
            UtypeOut.next = True
        if Auipc_type == True:
            AuipcOut.next = True
        if Jalr_type == True:
            JalrOut.next = True
        if UJ_type == True:
            JalOut.next = True
    
    return ControlDecoding

@block
def SimulateControlDecode():    
    R_type,I_type,B_type,L_type,S_type,U_type, UJ_type,Auipc_type,Jalr_type,branchOut,RegWriteOut,ImmediateOut,LoadOut, StoreOut,UtypeOut,AuipcOut,JalOut,JalrOut = [Signal(bool(False)) for i in range(18)]
    control = ControlDecode(R_type,I_type,B_type,L_type,S_type,U_type, UJ_type,Auipc_type,Jalr_type,branchOut,RegWriteOut,ImmediateOut,LoadOut, StoreOut,UtypeOut,AuipcOut,JalOut,JalrOut)
    lst =  [R_type,I_type,B_type,L_type,S_type,U_type, UJ_type,Auipc_type,Jalr_type]
    @instance
    def Run():
        for i in range(10):
            R_type.next,I_type.next,B_type.next,L_type.next,S_type.next,U_type.next, UJ_type.next,Auipc_type.next,Jalr_type.next = [False for i in range(9)]
            select = random.choice(lst)
            select.next = True
            
            print("iteration #",i)
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
          
            print("......................")
    return  Run,control
    

runControlDecode = SimulateControlDecode()
runControlDecode.run_sim()
