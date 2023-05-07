// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2022.2 (win64) Build 3671981 Fri Oct 14 05:00:03 MDT 2022
// Date        : Tue Apr 25 13:00:23 2023
// Host        : DESKTOP-T99OIQI running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode funcsim -rename_top bd_aa08_c_shift_ram_0_0 -prefix
//               bd_aa08_c_shift_ram_0_0_ bd_972b_c_shift_ram_0_0_sim_netlist.v
// Design      : bd_972b_c_shift_ram_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7a35ticsg324-1L
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "bd_972b_c_shift_ram_0_0,c_shift_ram_v12_0_14,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* x_core_info = "c_shift_ram_v12_0_14,Vivado 2022.2" *) 
(* NotValidForBitStream *)
module bd_aa08_c_shift_ram_0_0
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
  bd_aa08_c_shift_ram_0_0_c_shift_ram_v12_0_14 U0
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
`pragma protect encoding = (enctype = "BASE64", line_length = 76, bytes = 6784)
`pragma protect data_block
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
BA==
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
