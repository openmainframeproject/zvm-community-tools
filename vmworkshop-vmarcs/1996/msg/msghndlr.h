/* © Copyright 1996, Richard M. Troth, all rights reserved.  <plaintext> 
 *		(casita sourced) 
 * 
 *	  Name: msghndlr.h 
 *		header file for  msgd.c  and  msgcat.c 
 *	Author: Rick Troth, Houston, Texas, USA 
 *	  Date: 1994-Jul-26, 1996-Mar-24 
 */ 
 
#define 	MSG_VERSION		"MSG/1.3.0" 
 
#define 	MSG_IDENT		0x0001 
#define 	MSG_VERBOSE		0x0002 
 
#define 	MSP_HOST		"localhost" 
#define 	MSG_DEFAULT_HOST	"localhost" 
#define 	MSP_PORT		18 
#define 	MSG_MSP_PORT		18 
 
#define 	MSG_UFT_PORT		608 
 
#ifndef 	BUFSIZ 
#define 	BUFSIZ			4096 
#endif 
 
static char *msg_copyright = 
	"© Copyright 1996, Richard M. Troth, all rights reserved. "; 
 
 
