/* © Copyright 1995, Richard M. Troth, all rights reserved.  <plaintext> 
 * 
 *        Name: tcpiolib.c 
 *		various TCP utility functions 
 *      Author: Rick Troth, Houston, Texas, USA 
 *        Date: 1995-Apr-19 
 */ 
 
#include        <sys/types.h> 
#include        <sys/socket.h> 
#include        <stdio.h> 
#include        <netdb.h> 
 
#define 	TCPSMALL	256 
#define 	TCPLARGE	4096 
 
int	tcp_ubuf[TCPLARGE]; 
int	tcp_uoff, tcp_uend; 
char	tcp_umsg[TCPSMALL]; 
 
/* ------------------------------------------------------------- TCPOPEN 
 *  Tries to mimick  open(path,flags[,mode]) 
 *  but connects to a TCP port,  not a local file. 
 */ 
int tcpopen(host,flag,mode) 
  char  *host;  int  flag;  int  mode; 
  { 
    int         s, i, port, rc, j; 
    struct sockaddr name; 
    struct hostent *hent, myhent; 
    char       *myhental[2], myhenta0[4], myhenta1[4]; 
    char	temp[TCPSMALL], *p, *q; 
 
    /*  parse host address and port number by colon  */ 
    p = host; host = temp; i = 0; 
    while (i < TCPSMALL && *p != 0x00 && *p != ':') 
	host[i++] = *p++; host[i++] = 0x00; 
    if (*p != ':') port = 0; 
    else 
      { 
	p++; q = p; 
	while (i < TCPSMALL && *q != 0x00 && *q != ':') 
	    temp[i++] = *q++; temp[i++] = 0x00; 
	port = atoi(p); 
      } 
 
    /*  figure out where to connect  */
    hent = gethostbyname(host); 
    if (hent == NULL) 
      { 
	/*  netDB lookup failed;  numeric address supplied?  */ 
	p = host; 
	if (*p < '0' || '9' < *p) return -1; 
	hent = &myhent; 
	hent->h_addr_list = myhental;		/*  address list  */ 
	hent->h_addr_list[0] = myhenta0;	/*  address 0  */ 
	hent->h_addr_list[1] = myhenta1;	/*  address 1  */ 
	hent->h_addrtype = AF_INET; 
	hent->h_length = 4; 
 
	/*  try to pick-apart the string as dotted decimal  */ 
	hent->h_addr_list[0][0] = atoi(p); 
	while (*p != '.' && *p != 0x00) p++; p++; 
	if (*p < '0' || '9' < *p) return -1; 
	hent->h_addr_list[0][1] = atoi(p); 
	while (*p != '.' && *p != 0x00) p++; p++; 
	if (*p < '0' || '9' < *p) return -1; 
	hent->h_addr_list[0][2] = atoi(p); 
	while (*p != '.' && *p != 0x00) p++; p++; 
	if (*p < '0' || '9' < *p) return -1; 
	hent->h_addr_list[0][3] = atoi(p); 
 
	/*  dotted decimal worked!  now terminate the list  */ 
	hent->h_addr_list[1][0] = 0;	hent->h_addr_list[1][1] = 0; 
	hent->h_addr_list[1][2] = 0;	hent->h_addr_list[1][3] = 0; 
	/*  better form might be to use NULL pointer?  */ 
	hent->h_addr_list[1] = NULL; 
 
	/*  and what else do we need to set?  */ 
	hent->h_name = host; 
	/*  should probably call gethostbyaddr() 
	    at this point;  maybe in the next rev  */ 
      } 
 
    /*  gimme a socket  */
    s = socket(AF_INET,SOCK_STREAM,0);
    if (s < 0) return s; 
 
    /*  build that structure  */ 
    name.sa_family = AF_INET; 
    name.sa_data[0] = (port >> 8) & 0xFF; 
    name.sa_data[1] = port & 0xFF; 
 
    /*  try address one-by-one  */ 
    for (i = 0; hent->h_addr_list[i] != NULL; i++) 
      { 
	/*  any more addresses?  */ 
	if (hent->h_addr_list[i] == NULL) break; 
	if (hent->h_addr_list[i][0] == 0x00) break; 
 
	/*  fill-in this address to the structure  */ 
	for (j = 0; j < hent->h_length; j++) 
	    name.sa_data[j+2] = hent->h_addr_list[i][j]; 
	name.sa_data[j+2] = 0x00;	/*  terminate  */ 
 
	/*  note this attempt  */ 
	(void) sprintf(tcp_umsg,"trying %d.%d.%d.%d\n",name.sa_data[2], 
		name.sa_data[3],name.sa_data[4],name.sa_data[5]); 
 
	/*  can we talk?  */
	rc = connect(s, &name, 16); 
	if (rc == 0) return s; 
      } 
 
    /*  can't seem to reach this host on this port  :-(  */ 
    (void) close(s); 
    if (rc < 0) return rc; 
    return -1; 
  } 
 
