// Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2022.2 (win64) Build 3671981 Fri Oct 14 05:00:03 MDT 2022
// Date        : Tue Apr 25 13:03:41 2023
// Host        : DESKTOP-T99OIQI running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode funcsim -rename_top bd_aa08_c_counter_binary_0_0 -prefix
//               bd_aa08_c_counter_binary_0_0_ bd_972b_c_counter_binary_0_0_sim_netlist.v
// Design      : bd_972b_c_counter_binary_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7a35ticsg324-1L
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CHECK_LICENSE_TYPE = "bd_972b_c_counter_binary_0_0,c_counter_binary_v12_0_15,{}" *) (* downgradeipidentifiedwarnings = "yes" *) (* x_core_info = "c_counter_binary_v12_0_15,Vivado 2022.2" *) 
(* NotValidForBitStream *)
module bd_aa08_c_counter_binary_0_0
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
  bd_aa08_c_counter_binary_0_0_c_counter_binary_v12_0_15 U0
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
`pragma protect encoding = (enctype = "BASE64", line_length = 76, bytes = 14736)
`pragma protect data_block
aBSTqOpxa56i1GaqSraWK3xTyCCMr2y/hmv2SjwvEv/QdwFDO/+75l3fidhQaYOO/ivyPYLI3yCA
Xy55ULDKQ5QeH1dBDylIssMLeGw8wh8eCZEzHXnYjrLg5LKONpPvxDARB9tvxCxx1FbYV5lrFARe
ncB2ORD7Unxpn9NUO19R0cDQvpcccQPsSudXK1rHYoJ0J2tqvccQUvsMqwy6nhx1zH0k4M5QEkUP
w6bLjYQZUK8pJeeZvO/1haPIbWkOhcYEdrrkGVGwb8EQbR7ycakYYqCg2222roklaItEf91CLMSH
/jYO7PItOguth6B/BpqIwLeyEICPgLWzHRjToKZaGAMLFGtmi1KlU0fm8dv5/yZC1fVKbdZKL5qm
OnVQP+r7yn/Ai7KESa3lurNb2/UOMPlNGeVG1O4LsV847xfTHZeRVwj0eClfFw5cqpIyF14+T38C
MxWj7GkOqDAmh85OmeiowJtj9LmOK5cv1iiKVR96TkXXfswqXFHAvOq1mt8phj5IB08Q/VDnw3mL
3tWgzDf65qCfuscVZ8n9HOJOe1bPVBCpt0NcRXa5toBY3tzE4B4oCQ/HQ5ukkvZQEK59OaUaeOfj
9CjaBkStmPq+H1flp0vtPkr3fPuIWyidYiRTz630+qXK0FC3GbSPvwvuEGocNa53ba2MwxfCxiQ9
l8L969faPNP74+6w3vIkv/4MrKqyIddgMoyC2sfqdAzDOdgnW8RhcVlcuyc51nfwKp94JBwc23Wy
ltS+3qAhuUAtO9YYgtsbWh7Bqs5rBpVuufsET7fNsCEIRfANz4cCIxMywM1i5TXLCJO6FCAPw/u+
I5qJ2kkiVBm/AFiAr6Xf+nU/s2c7UwrPRh255KfXi2S5NcTvfFDeKoTUH+hX9E+25RGWmgO76TvQ
0IlzP1povs9v8HtXj34bACm0gu5o5FlZ/H43EHDsy89x4oGtk1+mORoDv6KtI9pz74UkV3Ays4BO
DBTRW1XDxre2o4iW0fsGIgk3VpbA+yGCCB64XdWjSW1ya1pO4MUVm5D0kycKzieHC+Bv5j0X3zAM
uTh3wRHx6sY9Xcgxci8J9dQfb1Od7LyoomgxxP0bJMpCRmVle3caK00sg8hn80Mp0R0kzz391nTQ
h17N5Mo57iYHIbApgnIPMqHt/LQ/NOCpLNtnyz3++FnK3lujNRwrpEDn/bKjIC5V2wI1BjQAy0OE
4R0vd7mOVMmxIzXiOtuarlENuQCbIiHoD/Fxz/cUTI4A0be45389FfytbdGrFmr1eo918gn8zTyU
5CxnpQC5abIQgPwX/NBc0Z3Qm1VQCMl5vxaki0HVtJlv5QCh5STfCRrKXQhwXhEpghMWw1fsAPBu
X1cBvtUoklMN9z9bwCUfoTOUzWKa0raYv6IvBdjfVPk09ZOvYlAgD2pfUd499i9/gnOakXtTQ5K/
oqLuYgCbwXfCenRvGmSQaJwQ94d/SGjN7mMGdkZIDar2kkZuhtpfo+T5OVxeI4YyJoDFQqT6HwQ3
+yfuU6dlxmyn0KveXXdmzUA+BbocOnSik/xxz7MHA58qXAgJ6A6hN+ZgKJce+EZIT1Dggwm+Dn6A
Vz5T9/KaILVVS/jRG/DqPZbpbPNGMhEjutleU8HajDe6bLlIlaMD1vjaBdypdCBhJSuoTXTokDOH
w8UBI1VHepKszKSC008U4xkyGrtHtdy0wrqJZspxhElp3o7ZP8q9QbxZMXDpN384GL+JMaQmDkNu
yZHSC44ynK6tEc5gDmbozCjEd+854lQWIgkQH8p4vwYukXUdO/yFHnKV/VW6EO9GPQ9tRtA/Lih8
N4zjpA51amMfKDqnsTdqOzCoEoARteYAnam9xNWk033dDnP2zVh/ddrZuUsjBOmegqnzIrLubNfZ
EnmGEidZlsH9lgM+KICbK7Uk5D9N3aReQNwRSPQPh29isk165SI7jwlbrUbhn1slaEusS2w1s3xZ
JHyuGetGvLskrNzcCGwyjWY5Yw1QX6oBIVXjZAD9MguJgg9dEaxN3iFVJPFfxf8IWxTVbRqBmWoD
ocRmGci71qH8LQZ/UxTvM6UjlNZG24cvtYp3NwJDUgSgnDIWrKCjeFNewmdgzHzYOigMOnFg6sSy
/91k7gUg6UP21wD1hjbDIV4uEA2JdY2QZsp7FaVQw9hnWBrxTQZvMbQIaspWtnVyBOhPBa9c68YF
sPRhJrosHFMWIqXycswQYnuW0h0vmBMUIpLW2Y/JG676OoGpGZsrePl1siE/ao0/WKrnW4jZmcNe
A3kAs9s17EbyCp3dbA6BJwQqNNXm60SKubb9QDk2Hc+UV3EIcsjquCc0Yet3i5x7YapJ7jeWXAFB
MadIsadGLu4UAP0zbR2bQwUOl3wHIp7bA8bpJ3OVKJ/OJPggEdXTljJ86QDi//7xIRamTF7oGFyy
/RQ9xdCLmQfse/2tQUvB/PssRj6dcJ2nOJLZtl/78bdlJ1cXIPJ/ChNDDzjo7ROZ43JrzZD3lmxh
zTGBmPU6GCy2YRpnT7yGEurEqf12VoPDafpELLyp40hOpiKXj7VSkKR/Jq5obWlnQsFGVbobQWre
+Y7Q8dFiiMS2O5hKAmGG+Q0I80OhyiCIP2ycMGwCmsXm9WqfPMxNOv/Xmzm9XTUPY5gSy/NAz3ZP
U499qFQQxrFpvvHmV6dKE5h0zifNfBgXxdMQtoD7qtnCgWWsas2DEDxsCWYrlN8eer09rn/anf+/
IyVUpp4khJeXyXWYlpkmAmnP58eGiAQ4v5Vode6umTpHpK2UsyT5q7rQJCDULFo2dgs4p6HocXNE
LkYUD2AAk1a7qLMRUlh68QBcQT5Wvh2QCEvlCWflzuKqgu09Plsg1hH4Vx8Ft+Ni8pg4jYcx/L25
+lhXWA2DmUCLDkcbTw1ba6GPnyQC7QWYvYSjSVMACCIUciMfDVyY11IAKRUBVemW8UkHV06X1RXv
3A1pnqpMKP6TUDkTUAJinMWLKWuuByYI4Krga+AFDvKFJlsGuwZszn+1U2bmCULanpObbH+KESlw
TIz3E3kQOZ1vkZRKwiVkhsA4WRRem1qgMZaC5C9z805qeFzNX6bHEDeSKJErznUUB+CZKJdZCeBs
u4suSb1aLKnDeeV7nIsHiKFbm2Dv0zxl/oOWVPy761OwRQAZmrpJz9tXi+Di7lvVvDEhnf9GasEv
3zbpSKS+EoGbuOSOAXHUnDD/dJhqooaFIAAf4UcPgiT4BYE0pqz+gzn2taDmL9LdSDlzqjK+4ZQv
+HKuhXCOEl5exEPIyzDnDeEk7AmvgLqCXgHGdvkMO+C5c8shgA9WjKooUQSY8wc50fAnSDnTe8N2
TL9MJ1EXi2n14JEVLMASjSLPSrIZFwhE2ZjIuuzNdaSgAFzB5FIBKtlHchc6edK+vKqzEOluhTxc
4OucJkBBAfPx0uneF+R7TiCoi4+/VTnUDrFJSnBrGzd4Ar+GDJws3bjxq+R/sb+qp3mEHNouymmD
uNTAcR1ci1XutY2ZIThQRRwQ8OaWZQS6uUawYiZjOcAeIjcRC8CujsmfYEuwnrjaLvgghGlpV1pS
AgE6nstTrwn4FVNBvloRAd3RS0AljR2HTI9D3F6towlmHzRA/pGH8XXMC3J74ScdkUrK/7QjtuER
zY2JQp9pUVr1q5eCodWXx1xgU+Q8qAa3FNUwQ7uDmCQ9B/lwckj5wHMjEzJAtYwh4QtGd7CeSXtv
AgTK2p9BnirxvfUruqA7WNSVDzDS28iW+DpU4wEY124tEX0+vhGmijwsXrK8hDlTaMhClGteAYNU
ogP+L5bGiXVntKPV7056Dxby1B76CDH3Rgv72b8vssmHEAXcZo0zOIrwZ5Ryj2Ue9+qGt5hMFhfq
ftvfzp1WVZXTZIqN5PPG0KVFS4090d9DGQYKJIl0AekYT0luQt18yGyiU/s+RnEAC3QNWBhWsd6R
yhQ009lo4goxBNpvjwtwzUVTTCh3U+0XMLkMBOdmQwYwE03M5FUkVakfroFjJE5kiOLpj2I4PqCm
LkutPt7ojWMscAFSN6MfGFg1SIjpaY5a9Jeb47Kg/ywlWkKAUoOcC74XAWZoFJvTnM38PFnTnPHB
JAC59czDeh7dI4fp7GEeUbl6ClRL0p7d28fyyR2k/82Z2qxPdz8doAE2ELmAVMGGf2jpmJbGXFu9
9omlNQsAMAaQZUeHaODyD7TZD1rSIFLKkCU6s5fpKf2pmMGEO4rN1QsVH2uMQ2SPSW1kAtAHlDI+
aBPgFGNgygbOv8KNn5k7RNBevRRKqRLUPPFNLFsW/dSSgB2drgPFYpVXaLWRRuPZ/W0WUio4fi65
Z4+TnVRv6hRFM6ITHVpkrBymWH5InFop/JcAbPPaBl3hxBdiqtfJek5ZZNHqaCYADzmdlx7BYokT
6YUY+gKCKXNP2wAGs73yzDlJqlaFM9S7sr6k+9sl4qI6bWY16udhR0zENpa+ijKWnc6MtMTLNFsC
nOCcMijNIGK6MfybXflB38QUpLLqSWIRu9Pvk0XpHk3de2cKh4eEv6LQy3vKxpA2ylPgXxyQ7z8V
29jsl1rfbKXU4K9XQDm18HdDjZloZiZCalgN4SnQ48ImFgS0oENY96dHTgjjugGyF7TMjn6oYaVi
gEW99d23AcIquzXbHD8YPKCZUVpXMKKlOezr8cF5s2mNJw2m0YNK8KAsh2h85k7hCIrg5emZrdsd
zclJT0ALwvj7LSpGEZPs4+9hwHMzHskdrLvv17Bvd+V8QnYvIsl4rERFrwv1wa+1tNhrqsftuoQp
kEp2OLXz1faL4rZJnsuv563b5SLKNNZYm4I7WPAGRsgbs0q/0xPr/JmPR8TB4G8SoOu3i9WW+Vtt
EkK1YC4I1GyO2/3L/9fMyhYAbI4vXQ2CRrtZMhauEfIelYztstxK3WtK1NIkBJeEFSQ9N+gkN7Sl
T4UFTXMA0gfreZKwkOq4g19myIIIftTlkcV9RTEqSIGwXSeAgOtKjHML38tV1Puy0CLDHJ2GPKgE
A3e4Y1MFdoJb+NgRvxKSrFmdk4MbCJolAMpoZceXfLI3ysICpCpXSjLWrLmzTHvnPPNsZr5VQMEQ
yxCgl+HbbRfwWHVyx0aODwoW7pYiDmQZdars8YOdstKJErHEkJUgF1bKXcUiBtlFT+QgYy5gFIH2
PHd4jkPSFJh9iq2zcwxekfoE+J92JsTbHPAo9CuF900d+GJ1J+XnSKpWZbBc4ftsmJZjYU4aGNsS
uJhpnj2ixyhMtJ6jmCmIuuiQTwT5Mjlis3dhDV6hgcZukvgqCmWih1CotrWT7DbBR0quJ1tQ+iWX
5Etpnzg1e16TpgAudCDzXQdUrsYcx2fOa2otDdsGEmM/t/LSlmxvJ1/wU+3L9kXSTcilSVI/oZIq
lCDrJV/Nbml88PiNWHm97rJyzA52emTT4aCfqlE2Jb1gNKSS4j2iqdu/VM2+umF5K+8RsWRInItp
USK9PI+gAcaob+fUDUONTrZV8nKAK40RPD0FHZNjV7UoBbF/4ANCWcisCs37OXkkNrpMcy1Ml99L
BdYzV9wdAz1CWtZDfvD4qF8Z1QD40pK/lQ3gnn9hb3XvM8AhufFv+HYFR4LwYbPY3IbK5xtfjFVo
/IwKVYu3l63K63AK28lL6tq6h5oGkF1iwnAg2LQVCH3Zrf+y193OrdQMpYN6JFyNQg2htCtmPq+F
r4kV/CNLm29GwpRBl2vluybzWDcjIbGJ0dWyRhyFNSMTG3WaCbu8+QOWrWEYmfi0NsVBSKSoHWWM
xYy6DrCKDL4MLOkGxel5/8nNpU/cWJ1HLnoTeScpEPXer2XAtfDJvQL8wR+nGU7xkFFDrTq9DDvT
neCWcvf4YiMkmYjfK22virbmvQWJdUf3UH504GDg7eOBIPQMwZ0JjgR9oQl0c5qQqFPpvjSPuSNx
gxEi7jPjODHTV8/LEXZBNbTVyC4yGMcW3lql6vs3Ru3UsnaRo013oIiqs5uds12jzHOMJ4LX4TIR
Ia36401/P5ykVtATgZFCJ5dKfUGBa/T78XLAa/EmAExGTVRnut1AlHoNMF1H94wraBAxoFgohgjc
Q6ZG+W5NMt8CAw0o6qxu2w5GV/DS8lvteHR1p8lU37ITnOBEld+r1nBSVZUm6OkNW2ECCaOGzscp
KESa3DZu6yDTmXzLjVThiudWujD4DvtWbuCTKj6oQdoBl0lXJKnzgCVUva8yKTtHaWEqU9A+RXnu
mD8YHFDJe92g6+oflZ5rLdw3zugQjBtfxRu607ir8gkjpVZdqn7MQ+bmzlIf5rGcLNl10GqhLvcn
tR/HDU06V7WtiXYK7xlwy+o5uoXSfGcHu4kLwU0oJkdvpBtETy59ZINX9I3m02i+1OYfPNdkPZVC
1Z1tRIlNKYWLlcBm93UuIQUfHybiQXXDHHYSzFgCHgn9zkfD7kpKlVFzG75xcuiCAxs9LMv+kHVw
8HevBt31if7AzJIsBzOIWa7wPmg18hdGX05GqGAxc8DS2W0+2Al9qoVwFt+wy+VPXD9j47Svh7F+
u3PEtofoHJD3qtOQ/DwPTEwhekZPOdzJV70X76jXWVaoCiTUOAQUt4YVoqGTvXx+d5cbSHi+x/db
Uw7WmJ5gCTDNJm3Ztq/P6qhP/ILG+ynzcM2dWzXzCTllKHBtPKuRg6dRb+DumpEQpODNyl7YdFok
SFed9fSQloaFUSzBAXEhqMmmVJO7eUI49w3/NcAYF76J02AA3SVdMrSQ7ifxJHracGhy8Zx9mWhU
t0FF1a61feHh5RBMAEKoSQbVhqi118IVjPSWMvVZxSDDOOF7SZfZSQ6OVv31h7W8Fj+IMnKzvQLQ
MiZLvelBUfJ7t+EmnRdGk98geyVztC00fwNyZtdomqrW/rtyIyoMiNkVkiV37O20krvEqZKJtv0n
HJTk2oQvlBBPhpR2QuqezRS/N0M460JNYbPmjpv6HYV0JcC/OoV6Cnj9q12lS2Nvy33uFpAX5V8j
/J2kYOOCWSttZzi11p8lwviV4m03wG2+QgqCpGCELxF1ZLRRPn5d/Gze/ZHeMopPKqlUNc7X8ZwF
KI4pufe64EFVehNr6mafdlKbamSGhxsdacAZvuY1WcFnse3iLanCLEqSHhrhqCiDoOUDyR5lkHxn
GXJFgVoZDn3UDy9Dx+koSjYBW6+LHfYhb5BfRBDYU6YXTZhyoNBMffhXBvE1e/v3fDFi/H50CLub
h1E2y1D+qqdXUWbg9s0IAA4rJpoW2vIrRQE9dvv/w8HX7SRk3G1+kwtNDb1Cc6Cmyccgjm24jZXO
LVaiO9ISy9BOTS5JfCAl+3C7sbpsqVWtVWTX1nVFHo6JETVEfo1p77IR6J3HQfa2S8izHk1NmgDg
0jCslQ7QEkR7ORs0zRUmJ4Hw81yvgO5yHBfv4WLYYInbLeDXgI4OyRVl++my51wxb7Qls0LsL3c5
m06jwlUSCqtkfgG6I0a3ZwwYFfNmeSm2RZs2cmGZjqfInjyiPiqxTsKRNcovJyyYAPvqVE75tMnG
3P7ticmaPW2+9EhSEmPOSZe1MP+NsnnNM2V7Hg4eGvsBSrMPwPpEouGNOtuYud229rgT7h1MTbpY
hdXbZ6bcrSvVKUN97b2UkNirA5zCA+SIQuD9yDFDU91jRvDqahtHEWq3dEm4MsTHoIUI6844v3G1
EYdJeVpQTCWerB14aGQib7L6ADjcKaVqTRnaN9AJmI3K+UMeCU8aNL55s+awam0Rs5YkouKiL1c3
MOAshGicS1EA5Aw79VsPYUh2gOdXQtKjixqz27FzWj5QLhZie6UrDPifzM5w4n7zuGqrhg6e5G8l
lKofKTYNF1aekKrmwCx2SoOG3hY8JwzuuHM67obSGpC+ZHvLjDFfZ0ZGMrK2rpvIWGVzvlwzbJSv
7OmJQkZSPYZ6mljYJkkPlAilpbsE5TkBM3rJ+rCO98RDlob9V4eK0a++JSDoBlA8KK83V0gAhK0Y
uTqjEOw7pTEnee8Eg+cxOYJO6zZ54/QFPgG8eDtbhyPDGPXRDZ6Iv3ahy8u/cCslbfOaGpa1gYST
16XYUvyNmxIC263+ZAiTRJnIO+T6LMlH2dqj6GGA2db0QrArjCeV8W7q/nc7Ew0DHmKNuLC3EVnW
W5IxFMOzPeii2V4TV5EHImQxVAlbInA1vVNTQu+K9lyjeWK89PisiOSpLjYh2+zxIAXjpXp3aMBy
mg+VXQBj8cXyqwiws6qkblBsNNWhCRuhxu1wW0QBiq/mCBmBjIrGMJ3Dno38AHfDcCa5KoyiVPD0
zl5WvPb0tqoW3EOfshQgQFofKouMN8ScPRQhtnI6yaaIrhRg/KIErSh5rt5yBYrgI/KKkdsZbM74
T3VhrvlBFKCXAH80A8vd64NfUZETmWGiwe9ie2qWxQFHfun7yBBK8G7vI3sl0G7ToNxt0TXNR1hK
UXnJgZHGvyTIQUL7WBrm4hMQ0fJ18wTFvXA2gk5dnfKs3MvhFe4tlXjtb+L/x3N2SVzicetFKA89
O4LRsdQpqXbsGmTV/4X4T/qyArCkCrpxfcdfR4hqtwid/jOMcjMrlbkNuWG7qI1/1/AXgu3dJTx9
MC1bS1/p5qDwjDNuAohDTicU7pynMQ6CeZrph6EjpJuibVahJVv4buQLXSk+Ibkkkaihq5bfJq6/
3akHC6xZCq9q3cfQcCuwyEAxgV6DYftZXl1qhjMFNd/rPYq6BZyTvoaOy+EDy29wCtMJQrBGb4Lv
kZAx5Jn0q6YC1yFQ/vh7BsdLWpL9f9hJAC1IlD8T+5dw9cYf8gNXZFe+YDT+AYOfOEOF8QCiuqbM
53Bz/Yugv2m1kM5z74M/nde0TFFhh6Fs1uaLIuntIJA1FZC4LHettVF3IgCkbSVz1+SCfYemW/4x
SITNTDfGhTAJM/6oaRowpVEv38BwNt7yvOkjeUR59Ypq8vgwc1dN7fUXxj4X9WyVVtP+HmiOo80N
ztB2PfBTkLmUgiMQLKSjwy4j3sMG/MepYYkd1wam1w2rLZ9E4YJXOii2wxXNF4O6Mwk5VgcSWCqN
VYkIKRGqlZc6gzomW6fKVmpo5ks1epV0yYDYR/xBVzqtgYwABqwUiCSCqyc71yoCd6BA3riiMlep
n0RIa8djVV8v6vnyy09l7H7V7Ka/BUiuPqvte1VT5DYou7CVTVTOG3oEs3WHwle4XtL9D+rCFfx8
bPJZsXUbB6Kw3qHdqc6riVSjHUFdBJiTOEsAgJHnjdg+sXKUO5NfNatONRrJ6iMnJ16NupD9jqLw
Xh3AYZCG0VWbhXFg6kGDUgFgnyf5jMzU3cw9ntdbcwClJasn0p3moZhS4vPjzWD5fhygOR9kyO8A
szV8FbAtgkM+COIVwlMjHWeVhgMclWBe/7J10dqlnWKLpYZnV19SYELxfvi9Sl0+mj4AfpvCPstv
oaiRvwNLrkbJsAzHmHLzcNQgOIrHOWJKyzT6iDXvUP4UAOjtNyWloxNvUJPoXVRkECz5JeCoq1NL
fWxcwuyyHgrzoU3iEN8nnvgUXHGTFGBQMfXS4cDTbX+0KuVern+36b2HdwDz9grmAmzOlv2RqNvB
fPyiy3tzOzeBge71CwNWq5t/DvZoX70ZQ5QqYvDb+HSO+CTuH5oWJMjjbs5vsavOJTza8z00qGBC
NbWBIDRCgRgSjAxCapWqs2m3SuwgSN+HvH1lPU3e0PUSkychpUEMuPdVgyPVSk86eg+VcvW69meV
fQQmGMDHGf7qKmNIfz5n9FygHJsiejtCgOlcbQRztRDGIOwaiEwz5/dw4na+r1EKwhkb1UTnWHSA
xwdDBTmbpP6HwW1Z336Jbaf034uYiC66P/TMnrx/z0+U2WOAhqc9EC0jdlqAQwNh5DqDRFpn9m/z
HeFqAJpZ29qZbsIwVjE7PJbx8165RFrrwjd4DyUzztskujmb3Ef6RndqhEssodfb3gUdZtvRc+FJ
9e2oynFHnCdav79Yrb5Aifqh4wvexY8O6ljQCh5Lpi+dgyeYYiH3DgVqkjZcXdJKL38IblLWbjxH
tNTWe/F+yYruxd+7aeQLI7jSGVuzTodGwjsXxRiJmYP3d4KYH0+/Oq64PTCs6zNDiAEXyFvtj6EY
Ww4m5gRyOYEchBFVFMx9gHGQp7HvElB77/v3ow2xq0bW7x0+ofNUVySyHBx4Da18Wb6r25m0MGZY
d+d++hqlnNkRndOF+Ch/HBstRt/u81dbJ1VtiGhtJuGsjQBqBfEBAF1d9/kYZwiNd3VOxgEBQK5n
GszfBQHtWchOXSqBaBjaVPRoC8hGcbFNq3lIWhiQQmNQAXzWQVLGiV/zJzmQu3kTZfTkbYjEvmA7
3lrWUgH1a7NfCs0JFRZTRMfC6NNy0BZxkk0I9oKRn990mgczyXVmzeDAG0R1H5TCkunz6NpmJEfc
16V1iJQqBnJxWyogwLM8v2l3IqCO3TwMfIcF91ItyFWggFoFjSbWTnlRjNikY5jLrJ420GjyAIdu
Wxiu+2OR591KHz7saqyXC07KqqH1Zf47q+H6iBJk3ZjuPGkN3k3HdEpx/G5mNQRyz2ApAmyOPIHp
Vv0wwVX1XHhGK2xe+JxlW9ROC6Tti81l8fy5/IHFm2i2nKj03hyKg7Ju4kJrqCc4ORumqKeBGLwz
e4u7+2cDsZWgJIGU2BNL8ddZQX1KjSdq38VETzK/Q9KXB35domA2gSmQOiZKWu1YEY0jIxJySi2q
pT9TKfr8PS8cGdbvvU5/dYFvlBjNbC0ioOn4I7Wx73i2c6I8mgllFVeq2e061wQ2YAvrf/yNbKYi
lqfA0Cg83KrGl9qqJwWOVmCJoK+2NfrjDFqJHbpvUJ+dKZVTxArs8HbWsg5najNriK0lbnn8AaaF
nz0cyFOeuhGb6T3lJoXMHjJTxWlkK3afl9T+nnFpz/RwlyDpxDe9xjJ4QKKuDmYv32+UuaVhY/+p
ni7vPsQFI0Z/CORW7Sl97dEFn/mdMJs66D9fxg/E8fsgROsye5AfFWDJhu87rEAMqpyFVd7ivO7C
xb+HqFSryPniErFAryoFelx0zhEMjKc0BlAsvn7MQXn8Xq0swiv+Xt9+kS0dWswr54CRK3OJTtbi
ppcEbWv1l8rcge0OCeXwUWfnowPO1VqMGbg0n3GPQh70cbRBPGHKY0pKCRtxUuhIROwmQNwwef6h
Z3zEKqzSW6vivZ+lHgxbMV9R6xfr03SkK0SbRz/+eCkkoDxhhpcMarvpYBMRZZGBp4kgX7Y33lMC
0vRjyYIY491Im3tOMJIFbKwlk5YS8xXC9/nehEnVeBx+6BQwFAkA9IXxRBJGLnfd7+mqcmF3FdzB
rDuC3syRaQzbGl/TmAnn5W9J8bzrh96FceBnT1xDMAuKOtAbweVhT9nblmv4RsyoBRUbd0o5CiJo
YJBlk9WYI9EcfBsMc+h5n5EzoOA0fXam2o0W9j6Tl65tzX80gmA4I4Py1tR9KZR5eDW4hxHlEd8C
nv7VwhIQgTu/Xbhh0l57fX6abj/zL4rmM0HWaQHF8tLsduKorHoc66XxgP4KAPrjUwRHUH9oVUpL
AKIfqQ+SXsPl5hRqpJ8Q/cTyC/rEIBuiNAJ6MDx0MmRdiEurvQOc55oWdEM4/t2TgRw/SM75Id04
pUb4zukUo0Qf6cORCifyadZv/EnY6lQRwe3CdwFuPePFvcDRRdNYMkitFldQfXGH9CQHFDUe33nu
yrUF2rtwNCD2/CLO0AJV1SYDvCk2QRqHUSGt5d28Jp9ZcUmdymTSbzegH0+D1hgBZEsCrtQ89obW
1NmKo/vGPZlZzboLBV4g3diGM+X0evWFi5nF6wIw6b+gCgadYAsfnRgcMrnb8cDmIydN2IqyXNL5
WVIU5eRNy+UmAA+rNnGMgZHSkSKryruHJJWqZyhMHfWtH76ycxAptKXR1Fs53CTQ+kxh5aoVzTcD
ZKJb1I9NF0d241T6QNsI7CYplR+OcZeb8SlF7EKohZTNiOXUZrERgS1cTwVSLltNGBrXQq7Dirq9
4bmVJJ0YELyQxqRKS4dr/q0C6wKz7HbkWJI/R2E2D08AgIg7N/jpu+pLpyG94xmEaJVni3ADSfLo
wtbKd/1LQoLY/IaIk/yq6UHlcDoIAVioqKn8R+tGgMZSxoJlzTSCgW0WDa+TouXOJBxFvFx5lMFG
LJ5J8JCEAat7lASyrI1A/CNswgEV7/gMyelzkdrNWqWzomZkTuXxsf2hOFSJjJH1RBQ+uvM1D6+L
4ZsVorN5qQIxIHzBd3Vwb4sgur3fAq81M1V3yZn/Xkcenu6ImUAMD9ZJ8Vf2Mf61QgsHap5b+Ijl
2jI8d1lL1aMEk3T+jgbWAbERopJxbEoxG7k+5pmtD3Zet/DBypuZsNsC/impqWEcHJpvZMsHdeFK
xmM9a9kyvrhAeERtd/5WGl+nxkenkrRqL+rECY/ZrSrG4v0ru6PTCxokGyAf34L6uF8BrNPrK6/u
e2EURkrs4/CfuR0Fc7nOYK75ft4LPrPNhlv3jpfYLKtKH6A01dn0kmV9ukAa5oM/bqI73aZAa82+
W/aQo2FpKbco1pA7TOLZ8AjawZaT0Rf+jhVlGWbUrNLETcnaOPtfDQ5Ub5Sx0hsaPXRtUpqXSHos
bc4wjZW3y7GvCqqU36EtIatZFQ8fZz+CFZGzdERifuFdCQ+scvvgw/vpIOzXeH9txCYUJ5TU3drA
/WdMVR4Al5hf+fZLGqMo5Yp72lHauehp/FYBGRDpltgoc4+7CayiTcGaLQx4S9BVgXjOaf06ZU9k
4gfm4u28PHO7yN/mpGFqBY3YskiRIYbzfJw/fE4+0XCmG54uaKt+jxlRu/NGQJfvSh4/lTU1xY+Z
g3JX2R+gfqON1M2h9Hjw1iSJOxrkcee9xh9hgir2nhouyT+24k5SmmNn5e2P7PM9e1qyD9IAvN5a
KGWUUNNsYVnk66tsqNiSt92LfX7Xb06G+yNyKpmtKm+Fb5WsgxEwH5sAhbl9FaQEr/3YkoRjohMd
5lOezaYpn+CfUopNzIgj0sSAMBU8t7OtZyIlhQLaaGq52qXWhAthhvyFhGuWMQkn80b1zP+VTyMm
XXLgC+C9SCPQ/G/MjLSkgZ7RAw5kKbB/fqWWFuy8mQZ/ftT+vHg8QpxMhqmOV18hlG3rIaa/nD3S
A5yrW4JVG58aUKAEjFm/YKYJPhgbROKAM3MN3M18tKYiNPekxpyTvfKWS5PIppRDtyHQKFJoUtz2
skdCh4E2+xDjwAJtk/B+4doHEa/WQm++I/apWxqsOl3H4l3G9kk3yRA+eHMMMg/xuHcqbtVq/jL5
N11iXn6XoIZC5cIWiyt7piyeJPh8GNwLTkV2b+yvqQ3u1293VLmO1bZgDdeSx9Vc9vQnIgarG1hQ
bRIbYFnH7DUYu2iiD7lgn3qV4HAp+ixR282uxy0Nx41CoF9oK/Yat7FQGLD7GjSSAnYYSRc3ymEB
ccDednD5p630miQiM1/UGK6NOxLjA4HBC6KCj8HBdJtZ757ZJI58vXkkQE291u0Cl407i752KKa7
WjPneO98TCsy6aCtIw7BOQXMct0Vkd0Xd4PJ17rsI7fPrlfxikRcw6si701uPHkQYthamB+6SMqv
Uswnn5k8UizKkxEd2xNo4EqtlVN5wh9i1Fc3BmK1dC9rqxK0L8r9Q9CwQQndTJH8TSvCnfUruREq
H6+PvpXhpugaWz/BvzT301GSHYPfaIq4VA/D7cwHkiWFRabddVgLHpY8Ymykf4mPW8BFb+WtWevk
rEHY2jSi1vYBOS9zSb5hcfDPw+IaqqR341nY0Cb5EIdqP9EKW9A8RM0yXb+5imH+PYyF5AJWc1+B
NsNRKDt3KH4xadAZA5rgfDee9TQUsd8vyGf/HM1SKtlzum4ueM4c8ySZPYWHM1kWT1Wj1FPIGgy0
v9JuztgvmDZc5tt3GN2jBsziynrO1kas7wa8Gu7Cm/yLil1mNBd8eQzFiJZgt9tQ98/PQW3uVrhF
6uxrf+miu5+BxrTPYLFtXQc5JVGiie7PRFf1Ln1AmUb8ljpYGzuthX6Bmg7x/WMb45mcdiH+PnEN
3MxoZoAGmvOK5vM172GGYjkDg9V/BneleIlDaj5n+dvcSe9jJZldCB6GMbvC7rSpDQGtgoWyPPpo
G+2ecUz/ODxCeVzjiMMYphhVs8h1RXTg2IldmRjSCu6nwBZcp3WruGWX1GgdPlMss+5p+lhxGZ9V
0WG5x2c4l19bYY27lOtJ0vm12VvhCUfwBJ6hyGVaKRR/5rzsXJmLnPk4N+NZq0BaKuBQ9WevOGkt
VdLFEBhQDUl2QeHO8mE2342PcYJbNJZd0BO8VxoXRY1FDtW6Kom5c64NwF83iSPLPeBrrS0DJQ9X
qOs9utreEu2SGpQFgSNMFd0s5RdHussFgTwbN7B+L7mzwFmq9tK4s5h8+oxQg2eey3ZZHr7aKpxT
ZE0KJY5KywVtMWSBu9VNtlnb0mfKCkzBLDskQsgBkU26P8d1j8bwpwpFepp6zJyGhAacPkFNikHl
8BZnB/DCWLtqGrjzU6/uWrN2kN+IN+ldO9wOu81L3qxcIW8zGlJLyK1c58QUCh0Fs8AxOehVq09o
FEG32Offl2TVBLaxHJLOshS2L1hvINTrQqh3TOfhA/AeaO4KeaNYBVQwiWJ+Lxpkyc9P3ntjLwkg
9Rob1TSNlkJiZFSltSBUrHyp0swJcAQROye4Zh6dfCIcysuvfYC+vvP2y2dX3Upj7KpSPldbozyg
tcoYeozn7ZrYyDCE7vDqL0He45VehD7IMo9nILPVdCqZp+5EEFDKOV3jjlktaoEN45FdVIUiXqqe
PRQsLHeeQGltsulogNP3s5C/4dZoThiM4dpW0In0RX0iQMs67P+HTl+hHlTC7g+zeTKwqzYNi+7C
osyS1f/wresE+lzNWyG+kY/EhrBhpO5pSx2C9+oQedZ+WbD/aJvOyST0sRGY4560KaeTfu8bd6h7
96yW8XrmwMImMwrAHdiyy3TbscDI0l/rHsacO0i5Wde82FKJE6wXKH3T1342eB6BBsSRIa+sZCQK
5uBQ22vKpgT+j0RAQMh1tygdOJPuJ4D/ZaURFZ/ygZxmmtPznfhlrMog1MwCxWZN9hNmrR3lSXZB
+Lzn1Q91nL4hgpkxUrFbnNhj0jbIje9xV7kzGaqgN7ZCynJQQU8dSiPhnXNzJi9JbmjcLK50qZQ0
djBYkw5EEcIzZQyZ2poGphME4lij1wAK1Fn3moJp2IjouFIDDXFHz4v0QA8EM9DbKFXr4kY6Ultr
IrAxW5oIwdfkOqYWBYD4bYgLliIK06wJBbf9lJlKIt87gsqVLBJiT3R+6mFDtQDoBzsQz9vZ3uir
44D6G83nGKiV5IFAUAVs22gNCQLUmfPtx811ftTYlrNxNV4MpD/r7fY8ZIeSi9sT3S6j4dBEGhOU
M1MzzdPIFlZEJCtEFh5fbFXrrVxQ8dm+bcZjAjpPmipwZnQ2dSIeQ0pTpY/GU4WET8y+aTtKDiQs
Hke8K2CLuixeVMuk8W0uZwFzISvm+r02YffLxNTDXHSJWkKMaLrSkQaTOzid+O13MToVJPwjsVQh
sv36vH+2kU4R3hdIMOcEcWDrn2LCJLrp4IcZH1gJWbbcYbQ0R1HYTxTdbLxamoM+43Xy/MmQT+I1
XczW2lpwzwEKRirgPhW85esBL8eKr4q4jeK2uirM9h/ktJ1qZ0OTBOXEqIm1kqEzfRHMbcZEyalp
OgUsAOKYOOwTULfd2ZJyvVwJVh3ypTng4kXLW1tdZRsrFrS4qR4JJ1dD4x558SjPdCX7pwFR/IWp
jGOZoeAgQfCGqyjqFR3JAAngf/Ds+Jv+MFH0Kein+JQgl1yXDDEc6cDBrUqr9sXz7qG2de/+uudB
OKpGhJ49FIHJjEYeYX3BDRbVBgAH828Wyq5MZn8Yq5TUw9J685tJ9JsP9s/rcOs2FYwRCDutyoMP
WJVzABJ1QeWy8A4z/KN+qvQh4WGHHIG+4Iz7tg27oXsW/nfjzOpzKcJod5/pWCteUiJ9LDWtsdkI
onvSrWPcifsfM24EQid47lyhnCmNP2eeUVeqQKbPdVpOGaFO0Dhgic2JZ6UNbGTnmU3zpzvplRbr
jYU+ZLNni4IlRDhyCLKcTXDrhT4q0lktwdGL4Wvkk6+plXmKz8MAdqdkcJMqygfs+ryF5Z+4cxw0
zSvnMqBFiByEUpqWCLlgppEZSWmsYAiRLT3I4LYGLztzTSUR/1Twc6fZnB2DuaFD77LUl+kjs8Sx
b7RnVZOvD0WE5NX9po5Ym3s2AIhQXh4hvNypCW+u0q8bq0ptxzXRmYcF9fgPqfo+xateX+HEFRRI
fTpr8mNd/3wHPXTDdF9aNh065pwPySleEyLENmwejszT4TC6ZbvMaqPS+tZpWC2dJygDsnnGgk8N
mKJ+R+3W8VC5XJSsVowtZ2q1GytJofn0lKZ1NXyQJ6Zao27jJgq7PrUUkppn+xbv4y+uBev/fVHo
ijT/AElhTzk+uXtHym4kja/MctEVFlFUzAS3n9tx9eL06HPgD3m6+3JrExXRaCsATfqVgx07tcJo
mUqUZQ2LAhfOqO4XhVpkm3mdp0BC4k2ogZRz8pUpHNgLdTqAH7Et8StkHKzk7jN9UVcYJhX1mDar
ghsBiAhJ+e2LMWyJxx1E+FX4fUMYsJ8H40QBXMIOPZSCoR0KG1REzy2vlnletj+JdEZBUMKdExbD
QIRmiSQiH3AtANAcRKypt3AErRaKeA1EWqGsj8f6pnsAIENA5+Q959FMUUxMKR3BfoHoRv7P9XDm
4c3o//7TaR1Q/d63lqpuqGUEuOeIi+onE8Hev7f0ClPdETlErH8Cf0kWF2Ia3RehGZfLDctOXO1J
jKmqZ49mjsYDAsdQTowAaF/3+vQrZYnA7hjEpdlulLSN9Kvl2Hj8c+pZ0Qgk68dHZ5U/E7dLuqBt
5h8I4Mr0HDlWTIe5VP/hrifGfiRcD1nLX5UYCScOTkmQfiGfLfHby+ULzO5ZzVZkQgUJFPDeqDxj
L9A1DjBGzWXNiuNL5mmmCBJzI9wpADTIsUkHN3tnE9L3jmWrDqM9lDtTHgtO+pCweU8H4BKCHSLP
oXZSO1+70UvY86UxXIA/njQTUDsgZ2D0l096IABFTaHVV0ef2I3YW6ntr88CGN5Mlh11NK5QWY9V
h8rRQdpmnlCFxBD7v68yUD+uSkgF0Hb+j3n7SXx2NX5jugBrVTLjaJVzhETlnOw1I3XMrmrNlrcQ
RORqow+Au60RI3jnB+fR30agGscQNeJf8VWX+XXkVRK0hnUyTQNl7Hib8KEEJJ0uFDarlrsQ7YvB
4/74FRF2STymQcDdxLY1WO3QSql6a/lJWsaW22PBqFhFLnDpm5Bli8Xa58xX3CCEnxNYB6rYZ8Kh
Q/u8fhPOrQfLpZo3wlh/HH0F0jtRVU+hxz7Sp9qpk0WyxC8Qex0pGpjv+yZ2iBvyEIcjKhOVdeMf
v/thaimBDDxc2g8vnP5enaHqECiRFHT8aWMSPw5/aHBykZfk8/ii1acnO0uU5RJPGk9j8TuoJoh2
xU4BSAhmaTxUiTQJ3szWJ3R2na/dhEaI9su45Kp3NMECdSp+s+cjfTor2nb0SuGpNWnRCi1Ae7Ig
hGfh6cQc+eFrE2/nJ4ux7l/r9vuWr4cEDJGrLIy1rFuROQMzoGK2PsxtxjhS04fPNa7xiga5mMnB
CZrjxROaS/sAu1OfBSYs1Qj5TjnLkAMSAZTXRCQZEQlja3Nliy/dsM/UHwUuTP+TIKp9qrukW0y3
6pb28bY6UdiVBv2HfAgzI/5FocYaw5j7opDKPoyYW6x9Fc+WTLAzXENYCdRVtkHsqTccwYbnB8KI
YE+qpkRAQbvo8iUr0aBlC7bt/4KetNaq5SAP4kuhYuJWMfBen9a90eXhDe9zGhEjimOgu8dzFFsd
7ENgEgFSUaGKT+1uIdlSAGYODf44QJaM6Gy4O9Yny0SfJjL98PbgD+m/eQd9K1hNzSDWT9TLFOqk
rKqAaeLNlP8/qRbgwbIAVY6+AlUyCr/RK3TV/I17bLQ6LWRhdKYjnsT7zN3noLVMXMRREW2+OuG/
0Np4w86CNlbuN2LyI2rzDajKsNB8niwatVbl6fGI8SyebOgo238DnP+fL7uDP/9VjIVIfJOGUht7
R+OjJtIgxPoCB1CmDt2b4BRO6QY5AcxCgYYr6LfjN8vHoPSYLO2yax3KfGgbq+zIqQ8HfUD7XYLL
9aT+Q4DNr9wyatj4sJZZjcmFhfZkMguC3wWBvIXQVlrpqCxA4EgjJXuUbmgVyBA+1ugcV8HPcTJP
iVmpS8747Dmdc23iFI5stu2yYc6GNPuX+ZdfIkeFxt2IMuvlxAtT0zrZ+auOeNe8nGf1dG2c1FHU
LYUAc/A1w8T7ZNmSn01Zh/qtrs23Zis3K4SHEI76fRFi+49fWoQR7FtZlj8dIGyiehBCbV98YeOG
RRH2zvxgOFI0ewp97iprhthmOKzaYwZFnKfjPAiBcQdY7NEI/4KrTgPNXGzU/R8QpJbPcGJl/KWl
014YMh+nlQSp+l/CQ7F9hCRAwfpdCjuGw9+vAjfd2qZUi+dAK56+sTb1xaBCN+Vbtc2irURYrOZ3
h14uV/GI7QLLqeRX0z/ElFXktUnwrsF7tT1K7sb2EDzaKPnyVGyNwzQf8TtzjGzAby1qm1F9nbPw
ZEdOv0/Nhzj1tg0tUdIAUP7rHDDQWAE3fOaEI7Sil+pzAFF9fad4WXqbQjJ9tqfw0TlRrsyhwSuJ
ZjaWtmc+IGlrVxQsJ3xQ6rI+YGVAksMdGE95gHtsDwBY6RupSbUPw5pecvJlzLcVANNflHI336BM
q/lN9Y447V/fAAjGu8/rbsn75FHSpQ8oxYPL66dZzL9Wz0wI9/n425cqARJugurwyqMqB115JjeB
2QmLMCt+BKYNGyOw73XwgIJwDtkPm+xKynaNFseGUBPpBi5hF9OqC3lAr8m81xDUHa76jEzN3oTd
8AQNtmIAQgYvxCajJblAjw8hc6eBqmpHVyHF0ksZH8whYuzn8qAIPpeswTaxqVcvMQf04aLCemeQ
bF2YLO+8FR/C+LN68NXr5PXV00fJIrFcVL/ld2rMaIDwek7yrnpsd5uUMaomEie5Zp+Lq8Fu5g5t
GYVlFbJuJ9X/0Sk0wlE2895i7bVipjzVz2MpA/JAef2IiGxzghKwYErV9yKFlPyIsfJpP/SrccFl
sqFS+Z9Zw+SYzPHY9WGKVs3G9crQ3fMT4E/4cJFZOchfKXVl/+hmS5F7MeZOMBoJveWyMWeFxXrp
6q+9RyrbWMNbFz7/Xi/7yZzEOFV+cp9yCd0TDkQ0pJ/Ra3Pw18LKdSPX4Xu8ONMc7z2YwFTasXfl
6vyVli7bowoxCye3hRGI9UUnb5o4O8NDy/cI6Sy0wACmiNJGsoIczRZePr+z6K02xrdCgn9HsqP8
yW/napvhrU9GfK9TUpT6DALrT38mE8FBmdNZkiCWR/fmndcFcruHVTqw4iuebMRt2fmUJ6GbqrDF
uSg/CeDLuA/q3os0LT5GIRmque94nl5Ene8cZQ2yEZ0U5SpBQ4OXoySS2+kVRxmFeBBQ6C++AHR7
SUQO92QuDkcHEwKgxx9LYsO3bUDRvT0gMRwLqECC
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
