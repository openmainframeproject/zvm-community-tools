/* © Copyright 1995, Richard M. Troth, all rights reserved.  <plaintext> 
 *		(casita sourced) 
 * 
 *	  Name: msgcat.c 
 *		writes incoming messages to standard output 
 *	Author: Rick Troth, Houston, Texas, USA 
 *	  Date: 1995-Oct-26 and prior 
 * 
 *   Operation: I think the original idea came from David Lippke, 
 *		that there should be a FIFO in the home directory 
 *		to which the user could attach any custom listener. 
 *		This is a quick and easy solution using that technique. 
 */ 
 
extern int errno; 
#include <fcntl.h> 
 
#include        "msghndlr.h" 
 
/* -------------------------------------------------------------- ENVGET 
 * Returns a pointer to the value of the requested variable, 
 * or points to the end of the environment buffer. 
 */ 
char *envget(env,var) 
  char   *env, *var; 
  { 
    char   *p, *q; 
 
    if (*env == 0x00) return env; 
 
    p = env;    q = var; 
    while (*p) 
      { 
        while (*p == *q && *p && *q && *p != '=') { p++; q++; } 
        if (*p == '=' && *q == 0x00) return ++p; 
        while (*p++);   q = var; 
      } 
 
    return p; 
  } 
 
/* ------------------------------------------------------------------ */ 
main(argc,argv) 
  int argc;  char *argv[]; 
  { 
    int 	i, fd; 
    char	buffer[4096], *p, *q, *arg0, *envbuf, *user; 
    char	outbuf[4096]; 
 
    arg0 = argv[0]; 
 
    /*  process options  */ 
    for (i = 1; i < argc && argv[i][0] == '-' && 
			    argv[i][1] != 0x00; i++) 
      { 
	switch (argv[i][1]) 
	  { 
	    case 'v':	(void) sprintf(buffer, 
				"%s: %s Internet TELL agent", 
				arg0,MSG_VERSION); 
			(void) putline(2,buffer); 
			return 0; 
			break; 
	    case 'u':	(void) close(1); 
			(void) open("/dev/console",O_WRONLY|O_NOCTTY,0); 
			(void) close(2); 
			user = argv[++i]; 
			i = fork();  if (i < 1) return i; 
			break; 
	    default:	(void) sprintf(buffer, 
				"%s: invalid option %s", 
				arg0,argv[i]); 
			(void) putline(2,buffer); 
			return 20; 
			break; 
	  } 
      } 
 
    /*  close stdin  */ 
    (void) close(0); 
 
    /*  loop forever  */ 
    while (1) 
      { 
	errno = 0; 
	sprintf(buffer,"%s/.msgpipe",getenv("HOME")); 
	fd = open(buffer,O_RDONLY); 
	if (fd < 0) 
	  { 
	    sprintf(buffer,"/tmp/%s.msgpipe",getenv("LOGNAME")); 
	    fd = open(buffer,O_RDONLY); 
	  } 
	if (fd < 0) break; 
 
	/*  loop on message instance  */ 
	while (1) 
	  { 
	    i = read(fd,buffer,4096); 
	    if (i < 1) 
	    i = read(fd,buffer,4096); 
	    if (i < 1) break; 
 
	    /*  be sure it's environment terminated (double NULL)  */ 
	    buffer[i++] = 0x00; buffer[i++] = 0x00; buffer[i++] = 0x00; 
	    /*  and reference the environment  */ 
	    envbuf = buffer; while (*envbuf) envbuf++;  envbuf++; 
 
	    /*  remove trailing line breaks and white space  */ 
	    i = strlen(buffer) - 1; 
	    while (i >= 0 && 
		(buffer[i] == '\n' || buffer[i] == '\r' 
			|| buffer[i] == ' ')) buffer[i--] = 0x00; 
 
	    /*  remove CTRLs and canonicalize line breaks  */ 
	    for (p = q = buffer; *p != 0x00; p++) 
	      { 
		if (*p < '\r') *q++ = ' '; 
		if (*p < ' ' && *p != '\t') *q++ = '.'; 
		else *q++ = *p; 
	      } 
 
	    /*  now write the message text  */ 
	    errno = 0; 
	    sprintf(outbuf,"From %s(%s): %s", 
		envget(envbuf,"MSGHOST"),envget(envbuf,"MSGUSER"),buffer); 
/* 
	    sprintf(outbuf,"From %s@%s: %s", 
		envget(envbuf,"MSGUSER"),envget(envbuf,"MSGHOST"),buffer); 
 */ 
	    if (putline(1,outbuf) < 0) break; 
	  } 
	(void) close(fd); 
      } 
    (void) perror(buffer); /* argv[0]? */ 
/* 
    (void) sprintf(buffer,"xmitmsg -2 -a errno %d",errno); 
    (void) system(buffer); 
 */ 
    return 0; 
  } 
 
 
