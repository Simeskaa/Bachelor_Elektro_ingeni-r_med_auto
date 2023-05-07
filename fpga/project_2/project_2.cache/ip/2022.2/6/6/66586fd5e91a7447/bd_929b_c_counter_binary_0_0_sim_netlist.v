// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2022.2 (win64) Build 3671981 Fri Oct 14 05:00:03 MDT 2022
// Date        : Wed Apr 26 16:24:04 2023
// Host        : DESKTOP-T99OIQI running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode funcsim -rename_top decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix -prefix
//               decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix_ bd_929b_c_counter_binary_0_0_sim_netlist.v
// Design      : bd_929b_c_counter_binary_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7a35ticsg324-1L
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "bd_929b_c_counter_binary_0_0,c_counter_binary_v12_0_15,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* x_core_info = "c_counter_binary_v12_0_15,Vivado 2022.2" *) 
(* NotValidForBitStream *)
module decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix
   (CLK,
    SCLR,
    THRESH0,
    Q);
  (* x_interface_info = "xilinx.com:signal:clock:1.0 clk_intf CLK" *) (* x_interface_parameter = "XIL_INTERFACENAME clk_intf, ASSOCIATED_BUSIF q_intf:thresh0_intf:l_intf:load_intf:up_intf:sinit_intf:sset_intf, ASSOCIATED_RESET SCLR, ASSOCIATED_CLKEN CE, FREQ_HZ 81247969, FREQ_TOLERANCE_HZ 0, PHASE 0, CLK_DOMAIN design_1_mig_7series_0_0_ui_clk, INSERT_VIP 0" *) input CLK;
  (* x_interface_info = "xilinx.com:signal:reset:1.0 sclr_intf RST" *) (* x_interface_parameter = "XIL_INTERFACENAME sclr_intf, POLARITY ACTIVE_HIGH, INSERT_VIP 0" *) input SCLR;
  (* x_interface_info = "xilinx.com:signal:data:1.0 thresh0_intf DATA" *) (* x_interface_parameter = "XIL_INTERFACENAME thresh0_intf, LAYERED_METADATA undef" *) output THRESH0;
  (* x_interface_info = "xilinx.com:signal:data:1.0 q_intf DATA" *) (* x_interface_parameter = "XIL_INTERFACENAME q_intf, LAYERED_METADATA xilinx.com:interface:datatypes:1.0 {DATA {datatype {name {attribs {resolve_type immediate dependency {} format string minimum {} maximum {}} value data} bitwidth {attribs {resolve_type generated dependency bitwidth format long minimum {} maximum {}} value 24} bitoffset {attribs {resolve_type immediate dependency {} format long minimum {} maximum {}} value 0} integer {signed {attribs {resolve_type immediate dependency {} format bool minimum {} maximum {}} value false}}}} DATA_WIDTH 24}" *) output [23:0]Q;

  wire CLK;
  wire [23:0]Q;
  wire SCLR;
  wire THRESH0;

  (* C_AINIT_VAL = "0" *) 
  (* C_CE_OVERRIDES_SYNC = "0" *) 
  (* C_FB_LATENCY = "0" *) 
  (* C_HAS_CE = "0" *) 
  (* C_HAS_SCLR = "1" *) 
  (* C_HAS_SINIT = "0" *) 
  (* C_HAS_SSET = "0" *) 
  (* C_IMPLEMENTATION = "0" *) 
  (* C_SCLR_OVERRIDES_SSET = "1" *) 
  (* C_SINIT_VAL = "0" *) 
  (* C_VERBOSITY = "0" *) 
  (* C_WIDTH = "24" *) 
  (* C_XDEVICEFAMILY = "artix7" *) 
  (* c_count_by = "1" *) 
  (* c_count_mode = "0" *) 
  (* c_count_to = "1100000000000000000000" *) 
  (* c_has_load = "0" *) 
  (* c_has_thresh0 = "1" *) 
  (* c_latency = "1" *) 
  (* c_load_low = "0" *) 
  (* c_restrict_count = "1" *) 
  (* c_thresh0_value = "1100000000000000000000" *) 
  (* downgradeipidentifiedwarnings = "yes" *) 
  (* is_du_within_envelope = "true" *) 
  decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix_c_counter_binary_v12_0_15 U0
       (.CE(1'b1),
        .CLK(CLK),
        .L({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0}),
        .LOAD(1'b0),
        .Q(Q),
        .SCLR(SCLR),
        .SINIT(1'b0),
        .SSET(1'b0),
        .THRESH0(THRESH0),
        .UP(1'b1));
endmodule
`pragma protect begin_protected
`pragma protect version = 1
`pragma protect encrypt_agent = "XILINX"
`pragma protect encrypt_agent_info = "Xilinx Encryption Tool 2022.2"
`pragma protect key_keyowner="Synopsys", key_keyname="SNPS-VCS-RSA-2", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=128)
`pragma protect key_block
KdkdvVsuosc8qR9X5PxQ/ghTeTrEz4qKVuenhDR9wRSL/BO/mhSwQtiFj74UO0sGv0zvjAntaq/3
l2/v8gOiVKmM666gbk/2UCISA4OFA3FDR9jYmiXdNXb2qHeS1ywQz5n/sTR5iu4KFEfwrl3IXtQw
aEiGegL+CQMaovJsto4=

`pragma protect key_keyowner="Aldec", key_keyname="ALDEC15_001", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
pZCj3qT3VD1SCS5RiZExsqqu16KpMtHXilQL9p5/eBl7qrfQjT1VhFtVbYUusepbChjsCCmCn7hr
72SuHmOmDWG78UARN7MLdO/+sePuyS06ak4nAw5xwjT0g+9970uMWYKvTeeYqoz2i+k+zX60Cuvu
iwBfxWM22DqukHlYzbEFWhNyXIkgJe71p67vGdXBmqu4/2wmlwGApqBxlwR+alwZ9UGHlxNQS4N5
z1wHu3Cp8LwGRjlaXjElcY8RDpvyz5l59ey8ar5HXR9Zqf6e1unE2NdhzHhEGRerRFXoKZppk1HB
6kIEY4EHAWz+HvPcqoP9eoYKDazoAGkJRVP6YA==

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-VELOCE-RSA", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=128)
`pragma protect key_block
gLgm7VvY3cNcNvdXvikCQd2nRniE4ae4hePOcAUlPDMoHDzQAD7Ngo12MGFns9JNPcCaUXfAmxL2
JNGojjrDRUWrv8FPV6FOEbDHs96fef8+gqLF4OqLck4kWpKhnJwaJjjzQirvXEzZxP+GsBKnkSp8
ceVlZJwP0F6XRv+RpQA=

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-VERIF-SIM-RSA-2", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
GeZP242oKQSNuofqDs4oIIXZEufPhRVrlFFeRSLY4VCxhMEMwfPrNXe33xO0zIEBoPW2X9mvUoTY
izdWQEtWImFzjzPCjkSLhEdIMmUBH02Y+Tw3eW5x23T0cK96pmoV2MH8kl99I27MN6stVd977fuB
Mjao5MnSXIGZ/uXGtgfUO9Zjs4/2wGmsI2/lANN2WOL9Sz4xeA8k40c2dNYgxgHoCwx8Ya/RYIZS
Cpuvzq4ZyFSNT/kMXnUmqj75/flpXT3mmyW+frexux3j9PxpKHmxAE9crvDx85rMamGiA4ftl+ac
H0FtL2cBqdlP60x+FjqleWCJoN6AYdxA0YZaeg==

`pragma protect key_keyowner="Real Intent", key_keyname="RI-RSA-KEY-1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
URmEGftuxvv0+tViRUdsFNnPXucZlVDfUQpjjXkpOA38QUzsIL9j1pGGp9doC4jcg/9MD149BTSw
vAG8684a3k+Tx/8sFGl/viK1q8ty9nktEABSahv8Etm5ZJVAzQJT7EaOzrYqyywSwabogvGUmN/7
DE3eOn6+sMCiMl6BLUhYyK39ntTWNFYVPiheclbBb36V1vzMOQl0mvPuS4hDXqba/+qBZXhqeYWK
ceNfwci6SsRRef6hLF/1S+20r2uBxJeYJjyfWGGFEGfxlAOz1MiYUUR/bEHWnbjwIcJTBHQNRdq4
4Ryb+iPuKcsXU/8ApD14i6ScW+VBPWSqnH9w+A==

`pragma protect key_keyowner="Xilinx", key_keyname="xilinxt_2021_07", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
NtQgA3rUKfJt+21sTot44yr4gmte57FoFl8Q/327tsRJeEyNAiwWZaZN2mbo2NFcvyN2GhDw6avJ
NsF1Oxs36P8shoqOOiloWWrdTcyAdMhdk+UjeZgKcNSqd4Js87w/5LVQTwjB2mcBDfe1jrivv+IW
ZRBC8NvlW5z/1wF7+vzXRMziLQYeOkLB0OkpIY+eT5cZXDKuZ+4l0FMPjd+El96JGAEHG7Q0qS3F
OEApYEp8+nSZnragoytq4pkhVJEC22ye0hBhoBClJpszCcg0u+Ugf+mYZsj8BC2uqSY6Hh/gpjjw
enQ7aEYBaUR7GCwQN7fZmNhZYtBkyvNqydRQcA==

`pragma protect key_keyowner="Metrics Technologies Inc.", key_keyname="DSim", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
CpIFM8Y8dBmpjtOVnOKcfppEFV+c1cRgsQtewNUe+5apiLDoRCdMyTqoCay7nz+Xagc0OvfZDg/Y
jSTsDjKVcEIyxOfix7iwjKW8Rz+a5wBIatI8wfCo7uLtuucz9otOWWI7BFQ2gn4VdQ73HJJlZMMY
OyEOd33tGjNSjxz3W07knDr1FwTE3BOfhq+Qj2ErnuV1dQbrTb3MiQMTnHaTCwtz6ip0pD6b5G4K
kBRUYe+UNXCMvSfNIN9MPSmolO4MjNwM5gnZZqLcR1hGuzH/Yeb/jPnhsZ7jFvlTT3nsM9JzMRAE
QwlzVuulHKQDS2I96arFosYPYMsalmn6CQW0gg==

`pragma protect key_keyowner="Atrenta", key_keyname="ATR-SG-RSA-1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=384)
`pragma protect key_block
qinIxHFISC9r9LS7OKOuYVGM5EBkuuQNV1nDRui+QVNLn2QFCrWPeEClQIlNViKOt8MX9urHvu4e
l2L+eZKw6+St9cW9yUsYu36yoB4LqwG+vKvfR9CW82LGPyMAxdgk/p3n+F0Xp9Y2HaERwWDL99tW
V7cDvLLhyIwz7w4rI0BWWV+KMjXP2F5MNgykzZn7tzV8oY6MxOykFqRdI8DLAdlYGAs90wjJ3x84
S3fHciSox97FYpDi64v31Vb4RmRrwueXcvCc3w8gzjuwg7qraWLMYyPB+mERB2v1htX80PsWWVHE
QXkWiHWYvvrXEykUS04MmLNHpV8ZgBXO/NBEGn7mrITDEswk3u1Yviqy7CW2wLPQBoo5xW+uiu2e
8YZV/E+bAt+P/EH5RsC9alBgtuVKU1s9DaiEH8eUPEgJQ/TXwQW01pg8ECTYgiBS+IQSbld23aq3
goVo0ZMzRu/SA00Jmwt7upvsMkh9Q+2732ahu1FmlSNmyNGB1+bYf782

`pragma protect key_keyowner="Cadence Design Systems.", key_keyname="CDS_RSA_KEY_VER_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
T1jqx5hmzZZMhPApzUC1oZLMAkHma8Ki4b2CvLNqxSn+MNWoTPomvQ775DMBEDai/gahYALsohdX
0f/e6LuPqt4zYtyAzmH+nRgOG/tilS1J674KsaHxudAfo4sM3awB/C4Q3VdYsO9FgvPQylnYKSGE
gJ46W+1Y789VQqPbt4dpnprhix6sLlwfww7We6cq2wu4PilFzovejouUBZqNMZHYi4suKcMcenp3
C7QRKloo8IF9yKrhGPcRJLQt2nus3bI0Q3ICxRk13Nrfhh/z4cdm0OGXz42q44snFEVy1lLxPOs7
W9tSe5ag3923oCT4NGGgK/gMTx5qXxFhV2MJUw==

`pragma protect key_keyowner="Mentor Graphics Corporation", key_keyname="MGC-PREC-RSA", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
CQ6Xz1vsXKcluPrOKO/u1Ff+J+6Ot8F+UKyCuTJ5yLizialmsj0wDB5YVyUtIi0DzWKt9w28iXWa
fgpK821PzYgs0Xy9kwNKaQTiZgZkmvtlKLU5MitaxXhgIVjuotHhLAwdstIDbQRnFl2LBt3anHnl
4xZuqLWdUZ+dIj/1kKc6igB1tLdin6EXUZcX8zr+LSlRkceHE+RgoXiah7bZ2tUJJSFmx9kSB9gy
oYOYsu1iT0iy6D73rzmYIM+SZD0ncnB7kH7U5vXan7IMX1mzWshL51gbTc24jn4o2tAuFwoXACCd
5zCu+FAst0cLPwMax4p5AovMs6qRkiK0xAe6OA==

`pragma protect key_keyowner="Synplicity", key_keyname="SYNP15_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
FTSoiMHqHJceQqTOl/d4cRkr2UlrLKNWTNnDH45UcTB+GahPDWdOv/QmV/p9f4O4FCqCzDsQZFwV
zznCGNaHoSLWoq9D4NYwut6ykP/hn+UBv2kVNbm4UCU1ZTpXpobV/UOasFNadkWOGAx0WOLmJZmY
PHCIHjdRxETI60KBogkry2C7L9C3flBeAo2UTZXk7j6N5KjPdJZ7N1rNmbUkKtAdGU82VhdmA3cP
92m6TOINa1GGTaIIxTR1SWaPbncC2LR6aNM6y5HLoA/7s4wScFsBWszgr1RTueFyFrmVFUMWb2+9
1lboNdtq5O+re4wZiKMy6oT6c1Qtae2a1aCdyA==

`pragma protect data_method = "AES128-CBC"
`pragma protect encoding = (enctype = "BASE64", line_length = 76, bytes = 14912)
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
