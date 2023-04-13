`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11.04.2023 11:12:15
// Design Name: 
// Module Name: xadc_free_hand
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


module xadc_free_hand(
input wire clk,         // 100MHz
input wire Vaux4_v_p,   // analog port A0 positiv
input wire Vaux4_v_n,   // analog port A0 negativ
output reg [3:0] ledr,  // red leds.
output reg [3:0] ledb,  // blue leds.
output reg [3:0] led    // show results
    );

wire enable;
reg bad_address = 0;  
reg [6:0] address_in = 8'h14;
reg [15:0] busy_in;
wire [15:0] data;  // reg for adc data
wire ready;


xadc_wiz_1 adc
       (.daddr_in(address_in),
        .dclk_in(clk),
        .den_in(enable & ~bad_address),
        .di_in(busy_in),
        .dwe_in(1'b0),
        .reset_in(1'b0),
        .eoc_out(enable),
        .do_out(data),
        .vauxn4(Vaux4_v_n),
        .vauxp4(Vaux4_v_p),
        .vn_in(1'b0),
        .drdy_out(ready),
        .vp_in(1'b0));

reg _ready = 0;
always@(posedge clk)
    _ready <= ready;

  //led visual dmm              
always@ (posedge clk)
    if (ready == 1 && _ready == 0) begin
        case(data[15:2] / 2030)
        0:  led <= 4'b0;
        1:  led <= 4'b1;
        2:  led <= 4'b11;
        3:  led <= 4'b111;
        4:  led <= 4'b1111;
        default: ledb <= 4'b1111;
        endcase
     end 
          
always@ (posedge clk)
     if (ready == 0 && _ready == 1) begin    
        if (data[15:12] >= 4'h5) begin // switch default case
            bad_address <= 1'b1;
            ledr <= 4'b1111;
        end else begin
            bad_address <= 1'b0;
            ledr <= 1'b0;
        end
     end
     
    

endmodule
