`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 15.04.2023 11:26:08
// Design Name: 
// Module Name: DC_base_removal
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module DC_base_removal(
    input clk,          // 100 MHz
    input ready,        // x has been changed
    input [11:0] x,     // signal
    
    output [11:0] _y
    );

reg y;
reg [11:0] x_prev = 0;
reg [11:0] y_prev = 0;
reg [11:0] alpha = 0.98;    // problem when trying to multiply with x. float has a different bit structure then an int. 

assign _y = y;

always@ ( posedge ready ) begin
    y = alpha * x - alpha * x_prev - alpha * y_prev;
    y_prev <= y;
    x_prev <= x;

end
endmodule