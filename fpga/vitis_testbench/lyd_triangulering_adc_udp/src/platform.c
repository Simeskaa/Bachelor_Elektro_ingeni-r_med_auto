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
#if __MICROBLAZE__ || __PPC__
#include "arch/cc.h"
#include "platform.h"
#include "platform_config.h"
#include "xil_cache.h"
#include "xparameters.h"
#include "xintc.h"
#include "xil_exception.h"
#include "lwip/tcp.h"
#include "netif/xadapter.h"
#ifdef STDOUT_IS_16550
#include "xuartns550_l.h"
#endif


#if LWIP_DHCP==1
volatile int dhcp_timoutcntr = 24;
void dhcp_fine_tmr();
void dhcp_coarse_tmr();
#endif

/********************** ADC STUFF ****************************************/
// includes for ADC
#include "xemaclite.h"
#include "xtmrctr.h"
#include "xsysmon.h"

volatile int TcpFastTmrFlag = 0;
volatile int TcpSlowTmrFlag = 0;

extern struct netif *echo_netif;

void
timer_callback()
{
	static int DetectEthLinkStatus = 0;
	/* we need to call tcp_fasttmr & tcp_slowtmr at intervals specified by lwIP.
	 * It is not important that the timing is absoluetly accurate.
	 */
	static int odd = 1;
#if LWIP_DHCP==1
    static int dhcp_timer = 0;
#endif

	DetectEthLinkStatus++;
	 TcpFastTmrFlag = 1;

	odd = !odd;
	if (odd) {

#if LWIP_DHCP==1
		dhcp_timer++;
		dhcp_timoutcntr--;
#endif
		TcpSlowTmrFlag = 1;
#if LWIP_DHCP==1
		dhcp_fine_tmr();
		if (dhcp_timer >= 120) {
			dhcp_coarse_tmr();
			dhcp_timer = 0;
		}
#endif
	}

	/* For detecting Ethernet phy link status periodically */
	if (DetectEthLinkStatus == ETH_LINK_DETECT_INTERVAL) {
		eth_link_detect(echo_netif);
		DetectEthLinkStatus = 0;
	}
}

/********************** GLOBAL ADC DEFINISIONS *****************************/
static XSysMon xadc_wiz_0_SysMon_ADC;
static XSysMon *SysMonInstPtr = &xadc_wiz_0_SysMon_ADC;
u16 SysMonDeviceId = XPAR_XADC_WIZ_0_DEVICE_ID;
u16 SysMonIntrId = XPAR_MICROBLAZE_0_AXI_INTC_XADC_WIZ_0_IP2INTC_IRPT_INTR;
static XIntc intc;

/********************** ADC FUNCTIONS ****************************************/
/*****************************************************/
int InitAdc()
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

	/*
	 * Setup the interrupt system.
	 */
	Status = SysMonSetupInterruptSystem(SysMonIntrId);
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
void StartAdc()
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

/**********************************************************
                Buffer for ADC samples:
**********************************************************/
u16 adc_buffer[2*ADC_BUFFER_SIZE];  // Buffer is in fact two buffers

u16 *adc_buff_write_p = adc_buffer;
u32 adc_buff_write_enable = TRUE;
u32 adc_buff_1_filled = FALSE;
u32 adc_buff_2_filled = FALSE;
u32 interrupt_counter = 0;

/**********************************************************
                ADC interrupt handler:
**********************************************************/
void SysMonInterruptHandler(void *CallBackRef)
{
	u32 IntrStatusValue;
	XSysMon *SysMonPtr = (XSysMon *) CallBackRef;
	interrupt_counter++;

	IntrStatusValue = XSysMon_IntrGetStatus(SysMonPtr);  // Get Interrupt Status Register

	if (IntrStatusValue & XSM_IPIXR_EOS_MASK)  // If this is End Of Sequence interrupt-
    {
        if (adc_buff_write_enable)  // -and we are allowed to write into adc_buffer:
        {
             // Move samples from the ADC into adc_buffer:
            *(adc_buff_write_p++) = XSysMon_GetAdcData(SysMonInstPtr, XSM_CH_AUX_MIN+4);
            *(adc_buff_write_p++) = XSysMon_GetAdcData(SysMonInstPtr, XSM_CH_AUX_MIN+5);
            *(adc_buff_write_p++) = XSysMon_GetAdcData(SysMonInstPtr, XSM_CH_AUX_MIN+6);
            *(adc_buff_write_p++) = XSysMon_GetAdcData(SysMonInstPtr, XSM_CH_AUX_MIN+7);

            if (adc_buff_write_p >= &adc_buffer[2*ADC_BUFFER_SIZE])  // We are at the end of buffer-2:
            {
                adc_buff_write_p = adc_buffer;  // Start at beginning of buffer-1 next time
                adc_buff_2_filled = TRUE;       // Tell main-loop that buffer-2 is ready
                if (adc_buff_1_filled)              // If buffer-1 is still filled -
                    adc_buff_write_enable = FALSE;  // - pause filling until buffer-1 is empty
            }
            else if (adc_buff_write_p == &adc_buffer[ADC_BUFFER_SIZE])  // We are at the end of buffer-1:
            {
                adc_buff_1_filled = TRUE;       // Tell main-loop that buffer-1 is ready
                if (adc_buff_2_filled)              // If buffer-2 is still filled -
                    adc_buff_write_enable = FALSE;  // - pause filling until buffer-2 is empty
            }
        }
	}
	XSysMon_IntrClear(SysMonPtr, IntrStatusValue);  // Clear interrupts from Interrupt Status Register
}

