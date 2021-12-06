from myhdl import *

@block
def ALU(operandA, operandB,aluControl,branchStatus,Result ):
    @always_comb
    def Alu():
        
        if aluControl == 0:
            Result.next = operandA + operandB # add
        elif aluControl == 8 :
            Result.next = operandA - operandB # sub
        elif aluControl == 1 : 
            Result.next = operandA << operandB # sll
        elif aluControl == 2  or aluControl == 3:
            Result.next = 1 if operandA.signed() < operandB.signed() else 0 # slt
        elif aluControl == 4 :
            Result.next =  operandA ^ operandB  # xor
        elif aluControl == 5 or aluControl == 13 :
            Result.next =  operandA >> operandB[5:0]  # srl sra
        elif aluControl == 6 :
            Result.next =  operandA | operandB # or
        elif aluControl == 7 :
            Result.next =  operandA & operandB # and
        elif aluControl == 16 :
            Result.next = 1 if operandA == operandB else 0 # beq
        elif aluControl == 17 :
            Result.next = 1 if operandA != operandB else 0 # bne
        elif aluControl == 20 or aluControl == 22 :
            Result.next = 1 if operandA < operandB else 0 # blt
        elif aluControl == 21 or aluControl == 23 :
            Result.next = 1 if operandA >= operandB else 0 # bge

        if aluControl[4] == 1 and aluControl[3] == 0 :
            branchStatus.next = 1
    return Alu
    
# @block
# def SimulateALU():
#     operandA = Signal(intbv(4278190335,0,2**32,32))
#     operandB = Signal(intbv(7,0,2**32,32))
#     AluControl = Signal(intbv(0,0,32,5))
#     branchStatus = Signal(intbv(0,0,2,1))
#     result = Signal(intbv(0,0,2**32,32))
#     ALUU = ALU(operandA,operandB,AluControl,branchStatus,result)
#     # ALUU.convert('Verilog')

#     @instance
#     def run():
#         yield delay(10)
#         print("operand A : ", bin(operandA))
#         print("operand B : ", bin(operandB))
#         print("Alu control : ", bin(AluControl))
#         print("branch status : ", bin(branchStatus))
#         print("result : ", bin(result))
#     return run, ALUU

# AluTester = SimulateALU()
# AluTester.config_sim(trace=True)
# AluTester.run_sim()