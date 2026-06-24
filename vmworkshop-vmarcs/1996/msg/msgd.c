/* © Copyright 1995, Richard M. Troth, all rights reserved.  <plaintext> 
 *		(casita sourced) 
 * 
 *	  Name: msgd.c 
 *		a simplistic MSP server using $HOME/.msgpipe FIFO 
 *	Author: Rick Troth, Houston, Texas, USA 
 *	  Date: 1995-Oct-27 and prior 
 */ 
 
#include	<errno.h> 
#include	<fcntl.h> 
#include        <pwd.h> 
#include	<sys/types.h> 
#include	<sys/stat.h> 
 
#include	"msghndlr.h" 
 
/* ------------------------------------------------------------------ */ 
int main(argc,argv) 
  int     argc; 
  char   *argv[]; 
  { 
    char	buff[BUFSIZ], temp[BUFSIZ], idnt[BUFSIZ]; 
    char       *p, *user, *term, *text, *from, *ftty, 
	       *time, *sqty, *host, *arg0; 
    int 	i, fd, msg_flag; 
    struct  passwd  *pwdent; 
    char	pipe[256]; 
 
    arg0 = argv[0]; 
 
    msg_flag = MSG_IDENT; 
    /*  process options  */ 
    for (i = 1; i < argc && argv[i][0] == '-' && 
			    argv[i][1] != 0x00; i++) 
      { 
	switch (argv[i][1]) 
	  { 
	    case 'v':	(void) sprintf(temp, 
				"%s: %s Internet TELL server", 
				arg0,MSG_VERSION); 
			(void) putline(2,temp); 
			return 0; 
			break; 
	    case 'n':	msg_flag = (msg_flag & ~MSG_IDENT); 
			break; 
	    case 'i':	msg_flag = (msg_flag | MSG_IDENT); 
			break; 
	    default:	(void) sprintf(temp, 
				"%s: invalid option %s", 
				arg0,argv[i]); 
			(void) putline(2,temp); 
			return 20; 
			break; 
	  } 
      } 
 
    /*  read the MSP data from the client  */ 
    read(0,buff,BUFSIZ); 
    p = buff; 
    user = term = text = ""; 
    switch (*p++) 
      { 
	case 'A':   user = p;   while (*p) p++;   p++; 
		    term = p;   while (*p) p++;   p++; 
		    text = p;   while (*p) p++; 
		    break; 
	case 'B':   user = p;   while (*p) p++;   p++; 
		    term = p;   while (*p) p++;   p++; 
		    text = p;   while (*p) p++;   p++; 
		    from = p;   while (*p) p++;   p++; 
		    ftty = p;   while (*p) p++;   p++; 
		    time = p;   while (*p) p++;   p++; 
		    sqty = p;   while (*p) p++; 
		    break; 
	default:    break; 
      } 
 
    /*  maybe try an IDENT lookup?  */ 
    if (msg_flag & MSG_IDENT) (void) tcpident(0,idnt,sizeof(idnt)); 
    host = idnt; 
    while (*host != 0x00 && *host != '@') host++; 
    if (*host == '@') *host++ = 0x00; 
    /*  trust IDENT's user value (if available) over MSP's  */ 
    if (idnt[0] != 0x00) user = idnt; 
 
    /*  clean-up the target username for security  */ 
    for (p = user;  *p != 0x00	&&  *p >= ' '  && 
		    *p != '|'	&&  *p != ';'  && 
		    *p != '/'	&&  *p != '*'  && 
		    *p != '$'	&&  *p != '\\';     p++);  *p = 0x00; 
    if (*user == 0x00) user = "operator"; 
 
    /*  compute the message pipe path  */ 
    pwdent = getpwnam(user); 
    if (pwdent) sprintf(pipe,"%s/.msgpipe",pwdent->pw_dir); 
    else (void) sprintf(pipe,"/home/%s/.msgpipe",user); 
 
    /*  try opening message pipe FIFO  */ 
    fd = open(pipe,O_WRONLY|O_NDELAY); 
    if (fd < 0 && errno == ENOENT) 
      { 
	(void) sprintf(pipe,"/tmp/%s.msgpipe",user); 
	fd = open(pipe,O_WRONLY|O_NDELAY); 
      } 
    if (fd < 0 && errno == ENOENT) 
      { 
	/*  try creating the FIFO;  world writable, yes!  */ 
	(void) mknod(pipe,S_IFIFO|0622,0); 
      } 
    if (fd < 0 && errno == ENXIO) 
      { 
	/*  launch default message handler  */ 
	(void) sprintf(temp,"msgcat -u '%s'",user); 
	(void) system(temp); 
	/*  see if that worked  */ 
	fd = open(pipe,O_WRONLY|O_NDELAY); 
      } 
    if (fd < 0) 
      { 
	/*  everything failed;  bail out  */ 
	sprintf(temp,"-%d (UNIX or POSIX ERRNO)",errno); 
	write(1,temp,strlen(temp)+1); 
	return fd; 
      } 
 
    /*  build the buffer;  begin at offset zero  */ 
    i = 0; 
 
    /*  copy the message text  */ 
    p = text;  while (*p) temp[i++] = *p++;  temp[i++] = 0x00; 
 
    /*  now environment variables;  first, who from?  */ 
    p = "MSGFROM=";  while (*p) temp[i++] = *p++; 
    p = from;  while (*p) temp[i++] = *p++;  temp[i++] = 0x00; 
 
    /*  what type of message?  (MSP if by way of this server)  */ 
    p = "MSGTYPE=MSP/";  while (*p) temp[i++] = *p++; 
	temp[i++] = buff[0];  temp[i++] = 0x00; 
 
    /*  also ... who's it too?  (in case that isn't obvious)  */ 
    p = "MSGUSER=";  while (*p) temp[i++] = *p++; 
    p = user;  while (*p) temp[i++] = *p++;  temp[i++] = 0x00; 
 
    /*  what about the sender's HOST address?  */ 
    p = "MSGHOST=";  while (*p) temp[i++] = *p++; 
    p = host;  while (*p) temp[i++] = *p++;  temp[i++] = 0x00; 
 
    /*  an additional NULL terminates the environment buffer  */ 
    temp[i++] = 0x00; 
 
    /*  hand it off;  feed the FIFO  (hoping there's a listener)  */ 
    (void) write(fd,temp,i); 
 
    /*  all done,  so close the file descriptor  */ 
    (void) close(fd); 
 
    /*  tell the client "okay"  */ 
    write(1,"+",1); 
 
    /*  get outta here  */ 
    return 0; 
  } 
 
 
