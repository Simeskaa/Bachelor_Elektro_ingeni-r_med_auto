// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2022.2 (win64) Build 3671981 Fri Oct 14 05:00:03 MDT 2022
// Date        : Wed Apr 26 16:38:33 2023
// Host        : DESKTOP-T99OIQI running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode funcsim -rename_top decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix -prefix
//               decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix_ bd_929b_c_shift_ram_0_0_sim_netlist.v
// Design      : bd_929b_c_shift_ram_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7a35ticsg324-1L
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "bd_929b_c_shift_ram_0_0,c_shift_ram_v12_0_14,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* x_core_info = "c_shift_ram_v12_0_14,Vivado 2022.2" *) 
(* NotValidForBitStream *)
module decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix
   (D,
    CLK,
    CE,
    SCLR,
    Q);
  (* x_interface_info = "xilinx.com:signal:data:1.0 d_intf DATA" *) (* x_interface_parameter = "XIL_INTERFACENAME d_intf, LAYERED_METADATA undef" *) input [0:0]D;
  (* x_interface_info = "xilinx.com:signal:clock:1.0 clk_intf CLK" *) (* x_interface_parameter = "XIL_INTERFACENAME clk_intf, ASSOCIATED_BUSIF q_intf:sinit_intf:sset_intf:d_intf:a_intf, ASSOCIATED_RESET SCLR, ASSOCIATED_CLKEN CE, FREQ_HZ 81247969, FREQ_TOLERANCE_HZ 0, PHASE 0, CLK_DOMAIN design_1_mig_7series_0_0_ui_clk, INSERT_VIP 0" *) input CLK;
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
e1qXPAzrtWz9idCEN1ukNjAifnFC9CJm2REsalzktgsokJvFfvSKlc2wigGNWb32rtmHkh2EcUL/
8gei6TG2uee58wfwTRbK1tux6BBnpW23nERaEszwTfLGucpFHWPUR2svzZeLUP1pY1bJJFqxL+Yt
iB0m6bzMN78dVwhbFpLklkpTyKBOrGwXMC4Csl19Q3h8yavVMZScfZRQSvjlNLKlZ0r6DUw8I1fD
jbEhpbMVjgxr+geUQK3kAbsdlNoidpQgiqcSdlh2aGiuNpwAExZel941HuFOwTjbwuoNocm/3Ur8
NjNv+oLz+KQRdrhgItJac6fwSylI6dWXnVrzeA==

`pragma protect key_keyowner="Synplicity", key_keyname="SYNP15_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
dRSHeglg9EauXGgM21I7C5yDbin9cwsulL0rLqTE88Ks08LzPTJqGZDWpbArbQ/y9DcvMajJc6lL
hOtTe++KEkO9jkdJXHa/j8LpUaz55DplJ7jT0C4vKnPE4otqbHYKtbSmzFCRVNyItHWk62FXIJhx
0eQTSSnzK1NusziR6+e2UToU1J6rXKTCJqxeehvuZBh2E5Q6cEqawD8pkOCdRmmCJ0LR0I+JsixM
l32VwooJfiSitcL9Tihn0/LJVhwUoUj/+uNi3cFFSJ2WlizUNThCePL/emEBWXt3JGuVq10EYYVJ
trmlEvAC6DWkCL/uGZB2C8S9CSkuyPnhzarpRw==

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
