/* ------------------------------------------------------------- PUTLINE 
 *	  Name: PUTLINE/UFTXPUTS 
 *		common Put String function 
 *   Operation: Writes the NULL terminated string from buffer b 
 *		to socket s with NL (UNIX text) line termination. 
 *	Author: Rick Troth, Ithaca, NY / Houston, TX (METRO) 
 *	  Date: 1993-Sep-19, Oct-20 
 * 
 *    See also: getline.c, netline.c 
 */ 
int putline(s,b) 
  int     s; 
  char   *b; 
  { 
    int 	i,  j; 
    char	temp[4096]; 
 
/*  i = strlen(b);  */ 
    for (i = 0; b[i] != 0x00; i++) temp[i] = b[i]; 
    temp[i] = '\n'; 
    j = write(s,temp,i+1); 
/*  b[i] = 0x00;  */ 
 
    if (j != i+1) return -1; 
    return i; 
  } 
 
