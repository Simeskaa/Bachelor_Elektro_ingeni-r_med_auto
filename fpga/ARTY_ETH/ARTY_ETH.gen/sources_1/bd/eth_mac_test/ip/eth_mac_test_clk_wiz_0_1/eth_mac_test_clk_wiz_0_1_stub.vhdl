-- Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2022.2 (win64) Build 3671981 Fri Oct 14 05:00:03 MDT 2022
-- Date        : Wed Apr 26 12:37:16 2023
-- Host        : DESKTOP-T99OIQI running 64-bit major release  (build 9200)
-- Command     : write_vhdl -force -mode synth_stub -rename_top eth_mac_test_clk_wiz_0_1 -prefix
--               eth_mac_test_clk_wiz_0_1_ eth_mac_test_clk_wiz_0_1_stub.vhdl
-- Design      : eth_mac_test_clk_wiz_0_1
-- Purpose     : Stub declaration of top-level module interface
-- Device      : xc7a35ticsg324-1L
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity eth_mac_test_clk_wiz_0_1 is
  Port ( 
    clk_out25 : out STD_LOGIC;
    resetn : in STD_LOGIC;
    locked : out STD_LOGIC;
    clk_in1 : in STD_LOGIC
  );

end eth_mac_test_clk_wiz_0_1;

architecture stub of eth_mac_test_clk_wiz_0_1 is
attribute syn_black_box : boolean;
attribute black_box_pad_pin : string;
attribute syn_black_box of stub : architecture is true;
attribute black_box_pad_pin of stub : architecture is "clk_out25,resetn,locked,clk_in1";
begin
end;
