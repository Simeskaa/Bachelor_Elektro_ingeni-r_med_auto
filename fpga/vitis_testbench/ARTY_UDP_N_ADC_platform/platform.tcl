# 
# Usage: To re-create this platform project launch xsct with below options.
# xsct C:\Users\Bruker\Documents\Bachelor_Elektro_ingenior_med_auto\fpga\vitis_testbench\ARTY_UDP_N_ADC_platform\platform.tcl
# 
# OR launch xsct and run below command.
# source C:\Users\Bruker\Documents\Bachelor_Elektro_ingenior_med_auto\fpga\vitis_testbench\ARTY_UDP_N_ADC_platform\platform.tcl
# 
# To create the platform in a different location, modify the -out option of "platform create" command.
# -out option specifies the output directory of the platform project.

platform create -name {ARTY_UDP_N_ADC_platform}\
-hw {C:\Users\Bruker\Documents\0_bachelor_fpga_designs\fpga\exported_hardware_versions\arty_adc_n_eth_v1.xsa}\
-proc {microblaze_0} -os {standalone} -out {C:/Users/Bruker/Documents/Bachelor_Elektro_ingenior_med_auto/fpga/vitis_testbench}

platform write
platform generate -domains 
platform active {ARTY_UDP_N_ADC_platform}
platform generate
bsp reload
platform active {ARTY_UDP_N_ADC_platform}
bsp reload
bsp reload
platform clean
platform generate
platform clean
platform generate
platform active {ARTY_UDP_N_ADC_platform}
platform config -updatehw {C:/Users/Bruker/Documents/0_bachelor_fpga_designs/fpga/exported_hardware_versions/arty_eth_n_adc_hardware_v2.xsa}
platform generate -domains 
platform config -updatehw {C:/Users/Bruker/Documents/0_bachelor_fpga_designs/fpga/exported_hardware_versions/arty_eth_n_adc_hardware_v2.xsa}
platform generate -domains 
platform config -updatehw {C:/Users/Bruker/Documents/0_bachelor_fpga_designs/fpga/exported_hardware_versions/arty_adc_n_eth_v1.xsa}
platform generate -domains 
platform config -updatehw {C:/Users/Bruker/Documents/0_bachelor_fpga_designs/fpga/exported_hardware_versions/arty_eth_adc_hw_design_v3.xsa}
platform generate -domains 
platform config -updatehw {C:/Users/Bruker/Documents/0_bachelor_fpga_designs/fpga/exported_hardware_versions/arty_eth_adc_hw_design_v3.xsa}
platform generate -domains 
platform config -updatehw {C:/Users/Bruker/Documents/0_bachelor_fpga_designs/fpga/exported_hardware_versions/arty_adc_eth_v6_wrapper.xsa}
platform generate -domains 
platform config -updatehw {C:/Users/Bruker/Documents/0_bachelor_fpga_designs/fpga/exported_hardware_versions/arty_eth_adc_hw_design_v3.xsa}
platform generate -domains 
platform active {ARTY_UDP_N_ADC_platform}
bsp reload
platform generate -domains 
