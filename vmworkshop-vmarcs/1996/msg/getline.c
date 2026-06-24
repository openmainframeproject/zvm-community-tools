/* ------------------------------------------------------------- GETLINE 
 *	  Name: GETLINE/UFTXGETS/UFTXRCVS 
 *		common Get/Receive String function 
 *   Operation: Reads a CR/LF terminated string from socket s 
 *		into buffer b.  Returns the length of that string. 
 *	Author: Rick Troth, Ithaca NY, Houston TX (METRO) 
 *	  Date: 1993-Sep-19, Oct-20 
 * 
 *    See also: putline.c, netline.c 
 */ 
int getline(s,b) 
  int     s; 
  char   *b; 
  { 
    char       *p; 
    int 	i; 
 
    p = b; 
    while (1) 
      { 
	if (read(s,p,1) != 1)		/*  get a byte  */ 
	if (read(s,p,1) != 1) return -1;	/*  try again  */ 
	if (*p == '\n') break;		/*  NL terminates  */ 
	if (*p == 0x00) break;		/*  NULL terminates  */ 
/*	if (*p == '\t') *p = ' ';	**  [don't] eliminate TABs  */ 
	p++;				/*  increment pointer  */ 
      } 
    *p = 0x00;		/*  NULL terminate,  even if NULL  */ 
 
    i = p - b;		/*  calculate the length  */ 
    if (i > 0 && b[i-1] == '\r')	/*  trailing CR?  */ 
      { 
	i = i - 1;	/*  shorten length by one  */ 
	p--;		/*  backspace  */ 
	*p = 0x00;	/*  remove trailing CR  */ 
      } 
 
    return i; 
  } 
 
