`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 15.04.2023 16:19:54
// Design Name: 
// Module Name: fill_buffer
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


module fill_buffer #(num_of_mics = 4, buffer_len = 4096)
(
input handler_rdy,
input [12*num_of_mics-1:0] data,
input counter,

output _write,
output [12*num_of_mics*buffer_len - 1 : 0] _buffer_vector
);

reg [11 : 0] buffer [buffer_len*num_of_mics-1 : 0];
reg [12*num_of_mics*buffer_len - 1 : 0] buffer_vector;
reg [11:0] handler [num_of_mics-1:0];
//reg write;

genvar i, j;
generate for (i = 0; i < num_of_mics*buffer_len; i = i+1) begin:for_mics
        assign _buffer_vector [12*i +: 12] = buffer[i];
end endgenerate

generate for (j=0; j < num_of_mics; j=j+1) begin:for_handler
    assign data [12*j +: 12] = handler [j];
end endgenerate
    
integer mic;    
always @( posedge handler_rdy ) begin
//    write = ~write;
    
    for (mic=0; mic < num_of_mics; mic=mic+1)
        buffer[counter+mic*buffer_len] <= handler[mic];
    
//    write = ~write;
end
    
endmodule