/* ------------------------------------------------------------ TCPCLOSE 
 */ 
int tcpclose(fd) 
  int fd; 
  { 
    return close(fd); 
  } 
 
/* ------------------------------------------------------------- TCPGETS 
 *   Operation: Reads a CR/LF terminated string from socket s 
 *		into buffer b.  Returns the length of that string. 
 *	Author: Rick Troth, Houston, Texas, USA 
 *	  Date: 1995-Apr-19 
 * 
 *    See also: getline.c, putline.c, netline.c 
 */ 
int tcpgets(s,b,l) 
  int  s;  char  *b;  int  l; 
  { 
    char       *p; 
    int 	i; 
 
    p = b; 
    for (i = 0; i < l; i++) 
      { 
	if (read(s,p,1) != 1)		/*  get a byte  */ 
	if (read(s,p,1) != 1) return -1;	/*  try again  */ 
	if (*p == '\n') break;		/*  NL terminates  */ 
	if (*p == 0x00) break;		/*  NULL terminates  */ 
/*	if (*p == '\t') *p = ' ';	**  [don't] eliminate TABs  */ 
	p++;				/*  increment pointer  */ 
      } 
    *p = 0x00;		/*  NULL terminate,  even if NULL  */ 
 
    if (i > 0 && b[i-1] == '\r')	/*  trailing CR?  */ 
      { 
	i = i - 1;	/*  shorten length by one  */ 
	p--;		/*  backspace  */ 
	*p = 0x00;	/*  remove trailing CR  */ 
      } 
 
    tcp_uoff = 0; 
    tcp_uend = 0; 
    return i; 
  } 
 
/* ------------------------------------------------------------- TCPPUTS 
 *   Operation: Writes the NULL terminated string from buffer b 
 *		to socket s with CR/LF (network text) line termination. 
 *	Author: Rick Troth, Houston, Texas, USA 
 *	  Date: 1995-Apr-19 
 * 
 *    See also: getline.c, putline.c, netline.c 
 */ 
int tcpputs(s,b) 
  int     s; 
  char   *b; 
  { 
    int 	i,  j; 
    char	temp[4096]; 
 
    for (i = 0; b[i] != 0x00; i++) temp[i] = b[i]; 
    temp[i+0] = '\r'; 
    temp[i+1] = '\n'; 
    j = write(s,temp,i+2); 
 
    if (j != i+2) return -1; 
    return i; 
  } 
 
/* ------------------------------------------------------------ TCPWRITE 
 */ 
int tcpwrite(fd,s,n) 
  int fd;  char *s;  int n; 
  { 
    return write(fd,s,n); 
  } 
 
/* ------------------------------------------------------------- TCPREAD 
 */ 
int tcpread(fd,s,n) 
  int fd;  char *s;  int n; 
  { 
    return read(fd,s,n); 
  } 
 
/* ------------------------------------------------------------ TCPIDENT 
 * 
 *        Name: tcpident.c 
 *		who's on the other end of this TCP socket? 
 *      Author: Rick Troth, Rice University, Information Systems 
 *        Date: 1995-Apr-19 
 * 
 *		This is the part that was done on Rice time, 
 *		prompting the "R" in the version string. 
 *		It was to shore-up the last requirements 
 *		for the implementation that Rice might keep. 
 *		Sadly (to me) someone yanked it (UFT entirely) 
 *		the very first day I was gone. 
 */ 
 
#ifndef 	NULL 
#define 	NULL		0x0000 
#endif 
 
#define 	HOST_BSZ	128 
#define 	USER_BSZ	64 
#define 	TEMP_BSZ	256 
 
#define 	IDENT_PORT	113 
 
/* ------------------------------------------------------------ TCPIDENT 
 */ 
