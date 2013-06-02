/* Copyright(C) 2013, GaInOS-TK by Fan Wang. All rights reserved.
 * Generated by GaInOS-TK Studio at 2013-06-02:10-28-27.
 * Don't Modify it by hand.
 * Email: parai@foxmail.com
 * URL: https://github.com/parai/gainos-tk  && http://hi.baidu.com/parai
 */


#include "osek_os.h"
#include "osek_cfg.h"
#include "knl_task.h"
#include "knl_alarm.h"
#include "knl_event.h"
#include <stdio.h>
GenTaskStack(vTaskInit,256);
GenTaskStack(vTaskSender,512);
GenTaskStack(vTaskReceiver,512);
GenTaskStack(vTaskMainFunction,512);
EXPORT const T_GTSK	knl_gtsk_table[cfgOSEK_TASK_NUM]=
{
	GenTaskInfo(vTaskInit,10,256,OSDEFAULTAPPMODE|PREEMTABLE,INVALID_EVENT,1,10),
	GenTaskInfo(vTaskSender,6,512,OSNONEAPPMODE|PREEMTABLE,INVALID_EVENT,1,6),
	GenTaskInfo(vTaskReceiver,6,512,OSNONEAPPMODE|PREEMTABLE,ID_vTaskReceiverEvent,1,6),
	GenTaskInfo(vTaskMainFunction,4,512,OSNONEAPPMODE|PREEMTABLE,INVALID_EVENT,1,4),
};

EXPORT const AlarmBaseType knl_almbase_table[cfgOSEK_COUNTER_NUM]=
{
	GenAlarmBaseInfo(30000,1,10), /* vSystemCounter */
};

EXPORT const T_GALM knl_galm_table[cfgOSEK_ALARM_NUM]=
{
	GenAlarmInfo(vAlarmSender,vSystemCounter),
	GenAlarmInfo(vAlarmReceiver,vSystemCounter),
	GenAlarmInfo(vAlarmMainFunction,vSystemCounter),
};

EXPORT const PRI knl_gres_table[cfgOSEK_RESOURCE_NUM]=
{
	/* ceilpri */ 1,  /* RES_SCHEDULER */
};

