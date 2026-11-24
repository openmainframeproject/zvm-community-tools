/* © Copyright 1994, 1996, Richard M. Troth, all rights reserved. 
 *		(casita sourced) <plaintext> 
 * 
 *	  Name: msgcuftd.c 
 *		part of multi-mode  'tell'  command for UNIX 
 *		(message client talking to UFT daemon) 
 *	Author: Rick Troth, Rice University, Houston, Texas, USA 
 *	  Date: 1994-Jul-25 and prior, 1996-May-09 (split from tell.c) 
 */ 
 
#include <errno.h> 
#include "msghndlr.h" 
 
/* ------------------------------------------------------------- MSGUFTD
 *  That's UFTD, not just UFT, because messaging isn't part of 
 *  UFT protocol, but may be a feature of some UFTD servers. 
 */ 
int msgcuftd(user,text) 
  char   *user, *text; 
  { 
    char	temp[256], ubuf[64], *host; 
    int 	port, rc, s; 
 
    /*  parse  */ 
    host = user;	user = ubuf; 
    while (*host != '@' && *host != 0x00) *user++ = *host++; 
    if (*host == '@') host++;  *user = 0x00;  user = ubuf; 
    if (host == 0x0000 || *host == 0x00) host = MSG_DEFAULT_HOST; 
    port = MSG_UFT_PORT; 
 
    /*  try to contact the UFT server  */ 
    errno = 0; 
    (void) sprintf(temp,"%s:%d",host,port); 
    s = tcpopen(temp,0,0); 
    if (s < 0) return s; 
 
    /*  wait on a UFT/1 or UFT/2 herald  */ 
    (void) tcpgets(s,temp,sizeof(temp)); 
 
    /*  now try a UFT "MSG" command,  if available  */ 
    (void) sprintf(temp,"MSG %s %s",user,text); 
    (void) tcpputs(s,temp); 
 
    /*  wait for ACK/NAK  */ 
    rc = uftcwack(s,temp,sizeof(temp)); 
 
    /*  say goodbye politely  */ 
    (void) tcpputs(s,"QUIT"); 
    (void) uftcwack(s,temp,sizeof(temp)); 
 
    /*  return cleanly  */ 
    (void) close(s); 
    return rc; 
  } 
 
/* ------------------------------------------------------------ UFTCWACK 
 */ 
int uftcwack(s,b,l) 
  int s;  char *b;  int l; 
  { 
    int 	i; 
    char       *p; 
 
    while (1) 
      { 
	errno = 0; 
	i = tcpgets(s,b,l); 
	if (i < 0) 
	  { 
	    /* broken pipe or network error */ 
	    b[0] = 0x00; 
	    return i; 
	  } 
	switch (b[0]) 
	  { 
	    case 0x00: 
		/* NULL ACK */ 
		(void) strncpy(b,"2XX ACK (NULL)",l); 
		return 0; 
	    case '6': 
		/* write to stdout, then loop */ 
		p = b; 
		while (*p != ' ' && *p != 0x00) p++; 
		if (*p != 0x00) (void) putline(1,++p); 
	    case '1':	case '#':   case '*': 
		/* discard and loop */ 
		break; 
	    case '2':   case '3': 
		/* simple ACK or "more required" */ 
		return 0; 
	    case '4':   case '5': 
		/*  "4" means client is confused anyway, 
		    and "5" means a hard error, so ...  */ 
		return -1; 
	    default: 
		/* protocol error */ 
		return -1; 
	  } 
/* 
	if (uftcflag & UFT_VERBOSE) 
		if (b[0] != 0x00) 
			(void) putline(2,b); 
 */ 
      } 
  } 
 
 
