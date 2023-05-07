`timescale 1ns / 1ps
// counter based
module clock_divider(
    input wire clk, //100MHz
    output reg divided_clk = 0// 1Hz => 0.5s ON and 0.5 OFF
    );
localparam div_value = 49999999; //1062; // 47KHz? (49999999)
// division_value = 100MHz/(2*desired Frequency) - 1 => 1Hz => 49999999
// counter
integer counter_value = 0;

always@ (posedge clk) // sensitivity list // rising edge 0-1
begin
// keep counteing until 1000
    if (counter_value == div_value)
        counter_value <= 0; // reset value
    else
        counter_value <= counter_value+1; // count up        
end

// divide clock
always@ (posedge clk)
begin
    if(counter_value == div_value)
        divided_clk <= ~divided_clk; // flip the signal
    else
        divided_clk <= divided_clk;
end    
endmodule
