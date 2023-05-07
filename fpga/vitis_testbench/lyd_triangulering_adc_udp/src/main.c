/*
 * Copyright (C) 2009 - 2019 Xilinx, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 *
 * 1. Redistributions of source code must retain the above copyright notice,
 *    this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
 * 3. The name of the author may not be used to endorse or promote products
 *    derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR IMPLIED
 * WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
 * SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
 * OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
 * IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
 * OF SUCH DAMAGE.
 *
 */

#include <stdio.h>

#include "xparameters.h"
#include "globals.h"
#include "netif/xadapter.h"
#include "platform.h"
#include "platform_config.h"
#if defined (__arm__) || defined(__aarch64__)
#include "xil_printf.h"
#endif

#include "lwip/tcp.h"
#include "lwip/udp.h"
#include "xil_cache.h"

#if LWIP_IPV6==1
#include "lwip/ip.h"
#else
#if LWIP_DHCP==1
#include "lwip/dhcp.h"
#endif
#endif

/********************** ADC STUFF ****************************************/
// includes for ADC
#include "xintc.h"
#include "xemaclite.h"
#include "xtmrctr.h"
#include "xsysmon.h"

/********************** GLOBAL VAR DEFINISIONS *****************************/
XSysMon xadc_wiz_0_SysMon_ADC;
XSysMon *SysMonInstPtr = &xadc_wiz_0_SysMon_ADC;

u16 SysMonDeviceId = XPAR_XADC_WIZ_0_DEVICE_ID;
u16 SysMonIntrId = XPAR_MICROBLAZE_0_AXI_INTC_XADC_WIZ_0_IP2INTC_IRPT_INTR;

volatile int eos_interrupt = FALSE; 	/* end of sequence alarm intr */

volatile u16 A0 = 0;
volatile u16 A1 = 0;
volatile u16 A2 = 0;
volatile u16 A3 = 0;

u32 trym_counter = 0;
u32 trym_counter2 = 0;


/********************** PROTOTYPE FUNCITONS *******************************/
int InitIntC(XIntc *IntcInstancePtr, u16 DeviceId);
static int InitAdc(XIntc* intc);
static void StartAdc(void);
void SysMonInterruptHandler(void *CallBackRef);
int SysMonSetupInterruptSystem(XIntc* IntcInstancePtr, XSysMon *SysMonPtr, u16 IntrId);

/********************** FUNCTIONS *****************************************/
int InitIntC(XIntc *IntcInstancePtr, u16 DeviceId)
{

	int Status;

	/*
	 * Initialize the interrupt controller driver so that it is
	 * ready to use.
	 */
	Status = XIntc_Initialize(IntcInstancePtr, DeviceId);
	if (Status != XST_SUCCESS) {
		return XST_FAILURE;
	}

	/*
	 * Perform a self-test to ensure that the hardware was built  correctly.
	 */
	Status = XIntc_SelfTest(IntcInstancePtr);
	if (Status != XST_SUCCESS) {
		return XST_FAILURE;
	}

	/*
	 * Initialize the exception table.
	 */
	Xil_ExceptionInit();

	/*
	 * Register the interrupt controller handler with the exception table.
	 */
	Xil_ExceptionRegisterHandler(XIL_EXCEPTION_ID_INT,
			(Xil_ExceptionHandler)XIntc_DeviceInterruptHandler,
			(void*) 0);

	/*
	 * Enable exceptions.
	 */
	Xil_ExceptionEnable();

	/*
	 * Start the interrupt controller such that interrupts are enabled for
	 * all devices that cause interrupts.
	 */
	Status = XIntc_Start(IntcInstancePtr, XIN_REAL_MODE);
	if (Status != XST_SUCCESS) {
		return XST_FAILURE;
	}

	return XST_SUCCESS;
}

