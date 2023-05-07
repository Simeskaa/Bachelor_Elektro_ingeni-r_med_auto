// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2022.2 (win64) Build 3671981 Fri Oct 14 05:00:03 MDT 2022
// Date        : Tue Apr 25 13:00:23 2023
// Host        : DESKTOP-T99OIQI running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode funcsim -rename_top decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix -prefix
//               decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix_ bd_972b_c_shift_ram_0_0_sim_netlist.v
// Design      : bd_972b_c_shift_ram_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7a35ticsg324-1L
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "bd_972b_c_shift_ram_0_0,c_shift_ram_v12_0_14,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* x_core_info = "c_shift_ram_v12_0_14,Vivado 2022.2" *) 
(* NotValidForBitStream *)
module decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix
   (D,
    CLK,
    CE,
    SCLR,
    Q);
  (* x_interface_info = "xilinx.com:signal:data:1.0 d_intf DATA" *) (* x_interface_parameter = "XIL_INTERFACENAME d_intf, LAYERED_METADATA undef" *) input [0:0]D;
  (* x_interface_info = "xilinx.com:signal:clock:1.0 clk_intf CLK" *) (* x_interface_parameter = "XIL_INTERFACENAME clk_intf, ASSOCIATED_BUSIF q_intf:sinit_intf:sset_intf:d_intf:a_intf, ASSOCIATED_RESET SCLR, ASSOCIATED_CLKEN CE, FREQ_HZ 81247969, FREQ_TOLERANCE_HZ 0, PHASE 0, CLK_DOMAIN design_2_udp_mig_7series_0_0_ui_clk, INSERT_VIP 0" *) input CLK;
  (* x_interface_info = "xilinx.com:signal:clockenable:1.0 ce_intf CE" *) (* x_interface_parameter = "XIL_INTERFACENAME ce_intf, POLARITY ACTIVE_HIGH" *) input CE;
  (* x_interface_info = "xilinx.com:signal:reset:1.0 sclr_intf RST" *) (* x_interface_parameter = "XIL_INTERFACENAME sclr_intf, POLARITY ACTIVE_HIGH, INSERT_VIP 0" *) input SCLR;
  (* x_interface_info = "xilinx.com:signal:data:1.0 q_intf DATA" *) (* x_interface_parameter = "XIL_INTERFACENAME q_intf, LAYERED_METADATA xilinx.com:interface:datatypes:1.0 {DATA {datatype {name {attribs {resolve_type immediate dependency {} format string minimum {} maximum {}} value data} bitwidth {attribs {resolve_type generated dependency data_bitwidth format long minimum {} maximum {}} value 1} bitoffset {attribs {resolve_type immediate dependency {} format long minimum {} maximum {}} value 0}}} DATA_WIDTH 1}" *) output [0:0]Q;

  wire CE;
  wire CLK;
  wire [0:0]D;
  wire [0:0]Q;
  wire SCLR;

  (* C_AINIT_VAL = "0" *) 
  (* C_HAS_CE = "1" *) 
  (* C_HAS_SCLR = "1" *) 
  (* C_HAS_SINIT = "0" *) 
  (* C_HAS_SSET = "0" *) 
  (* C_SINIT_VAL = "0" *) 
  (* C_SYNC_ENABLE = "0" *) 
  (* C_SYNC_PRIORITY = "1" *) 
  (* C_WIDTH = "1" *) 
  (* c_addr_width = "4" *) 
  (* c_default_data = "0" *) 
  (* c_depth = "1" *) 
  (* c_elaboration_dir = "./" *) 
  (* c_has_a = "0" *) 
  (* c_mem_init_file = "no_coe_file_loaded" *) 
  (* c_opt_goal = "0" *) 
  (* c_parser_type = "0" *) 
  (* c_read_mif = "0" *) 
  (* c_reg_last_bit = "1" *) 
  (* c_shift_type = "0" *) 
  (* c_verbosity = "0" *) 
  (* c_xdevicefamily = "artix7" *) 
  (* downgradeipidentifiedwarnings = "yes" *) 
  (* is_du_within_envelope = "true" *) 
  decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix_c_shift_ram_v12_0_14 U0
       (.A({1'b0,1'b0,1'b0,1'b0}),
        .CE(CE),
        .CLK(CLK),
        .D(D),
        .Q(Q),
        .SCLR(SCLR),
        .SINIT(1'b0),
        .SSET(1'b0));
endmodule
`pragma protect begin_protected
`pragma protect version = 1
`pragma protect encrypt_agent = "XILINX"
`pragma protect encrypt_agent_info = "Xilinx Encryption Tool 2022.2"
`pragma protect key_keyowner="Synopsys", key_keyname="SNPS-VCS-RSA-2", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=128)
`pragma protect key_block
c/wA5liyV/LPsKRmFzwxOzMM9n38OKoskM2eV12+p8ymcpS5TSWtutYPfQvZnGZZfd8i/h93sskE
aYtyaj9r82ZsRS//wjee3CGcJ96gsie1s/zVMyvtQwl06PGFCfBpzauOVKiMwENeLpUT1RKqAXkx
Yl5ZRwDQye7scTEiJ00=

`pragma protect key_keyowner="Aldec", key_keyname="ALDEC15_001", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
pvq46JXLahp5XPx+a/0qqI+q3DAS5hdJHtrc58f+wKPIWSonA73Ry+sA2G22W5m9gcLjdutlrO3Z
tCFoOk9903pekANOyDnxNVC3XokdoOx60qR9SkTdoRSoFtoxsXGHf/DcXUII9M+W0bO/CDmYDcNo
r7aqLbU+SA6OqBOCM8rMYE4IRqWsN0B39RVdHWhmWVgQBS2mZk+30c3XYyN7rnCOE6eaGwaVtnwH
VfWH9pTe4g8uibOl93VQ7HnnI1im9xFEv0e1HXGZooWf4JBBcPjWG2olWoMegh1BWyXPDYsLai8q
DiMBE0Qcpk5n0TNTCsarWZUuaxcDrGxLdPdlKQ==

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-VELOCE-RSA", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=128)
`pragma protect key_block
mB8YWCR0O9x0T00SavylLJzD4EOwijo0xEcicZ6cVxQZWuyWbx+k/ZiPXGZlw54BI2rUVCcV2BLI
4gUw7aTkHqyMqWOZpc4RgAwB2x7+FB4EO/gBeGyMowJrid6yIiuOU1eXMIJlEudw057p9X069359
VOBwC7cPvZI8vSf4TAU=

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-VERIF-SIM-RSA-2", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
Q3No/YDkVIy0FiweeVvn76i7Ri3EOYVbYAiHi2wWauttiokshnXqj8dkiKMFGvPocjMgQabi5r+y
aL7TsVpBMAiOxtVu1Mt6MAqN751M3k7qrb0Z0nLX3H/YHpXC7njMit3jmOHIafYANCF1YyMgR06C
lsmoPymvHm7N9d9Bj92VCkDOO0UYArO9YpQYzlUCe4iN6Bawbjge00kwpPm06b+LF85F+tlqlAxx
ntSor+XsBKxptIxSH+4BJafJ02+0JVXsdURVaycuWGCJsvUAbWNiRoPeN2woA3V/7ZIp551OSSJA
FHwaGLDcmtxipE0tjMmg/fMt8sEatgUs9amLcA==

`pragma protect key_keyowner="Real Intent", key_keyname="RI-RSA-KEY-1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
jnx7WBfdUta1DP+YRTT3fGRtjq857NO8Wcmmz63XNNB7mnqRUarhreRnndqogngF5poSxm+Fp9Qe
5/N64PQhcrXe7INbzX7GqJBCYQaDzLlx56Ezocscr/wB/94g1XHh5C7L+OaGsz73/C6nTrTx+qoO
vYXsLhOATbupH15I0QqrflKRn191h77YQ6O9D2LbiFJLiBIlQibYncy/VYCVBL3bZwpru4o+gy64
EClBbsC0+k/WEH0aCsQDlF37rB3VMvcwl0smwqdm6RZ2gzh2ohWxtz+8yh604ISRnvEqw+NQyZQf
QshGn3q1u43MADSpPe9C5Gl4T6pk+LZ/JSs3lw==

`pragma protect key_keyowner="Xilinx", key_keyname="xilinxt_2021_07", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
S4JCYpvS357WfAEsQX/qUC4UZCr/A2YWWyJiXN9E8HjVpOdVBXoy9Yw4qqWt5SAZDrW3fpCiU6Xk
I3QWXZAsQv0gGfjq5c+nhZBf5SZ75y594X6JmZur+YdJk/D0QxsIXGWxZsRjfV5PXynYs9YZuxMc
PY5DzwXE9IIacOBWm31qWbCIhMpZwoDkmkU6+q8bWNbhSwGwr+XN9yy9KdFMwoQUPjQ7CL0HdF+o
DYz5SXrTzlc+1BZNT82zYZqGwxDcghaR33/vWKZMzqeR3ZpnIUUZBKJIroCkx+oEaeczxK5/DBcc
t7cgRzglxN2qg60fApXAf3SDcJ/+weCZKL1nGw==

`pragma protect key_keyowner="Metrics Technologies Inc.", key_keyname="DSim", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
Vjtlu8KNjnlNuUIE5zPRhhb8tB0OK/vR9xaBOqOYDrP2jeqyxMSFwVjyddbpvhJa4cs7tpaKRfqn
s4JFJ7oeyKOadS9yc/j1irJpOQQ4riipe4vewDCIq71FwpXqXOnRlt26x0r5rH9Y5eNCMItZs5II
8VnEtl8vauM5POdGNhFUGryFciFJg/7/xFV29uZxlno+WssvhIerE0b6i4Yj6PdEVf4KX2tMA8l9
g+sUhj5pwuErpZh8WwZYeve4N9FuVSUYlMmxJgpjPBPRdHXOtONBerkAJMxrr/1DhwILKg0RB3sm
rGYB7e6AiN9fJHD89spJ4K1S4h200ROiEbpNug==

`pragma protect key_keyowner="Atrenta", key_keyname="ATR-SG-RSA-1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=384)
`pragma protect key_block
G43T8ZCfcyBws9KaAojYCDvIQxBJSUDk3BWoc7oxKs/Bh7fzJ8yxhRl3C4UER8pby+YR52a1OhxH
Gpcoj3PHLWs8FpQkDOgIbp7KEdqdbJ/7IjPbOWyn+Mjgni7Jk9ZsKLq023EGhEwxyz8KR492uBhP
y2S7Pkb9myeTsa6kHt6qseaYyHJG4Tt6iwEaQSFLscOQwGw2eNnH3Bm6v4ZEqL0W0iIpBqYvpeiE
GJApSzBSZ30dACWN2sN0OuBC0/IXNmR+syVqSB+PO/GN1n1p9E+ltyzmOgWeWiqBwxJhstmViafi
01TSaGccEU1yzCSNTWINZ7UhLf+0zGvHXdPZRblwHA91uxGramDe4ElhhYOLpbY8aKN1Tvst37Lw
Ev1cq+WJTrArjWnNufDZAxwO0huX9sDiT19/v28kSfYeTzFRxcyjCSRSjUxhmYMR+EM8DNfpvWFu
V2tqwwoQ35phMEIidKsu81KHd6hjUph5Ii3jbgSuDXYqHydSoflU4FZT

`pragma protect key_keyowner="Cadence Design Systems.", key_keyname="CDS_RSA_KEY_VER_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
LTVGG4EqxAN35+EjEQ5dQgqkhUon8FKa6+oaA5F3/XQpOpJaz5NletAny4izGuEj/Rcko5Mb15Sv
55lokHX4MQDMfJEvj/xRT2uEHXNljDKmKN8zikxCTdy9H1PdStFfNS1CWujTtex7/zc9dxqgOd67
QcK7WbgKgh04q+osXEo4VG7R4xmwNDdiprgPhEOw+q0jLkLX9kdvNuzZ4KkdTBFHG2q2Ho4epXzg
wTRR/KDnf9ffxfSFCsxB49EOByzVzzdO2bud/VCR5VKw5dgQ3uTI6BTBEGKOe0igY+nZ2l6VtFv3
OL3+xEJUZheoPKRNA62H+2zw/prkdd2r+oBWOA==

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-PREC-RSA", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
Od97fXGtl2pdDYJM5SZFje+SlTpQtyGwZ3a8telkZsGyjMLwGnVM+6z6QJBOfAk/Zw2cQ1Xw7Jxn
6u19tH7npASezvq8JUVoJKXPmaZ0bn5twwhP/VbAXPTng64toQCkCxnQh7DFBC0Ib70helnjIOsd
JvyeQJBDhNNKWqMjN52+eeVUx65BFqm9NeU/qa47OQJvlkjHVsX5k65n6BWPYuYdzPCE1tn3GkxU
azfAsWC65XFXP4/6ezSk845QjRWDd3N9yVcfcMetYVFGqUaEvDJmICewYtQeQrKC6FpbZq4Zyf9p
hfKU/NTQUPfxTDuCyh3UeEbM5x0udPqE2p/Qxw==

`pragma protect key_keyowner="Synplicity", key_keyname="SYNP15_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
JNSsfcpthLCWzhzPfHOOrmALUDwSxJwGvCXUF5yrn0HppXGcDnSIA4ljhiAF3144x8ukwJ7UhvST
P3BFBu2/CvbjJ4b5FcuniTMx7v5g8P8rZAy4WZ5kmU0oYAgisvd70/kOGxy6fVT4hvBGj1jx8P8V
pNfJepYjAKhVG3jT+u1PrLvQaE3bw18bQksQ9weBN91Tkl4HXbIEWPGwyYExNhSVx3cuFry7bYix
L5kiHEnJveDaKtjrCXpRilGuo9h/YAidE6fsUUdKip3b8X7RjLBmh3yHPmY6A6pZJJNd0GMPRQKB
fpX2/tfyqD0ZjUwC7c8jtnZIXRQryp2c0sI7hg==

`pragma protect data_method = "AES128-CBC"
`pragma protect encoding = (enctype = "BASE64", line_length = 76, bytes = 6896)
`pragma protect data_block
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
`pragma protect end_protected
`ifndef GLBL
`define GLBL
`timescale  1 ps / 1 ps

module glbl ();

    parameter ROC_WIDTH = 100000;
    parameter TOC_WIDTH = 0;
    parameter GRES_WIDTH = 10000;
    parameter GRES_START = 10000;

//--------   STARTUP Globals --------------
    wire GSR;
    wire GTS;
    wire GWE;
    wire PRLD;
    wire GRESTORE;
    tri1 p_up_tmp;
    tri (weak1, strong0) PLL_LOCKG = p_up_tmp;

    wire PROGB_GLBL;
    wire CCLKO_GLBL;
    wire FCSBO_GLBL;
    wire [3:0] DO_GLBL;
    wire [3:0] DI_GLBL;
   
    reg GSR_int;
    reg GTS_int;
    reg PRLD_int;
    reg GRESTORE_int;

//--------   JTAG Globals --------------
    wire JTAG_TDO_GLBL;
    wire JTAG_TCK_GLBL;
    wire JTAG_TDI_GLBL;
    wire JTAG_TMS_GLBL;
    wire JTAG_TRST_GLBL;

    reg JTAG_CAPTURE_GLBL;
    reg JTAG_RESET_GLBL;
    reg JTAG_SHIFT_GLBL;
    reg JTAG_UPDATE_GLBL;
    reg JTAG_RUNTEST_GLBL;

    reg JTAG_SEL1_GLBL = 0;
    reg JTAG_SEL2_GLBL = 0 ;
    reg JTAG_SEL3_GLBL = 0;
    reg JTAG_SEL4_GLBL = 0;

    reg JTAG_USER_TDO1_GLBL = 1'bz;
    reg JTAG_USER_TDO2_GLBL = 1'bz;
    reg JTAG_USER_TDO3_GLBL = 1'bz;
    reg JTAG_USER_TDO4_GLBL = 1'bz;

    assign (strong1, weak0) GSR = GSR_int;
    assign (strong1, weak0) GTS = GTS_int;
    assign (weak1, weak0) PRLD = PRLD_int;
    assign (strong1, weak0) GRESTORE = GRESTORE_int;

    initial begin
	GSR_int = 1'b1;
	PRLD_int = 1'b1;
	#(ROC_WIDTH)
	GSR_int = 1'b0;
	PRLD_int = 1'b0;
    end

    initial begin
	GTS_int = 1'b1;
	#(TOC_WIDTH)
	GTS_int = 1'b0;
    end

    initial begin 
	GRESTORE_int = 1'b0;
	#(GRES_START);
	GRESTORE_int = 1'b1;
	#(GRES_WIDTH);
	GRESTORE_int = 1'b0;
    end

endmodule
`endif
