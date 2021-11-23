from typing import List
from myhdl import * 
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
            RegArray[int(Rd)].next =  WriteBack
    
    return read, write
@block
def SimulateReg():
    rs_A = Signal(int(32))
    rs_B = Signal(int(13))
    Rd = Signal(int(32))
    WriteBack = Signal(int(200))
    writeEnable = Signal(int(1))
    Data_A = Signal(int(0))
    Data_B = Signal(int(0))
    regg = RegFile(rs_A,rs_B,Rd,WriteBack,writeEnable,Data_A,Data_B)
    regg.convert('Verilog')
    @instance
    def simulatingReg():
        for i in range(2):
            yield delay(10)
            print("rs_a : ",rs_A)
            print("rs_b : ",rs_B)
            print("rd : ",Rd)
            print("writeback : ",WriteBack)
            print("writeEnable : ",writeEnable)
            print("data A : ",Data_A)
            print("data B : ",Data_B)
            print("-------------------------------------")
    return regg, simulatingReg


tb = SimulateReg()
tb.config_sim(trace=True)
tb.run_sim()