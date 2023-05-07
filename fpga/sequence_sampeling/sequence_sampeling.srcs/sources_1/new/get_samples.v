`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 17.04.2023 13:41:35
// Design Name: 
// Module Name: get_samples
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


module get_samples #(num_of_mics = 4)
(
    input clk,
    input rdy,
    input [11:0] data,
    input [6:0] addr,
    input rst,
    
    output _finished,
    output _bad_address,
    output [12*num_of_mics-1:0] _buff_handler
    );

reg finished;
reg bad_address;
reg [11:0] buff_handler [num_of_mics-1:0];
reg [6:0] addr_q, addr_d;

assign _finished = finished;
assign _bad_address = bad_address;
assign addr = addr_d;

genvar i;
generate for (i = 0; i < num_of_mics; i = i+1) begin:instmem
    assign _buff_handler[12*i +: 12] = buff_handler[i]; 
end endgenerate

reg _rdy = 0;
always@(posedge clk)
    _rdy <= rdy;

always@ (posedge clk)
    if (rdy == 1 && _rdy == 0) begin
        if (addr_q != addr_d)
            finished = ~finished;
        
        if (addr_d == 8'h14)
            buff_handler[0] = data;
        else if (addr_d == 8'h15)
            buff_handler[1] = data;
        
        addr_q = addr_d;

    end

//integer counter = 0;
    
//always @( posedge rdy ) begin
//    case(addr)
//    14 : buff_handler[0] <= data;
//    15 : buff_handler[1] <= data;
////    16 : buff_handler[2] <= data;
////    17 : buff_handler[3] <= data;
//    default : bad_address <= 1'b0;
//    endcase
//    if (addr == 6'h14)
//        buff_handler[0] <= data;
//    else if (addr == 6'h15)
//        buff_handler[1] <= data;
    
//    if ( counter > num_of_mics-1 ) begin
//        finished <= 1'b1;
//        counter <= 0;
//    end else begin
//        finished <= 1'b0;
//        counter <= counter+1;
//    end
//end

always @( posedge rst ) 
    bad_address <= 0;

endmodule