/*****************************************************/
static int InitAdc(XIntc* intc_p)
{
	int Status;
	u32 IntrStatus;
	XSysMon_Config *ConfigPtr;

	/*
	 * Initialize the SysMon driver.
	 */
	ConfigPtr = XSysMon_LookupConfig(SysMonDeviceId);
	if (ConfigPtr == NULL) {
		return XST_FAILURE;
	}

	XSysMon_CfgInitialize(SysMonInstPtr, ConfigPtr, ConfigPtr->BaseAddress);

#if 0

	/*
	 * Disable the Channel Sequencer before configuring the Sequence
	 * registers.
	 */
	XSysMon_SetSequencerMode(SysMonInstPtr, XSM_SEQ_MODE_SAFE);

	/*
	 * Enable the following channels in the Sequencer registers:
	 * 	- On-chip Temperature
	 * 	- On-chip VCCAUX supply sensor
	 * 	- 1st Auxiliary Channel
	 * 	- 16th Auxiliary Channel
	 *
	 * Uncertain if I need to set channels to sample from, since I've set it up in the hardware design.
	 */
	Status = XSysMon_SetSeqChEnables(SysMonInstPtr, XSM_SEQ_CH_AUX04 |
													XSM_SEQ_CH_AUX05 |
													XSM_SEQ_CH_AUX06 |
													XSM_SEQ_CH_AUX07);
	if (Status != XST_SUCCESS)
	{
		return XST_FAILURE;
	}
	/*
	 * Enable the Channel Sequencer in continuous sequencer cycling mode.
	 */
	//XSysMon_SetSequencerMode(SysMonInstPtr, XSM_SEQ_MODE_CONTINPASS);
	//XSysMon_SetSequencerMode(SysMonInstPtr, XSM_SEQ_MODE_ONEPASS);
#endif

	/*
	 * Setup the interrupt system.
	 */
	Status = SysMonSetupInterruptSystem(intc_p,
					    SysMonInstPtr,
					    SysMonIntrId);
	if (Status != XST_SUCCESS) {
		return XST_FAILURE;
	}

	/*
	 * Clear any bits set in the Interrupt Status Register.
	 */
	IntrStatus = XSysMon_IntrGetStatus(SysMonInstPtr);
	XSysMon_IntrClear(SysMonInstPtr, IntrStatus);

	return 0;
}

/*****************************************************/
static void StartAdc()
{
	/*
	 * Enable end of sequence interrupt for vaux channels.
	 */
	XSysMon_IntrEnable(SysMonInstPtr, XSM_IPIXR_EOS_MASK);

	/*
	 * Enable global interrupt of System Monitor.
	 */
	XSysMon_IntrGlobalEnable(SysMonInstPtr);
}

/*****************************************************/
void SysMonInterruptHandler(void *CallBackRef) {
	u32 IntrStatusValue;
	XSysMon *SysMonPtr = (XSysMon *) CallBackRef;

	/*
	 * Get the interrupt status from the device and check the value.
	 */
	IntrStatusValue = XSysMon_IntrGetStatus(SysMonPtr);

	if (IntrStatusValue & XSM_IPIXR_EOS_MASK) {
		/*
		 * Read the ADC converted Data from the data registers.
		 */
		A0 = XSysMon_GetAdcData(SysMonInstPtr, XSM_CH_AUX_MIN+4);
		A1 = XSysMon_GetAdcData(SysMonInstPtr, XSM_CH_AUX_MIN+5);
		A2 = XSysMon_GetAdcData(SysMonInstPtr, XSM_CH_AUX_MIN+6);
		A3 = XSysMon_GetAdcData(SysMonInstPtr, XSM_CH_AUX_MIN+7);

		/*
		 * Set eos interrupt flag so the code
		 * in application context can be aware of this interrupt.
		 */
		eos_interrupt = TRUE;
		trym_counter2++;
		if(trym_counter2 > 10000)
		{
			trym_counter2 = 0;
		}
	}

	/*
	 * Clear all bits in Interrupt Status Register.
	 */
	XSysMon_IntrClear(SysMonPtr, IntrStatusValue);
}

/*****************************************************/
int SysMonSetupInterruptSystem(XIntc* IntcInstancePtr, XSysMon *SysMonPtr, u16 IntrId) {

	int Status;


	/*
	 * Connect the handler that will be called when an interrupt
	 * for the device occurs, the handler defined above performs the
	 * specific interrupt processing for the device.
	 */
	Status = XIntc_Connect(IntcInstancePtr,
				IntrId,
				(XInterruptHandler) SysMonInterruptHandler,
				SysMonPtr);
	if (Status != XST_SUCCESS) {
		return XST_FAILURE;
	}

	/*
	 * Enable the interrupt for the System Monitor/ADC device.
	 */
	XIntc_Enable(IntcInstancePtr, IntrId);

	return XST_SUCCESS;
}

/********************** ADC STUFF END  ***********************************/

