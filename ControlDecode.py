from myhdl import block, always_comb, intbv
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
        branchOut.next = intbv(0)[1:]
        RegWriteOut.next = intbv(0)[1:]
        ImmediateOut.next = intbv(0)[1:]
        LoadOut.next = intbv(0)[1:]
        StoreOut.next = intbv(0)[1:]
        UtypeOut.next = intbv(0)[1:]
        AuipcOut.next = intbv(0)[1:]
        JalOut.next = intbv(0)[1:]
        JalrOut.next = intbv(0)[1:]
        # print("hello worlddd")
        if B_type == intbv(1)[1:]:
            branchOut.next = intbv(1)[1:]
        if (UJ_type | U_type | R_type | I_type | L_type | Auipc_type) == intbv(1)[1:]:
            RegWriteOut.next = intbv(1)[1:]
        if (I_type | S_type | L_type) == intbv(1)[1:]:
            ImmediateOut.next = intbv(1)[1:]
        if S_type == intbv(1)[1:]:
            StoreOut.next = intbv(1)[1:]
        if L_type == intbv(1)[1:]:
            LoadOut.next = intbv(1)[1:]
        if U_type == intbv(1)[1:]:
            UtypeOut.next = intbv(1)[1:]
        if Auipc_type == intbv(1)[1:]:
            AuipcOut.next = intbv(1)[1:]
        if Jalr_type == intbv(1)[1:]:
            JalrOut.next = intbv(1)[1:]
        if UJ_type == intbv(1)[1:]:
            JalOut.next = intbv(1)[1:]

    return ControlDecoding


@block
def SimulateControlDecode():
    R_type, I_type, B_type, L_type, S_type, U_type, UJ_type, Auipc_type, Jalr_type, branchOut, RegWriteOut, ImmediateOut, LoadOut, StoreOut, UtypeOut, AuipcOut, JalOut, JalrOut = [Signal(intbv(1)[1:]) for i in range(18)]
    control = ControlDecode(R_type, I_type, B_type, L_type, S_type, U_type, UJ_type, Auipc_type, Jalr_type, branchOut, RegWriteOut, ImmediateOut, LoadOut, StoreOut, UtypeOut, AuipcOut, JalOut, JalrOut)
    lst = [R_type, I_type, B_type, L_type, S_type, U_type, UJ_type, Auipc_type, Jalr_type]

    @instance
    def Run():
        # for i in range(10):
        R_type.next, I_type.next, B_type.next, L_type.next, S_type.next, U_type.next, UJ_type.next, Auipc_type.next, Jalr_type.next = [False for i in range(9)]
        select = random.choice(lst)
        select.next = intbv(1)[1:]

        # print("iteration #",i)
        yield delay(10)
        # print("R_type ", R_type,"branchOut ", branchOut)
        # print("I_type ", I_type,"RegWriteOut ", RegWriteOut)
        # print("B_type ", B_type,"ImmediateOut ", ImmediateOut)
        # print("L_type ", L_type,"LoadOut ", LoadOut)
        # print("S_type ", S_type,"StoreOut ", StoreOut)
        # print("U_type ", U_type,"UtypeOut ", UtypeOut)
        # print("UJ_type ", UJ_type,"Auipc_type ", AuipcOut)
        # print("Auipc_type ", Auipc_type,"Jalr_type ", JalrOut)
        # print("Jalr_type ", Jalr_type,"JalOut ", JalOut)

        # print("......................")
    return  Run, control

# runControlDecode = SimulateControlDecode()
# runControlDecode.run_sim()
