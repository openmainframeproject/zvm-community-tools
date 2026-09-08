/* © Copyright 1994, 1996, Richard M. Troth, all rights reserved. 
 *		(casita sourced) <plaintext> 
 * 
 *	  Name: msglocal.c 
 *		a multi-mode  'tell'  command for UNIX 
 *	Author: Rick Troth, Houston, Texas, USA 
 *	  Date: 1994-Jul-25 and prior 
 */ 
 
#include <fcntl.h> 
#include <errno.h> 
#include "msghndlr.h" 
 
/* ------------------------------------------------------------- HOMEDIR
 *  Attempt to write the message directly to the user's ".msgpipe". 
 */ 
#include        <pwd.h> 
char *homedir(u) 
  char   *u; 
  { 
    struct  passwd     *pwdent; 
    static  char        failsafe[256]; 
    pwdent = getpwnam(u); 
    if (pwdent) return pwdent->pw_dir; 
    (void) sprintf(failsafe,"/home/%s",u); 
    return failsafe; 
  } 
 
/* ------------------------------------------------------------ MSGLOCAL
 */ 
int msglocal(user,text) 
  char   *user, *text; 
  { 
    int 	fd; 
    char	temp[256]; 
 
    (void) sprintf(temp,"%s/.msgpipe",homedir(user)); 
    fd = open(temp,O_WRONLY|O_NDELAY); 
/*  if (fd < 0 && errno == ENOENT) 
	then  'mknod'  with 622 perms (writable  */ 
    if (fd < 0 && errno == ENXIO) 
      { 
	/*  launch our special application  */ 
	fd = open(temp,O_WRONLY|O_NDELAY); 
      } 
    if (fd < 0) return fd; 
 
    (void) write(fd,text,strlen(text)); 
    (void) close(fd); 
 
    return 0; 
  } 
 
/* 
     O_NDELAY       When  opening  a  FIFO  (named  pipe  -   see 
                    mknod(2V)) with O_RDONLY or O_WRONLY set: 
 
                    If O_NDELAY is set: 
                         An  open()  for   reading-only   returns 
                         without  delay.   An open() for writing- 
                         only returns  an  error  if  no  process 
                         currently has the file open for reading. 
 
                    If O_NDELAY is clear: 
                         A call to open() for reading-only blocks 
                         until a process opens the file for writ- 
                         ing.  A call to open() for  writing-only 
                         blocks  until  a  process opens the file 
                         for reading. 
 */ 
 
 