/* defined by each RAW mode application */
void print_app_header();
int start_application();
int transfer_data();
void tcp_fasttmr(void);
void tcp_slowtmr(void);

/* missing declaration in lwIP */
void lwip_init();

#if LWIP_IPV6==0
#if LWIP_DHCP==1
extern volatile int dhcp_timoutcntr;
err_t dhcp_start(struct netif *netif);
#endif
#endif

extern volatile int TcpFastTmrFlag;
extern volatile int TcpSlowTmrFlag;
static struct netif server_netif;
struct netif *echo_netif;

#if LWIP_IPV6==1
void print_ip6(char *msg, ip_addr_t *ip)
{
	print(msg);
	xil_printf(" %x:%x:%x:%x:%x:%x:%x:%x\n\r",
			IP6_ADDR_BLOCK1(&ip->u_addr.ip6),
			IP6_ADDR_BLOCK2(&ip->u_addr.ip6),
			IP6_ADDR_BLOCK3(&ip->u_addr.ip6),
			IP6_ADDR_BLOCK4(&ip->u_addr.ip6),
			IP6_ADDR_BLOCK5(&ip->u_addr.ip6),
			IP6_ADDR_BLOCK6(&ip->u_addr.ip6),
			IP6_ADDR_BLOCK7(&ip->u_addr.ip6),
			IP6_ADDR_BLOCK8(&ip->u_addr.ip6));

}
#else
void
print_ip(char *msg, ip_addr_t *ip)
{
	print(msg);
	xil_printf("%d.%d.%d.%d\n\r", ip4_addr1(ip), ip4_addr2(ip),
			ip4_addr3(ip), ip4_addr4(ip));
}

void
print_ip_settings(ip_addr_t *ip, ip_addr_t *mask, ip_addr_t *gw)
{

	print_ip("Board IP: ", ip);
	print_ip("Netmask : ", mask);
	print_ip("Gateway : ", gw);
}
#endif

#if defined (__arm__) && !defined (ARMR5)
#if XPAR_GIGE_PCS_PMA_SGMII_CORE_PRESENT == 1 || XPAR_GIGE_PCS_PMA_1000BASEX_CORE_PRESENT == 1
int ProgramSi5324(void);
int ProgramSfpPhy(void);
#endif
#endif

#ifdef XPS_BOARD_ZCU102
#ifdef XPAR_XIICPS_0_DEVICE_ID
int IicPhyReset(void);
#endif
#endif

