
/* Copyright(C) 2013, GaInOS-TK by Fan Wang. All rights reserved.
 * Generated by GaInOS-TK Studio at 2013-05-12:15-51-52. 
 * This is a template for "app.c", you can add your application code here.
 */
#include <stdio.h>
#include "Os.h"

TASK(vTaskInit)
{
	StatusType ercd;
	(void)SetRelAlarm(ID_vAlarmReceiver,50,200);
	(void)SetRelAlarm(ID_vAlarmSender,100,200);
	(void)SetRelAlarm(ID_vAlarmMainFunction,150,200);
	
	(void)ActivateTask(ID_vTaskSender);
	(void)ActivateTask(ID_vTaskReceiver);
	(void)ActivateTask(ID_vTaskMainFunction);
    /* Add your task special code here, but Don't delete this Task declaration.*/
    (void)printf("vTaskInit is running.\r\n");

    (void)TerminateTask();
}

TASK(vTaskSender)
{
    /* Add your task special code here, but Don't delete this Task declaration.*/
    (void)printf("vTaskSender is running.\r\n");
    (void)GetResource(RES_SCHEDULER);
    (void)SetEvent(ID_vTaskReceiver,0x01);
    (void)ReleaseResource(RES_SCHEDULER);
    (void)TerminateTask();
}

TASK(vTaskReceiver)
{
    /* Add your task special code here, but Don't delete this Task declaration.*/
    (void)printf("vTaskReceiver is running.\r\n");
    (void)WaitEvent(0x01);
    (void)ClearEvent(0x01);
    (void)TerminateTask();
}

TASK(vTaskMainFunction)
{
    /* Add your task special code here, but Don't delete this Task declaration.*/
    (void)printf("vTaskMainFunction is running.\r\n");
    (void)TerminateTask();
}

TASK(vTaskIdle)
{
    /* Add your task special code here, but Don't delete this Task declaration.*/
	for(;;)
	{
		printf("vTaskIdle is running.\r\n");
		SleepTask(200);
	}
    (void)ChainTask(ID_vTaskIdle);
    (void)TerminateTask();
}

ALARM(vAlarmSender)
{
    /* Alarm Type: Task, you still can add your special code here.*/
    (void)ActivateTask(ID_vTaskSender);
}
ALARM(vAlarmReceiver)
{
    /* Alarm Type: Task, you still can add your special code here.*/
    (void)ActivateTask(ID_vTaskReceiver);
}
ALARM(vAlarmMainFunction)
{
    /* Alarm Type: Task, you still can add your special code here.*/
    (void)ActivateTask(ID_vTaskMainFunction);
}
