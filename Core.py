from myhdl import *

from ALU import ALU
from ALUControl import ALUcontrol
from ControlUnit import ControlUnit
from DataMemory import DataMemory
from InstructionMemory import InstructionMemory
from RegisterFile import RegFile
from ImmediateGenerator import ImmediateGen
from PC import PC

@block
def Core(clk,Reset):
    @always_seq(clk.posedge)
    def TopModule():
        
        # PC
        
        pc_out,pc4_out,pc_in = [Signal(intbv(0,0,2**32,32))]
        pc = PC(clk,pc_in,pc_out,pc4_out)
        
        # INSTRUCTION MEMORY

        instructionsList = [0x00500193,0x00500113,0x00500213,0xfa610193,0x00510193,0x00418663,0x00000013,0x00302423]
        instructionOut = Signal(intbv(0,0,2**32,32))
        inst_mem = InstructionMemory(pc,instructionOut,instructionsList)

        # Control Unit
        
        CUsignals = [Signal(intbv(0)[1:]) for i in range(9)]
        branchOut, RegWriteOut, ImmediateOut, LoadOut, StoreOut, UtypeOut, AuipcOut, JalOut, JalrOut = [Signal(intbv(0)[1:]) for i in range(9)]
        CU = ControlUnit(instructionOut[6:],*CUsignals,branchOut, RegWriteOut, ImmediateOut, LoadOut, StoreOut, UtypeOut, AuipcOut, JalOut, JalrOut)

        # Immediate Generator
        
        s_imm, sb_imm, uj_imm, u_imm, i_imm = [Signal(intbv(0)[32:]) for i in range(5)]
        ImmediateGenerator = ImmediateGen(instructionOut,pc_out,s_imm, sb_imm, uj_imm, u_imm, i_imm)

        # Register File
        bus_A, bus_B = Signal(intbv(0)[32:])
        
        #   ///// write back logic

        writeBack = Signal(0)[32:]
        if JalOut == 1:
            writeBack.next = pc4_out
        elif UtypeOut == 1:
            writeBack.next == u_imm
        elif LoadOut == 1:
            writeBack.next == Data_out
        else:
            writeBack.next = result

        #  ///// rd logic

        rd = Signal(0)[5:]
        if JalOut == 1 :
            rd.next = 1
        else:
            rd.next = instructionOut[11,7]
                                         # rs_a        rs_b                    rd writeback , writeEnable , dataA, dataB               
        regiterFile = RegFile(clk,instructionOut[19:15], instructionOut[24:20],rd,writeBack, RegWriteOut , bus_A , bus_B)

        #  ALU CONTROL

        aluControlpin = Signal(intbv(0,0,(2**32)-1))
        aluControl = ALUcontrol(instructionOut[14:12], instructionOut[30],branchOut,aluControlpin)

        # ALU

        