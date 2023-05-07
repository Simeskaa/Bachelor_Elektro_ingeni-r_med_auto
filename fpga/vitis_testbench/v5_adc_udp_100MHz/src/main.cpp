/*
 * This is an attempt to make a program that reads from the fpga's adc and prints the value to the terminal.
 *
 *
 */

// INCLUDES -------------------------------------------
#include <stdio.h>
#include "xparameters.h"
#include "xil_cache.h"
#include "xintc.h"
#include "xemaclite.h"
#include "xtmrctr.h"
#include "xsysmon.h"
//#include "adc_intc_callback.c"

/********************** GLOBAL VAR DEFINISIONS *******************************/
static XSysMon xadc_wiz_0_SysMon_ADC;
XSysMon *SysMonInstPtr = &xadc_wiz_0_SysMon_ADC;

u16 SysMonDeviceId = XPAR_XADC_WIZ_0_DEVICE_ID;
u16 SysMonIntrId = XPAR_MICROBLAZE_0_AXI_INTC_XADC_WIZ_0_IP2INTC_IRPT_INTR;

volatile static int eos_interrupt = FALSE; 	/* end of sequence alarm intr */


/********************** PROTOTYPE FUNCITONS *******************************/
int InitIntC(XIntc *IntcInstancePtr, u16 DeviceId);
static int InitAdc(XIntc* intc);
static void StartAdc(void);
static void SysMonInterruptHandler(void *CallBackRef);
int SysMonSetupInterruptSystem(XIntc* IntcInstancePtr, XSysMon *SysMonPtr, u16 IntrId);

/*****************************************************/
int main(void)
{
	int Status;
	static XIntc intc;
	u16 A0;
	u16 A1;
	u16 A2;
	u16 A3;
	print("Hello World! I am a program written by Trym, entering Main now.\r\n");

	print("Entering InitIntC\r\n");
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


	print("Entering init adc\n\r");
	Status = InitAdc(&intc);
	if (Status == XST_FAILURE)
	{
		print("Error XST_FAILURE\r\n");
		while(1);
	}

	print("Entering start\n\r");
	StartAdc();
	print("adc started\n\r");

	//extern volatile int eos_interrupt; 	/* end of sequence alarm intr */

	while(1)
	{
		if(eos_interrupt == TRUE)
		{
			eos_interrupt = FALSE;

			/*
			 * Read the ADC converted Data from the data registers.
			 */
			A0 = XSysMon_GetAdcData(SysMonInstPtr, XSM_SEQ_CH_AUX04);
			A1 = XSysMon_GetAdcData(SysMonInstPtr, XSM_SEQ_CH_AUX05);
			A2 = XSysMon_GetAdcData(SysMonInstPtr, XSM_SEQ_CH_AUX06);
			A3 = XSysMon_GetAdcData(SysMonInstPtr, XSM_SEQ_CH_AUX07);


			xil_printf("data: %d == %d == %d == %d\r\n\n", A0, A1, A2, A3);
		}
	}

	/*
	 * Disable global interrupt of System Monitor.
	 */
	XSysMon_IntrGlobalDisable(SysMonInstPtr);

}

/******************** FUNCTIONS **********************/
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
	XSysMon_SetSequencerMode(SysMonInstPtr, XSM_SEQ_MODE_CONTINPASS);


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

static void SysMonInterruptHandler(void *CallBackRef) {
	u32 IntrStatusValue;
	XSysMon *SysMonPtr = (XSysMon *) CallBackRef;

	/*
	 * Get the interrupt status from the device and check the value.
	 */
	IntrStatusValue = XSysMon_IntrGetStatus(SysMonPtr);

	if (IntrStatusValue & XSM_IPIXR_EOS_MASK) {
		/*
		 * Set Temperature interrupt flag so the code
		 * in application context can be aware of this interrupt.
		 */
		eos_interrupt = TRUE;
	}

	/*
	 * Clear all bits in Interrupt Status Register.
	 */
	XSysMon_IntrClear(SysMonPtr, IntrStatusValue);
}

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
