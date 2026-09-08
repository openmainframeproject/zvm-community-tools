/* © Copyright 1994, 1996, Richard M. Troth, all rights reserved. 
 *		(casita sourced) <plaintext> 
 * 
 *	  Name: msgc.c (tell.c) 
 *		a multi-mode  'tell'  command for UNIX 
 *	Author: Rick Troth, Rice University, Houston, Texas, USA 
 *	  Date: 1994-Jul-25 and prior 
 */ 
 
#include <fcntl.h> 
#include <errno.h> 
#include "msghndlr.h" 
 
/* ------------------------------------------------------------ MSGWRITE 
 *  Try stock UNIX 'write' command if local user. 
 */ 
int msgwrite(user,text) 
  char   *user, *text; 
  { 
    char	temp[256]; 
    (void) sprintf(temp,"echo \"%s\" | write %s",text,user); 
    return system(temp); 
  } 
 
/* ------------------------------------------------------------ MSGSMTPS 
 *  Try SMTP "send" command.  (not always implemented) 
 */ 
int msgsmtps(user,text) 
  char   *user, *text; 
  { 
    return -1; 
  } 
 
/* ------------------------------------------------------------ MSGSMTPM 
 *  Try SMTP mail.  (advantage is direct -vs- queued) 
 */ 
int msgsmtpm(user,text) 
  char   *user, *text; 
  { 
    return -1; 
  } 
 
/* ------------------------------------------------------------- MSGMAIL 
 *  Try queued mail (sendmail) as a last resort. 
 */ 
int msgmail(user,text) 
  char   *user, *text; 
  { 
    return -1; 
  } 
 
/* -------------------------------------------------------------- DOTELL 
 */ 
int dotell(user,text) 
  char   *user, *text; 
  { 
    if (msgcmsp(user,text) && 
	msgcuftd(user,text) && 
	msglocal(user,text) && 
	msgwrite(user,text) && 
	msgsmtps(user,text) && 
	msgsmtpm(user,text) && 
	msgmail(user,text)) return -1; 
    else return 0; 
  } 
 
/* ------------------------------------------------------------------ */ 
int main(argc,argv) 
  int     argc; 
  char   *argv[]; 
  { 
    int     i, j, k; 
    char    msgbuf[4096], *arg0; 
 
    arg0 = argv[0]; 
 
    /*  process options  */ 
    for (i = 1; i < argc && argv[i][0] == '-' && 
			    argv[i][1] != 0x00; i++) 
      { 
	switch (argv[i][1]) 
	  { 
	    case 'v':	(void) sprintf(msgbuf, 
				"%s: %s Internet TELL client", 
				arg0,MSG_VERSION); 
			(void) putline(2,msgbuf); 
			return 0; 
			break; 
	    default:	(void) sprintf(msgbuf, 
				"%s: invalid option %s", 
				arg0,argv[i]); 
			(void) putline(2,msgbuf); 
			return 20; 
			break; 
	  } 
      } 
 
    /*  confirm sufficient arguments  */ 
    if (argc < 2) 
      { 
	(void) system("xmitmsg -2 386"); 
	return 24; 
      } 
 
    /*  parse them  */ 
    if (argc > 2) 
      { 
	k = 0; 
	for (i = 2; i < argc; i++) 
	  { 
	    for (j = 0; argv[i][j] != 0x00; j++) 
	    msgbuf[k++] = argv[i][j]; 
	    msgbuf[k++] = ' '; 
	  } 
	msgbuf[k++] = 0x00; 
	(void) dotell(argv[1],msgbuf); 
      } 
    else while (1) 
      { 
	(void) getline(0,msgbuf); 
	if (msgbuf[0] == '.' && msgbuf[1] == 0x00) break; 
	(void) dotell(argv[1],msgbuf); 
      } 
    return 0; 
  } 
 
 
