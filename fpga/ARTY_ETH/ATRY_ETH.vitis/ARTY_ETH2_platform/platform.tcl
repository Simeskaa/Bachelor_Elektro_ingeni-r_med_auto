# 
# Usage: To re-create this platform project launch xsct with below options.
# xsct C:\Users\Bruker\Documents\Bachelor_Elektro_ingenior_med_auto\fpga\ARTY_ETH\ATRY_ETH.vitis\ARTY_ETH2_platform\platform.tcl
# 
# OR launch xsct and run below command.
# source C:\Users\Bruker\Documents\Bachelor_Elektro_ingenior_med_auto\fpga\ARTY_ETH\ATRY_ETH.vitis\ARTY_ETH2_platform\platform.tcl
# 
# To create the platform in a different location, modify the -out option of "platform create" command.
# -out option specifies the output directory of the platform project.

platform create -name {ARTY_ETH2_platform}\
-hw {C:\Users\Bruker\Documents\Bachelor_Elektro_ingenior_med_auto\fpga\ARTY_ETH\design_1_wrapper_hardware.xsa}\
-proc {microblaze_0} -os {standalone} -out {C:/Users/Bruker/Documents/Bachelor_Elektro_ingenior_med_auto/fpga/ARTY_ETH/ATRY_ETH.vitis}

platform write
platform generate -domains 
platform active {ARTY_ETH2_platform}
bsp reload
bsp setlib -name lwip211 -ver 1.8
bsp config phy_link_speed "CONFIG_LINKSPEED100"
bsp write
bsp reload
catch {bsp regenerate}
platform generate
platform active {ARTY_ETH2_platform}
bsp reload
bsp reload
bsp config lwip_tcp "false"
bsp config lwip_tcp "false"
bsp config lwip_tcp "false"
bsp config tcp_wnd "2048"
bsp config tcp_ttl "255"
bsp config tcp_synmaxrtx "4"
bsp config tcp_queue_ooseq "1"
bsp config lwip_tcp "true"
bsp reload
bsp config lwip_tcp "false"
bsp config phy_link_speed "CONFIG_LINKSPEED100"
bsp write
bsp reload
catch {bsp regenerate}
bsp reload
bsp config lwip_tcp "true"
bsp write
bsp reload
catch {bsp regenerate}
platform generate
platform active {ARTY_ETH2_platform}
bsp reload
bsp reload
platform active {ARTY_ETH2_platform}
bsp reload
platform generate
