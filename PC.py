from myhdl import *

@block
def PC(clk,input,pc,pc4):
    reg = Signal(modbv(0,0,2**32))
    @always_comb
    def read():
        pc.next = reg 
        pc4.next = reg + 4
    @always_comb
    def write():
        if clk == 1:
            reg.next = input
    return write, read

@block
def SimulatePC():
    clk = Signal(bool(False))
    input = Signal(intbv(10,0,2**32,32))
    pc = Signal(intbv(0,0,2**32,32))
    pc4 = Signal(intbv(0,0,2**32,32))
    runPC = PC(clk,input,pc,pc4)
    runPC.convert('Verilog')
    @instance
    def Run():
        yield delay(10)
        print("clk : ",clk)
        print("input : ",input)
        print("pc : ",pc)
        print("pc4 : ",pc4)
    return Run, runPC

a = SimulatePC()
a.config_sim(trace=True)
a.run_sim()