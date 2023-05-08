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
#include <string.h>

#include "globals.h"

#include "lwip/err.h"
#include "lwip/tcp.h"
#include "lwip/udp.h"
#if defined (__arm__) || defined (__aarch64__)
#include "xil_printf.h"
#endif

// remember the udp pcb_p.
struct udp_pcb *pcb_p;

//payload

volatile u8_t err_counter = 0;

int transfer_data(struct pbuf *p, ip_addr_t *ip)
{
	err_t err;

	// send 1 on udp
	err = udp_sendto(pcb_p, p, ip, REMOTE_UDP_PORT);
	if (err != ERR_OK)
	{
		err_counter++;
		printf("\n\r udp send encountered an issue! \n\r"
				"err_counter: %d\n\r", err_counter);
	}


    // pbuf_free(p);

	return 0;
}

void print_app_header()
{
#if (LWIP_IPV6==0)
	xil_printf("\n\r\n\r-----lwIP UDP sound triangulation application by Trym Brabrand------\n\r");
#else
	xil_printf("\n\r\n\r-----lwIPv6 TCP echo server ------\n\r");
#endif
	xil_printf("UDP packets sent to port %d will be echoed back\n\r", REMOTE_UDP_PORT);
}


#ifdef TCP_YES

err_t recv_callback(void *arg, struct tcp_pcb *tpcb,
                               struct pbuf *p, err_t err)
{
	/* do not read the packet if we are not in ESTABLISHED state */
	if (!p) {
		tcp_close(tpcb);
		tcp_recv(tpcb, NULL);
		return ERR_OK;
	}

	/* indicate that the packet has been received */
	tcp_recved(tpcb, p->len);

	/* echo back the payload */
	/* in this case, we assume that the payload is < TCP_SND_BUF */
	if (tcp_sndbuf(tpcb) > p->len) {
		err = tcp_write(tpcb, p->payload, p->len, 1);
	} else
		xil_printf("no space in tcp_sndbuf\n\r");

	/* free the received pbuf */
	pbuf_free(p);

	return ERR_OK;
}

err_t accept_callback(void *arg, struct tcp_pcb *newpcb, err_t err)
{
	static int connection = 1;

	/* set the receive callback for this connection */
	tcp_recv(newpcb, recv_callback);

	/* just use an integer number indicating the connection id as the
	   callback argument */
	tcp_arg(newpcb, (void*)(UINTPTR)connection);

	/* increment for subsequent accepted connections */
	connection++;

	return ERR_OK;
}

#endif /* TCP_YES */


void udp_echo_recv(void *arg, struct udp_pcb *pcb_p, struct pbuf *p, ip_addr_t *ip, u16_t port)
{
    if (p != NULL) {
        /* send received packet back to sender */
        udp_sendto(pcb_p, p, ip, port);
        /* free the pbuf */
        pbuf_free(p);
    }
}


int start_application(const ip_addr_t *local_ip, const ip_addr_t *remote_ip)
{
	err_t err;

	/* create new TCP PCB structure */
	pcb_p = udp_new();
	if (!pcb_p) {
		xil_printf("Error creating PCB. Out of Memory\n\r");
		return -1;
	}

	/* bind to specified @port */
	err = udp_bind(pcb_p, local_ip, REMOTE_UDP_PORT); // TRYM Try switching out local port to be the same as remote port
	if (err != ERR_OK) {
		xil_printf("Unable to bind to port %d: err = %d\n\r", REMOTE_UDP_PORT, err);
		return -2;
	}

	udp_recv(pcb_p, (udp_recv_fn) udp_echo_recv, NULL);

	//udp_connect(struct udp_pcb *pcb_p, const ip_addr_t *ipaddr, u16_t port)
	err = udp_connect(pcb_p, remote_ip, REMOTE_UDP_PORT);
	if (err != ERR_OK)
	{
		xil_printf("Unable to connect: err = %d\n\r", err);
		return -2;
	}


	xil_printf("UDP echo server started @ port %d\n\r", REMOTE_UDP_PORT);

	return 0;
}
