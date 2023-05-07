// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2022.2 (win64) Build 3671981 Fri Oct 14 05:00:03 MDT 2022
// Date        : Sun May  7 15:13:23 2023
// Host        : DESKTOP-T99OIQI running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode synth_stub
//               c:/Users/Bruker/Documents/Bachelor_Elektro_ingenior_med_auto/fpga/project_2/project_2.gen/sources_1/bd/arty_adc_eth_v4/ip/arty_adc_eth_v4_clk_wiz_0_0/arty_adc_eth_v4_clk_wiz_0_0_stub.v
// Design      : arty_adc_eth_v4_clk_wiz_0_0
// Purpose     : Stub declaration of top-level module interface
// Device      : xc7a35ticsg324-1L
// --------------------------------------------------------------------------------

// This empty module with port declaration file causes synthesis tools to infer a black box for IP.
// The synthesis directives are for Synopsys Synplify support to prevent IO buffer insertion.
// Please paste the declaration into a Verilog source file or add the file as an additional source.
module arty_adc_eth_v4_clk_wiz_0_0(clk_out25, resetn, clk_in1)
/* synthesis syn_black_box black_box_pad_pin="clk_out25,resetn,clk_in1" */;
  output clk_out25;
  input resetn;
  input clk_in1;
endmodule
