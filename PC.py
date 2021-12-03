from myhdl import *

@block
def PC(clk,input,pc,pc4):
    reg = Signal(modbv(0,0,2**32))
    @always_comb
    def read():
        pc.next = reg 
        pc4.next = reg + 4
    always(clk.posedge)
    def write():
        reg.next = input
    return read, write
