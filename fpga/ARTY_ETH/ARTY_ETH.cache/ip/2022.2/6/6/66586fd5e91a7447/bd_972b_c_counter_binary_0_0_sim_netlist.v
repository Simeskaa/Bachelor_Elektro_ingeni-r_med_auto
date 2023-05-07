// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2022.2 (win64) Build 3671981 Fri Oct 14 05:00:03 MDT 2022
// Date        : Tue Apr 25 13:03:41 2023
// Host        : DESKTOP-T99OIQI running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode funcsim -rename_top decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix -prefix
//               decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix_ bd_972b_c_counter_binary_0_0_sim_netlist.v
// Design      : bd_972b_c_counter_binary_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7a35ticsg324-1L
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "bd_972b_c_counter_binary_0_0,c_counter_binary_v12_0_15,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* x_core_info = "c_counter_binary_v12_0_15,Vivado 2022.2" *) 
(* NotValidForBitStream *)
module decalper_eb_ot_sdeen_pot_pi_dehcac_xnilix
   (CLK,
    SCLR,
    THRESH0,
    Q);
  (* x_interface_info = "xilinx.com:signal:clock:1.0 clk_intf CLK" *) (* x_interface_parameter = "XIL_INTERFACENAME clk_intf, ASSOCIATED_BUSIF q_intf:thresh0_intf:l_intf:load_intf:up_intf:sinit_intf:sset_intf, ASSOCIATED_RESET SCLR, ASSOCIATED_CLKEN CE, FREQ_HZ 81247969, FREQ_TOLERANCE_HZ 0, PHASE 0, CLK_DOMAIN design_2_udp_mig_7series_0_0_ui_clk, INSERT_VIP 0" *) input CLK;
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
QHOMXLd+wSfE0FzjlbxR6ysk4edtZO1wU8OVy558Y3vHy8oEeG9ZFRaMMj6EcvdWB3fHZgmyYw7M
9wOFAwlqoS6Q9t5gLMEec5byKnxt7fpOp14myr18/I2a+EnsOHeh+lz9WzbF7RkkvZurdJY6/EZb
bFbhWYsKBJxKeAmLCMmsx+bYcmJFS8NLAA/wv8XM/haQ5UUh7o1yqY7yT4Lsbbs6dCMTrMZAs6N2
LT9kt+SSVnpZigeIvaU7mbKRIvidgzM5m3hGkQ8BYEP8CFHEBReN9+bAYWUVUE/Y1wgaz+Mb7iZi
q4TY9h+oTBjostkMZJhdrXY5YeNVyLjT3FaVew==

`pragma protect key_keyowner="Synplicity", key_keyname="SYNP15_1", key_method="rsa"
`pragma protect encoding = (enctype="BASE64", line_length=76, bytes=256)
`pragma protect key_block
e+uXtH1NghiTU3cca7tWp2GjsrAOlU5J8RU1kngmIfq9un0hBl1z+DpW3eGaWbKrHHILbLiKB6ZC
U3sZwqEY2XXW1Z93x3KGUCVwxFcaoCk2BJ+RB5SxhLQp+p+lbqd5mrpO1hHe4k0vhXDj2SLn5KLx
rJZ0D1EQ6h1t5PY5HrObw8gb0wXQ9P77bjDvWd1y/HiNkan6HHbWMZjwqz+vetflGwHtf6M/2uS3
ZPiBcwQFi/C1msFrBHktg90eD409U4u0BF6r+1CsZyGZGcH2Or/+y5rRWW/jzpxvtgCJWersl2BD
nRPcT1kw+W4eMldAY8SYZn2+2LeDg8XogA7fRg==

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
