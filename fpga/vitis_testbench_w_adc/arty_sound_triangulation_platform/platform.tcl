# 
# Usage: To re-create this platform project launch xsct with below options.
# xsct C:\Users\Bruker\Documents\Bachelor_Elektro_ingenior_med_auto\fpga\vitis_testbench_w_adc\arty_sound_triangulation_platform\platform.tcl
# 
# OR launch xsct and run below command.
# source C:\Users\Bruker\Documents\Bachelor_Elektro_ingenior_med_auto\fpga\vitis_testbench_w_adc\arty_sound_triangulation_platform\platform.tcl
# 
# To create the platform in a different location, modify the -out option of "platform create" command.
# -out option specifies the output directory of the platform project.

platform create -name {arty_sound_triangulation_platform}\
-hw {C:\Users\Bruker\Documents\0_bachelor_fpga_designs\fpga\exported_hardware_versions\arty_adc_n_eth_v1.xsa}\
-proc {microblaze_0} -os {standalone} -out {C:/Users/Bruker/Documents/Bachelor_Elektro_ingenior_med_auto/fpga/vitis_testbench_w_adc}

platform write
platform generate -domains 
platform active {arty_sound_triangulation_platform}
bsp reload
bsp setlib -name lwip211 -ver 1.8
bsp config phy_link_speed "CONFIG_LINKSPEED100"
bsp write
bsp reload
catch {bsp regenerate}
platform generate
platform active {arty_sound_triangulation_platform}
bsp reload
platform generate
platform active {arty_sound_triangulation_platform}
platform generate -domains 
platform clean
platform generate
platform config -updatehw {C:/Users/Bruker/Documents/0_bachelor_fpga_designs/fpga/exported_hardware_versions/arty_adc_n_eth_v1.xsa}
platform generate -domains 
platform generate -domains standalone_domain 
