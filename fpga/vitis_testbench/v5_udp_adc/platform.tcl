# 
# Usage: To re-create this platform project launch xsct with below options.
# xsct C:\Users\Bruker\Documents\Bachelor_Elektro_ingenior_med_auto\fpga\vitis_testbench\v5_udp_adc\platform.tcl
# 
# OR launch xsct and run below command.
# source C:\Users\Bruker\Documents\Bachelor_Elektro_ingenior_med_auto\fpga\vitis_testbench\v5_udp_adc\platform.tcl
# 
# To create the platform in a different location, modify the -out option of "platform create" command.
# -out option specifies the output directory of the platform project.

platform create -name {v5_udp_adc}\
-hw {C:\Users\Bruker\Documents\Bachelor_Elektro_ingenior_med_auto\fpga\project_2\arty_adc_eth_v8_wrapper.xsa}\
-proc {microblaze_0} -os {standalone} -out {C:/Users/Bruker/Documents/Bachelor_Elektro_ingenior_med_auto/fpga/vitis_testbench}

platform write
platform generate -domains 
platform active {v5_udp_adc}
platform generate
platform generate
platform generate
platform generate