int main()
{
	/********************** ADC STUFF  ***********************************/
	int Status;
	static XIntc intc;
	/********************** ADC STUFF END  *******************************/
#if LWIP_IPV6==0
	ip_addr_t ipaddr, netmask, gw, remote_ip;

#endif
	/* the mac address of the board. this should be unique per board */
	unsigned char mac_ethernet_address[] =
	{ 0xe3, 0xf5, 0x03, 0x3e, 0x18, 0x00 }; /* dette er riktig mac addresse */
	//{ 0x00, 0x18, 0x3e, 0x03, 0xf5, 0xe3 }; /* dette er riktig mac addresse */
	//{ 0x00, 0x0a, 0x35, 0x00, 0x01, 0x02 }; /* Dette er den orginale */

	echo_netif = &server_netif;
#if defined (__arm__) && !defined (ARMR5)
#if XPAR_GIGE_PCS_PMA_SGMII_CORE_PRESENT == 1 || XPAR_GIGE_PCS_PMA_1000BASEX_CORE_PRESENT == 1
	ProgramSi5324();
	ProgramSfpPhy();
#endif
#endif

/* Define this board specific macro in order perform PHY reset on ZCU102 */
#ifdef XPS_BOARD_ZCU102
	if(IicPhyReset()) {
		xil_printf("Error performing PHY reset \n\r");
		return -1;
	}
#endif

	init_platform();

#if LWIP_IPV6==0
#if LWIP_DHCP==1
    ipaddr.addr = 0;
	gw.addr = 0;
	netmask.addr = 0;
#else
	/* initialize IP addresses to be used */
	IP4_ADDR(&ipaddr,    192, 168,   1,  10);
	IP4_ADDR(&netmask,   255, 255, 255,   0);
	IP4_ADDR(&gw,        192, 168,   1,   1);
	IP4_ADDR(&remote_ip, 192, 168,   1,  50);

#endif
#endif
	print_app_header();

	lwip_init();

#if (LWIP_IPV6 == 0)
	/* Add network interface to the netif_list, and set it as default */
	if (!xemac_add(echo_netif, &ipaddr, &netmask,
						&gw, mac_ethernet_address,
						PLATFORM_EMAC_BASEADDR)) {
		xil_printf("Error adding N/W interface\n\r");
		return -1;
	}


#else
	/* Add network interface to the netif_list, and set it as default */
	if (!xemac_add(echo_netif, NULL, NULL, NULL, mac_ethernet_address,
						PLATFORM_EMAC_BASEADDR)) {
		xil_printf("Error adding N/W interface\n\r");
		return -1;
	}
	echo_netif->ip6_autoconfig_enabled = 1;

	netif_create_ip6_linklocal_address(echo_netif, 1);
	netif_ip6_addr_set_state(echo_netif, 0, IP6_ADDR_VALID);

	print_ip6("\n\rBoard IPv6 address ", &echo_netif->ip6_addr[0].u_addr.ip6);

#endif

	/* This is the threshold, it's ok to let the code go from here. */
	netif_set_default(echo_netif);

	/* now enable interrupts */
	platform_enable_interrupts();

	/* specify that the network if is up */
	netif_set_up(echo_netif);

#if (LWIP_IPV6 == 0)
#if (LWIP_DHCP==1)
	/* Create a new DHCP client for this interface.
	 * Note: you must call dhcp_fine_tmr() and dhcp_coarse_tmr() at
	 * the predefined regular intervals after starting the client.
	 */
	dhcp_start(echo_netif);
	dhcp_timoutcntr = 24;

	while(((echo_netif->ip_addr.addr) == 0) && (dhcp_timoutcntr > 0))
		xemacif_input(echo_netif);

	if (dhcp_timoutcntr <= 0) {
		if ((echo_netif->ip_addr.addr) == 0) {
			xil_printf("DHCP Timeout\r\n");
			xil_printf("Configuring default IP of 192.168.1.10\r\n");
			IP4_ADDR(&(echo_netif->ip_addr),  192, 168,   1, 10);
			IP4_ADDR(&(echo_netif->netmask), 255, 255, 255,  0);
			IP4_ADDR(&(echo_netif->gw),      192, 168,   1,  1);
		}
	}

	ipaddr.addr = echo_netif->ip_addr.addr;
	gw.addr = echo_netif->gw.addr;
	netmask.addr = echo_netif->netmask.addr;
#endif

	print_ip_settings(&ipaddr, &netmask, &gw);

#endif
	/* start the application (web server, rxtest, txtest, etc..) */
	start_application(&ipaddr, &remote_ip);

	/* set up link with remote ip (I hope) */
	// netif_set_link_up(echo_netif);

	struct pbuf my_pbuf;

	extern struct udp_pcb *pcb_p;

	my_pbuf.payload = NULL;
	my_pbuf.len		= 0;
	my_pbuf.tot_len	= 0;
	my_pbuf.next	= 0;

	udp_sendto(pcb_p, &my_pbuf, &remote_ip, REMOTE_UDP_PORT);


	/* we need two buffers, one for the adc to fill while the other is transfered */
	/* pool of buffers */

#if 1
	/********************** ADC STUFF  ***********************************/
	/*
	 * Initialize and setup the interrupt driver
	 */
    Status = InitIntC(&intc, XPAR_MICROBLAZE_0_AXI_INTC_DEVICE_ID);
    if (Status == 0) {
       print("Intc Interrupt Setup PASSED\r\n");
    }
    else {
      print("Intc Interrupt Setup FAILED\r\n");
   }


	//print("Entering init adc\n\r");
	Status = InitAdc(&intc);
	if (Status == XST_FAILURE)
	{
		print("Error XST_FAILURE\r\n");
		while(1);
	}

	//print("Entering start\n\r");
	StartAdc();
	//print("adc started\n\r");

	/********************** ADC STUFF END  *******************************/
#endif

	/* receive and process packets */
	while (1)
	{
		/* get adc data, maybe move outside while if it is driven by interrupt */

		xemacif_input(echo_netif);


		/* if adc buffer ready */
		transfer_data(&my_pbuf, &remote_ip);
	}

	/*
	 * Disable global interrupt of System Monitor.
	 * ADC STUFF
	 */
	XSysMon_IntrGlobalDisable(SysMonInstPtr);

	/* never reached */
	cleanup_platform();

	return 0;
}
