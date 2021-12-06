from myhdl import *
from array import array
from ALU import ALU
from ALUControl import ALUcontrol
from ControlUnit import ControlUnit
from DataMemory import DataMemory
from InstructionMemory import InstructionMemory
from RegisterFile import RegFile
from ImmediateGenerator import ImmediateGen
from PC import PC

@block
def Core(clk,reset_n,
pc_out,pc4_out,pc_in,
instructionOut,
CUsignals,
branchOut, RegWriteOut, ImmediateOut, LoadOut, StoreOut, UtypeOut, AuipcOut, JalOut, JalrOut,
s_imm, sb_imm, uj_imm, u_imm, i_imm,
bus_A, bus_B,
writeBack,
rd,
aluControlpin,
operandA , operandB,
ALUbranchOut,
ALUOP,
result,
DMdataOut):
    @always(clk.posedge)
    def TopModule():
        
        # defining all signals

        # pc_out,pc4_out,pc_in = [Signal(intbv(0,0,2**32,32)) for i in range(3)]
        # instructionOut = Signal(intbv(0,0,2**32,32))
        # CUsignals = [Signal(intbv(0)[1:]) for i in range(9)]
        # branchOut, RegWriteOut, ImmediateOut, LoadOut, StoreOut, UtypeOut, AuipcOut, JalOut, JalrOut = [Signal(intbv(0)[1:]) for i in range(9)]
        # s_imm, sb_imm, uj_imm, u_imm, i_imm = [Signal(intbv(0)[32:]) for i in range(5)]
        # bus_A, bus_B = [Signal(intbv(0)[32:]) for i in range(2)]
        # writeBack = Signal(intbv(0)[32:])
        # rd = Signal(intbv(0)[5:])
        # aluControlpin = Signal(intbv(0,0,(2**32)-1))
        # operandA , operandB= [Signal(intbv(0,0,2**32)) for i in range(2)] 
        # ALUbranchOut = Signal(intbv(0)[1:])
        # ALUOP = Signal(intbv(0)[5:])
        # result = Signal(intbv(0,0,2**32,32))
        # DMdataOut = Signal(intbv(0,0,2**32,32))


        # PC
        
        
        if JalrOut == 1:
            pc_out.next = result
        elif JalOut == 1:
            pc_out.next = uj_imm
        elif ALUbranchOut == 1 and branchOut == 1 :
            pc_out.next = sb_imm
        else:
            pc_out.next = pc4_out
        pc = PC(clk,pc_in,pc_out,pc4_out)
        
        # INSTRUCTION MEMORY

        instructionsList = [0x0040006f,0x0040006f]
        # instructionsList = array[0x04020193,0x00500113,0x00500213,0xfa610193,0x00510193,0x00418663,0x00000013,0x00302423]
        dummyCLK = Signal(intbv(1))
        IM = InstructionMemory(dummyCLK,pc,instructionOut,instructionsList)

        # Control Unit
        

        CU = ControlUnit(dummyCLK,instructionOut[6:],*CUsignals,branchOut, RegWriteOut, ImmediateOut, LoadOut, StoreOut, UtypeOut, AuipcOut, JalOut, JalrOut)

        # Immediate Generator
        

        IMGEN = ImmediateGen(instructionOut,pc_out,s_imm, sb_imm, uj_imm, u_imm, i_imm)

        # Register File

        
        #   ///// write back logic

        
        if JalOut == 1:
            writeBack.next = pc4_out
        elif UtypeOut == 1:
            writeBack.next == u_imm
        elif LoadOut == 1:
            writeBack.next == DMdataOut
        else:
            writeBack.next = result

        #  ///// rd logic

        if JalOut == 1 :
            rd.next = 1
        else:
            rd.next = instructionOut[11:7]
                                            # rs_a        rs_b                    rd writeback , writeEnable , dataA, dataB               
        REGFILE = RegFile(clk,instructionOut[19:15], instructionOut[24:20],rd,writeBack, RegWriteOut , bus_A , bus_B)

        #  ALU CONTROL

        ALUcnt = ALUcontrol(instructionOut[14:12], instructionOut[30],branchOut,aluControlpin)

        # ALU
        
        # ///// operand A logic

        if AuipcOut == 1:
            operandA.next = pc4_out
        else:
            operandA.next = bus_A
        
        # ///// operand B logic

        if AuipcOut == 0 and ImmediateOut == 1 :
            if LoadOut == 1 or StoreOut == 1:
                operandB.next = s_imm
            else:
                operandB.next = i_imm
        elif AuipcOut == 1 and ImmediateOut == 0 :
            operandB.next = u_imm
        else:
            operandB.next = bus_B

        # ///// ALUOP logic
        if StoreOut == 1 or LoadOut == 1:
            ALUOP.next = 0
        else:
            ALUOP.next = aluControlpin

        Aluu = ALU(operandA,operandB,ALUOP,ALUbranchOut,result)


        #  DATA MEMORY 
        
        DM = DataMemory(clk,result,bus_B,DMdataOut,LoadOut,StoreOut)
        
        # return DM,Aluu,IM,IMGEN,REGFILE,ALUcnt,CU,pc
    return TopModule

