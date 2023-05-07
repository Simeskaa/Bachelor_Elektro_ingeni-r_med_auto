#ifdef NOT_SET

//#include "adc_intc_callback.h"
#include "xsysmon.h"
#include "xparameters.h"
#include "xstatus.h"
#include "xil_exception.h"
#include "xil_printf.h"
#include "xintc.h"
#include "xil_types.h"

/************************** Constant Definitions ****************************/



/*********************** FLAG VARIABLES ************************/

/*
 * Shared variables used to test the callbacks.
 */
volatile int eos_interrupt = FALSE; 	/* end of sequence alarm intr */

/*****************************************************************************/
/**
 *
 * This function is the Interrupt Service Routine for the System Monitor device.
 * It will be called by the processor whenever an interrupt is asserted
 * by the device.
 *
 * There are 10 different interrupts supported
 *	- Over Temperature
 *	- ALARM 0
 *	- ALARM 1
 *	- ALARM 2
 *	- End of Sequence
 *	- End of Conversion
 *	- JTAG Locked
 *	- JATG Modified
 *	- Over Temperature deactivate
 *	- ALARM 0 deactivate
 *
 * This function only handles ALARM 0 and ALARM 2 interrupts. User of this
 * code may need to modify the code to meet needs of the application.
 *
 * @param	CallBackRef is the callback reference passed from the Interrupt
 *		controller driver, which in our case is a pointer to the
 *		driver instance.
 *
 * @return	None.
 *
 * @note		This function is called within interrupt context.
 *
 ******************************************************************************/
static void SysMonInterruptHandler(void *CallBackRef) {
	u32 IntrStatusValue;
	XSysMon *SysMonPtr = (XSysMon *) CallBackRef;

	/*
	 * Get the interrupt status from the device and check the value.
	 */
	IntrStatusValue = XSysMon_IntrGetStatus(SysMonPtr);

	if (IntrStatusValue & XSM_SR_EOS_MASK) {
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

/****************************************************************************/
/**
*
* This function sets up the interrupt system so interrupts can occur for the
* System Monitor/ADC.  The function is application-specific since the actual
* system may or may not have an interrupt controller. The System Monitor/ADC
* device could be directly connected to a processor without an interrupt
* controller. The user should modify this function to fit the application.
*
* @param	IntcInstancePtr is a pointer to the Interrupt Controller
*		driver Instance.
* @param	SysMonPtr is a pointer to the driver instance for the System
* 		Monitor device which is going to be connected to the interrupt
*		controller.
* @param	IntrId is XPAR_<INTC_instance>_<SYSMON_ADC_instance>_VEC_ID
*		value from xparameters.h.
*
* @return	XST_SUCCESS if successful, or XST_FAILURE.
*
* @note		None.
*
*
****************************************************************************/
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

#endif /* NOT_SET */
