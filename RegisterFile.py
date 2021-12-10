from myhdl import block, Signal, intbv, always_comb, always_seq


@block
def RegFile(clk, rs_A, rs_B, Rd, WriteBack , WriteEnable, Data_A, Data_B):
    rows = 32
    DW = 2 ** (rows - 1)
    RegArray = [Signal(intbv(0, -DW, DW)) for __ in range(rows + 1)]

    @always_comb
    def read():
        Data_A.next = RegArray[int(rs_A)]
        Data_B.next = RegArray[int(rs_B)]

    @always_seq(clk.posedge, reset=None)
    def write():
        if WriteEnable == 1 and int(Rd) != 0:
            RegArray[Rd].next = WriteBack

    return read, write
# @block
# def SimulateReg():
#     rs_A = Signal(intbv(1,0,rows+1))
#     rs_B = Signal(intbv(13,0,rows+1))
#     Rd = Signal(intbv(1,0,rows+1))
#     WriteBack = Signal(intbv(200,-DW,DW))
#     writeEnable = Signal(intbv(1,0,2))
#     Data_A = Signal(intbv(0,-DW,DW))
#     Data_B = Signal(intbv(0,-DW,DW))
#     regg = RegFile(rs_A,rs_B,Rd,WriteBack,writeEnable,Data_A,Data_B)
#     regg.convert('Verilog')
#     @instance
#     def simulatingReg():
#         for i in range(1):
#             yield delay(10)
#             print("rs_a : ",int(rs_A))
#             print("rs_b : ",int(rs_B))
#             print("rd : ",int(Rd))
#             print("writeback : ",int(WriteBack))
#             print("writeEnable : ",int(writeEnable))
#             print("data A : ",int(Data_A))
#             print("data B : ",int(Data_B))
#             print("-------------------------------------")
#             print('\nUsing MyHDL version: {}'.format(myhdl.__version__))
#     return regg, simulatingReg

# tb = SimulateReg()
# tb.config_sim(trace=True)
# tb.run_sim()
