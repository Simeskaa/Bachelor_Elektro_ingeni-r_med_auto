# Usage with Vitis IDE:
# In Vitis IDE create a Single Application Debug launch configuration,
# change the debug type to 'Attach to running target' and provide this 
# tcl script in 'Execute Script' option.
# Path of this script: C:\Users\Bruker\Documents\Bachelor_Elektro_ingenior_med_auto\fpga\vitis_testbench\v5_adc_udp_100MHz_system\_ide\scripts\debugger_v5_adc_udp_100mhz-default.tcl
# 
# 
# Usage with xsct:
# To debug using xsct, launch xsct and run below command
# source C:\Users\Bruker\Documents\Bachelor_Elektro_ingenior_med_auto\fpga\vitis_testbench\v5_adc_udp_100MHz_system\_ide\scripts\debugger_v5_adc_udp_100mhz-default.tcl
# 
connect -url tcp:127.0.0.1:3121
targets -set -filter {jtag_cable_name =~ "Digilent Arty A7-35T 210319B57FF6A" && level==0 && jtag_device_ctx=="jsn-Arty A7-35T-210319B57FF6A-0362d093-0"}
fpga -file C:/Users/Bruker/Documents/Bachelor_Elektro_ingenior_med_auto/fpga/vitis_testbench/v5_adc_udp_100MHz/_ide/bitstream/download.bit
targets -set -nocase -filter {name =~ "*microblaze*#0" && bscan=="USER2" }
loadhw -hw C:/Users/Bruker/Documents/Bachelor_Elektro_ingenior_med_auto/fpga/vitis_testbench/v5_udp_adc/export/v5_udp_adc/hw/arty_adc_eth_v8_wrapper.xsa -regs
configparams mdm-detect-bscan-mask 2
targets -set -nocase -filter {name =~ "*microblaze*#0" && bscan=="USER2" }
rst -system
after 3000
targets -set -nocase -filter {name =~ "*microblaze*#0" && bscan=="USER2" }
dow C:/Users/Bruker/Documents/Bachelor_Elektro_ingenior_med_auto/fpga/vitis_testbench/v5_adc_udp_100MHz/Debug/v5_adc_udp_100MHz.elf
targets -set -nocase -filter {name =~ "*microblaze*#0" && bscan=="USER2" }
con
