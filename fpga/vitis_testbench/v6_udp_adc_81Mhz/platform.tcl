# 
# Usage: To re-create this platform project launch xsct with below options.
# xsct C:\Users\Bruker\Documents\Bachelor_Elektro_ingenior_med_auto\fpga\vitis_testbench\v6_udp_adc_81Mhz\platform.tcl
# 
# OR launch xsct and run below command.
# source C:\Users\Bruker\Documents\Bachelor_Elektro_ingenior_med_auto\fpga\vitis_testbench\v6_udp_adc_81Mhz\platform.tcl
# 
# To create the platform in a different location, modify the -out option of "platform create" command.
# -out option specifies the output directory of the platform project.

platform create -name {v6_udp_adc_81Mhz}\
-hw {C:\Users\Bruker\Documents\0_bachelor_fpga_designs\fpga\exported_hardware_versions\arty_adc_eth_v9_81MHz.xsa}\
-proc {microblaze_0} -os {standalone} -out {C:/Users/Bruker/Documents/Bachelor_Elektro_ingenior_med_auto/fpga/vitis_testbench}

platform write
platform generate -domains 
platform active {v6_udp_adc_81Mhz}
platform generate
bsp reload
bsp reload
bsp setlib -name lwip211 -ver 1.8
bsp config phy_link_speed "CONFIG_LINKSPEED100"
bsp write
bsp reload
catch {bsp regenerate}
platform generate -domains standalone_domain 
platform generate -domains standalone_domain 
platform generate
platform active {v6_udp_adc_81Mhz}
platform generate -domains 
