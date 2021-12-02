// File: DataMemory.v
// Generated by MyHDL 0.11
// Date: Wed Dec  1 23:29:53 2021


`timescale 1ns/10ps

module DataMemory (
    clk,
    addr,
    data_in,
    data_out,
    load,
    store
);


input [0:0] clk;
input [9:0] addr;
input signed [31:0] data_in;
output signed [31:0] data_out;
wire signed [31:0] data_out;
input [0:0] load;
input [0:0] store;

wire signed [31:0] Memory [0:1024-1];




assign Memory[addr] = ((store == 1) && (clk == 1)) ? data_in : 0;



assign data_out = load ? Memory[addr] : 0;

endmodule