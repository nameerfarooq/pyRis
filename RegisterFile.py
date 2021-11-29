from myhdl import * 
import array as arr
rows = 32
DW = 2**(rows-1)
RegArray = [Signal(intbv(0,-DW,DW)) for i in range(rows+1)]
@block
def RegFile(rs_A,rs_B,Rd,WriteBack , WriteEnable, Data_A, Data_B):

    @always_comb
    def read():
        Data_A.next = RegArray[int(rs_A)]
        Data_B.next = RegArray[int(rs_B)]
    @always_comb
    def write():
        if WriteEnable == 1 and int(Rd) != 0 :
            RegArray[Rd].next =  WriteBack
    
    return read, write
@block
def SimulateReg():
    rs_A = Signal(intbv(1,0,rows+1))
    rs_B = Signal(intbv(13,0,rows+1))
    Rd = Signal(intbv(1,0,rows+1))
    WriteBack = Signal(intbv(200,-DW,DW))
    writeEnable = Signal(intbv(1,0,2))
    Data_A = Signal(intbv(0,-DW,DW))
    Data_B = Signal(intbv(0,-DW,DW))
    regg = RegFile(rs_A,rs_B,Rd,WriteBack,writeEnable,Data_A,Data_B)
    # regg.convert('Verilog')
    @instance
    def simulatingReg():
        for i in range(1):
            yield delay(10)
            print("rs_a : ",int(rs_A))
            print("rs_b : ",int(rs_B))
            print("rd : ",int(Rd))
            print("writeback : ",int(WriteBack))
            print("writeEnable : ",int(writeEnable))
            print("data A : ",int(Data_A))
            print("data B : ",int(Data_B))
            print("-------------------------------------")
    return regg, simulatingReg


tb = SimulateReg()
tb.config_sim(trace=True)
tb.run_sim()