@block
def SimulateCore():
    pc_out,pc4_out,pc_in = [Signal(intbv(0,0,2**32,32)) for i in range(3)]
    instructionOut = Signal(intbv(0,0,2**32,32))
    CUsignals = [Signal(intbv(0)[1:]) for i in range(9)]
    branchOut, RegWriteOut, ImmediateOut, LoadOut, StoreOut, UtypeOut, AuipcOut, JalOut, JalrOut = [Signal(intbv(0)[1:]) for i in range(9)]
    s_imm, sb_imm, uj_imm, u_imm, i_imm = [Signal(intbv(0)[32:]) for i in range(5)]
    bus_A, bus_B = [Signal(intbv(0)[32:]) for i in range(2)]
    writeBack = Signal(intbv(0)[32:])
    rd = Signal(intbv(0)[5:])
    aluControlpin = Signal(intbv(0,0,(2**32)-1))
    operandA , operandB= [Signal(intbv(0,0,2**32)) for i in range(2)] 
    ALUbranchOut = Signal(intbv(0)[1:])
    ALUOP = Signal(intbv(0)[5:])
    result = Signal(intbv(0,0,2**32,32))
    DMdataOut = Signal(intbv(0,0,2**32,32))
    clk = Signal(bool(1))
    reset_n = ResetSignal(0, active=0, isasync=False)
    
    
    core = Core(clk,reset_n,
pc_out,pc4_out,pc_in,
instructionOut,
CUsignals,
branchOut, RegWriteOut, ImmediateOut, LoadOut, StoreOut, UtypeOut, AuipcOut, JalOut, JalrOut,
s_imm, sb_imm, uj_imm, u_imm, i_imm,
bus_A, bus_B,
writeBack,
rd,
aluControlpin,
operandA , operandB,
ALUbranchOut,
ALUOP,
result,
DMdataOut)
    # core.convert('Verilog')
    @instance
    def clockGen():
        c = 0
        while c <= 15:
            clk.next = not clk
            c+=1
            yield delay(10)

    @instance
    def stimulus():
        yield delay(10)
        reset_n.next = 1
    @instance
    def RunCore():
        for i in range(2):
            yield delay(10)
            print("PC :",pc_out)
            print("Instruction memory out :",instructionOut)
            print("rd :",rd)
            print("bus A :",bus_A)
            print("bus B :",bus_B)
            print("write back :",writeBack)
            print("rs_a :",operandA)
            print("rs_b :",operandB)
            print("aluop :",ALUOP)
            print("result :",result)
            print("DM out :",DMdataOut)
            print("i type immediate :",i_imm)
            print("s type immediate :",s_imm)
            print("u type immediate :",u_imm)
            print("uj type immediate :",uj_imm)
            print("i type :",ImmediateOut)
            
    return RunCore, stimulus, clockGen, core
    
TestingCore = SimulateCore()
TestingCore.config_sim(trace=True)
TestingCore.run_sim()