int tcpident(sock,buff,size) 
  int  sock;  char  *buff;  int  size; 
  { 
    struct  sockaddr	sadr; 
    struct  hostent    *hent; 
    int 	i, rc, slen, styp, soff; 
    char	temp[TEMP_BSZ]; 
    char	hadd[16];	/*  is that enough?  */ 
    char	host[HOST_BSZ]; 
    char	user[USER_BSZ]; 
    int 	plcl, prmt; 
    char       *p; 
 
/* 
(void) netline(2,">>>>>>>>"); 
 */ 
 
    /*  preload a few storage areas  */ 
    host[0] = 0x00; 
    user[0] = 0x00; 
 
    /*  first,  tell me about this end  */ 
    slen = sizeof(sadr); 
    rc = getsockname(sock,&sadr,&slen); 
    if (rc != 0) 
      { 
/*	perror("getsockname()");  */ 
	if (rc < 0) return rc; 
		else return -1; 
      } 
    styp = sadr.sa_family; 
 
    /*  where's the offset into the address?  */ 
    switch (styp) 
      { 
	case AF_INET:	soff = 2;   slen = 4; 
			break; 
	default:	soff = 2; 
			break; 
      } 
 
    /*  and snag that port number  */ 
    plcl = 0; 
    for (i = 0; i < soff; i++) 
        plcl = (plcl << 8) + (sadr.sa_data[i] & 0xFF); 
 
/* 
(void) sprintf(temp,"PORT=%d (mine)",plcl); 
(void) netline(2,temp); 
 */ 
 
    /*  what's the host on the other end?  */ 
    slen = sizeof(sadr); 
    rc = getpeername(sock,&sadr,&slen); 
    if (rc != 0) 
      { 
/*	perror("getpeername()");  */ 
	if (rc < 0) return rc; 
		else return -1; 
      } 
    styp = sadr.sa_family; 
 
    /*  where's the offset into the address?  */ 
    switch (styp) 
      { 
	case AF_INET:	soff = 2;   slen = 4; 
			break; 
	default:	soff = 2; 
			break; 
      } 
 
    /*  now copy the address  */ 
    for (i = 0; i < slen; i++) 
	hadd[i] = sadr.sa_data[i+soff]; 
 
    /*  and snag that port number  */ 
    prmt = 0; 
    for (i = 0; i < soff; i++) 
	prmt = (prmt << 8) + (sadr.sa_data[i] & 0xFF); 
 
/* 
(void) sprintf(temp,"PORT=%d (yours)",prmt); 
(void) netline(2,temp); 
 */ 
 
    /*  what host is at that address?  */
    hent = gethostbyaddr(hadd,slen,styp); 
    if (hent == NULL) 
      { 
/*	perror("gethostbyaddr()");  */ 
	if (rc < 0) return rc; 
		else return -1; 
      } 
    strncpy(host,hent->h_name,HOST_BSZ);    /*  keep it  */ 
    host[HOST_BSZ-1] = 0x00;	/*  safety net  */ 
 
/* 
(void) sprintf(temp,"HOST=%s (yours)",host); 
(void) netline(2,temp); 
 */ 
 
    /*  try a little IDENT client/server action  */ 
    (void) sprintf(temp,"%s:%d",host,IDENT_PORT); 
    sock = tcpopen(temp,0,0); 
    if (sock >= 0) 
      { 
	/*  build and send the IDENT request  */ 
	(void) sprintf(temp,"%d , %d",prmt,plcl); 
/*	(void) netline(sock,temp);  */ 
	(void) tcpputs(sock,temp); 
/*	(void) getline(sock,temp,TEMP_BSZ);  */ 
	(void) tcpgets(sock,temp,TEMP_BSZ); 
/*	(void) netline(1,temp);  */ 
 
	for (p = temp; *p != 0x00 && *p != ':'; p++); 
	if (*p == ':') 
	  { 
	    p++; 
	    while (*p != 0x00 && *p <= ' ') p++; 
/*  (void) netline(2,p);  */ 
	    if (strncmp(p,"USERID",6) == 0) 
	      { 
		while (*p != 0x00 && *p != ':') p++; 
		if (*p == ':') p++; 
		while (*p != 0x00 && *p != ':') p++; 
		if (*p == ':') p++; 
		while (*p != 0x00 && *p <= ' ') p++; 
		(void) strncpy(user,p,USER_BSZ); 
	      } 
	  } 
      } 
 
    (void) sprintf(buff,"%s@%s",user,host); 
 
/* 
(void) netline(2,"<<<<<<<<"); 
 */ 
 
    return 0; 
  } 
 
