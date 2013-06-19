/* Copyright(C) 2013, GaInOS-TK by Fan Wang. All rights reserved.
 * Generated by GaInOS-TK Studio at 2013-06-19:21-10-07.
 * Don't Modify it by hand.
 * Email: parai@foxmail.com
 * URL: https://github.com/parai/gainos-tk  && http://hi.baidu.com/parai
 */

#if !(((J1939TP_SW_MAJOR_VERSION == 1) && (J1939TP_SW_MINOR_VERSION == 0)) )
#error J1939Tp: Configuration file expected BSW module version to be 1.0.*
#endif

#ifndef J1939TP_CFG_H
#define J1939TP_CFG_H

#include "J1939Tp.h"

#define J1939TP_DEV_ERROR_DETECT STD_ON
#define J1939TP_PACKETS_PER_BLOCK     5
#define J1939TP_MAIN_FUNCTION_PERIOD  4
#define J1939TP_TX_CONF_TIMEOUT       99

#define J1939TP_CHANNEL_COUNT       2
#define J1939TP_TX_CHANNEL_COUNT    1
#define J1939TP_RX_CHANNEL_COUNT    1

#define J1939TP_PG_COUNT        2
#define J1939TP_TX_PG_COUNT     1
#define J1939TP_RX_PG_COUNT     1

// Number of pgs for each channel 
#define J1939TP_vRxChannel_0_PG_COUNT 1
#define J1939TP_vTxChannel_0_PG_COUNT 1

// NSDU:s
#define J1939TP_RX_vEcuC_Pdu_1 0
#define J1939TP_TX_vEcuC_Pdu_1 1

// PDU:s
//#define J1939TP_RX_vEcuC_Pdu_1 0 //FcNPdu
//#define J1939TP_TX_vEcuC_Pdu_1 1 //DtNPdu
//#define J1939TP_TX_vEcuC_Pdu_1 2 //DirectNPdu
//#define J1939TP_TX_vEcuC_Pdu_1 3 //CmNPdu
//#define J1939TP_TX_vEcuC_Pdu_0 4 //FcNPdu
//#define J1939TP_RX_vEcuC_Pdu_0 5 //DtNPdu
//#define J1939TP_RX_vEcuC_Pdu_1 6 //DirectNPdu
//#define J1939TP_RX_vEcuC_Pdu_0 7 //CmNPdu
#define J1939TP_RX_PDU_COUNT   8 /*? I don't understand */

extern const J1939Tp_ConfigType J1939Tp_Config;


#endif /*J1939TP_CFG_H*/

