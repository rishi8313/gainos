/*
 *----------------------------------------------------------------------
 *    micro T-Kernel
 *
 *    Copyright (C) 2006-2008 by Ken Sakamura. All rights reserved.
 *    micro T-Kernel is distributed under the micro T-License.
 *----------------------------------------------------------------------
 *
 *    Version:   1.01.00
 *    Released by T-Engine Forum(http://www.t-engine.org) at 2008/02/25.
 *
 *----------------------------------------------------------------------
 */

/*
 *	inittask_main.c (sysmain)
 *	Initial Task
 */

#include "sysmain.h"
#include "kernel.h"
#include <sys/debug.h>

typedef INT	(*MAIN_FP)(INT, UB **);

#if USE_KERNEL_MESSAGE
LOCAL const char knl_boot_message[] = {	/* Boot message */
	BOOT_MESSAGE
};
LOCAL const char knl_user_message[] = {	/* user Boot message */
	USER_BOOT_MESSAGE
};
#endif

/* ------------------------------------------------------------------------ */

/*
 * Initial task Main
 *	The available stack size is slightly less than 8KB.
 *	The initial task is the system task,
 *	so it should not be deleted.
 */
EXPORT INT knl_init_task_main( void )
{
	INT	fin;

	/* Start message */
#if USE_KERNEL_MESSAGE
	tm_putstring((UB*)knl_boot_message);
	tm_putstring((UB*)knl_user_message);
#endif

	fin = 1;

#if RI_USERINIT != NULL
	/* Perform user defined initialization sequence */
	fin = (*(MAIN_FP)RI_USERINIT)(0, NULL);
#endif

	if ( fin > 0 ) {
		/* Perform user main */
		fin = usermain();
	}

#if RI_USERINIT != NULL
	/* Perform user defined finalization sequence */
	(*(MAIN_FP)RI_USERINIT)(-1, NULL);
#endif

	return fin;
}
