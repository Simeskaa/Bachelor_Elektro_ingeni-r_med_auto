-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2022.2 (win64) Build 3671981 Fri Oct 14 05:00:03 MDT 2022
-- Date        : Sun May  7 15:13:23 2023
-- Host        : DESKTOP-T99OIQI running 64-bit major release  (build 9200)
-- Command     : write_vhdl -force -mode synth_stub
--               c:/Users/Bruker/Documents/Bachelor_Elektro_ingenior_med_auto/fpga/project_2/project_2.gen/sources_1/bd/arty_adc_eth_v4/ip/arty_adc_eth_v4_clk_wiz_0_0/arty_adc_eth_v4_clk_wiz_0_0_stub.vhdl
-- Design      : arty_adc_eth_v4_clk_wiz_0_0
-- Purpose     : Stub declaration of top-level module interface
-- Device      : xc7a35ticsg324-1L
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity arty_adc_eth_v4_clk_wiz_0_0 is
  Port ( 
    clk_out25 : out STD_LOGIC;
    resetn : in STD_LOGIC;
    clk_in1 : in STD_LOGIC
  );

end arty_adc_eth_v4_clk_wiz_0_0;

architecture stub of arty_adc_eth_v4_clk_wiz_0_0 is
attribute syn_black_box : boolean;
attribute black_box_pad_pin : string;
attribute syn_black_box of stub : architecture is true;
attribute black_box_pad_pin of stub : architecture is "clk_out25,resetn,clk_in1";
begin
end;