/*********************************************************/

/*****************************************************/
int SysMonSetupInterruptSystem(u16 IntrId) {

	int Status;
	XIntc *intcp;
	intcp = &intc;

	/*
	 * Connect the handler that will be called when an interrupt
	 * for the device occurs, the handler defined above performs the
	 * specific interrupt processing for the device.
	 */
	Status = XIntc_Connect(intcp,
				IntrId,
				(XInterruptHandler) SysMonInterruptHandler,
				SysMonInstPtr);
	if (Status != XST_SUCCESS) {
		return XST_FAILURE;
	}

	/*
	 * Enable the interrupt for the System Monitor/ADC device.
	 */
	XIntc_Enable(intcp, IntrId);

	return XST_SUCCESS;
}

/********************** ADC STUFF END  ***********************************/

void platform_setup_interrupts()
{
	XIntc *intcp;
	intcp = &intc;

	XIntc_Initialize(intcp, XPAR_INTC_0_DEVICE_ID);
	XIntc_Start(intcp, XIN_REAL_MODE);

	/* Start the interrupt controller */
	XIntc_MasterEnable(XPAR_INTC_0_BASEADDR);

#ifdef __PPC__
	Xil_ExceptionInit();
	Xil_ExceptionRegisterHandler(XIL_EXCEPTION_ID_INT,
			(XExceptionHandler)XIntc_DeviceInterruptHandler,
			(void*) XPAR_INTC_0_DEVICE_ID);
#elif __MICROBLAZE__
	microblaze_register_handler((XInterruptHandler)XIntc_InterruptHandler, intcp);
#endif

	platform_setup_timer();

#ifdef XPAR_ETHERNET_MAC_IP2INTC_IRPT_MASK
	/* Enable timer and EMAC interrupts in the interrupt controller */
	XIntc_EnableIntr(XPAR_INTC_0_BASEADDR,
#ifdef __MICROBLAZE__
			PLATFORM_TIMER_INTERRUPT_MASK |
#endif
			XPAR_ETHERNET_MAC_IP2INTC_IRPT_MASK);
#endif


#ifdef XPAR_INTC_0_LLTEMAC_0_VEC_ID
#ifdef __MICROBLAZE__
	XIntc_Enable(intcp, PLATFORM_TIMER_INTERRUPT_INTR);
#endif
	XIntc_Enable(intcp, XPAR_INTC_0_LLTEMAC_0_VEC_ID);
#endif


#ifdef XPAR_INTC_0_AXIETHERNET_0_VEC_ID
	XIntc_Enable(intcp, PLATFORM_TIMER_INTERRUPT_INTR);
	XIntc_Enable(intcp, XPAR_INTC_0_AXIETHERNET_0_VEC_ID);
#endif


#ifdef XPAR_INTC_0_EMACLITE_0_VEC_ID
#ifdef __MICROBLAZE__
	XIntc_Enable(intcp, PLATFORM_TIMER_INTERRUPT_INTR);
#endif
	XIntc_Enable(intcp, XPAR_INTC_0_EMACLITE_0_VEC_ID);
#endif


}

void
enable_caches()
{
#ifdef __PPC__
	Xil_ICacheEnableRegion(CACHEABLE_REGION_MASK);
	Xil_DCacheEnableRegion(CACHEABLE_REGION_MASK);
#elif __MICROBLAZE__
#ifdef XPAR_MICROBLAZE_USE_ICACHE
	Xil_ICacheEnable();
#endif
#ifdef XPAR_MICROBLAZE_USE_DCACHE
	Xil_DCacheEnable();
#endif
#endif
}

void
disable_caches()
{
	Xil_DCacheDisable();
	Xil_ICacheDisable();
}

void init_platform()
{
	enable_caches();

#ifdef STDOUT_IS_16550
	XUartNs550_SetBaud(STDOUT_BASEADDR, XPAR_XUARTNS550_CLOCK_HZ, 9600);
	XUartNs550_SetLineControlReg(STDOUT_BASEADDR, XUN_LCR_8_DATA_BITS);
#endif

	platform_setup_interrupts();
}

void cleanup_platform()
{
#if 0
	/*
	 * Disable global interrupt of System Monitor.
	 * ADC STUFF
	 */
	XSysMon_IntrGlobalDisable(SysMonInstPtr);
#endif
	disable_caches();
}
#endif
