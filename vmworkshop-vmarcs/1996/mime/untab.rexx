/*
 *        Name: EXPAND REXX
 *              Expand Tab Characters function as a pipeline filter
 *              This gem can be replaced with  UNTAB -8,  if available.
 *      Author: Rick Troth, Rice University, Information Systems
 *        Date: 1992-Apr-17, Dec-06
 */
 
/*  'CALLPIPE *: | UNTAB -8 | *:'  */
 
Do Forever
 
    'PEEKTO LINE'
    If rc ^= 0 Then Leave
 
    tabpos = Pos('05'x,line)
    Do While tabpos > 0
        line = Substr(line,1,tabpos-1) || ,
               Copies('40'x,((tabpos+7)%8)*8-tabpos+1) || ,
               Substr(line,tabpos+1)
        tabpos = Pos('05'x,line)
        End  /*  Do  While  */
 
    'OUTPUT' line
    If rc ^= 0 Then Leave
 
    'READTO'
 
    End  /*  Do  While  */
 
Exit rc * (rc ^= 12)
 
