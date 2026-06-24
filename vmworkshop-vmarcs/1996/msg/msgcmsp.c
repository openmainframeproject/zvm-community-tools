/* © Copyright 1994, 1996, Richard M. Troth, all rights reserved. 
 *		(casita sourced) <plaintext> 
 * 
 *	  Name: msgcmsp.c 
 *		part of multi-mode  'tell'  command for UNIX 
 *	Author: Rick Troth, Houston, Texas, USA 
 *	  Date: 1996-May-08 (split from tell.c) 
 */ 
 
/* #include <fcntl.h> */ 
#include <errno.h> 
#include "msghndlr.h" 
 
/* -------------------------------------------------------------- MSGMSP 
 *  Try to send the message via MSP.   See RFC 1312. 
 *  This method should work even if the user is local, 
 *  but requires an MSP server to be running (psbly under 'inetd'). 
 */ 
int msgcmsp(user,text) 
  char   *user, *text; 
  { 
    char       *host, temp[256], *p, *q, buffer[BUFSIZ]; 
    int 	s, port; 
    extern  char  *userid(); 
 
    /*  parse  */ 
    host = user;	user = p = temp; 
    while (*host != '@' && *host != 0x00) *p++ = *host++; 
    if (*host == '@') host++; 
    if (host == 0x0000 || *host == 0x00) host = MSP_HOST; 
    port = MSP_PORT; 
 
    /*  try to contact the MSP server  */ 
    errno = 0; 
    (void) sprintf(temp,"%s:%d",host,port); 
    s = tcpopen(temp,0,0); 
    if (s < 0) return s; 
 
    /*  build an MSP message structure  */ 
    p = buffer; 
    *p++ = 'B';  /*  use "type B" MSP structure  */ 
    q = user; while (*q) *p++ = *q++; *p++ = 0x00; 
    q = "*";  while (*q) *p++ = *q++; *p++ = 0x00; 
    /*  canonicalize text to CR/LF  */ 
    q = text; while (*q) 
      { if (*q == '\n') *p++ = '\r'; 
	*p++ = *q++; } *p++ = 0x00; 
    q = userid(); while (*q) *p++ = *q++; *p++ = 0x00; 
    q = "?";  while (*q) *p++ = *q++; *p++ = 0x00;  /*  my terminal?  */ 
    q = "-";  while (*q) *p++ = *q++; *p++ = 0x00;  /*  ticket  */ 
    q = "-";  while (*q) *p++ = *q++; *p++ = 0x00;  /*  secure  */ 
    *p++ = 0x00; 
 
    /*  send the message  */ 
    (void) write(s,buffer,p-buffer); 
    (void) read(s,buffer,BUFSIZ); 
 
    /*  clean up  */ 
    (void) close(s); 
 
    return 0; 
  } 
 
 
