from myhdl import block, always_comb, always_seq, Signal, intbv


@block
def DataMemory(clk, addr, data_in, data_out, load, store):
    DW = 2 ** 31
    rows = 1024
    Memory = [Signal(intbv(0, -DW, DW)) for __ in range(rows)]

    @always_comb
    def read():
        data_out.next = Memory[int(addr)] if load else 0

    @always_seq(clk.posedge, reset=None)
    def write():
        Memory[int(addr)].next = data_in if store == 1 and  clk == 1 else 0

    return write, read

# @block
# def SimulatingDataMem():
#     clk = Signal(intbv(1,0,2))
#     addr = Signal(intbv(88,0,rows))
#     data_in =Signal(intbv(0,-DW,DW))
#     data_out = Signal(intbv(0,-DW,DW))
#     load = Signal(intbv(1,0,2))
#     store = Signal(intbv(1,0,2))

#     DM = DataMemory(clk,addr,data_in,data_out,load,store)
#     DM.convert('Verilog')
#     dataList=[323423]
#     @instance
#     def RunDM():
#         for i in dataList:
#             data_in.next = i

#             yield delay(10)
#             print("clock : " ,int(clk))
#             print("load : " ,int(load))
#             print("store : " ,int(store))
#             print("addr : " ,int(addr))
#             print("data_in : " ,int(data_in))
#             print("data_out : " ,int(data_out))
#             print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#     return RunDM, DM

# tb = SimulatingDataMem()
# tb.config_sim(trace=True)
# tb.run_sim()

